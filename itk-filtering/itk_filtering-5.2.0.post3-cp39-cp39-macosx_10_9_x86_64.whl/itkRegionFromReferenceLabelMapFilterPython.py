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
    from . import _itkRegionFromReferenceLabelMapFilterPython
else:
    import _itkRegionFromReferenceLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRegionFromReferenceLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRegionFromReferenceLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImagePython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.pyBasePython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.ITKCommonBasePython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.ITKLabelMapBasePython
import itk.itkStatisticsLabelObjectPython
import itk.itkShapeLabelObjectPython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkVariableLengthVectorPython
import itk.itkArray2DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkImageToImageFilterCommonPython
import itk.itkChangeRegionLabelMapFilterPython
import itk.itkInPlaceLabelMapFilterPython
import itk.itkLabelMapFilterPython

def itkRegionFromReferenceLabelMapFilterLM2_New():
    return itkRegionFromReferenceLabelMapFilterLM2.New()

class itkRegionFromReferenceLabelMapFilterLM2(itk.itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2):
    r"""


    Set the region from a reference image.

    Change the region of a label map to be the same as one of a reference
    image. This filter implements the same feature as its superclass, but
    with the input region well integrated in the pipeline architecture. If
    the output cannot contain some of the objects' lines, they are
    truncated or removed. All objects fully outside the output region are
    removed.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_Clone)
    SetReferenceImage = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetReferenceImage)
    GetReferenceImage = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_GetReferenceImage)
    SetInput1 = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_SetInput2)
    __swig_destroy__ = _itkRegionFromReferenceLabelMapFilterPython.delete_itkRegionFromReferenceLabelMapFilterLM2
    cast = _swig_new_static_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkRegionFromReferenceLabelMapFilterLM2

        Create a new object of the class itkRegionFromReferenceLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegionFromReferenceLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRegionFromReferenceLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRegionFromReferenceLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRegionFromReferenceLabelMapFilterLM2 in _itkRegionFromReferenceLabelMapFilterPython:
_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_swigregister(itkRegionFromReferenceLabelMapFilterLM2)
itkRegionFromReferenceLabelMapFilterLM2___New_orig__ = _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2___New_orig__
itkRegionFromReferenceLabelMapFilterLM2_cast = _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM2_cast


def itkRegionFromReferenceLabelMapFilterLM3_New():
    return itkRegionFromReferenceLabelMapFilterLM3.New()

class itkRegionFromReferenceLabelMapFilterLM3(itk.itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3):
    r"""


    Set the region from a reference image.

    Change the region of a label map to be the same as one of a reference
    image. This filter implements the same feature as its superclass, but
    with the input region well integrated in the pipeline architecture. If
    the output cannot contain some of the objects' lines, they are
    truncated or removed. All objects fully outside the output region are
    removed.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_Clone)
    SetReferenceImage = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetReferenceImage)
    GetReferenceImage = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_GetReferenceImage)
    SetInput1 = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_SetInput2)
    __swig_destroy__ = _itkRegionFromReferenceLabelMapFilterPython.delete_itkRegionFromReferenceLabelMapFilterLM3
    cast = _swig_new_static_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkRegionFromReferenceLabelMapFilterLM3

        Create a new object of the class itkRegionFromReferenceLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegionFromReferenceLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRegionFromReferenceLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRegionFromReferenceLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRegionFromReferenceLabelMapFilterLM3 in _itkRegionFromReferenceLabelMapFilterPython:
_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_swigregister(itkRegionFromReferenceLabelMapFilterLM3)
itkRegionFromReferenceLabelMapFilterLM3___New_orig__ = _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3___New_orig__
itkRegionFromReferenceLabelMapFilterLM3_cast = _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM3_cast


def itkRegionFromReferenceLabelMapFilterLM4_New():
    return itkRegionFromReferenceLabelMapFilterLM4.New()

class itkRegionFromReferenceLabelMapFilterLM4(itk.itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM4):
    r"""


    Set the region from a reference image.

    Change the region of a label map to be the same as one of a reference
    image. This filter implements the same feature as its superclass, but
    with the input region well integrated in the pipeline architecture. If
    the output cannot contain some of the objects' lines, they are
    truncated or removed. All objects fully outside the output region are
    removed.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM4_Clone)
    SetReferenceImage = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM4_SetReferenceImage)
    GetReferenceImage = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM4_GetReferenceImage)
    SetInput1 = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM4_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM4_SetInput2)
    __swig_destroy__ = _itkRegionFromReferenceLabelMapFilterPython.delete_itkRegionFromReferenceLabelMapFilterLM4
    cast = _swig_new_static_method(_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkRegionFromReferenceLabelMapFilterLM4

        Create a new object of the class itkRegionFromReferenceLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegionFromReferenceLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRegionFromReferenceLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRegionFromReferenceLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRegionFromReferenceLabelMapFilterLM4 in _itkRegionFromReferenceLabelMapFilterPython:
_itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM4_swigregister(itkRegionFromReferenceLabelMapFilterLM4)
itkRegionFromReferenceLabelMapFilterLM4___New_orig__ = _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM4___New_orig__
itkRegionFromReferenceLabelMapFilterLM4_cast = _itkRegionFromReferenceLabelMapFilterPython.itkRegionFromReferenceLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def region_from_reference_label_map_filter(*args: itkt.ImageLike,  reference_image: itkt.ImageBase=..., region: itkt.ImageRegion=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for RegionFromReferenceLabelMapFilter"""
    import itk

    kwarg_typehints = { 'reference_image':reference_image,'region':region }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.RegionFromReferenceLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def region_from_reference_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.RegionFromReferenceLabelMapFilter
    region_from_reference_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    region_from_reference_label_map_filter.__doc__ = filter_object.__doc__




