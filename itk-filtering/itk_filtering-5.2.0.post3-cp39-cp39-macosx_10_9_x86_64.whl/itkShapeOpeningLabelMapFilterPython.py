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
    from . import _itkShapeOpeningLabelMapFilterPython
else:
    import _itkShapeOpeningLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapeOpeningLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapeOpeningLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkInPlaceLabelMapFilterPython
import itk.ITKLabelMapBasePython
import itk.itkImagePython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkImageRegionPython
import itk.itkIndexPython
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
import itk.itkLabelMapFilterPython

def itkShapeOpeningLabelMapFilterLM2_New():
    return itkShapeOpeningLabelMapFilterLM2.New()

class itkShapeOpeningLabelMapFilterLM2(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    r"""


    Remove objects according to the value of their shape attribute.

    ShapeOpeningLabelMapFilter removes objects in a label collection image
    with an attribute value smaller or greater than a threshold called
    Lambda. The attributes are those of the ShapeLabelObject.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, BinaryShapeOpeningImageFilter,
    LabelStatisticsOpeningImageFilter
    example{Filtering/LabelMap/KeepRegionsThatMeetSpecific,Keep Regions
    That Meet Specific Properties} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_Clone)
    GetLambda = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_GetLambda)
    SetLambda = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_SetLambda)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_SetAttribute)
    __swig_destroy__ = _itkShapeOpeningLabelMapFilterPython.delete_itkShapeOpeningLabelMapFilterLM2
    cast = _swig_new_static_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkShapeOpeningLabelMapFilterLM2

        Create a new object of the class itkShapeOpeningLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeOpeningLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeOpeningLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeOpeningLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeOpeningLabelMapFilterLM2 in _itkShapeOpeningLabelMapFilterPython:
_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_swigregister(itkShapeOpeningLabelMapFilterLM2)
itkShapeOpeningLabelMapFilterLM2___New_orig__ = _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2___New_orig__
itkShapeOpeningLabelMapFilterLM2_cast = _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2_cast


def itkShapeOpeningLabelMapFilterLM3_New():
    return itkShapeOpeningLabelMapFilterLM3.New()

class itkShapeOpeningLabelMapFilterLM3(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    r"""


    Remove objects according to the value of their shape attribute.

    ShapeOpeningLabelMapFilter removes objects in a label collection image
    with an attribute value smaller or greater than a threshold called
    Lambda. The attributes are those of the ShapeLabelObject.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, BinaryShapeOpeningImageFilter,
    LabelStatisticsOpeningImageFilter
    example{Filtering/LabelMap/KeepRegionsThatMeetSpecific,Keep Regions
    That Meet Specific Properties} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_Clone)
    GetLambda = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_GetLambda)
    SetLambda = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_SetLambda)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_SetAttribute)
    __swig_destroy__ = _itkShapeOpeningLabelMapFilterPython.delete_itkShapeOpeningLabelMapFilterLM3
    cast = _swig_new_static_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkShapeOpeningLabelMapFilterLM3

        Create a new object of the class itkShapeOpeningLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeOpeningLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeOpeningLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeOpeningLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeOpeningLabelMapFilterLM3 in _itkShapeOpeningLabelMapFilterPython:
_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_swigregister(itkShapeOpeningLabelMapFilterLM3)
itkShapeOpeningLabelMapFilterLM3___New_orig__ = _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3___New_orig__
itkShapeOpeningLabelMapFilterLM3_cast = _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3_cast


def itkShapeOpeningLabelMapFilterLM4_New():
    return itkShapeOpeningLabelMapFilterLM4.New()

class itkShapeOpeningLabelMapFilterLM4(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4):
    r"""


    Remove objects according to the value of their shape attribute.

    ShapeOpeningLabelMapFilter removes objects in a label collection image
    with an attribute value smaller or greater than a threshold called
    Lambda. The attributes are those of the ShapeLabelObject.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, BinaryShapeOpeningImageFilter,
    LabelStatisticsOpeningImageFilter
    example{Filtering/LabelMap/KeepRegionsThatMeetSpecific,Keep Regions
    That Meet Specific Properties} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_Clone)
    GetLambda = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_GetLambda)
    SetLambda = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_SetLambda)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_SetAttribute)
    __swig_destroy__ = _itkShapeOpeningLabelMapFilterPython.delete_itkShapeOpeningLabelMapFilterLM4
    cast = _swig_new_static_method(_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkShapeOpeningLabelMapFilterLM4

        Create a new object of the class itkShapeOpeningLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeOpeningLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeOpeningLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeOpeningLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeOpeningLabelMapFilterLM4 in _itkShapeOpeningLabelMapFilterPython:
_itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_swigregister(itkShapeOpeningLabelMapFilterLM4)
itkShapeOpeningLabelMapFilterLM4___New_orig__ = _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4___New_orig__
itkShapeOpeningLabelMapFilterLM4_cast = _itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def shape_opening_label_map_filter(*args: itkt.ImageLike,  reverse_ordering: bool=..., attribute: Union[str, int]=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for ShapeOpeningLabelMapFilter"""
    import itk

    kwarg_typehints = { 'reverse_ordering':reverse_ordering,'attribute':attribute }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ShapeOpeningLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def shape_opening_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.ShapeOpeningLabelMapFilter
    shape_opening_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    shape_opening_label_map_filter.__doc__ = filter_object.__doc__




