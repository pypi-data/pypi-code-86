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
    from . import _itkAutoCropLabelMapFilterPython
else:
    import _itkAutoCropLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkAutoCropLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkAutoCropLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkSizePython
import itk.pyBasePython
import itk.itkChangeRegionLabelMapFilterPython
import itk.ITKCommonBasePython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkStatisticsLabelObjectPython
import itk.itkShapeLabelObjectPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkPointPython
import itk.itkVariableLengthVectorPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkArray2DPython
import itk.itkTransformBasePython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkInPlaceLabelMapFilterPython
import itk.ITKLabelMapBasePython
import itk.itkImageToImageFilterCommonPython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkImageSourceCommonPython
import itk.itkLabelMapFilterPython

def itkAutoCropLabelMapFilterLM2_New():
    return itkAutoCropLabelMapFilterLM2.New()

class itkAutoCropLabelMapFilterLM2(itk.itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2):
    r"""


    Crop a LabelMap image to fit exactly the objects in the LabelMap.

    The CropBorder can be used to add a border which will never be larger
    than the input image. To add a border of size independent of the input
    image, PadLabelMapFilter can be used.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   PadLabelMapFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_Clone)
    SetCropBorder = _swig_new_instance_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_SetCropBorder)
    GetCropBorder = _swig_new_instance_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_GetCropBorder)
    __swig_destroy__ = _itkAutoCropLabelMapFilterPython.delete_itkAutoCropLabelMapFilterLM2
    cast = _swig_new_static_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkAutoCropLabelMapFilterLM2

        Create a new object of the class itkAutoCropLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAutoCropLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAutoCropLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAutoCropLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAutoCropLabelMapFilterLM2 in _itkAutoCropLabelMapFilterPython:
_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_swigregister(itkAutoCropLabelMapFilterLM2)
itkAutoCropLabelMapFilterLM2___New_orig__ = _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2___New_orig__
itkAutoCropLabelMapFilterLM2_cast = _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM2_cast


def itkAutoCropLabelMapFilterLM3_New():
    return itkAutoCropLabelMapFilterLM3.New()

class itkAutoCropLabelMapFilterLM3(itk.itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3):
    r"""


    Crop a LabelMap image to fit exactly the objects in the LabelMap.

    The CropBorder can be used to add a border which will never be larger
    than the input image. To add a border of size independent of the input
    image, PadLabelMapFilter can be used.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   PadLabelMapFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_Clone)
    SetCropBorder = _swig_new_instance_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_SetCropBorder)
    GetCropBorder = _swig_new_instance_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_GetCropBorder)
    __swig_destroy__ = _itkAutoCropLabelMapFilterPython.delete_itkAutoCropLabelMapFilterLM3
    cast = _swig_new_static_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkAutoCropLabelMapFilterLM3

        Create a new object of the class itkAutoCropLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAutoCropLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAutoCropLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAutoCropLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAutoCropLabelMapFilterLM3 in _itkAutoCropLabelMapFilterPython:
_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_swigregister(itkAutoCropLabelMapFilterLM3)
itkAutoCropLabelMapFilterLM3___New_orig__ = _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3___New_orig__
itkAutoCropLabelMapFilterLM3_cast = _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM3_cast


def itkAutoCropLabelMapFilterLM4_New():
    return itkAutoCropLabelMapFilterLM4.New()

class itkAutoCropLabelMapFilterLM4(itk.itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM4):
    r"""


    Crop a LabelMap image to fit exactly the objects in the LabelMap.

    The CropBorder can be used to add a border which will never be larger
    than the input image. To add a border of size independent of the input
    image, PadLabelMapFilter can be used.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   PadLabelMapFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM4_Clone)
    SetCropBorder = _swig_new_instance_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM4_SetCropBorder)
    GetCropBorder = _swig_new_instance_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM4_GetCropBorder)
    __swig_destroy__ = _itkAutoCropLabelMapFilterPython.delete_itkAutoCropLabelMapFilterLM4
    cast = _swig_new_static_method(_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkAutoCropLabelMapFilterLM4

        Create a new object of the class itkAutoCropLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAutoCropLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAutoCropLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAutoCropLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAutoCropLabelMapFilterLM4 in _itkAutoCropLabelMapFilterPython:
_itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM4_swigregister(itkAutoCropLabelMapFilterLM4)
itkAutoCropLabelMapFilterLM4___New_orig__ = _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM4___New_orig__
itkAutoCropLabelMapFilterLM4_cast = _itkAutoCropLabelMapFilterPython.itkAutoCropLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def auto_crop_label_map_filter(*args: itkt.ImageLike,  crop_border: Sequence[int]=..., region: itkt.ImageRegion=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for AutoCropLabelMapFilter"""
    import itk

    kwarg_typehints = { 'crop_border':crop_border,'region':region }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.AutoCropLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def auto_crop_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.AutoCropLabelMapFilter
    auto_crop_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    auto_crop_label_map_filter.__doc__ = filter_object.__doc__




