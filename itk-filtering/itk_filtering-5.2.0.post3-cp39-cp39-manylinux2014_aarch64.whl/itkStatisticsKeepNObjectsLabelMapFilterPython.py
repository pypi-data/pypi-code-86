# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKLabelMapPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkStatisticsKeepNObjectsLabelMapFilterPython
else:
    import _itkStatisticsKeepNObjectsLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkStatisticsKeepNObjectsLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkStatisticsKeepNObjectsLabelMapFilterPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import collections.abc
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkShapeKeepNObjectsLabelMapFilterPython
import itk.itkInPlaceLabelMapFilterPython
import itk.ITKLabelMapBasePython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkStatisticsLabelObjectPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkShapeLabelObjectPython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkArray2DPython
import itk.itkVariableLengthVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkDiffusionTensor3DPython
import itk.itkTransformBasePython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkLabelMapFilterPython

def itkStatisticsKeepNObjectsLabelMapFilterLM2_New():
    return itkStatisticsKeepNObjectsLabelMapFilterLM2.New()

class itkStatisticsKeepNObjectsLabelMapFilterLM2(itk.itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2):
    r"""


    keep N objects according to their statistics attributes

    StatisticsKeepNObjectsLabelMapFilter keep the N objects in a label
    collection image with the highest (or lowest) attribute value. The
    attributes are the ones of the StatisticsLabelObject.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   StatisticsLabelObject, BinaryStatisticsKeepNObjectsImageFilter,
    LabelShapeKeepNObjectsImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM2_Clone)
    __swig_destroy__ = _itkStatisticsKeepNObjectsLabelMapFilterPython.delete_itkStatisticsKeepNObjectsLabelMapFilterLM2
    cast = _swig_new_static_method(_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsKeepNObjectsLabelMapFilterLM2

        Create a new object of the class itkStatisticsKeepNObjectsLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsKeepNObjectsLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsKeepNObjectsLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsKeepNObjectsLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsKeepNObjectsLabelMapFilterLM2 in _itkStatisticsKeepNObjectsLabelMapFilterPython:
_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM2_swigregister(itkStatisticsKeepNObjectsLabelMapFilterLM2)
itkStatisticsKeepNObjectsLabelMapFilterLM2___New_orig__ = _itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM2___New_orig__
itkStatisticsKeepNObjectsLabelMapFilterLM2_cast = _itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM2_cast


def itkStatisticsKeepNObjectsLabelMapFilterLM3_New():
    return itkStatisticsKeepNObjectsLabelMapFilterLM3.New()

class itkStatisticsKeepNObjectsLabelMapFilterLM3(itk.itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3):
    r"""


    keep N objects according to their statistics attributes

    StatisticsKeepNObjectsLabelMapFilter keep the N objects in a label
    collection image with the highest (or lowest) attribute value. The
    attributes are the ones of the StatisticsLabelObject.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   StatisticsLabelObject, BinaryStatisticsKeepNObjectsImageFilter,
    LabelShapeKeepNObjectsImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM3_Clone)
    __swig_destroy__ = _itkStatisticsKeepNObjectsLabelMapFilterPython.delete_itkStatisticsKeepNObjectsLabelMapFilterLM3
    cast = _swig_new_static_method(_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsKeepNObjectsLabelMapFilterLM3

        Create a new object of the class itkStatisticsKeepNObjectsLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsKeepNObjectsLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsKeepNObjectsLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsKeepNObjectsLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsKeepNObjectsLabelMapFilterLM3 in _itkStatisticsKeepNObjectsLabelMapFilterPython:
_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM3_swigregister(itkStatisticsKeepNObjectsLabelMapFilterLM3)
itkStatisticsKeepNObjectsLabelMapFilterLM3___New_orig__ = _itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM3___New_orig__
itkStatisticsKeepNObjectsLabelMapFilterLM3_cast = _itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM3_cast


def itkStatisticsKeepNObjectsLabelMapFilterLM4_New():
    return itkStatisticsKeepNObjectsLabelMapFilterLM4.New()

class itkStatisticsKeepNObjectsLabelMapFilterLM4(itk.itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4):
    r"""


    keep N objects according to their statistics attributes

    StatisticsKeepNObjectsLabelMapFilter keep the N objects in a label
    collection image with the highest (or lowest) attribute value. The
    attributes are the ones of the StatisticsLabelObject.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   StatisticsLabelObject, BinaryStatisticsKeepNObjectsImageFilter,
    LabelShapeKeepNObjectsImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM4_Clone)
    __swig_destroy__ = _itkStatisticsKeepNObjectsLabelMapFilterPython.delete_itkStatisticsKeepNObjectsLabelMapFilterLM4
    cast = _swig_new_static_method(_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsKeepNObjectsLabelMapFilterLM4

        Create a new object of the class itkStatisticsKeepNObjectsLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsKeepNObjectsLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsKeepNObjectsLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsKeepNObjectsLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsKeepNObjectsLabelMapFilterLM4 in _itkStatisticsKeepNObjectsLabelMapFilterPython:
_itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM4_swigregister(itkStatisticsKeepNObjectsLabelMapFilterLM4)
itkStatisticsKeepNObjectsLabelMapFilterLM4___New_orig__ = _itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM4___New_orig__
itkStatisticsKeepNObjectsLabelMapFilterLM4_cast = _itkStatisticsKeepNObjectsLabelMapFilterPython.itkStatisticsKeepNObjectsLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def statistics_keep_n_objects_label_map_filter(*args: itkt.ImageLike,  reverse_ordering: bool=..., number_of_objects: int=..., attribute: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for StatisticsKeepNObjectsLabelMapFilter"""
    import itk

    kwarg_typehints = { 'reverse_ordering':reverse_ordering,'number_of_objects':number_of_objects,'attribute':attribute }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.StatisticsKeepNObjectsLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def statistics_keep_n_objects_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.StatisticsKeepNObjectsLabelMapFilter
    statistics_keep_n_objects_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    statistics_keep_n_objects_label_map_filter.__doc__ = filter_object.__doc__




