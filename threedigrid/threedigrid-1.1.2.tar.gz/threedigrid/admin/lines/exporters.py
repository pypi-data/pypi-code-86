# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
"""
Exporters
---------
"""
from __future__ import unicode_literals
from __future__ import print_function

from __future__ import absolute_import
import os
import logging
import six
from six.moves import range

try:
    from osgeo import ogr
except ImportError:
    ogr = None

try:
    from shapely import geometry as shapely_geom
except ImportError:
    shapely_geom = None


from threedigrid.geo_utils import get_spatial_reference
from threedigrid.geo_utils import raise_import_exception
from threedigrid.admin.utils import KCUDescriptor
from threedigrid.orm.base.exporters import BaseOgrExporter
from threedigrid.admin import exporter_constants as const
from threedigrid.admin.constants import LINE_BASE_FIELDS_ALL
from threedigrid.admin.constants import LINE_FIELD_NAME_MAP
from threedigrid.admin.constants import TYPE_FUNC_MAP


logger = logging.getLogger(__name__)


class LinesOgrExporter(BaseOgrExporter):
    """
    Exports to ogr formats. You need to set the driver explicitly
    before calling save()
    """
    def __init__(self, lines):
        """
        :param lines: lines.models.Lines instance
        """
        self._lines = lines
        self.supported_drivers = {
            const.GEO_PACKAGE_DRIVER_NAME,
            const.SHP_DRIVER_NAME,
            const.GEOJSON_DRIVER_NAME,
        }
        self.driver = None

    def save(self, file_name, line_data, target_epsg_code, **kwargs):
        """
        save to file format specified by the driver, e.g. shapefile

        :param file_name: name of the outputfile
        :param line_data: dict of line data
        """
        if self.driver is None:
            self.set_driver(extension=os.path.splitext(file_name)[1])

        assert self.driver is not None

        kcu_dict = KCUDescriptor()
        geomtype = 0
        sr = get_spatial_reference(target_epsg_code)

        geom_source = 'from_threedicore'
        if 'geom' in kwargs:
            geom_source = kwargs['geom']

        # shapely is needed for the LineString creation, check if installed
        if geom_source == 'from_spatialite' and shapely_geom is None:
            raise_import_exception('shapely')

        self.del_datasource(file_name)
        data_source = self.driver.CreateDataSource(file_name)
        layer = data_source.CreateLayer(
            str(os.path.basename(file_name)),
            sr,
            geomtype
        )
        fields = kwargs.get('fields', LINE_BASE_FIELDS_ALL)
        for field_name, field_type in six.iteritems(fields):
            layer.CreateField(ogr.FieldDefn(
                    str(field_name),
                    const.OGR_FIELD_TYPE_MAP[field_type])
            )
        _definition = layer.GetLayerDefn()

        node_a = line_data['line'][0]
        node_b = line_data['line'][1]
        for i in range(node_a.size):
            if geom_source == 'from_threedicore':
                line = ogr.Geometry(ogr.wkbLineString)
                line.AddPoint(line_data['line_coords'][0][i],
                              line_data['line_coords'][1][i])
                line.AddPoint(line_data['line_coords'][2][i],
                              line_data['line_coords'][3][i])
            elif geom_source == 'from_spatialite':
                linepoints = line_data['line_geometries'][i].reshape(
                    2, -1).T.astype('float64')
                line_geom = shapely_geom.LineString(linepoints)
                line = ogr.CreateGeometryFromWkt(line_geom.wkt)

            feature = ogr.Feature(_definition)
            feature.SetGeometry(line)
            for field_name, field_type in six.iteritems(fields):
                fname = LINE_FIELD_NAME_MAP.get(field_name, field_name)
                if field_name == 'kcu_descr':
                    value = ''
                    try:
                        value = str(kcu_dict[int(line_data['kcu'][i])])
                    except KeyError:
                        pass
                elif field_name == 'node_a':
                    value = TYPE_FUNC_MAP[field_type](node_a[i])
                elif field_name == 'node_b':
                    value = TYPE_FUNC_MAP[field_type](node_b[i])
                else:
                    try:
                        raw_value = line_data[fname][i]
                    except IndexError:
                        raw_value = '-9999'
                    value = TYPE_FUNC_MAP[field_type](raw_value)
                feature.SetField(str(field_name), value)

            layer.CreateFeature(feature)
            feature.Destroy()
