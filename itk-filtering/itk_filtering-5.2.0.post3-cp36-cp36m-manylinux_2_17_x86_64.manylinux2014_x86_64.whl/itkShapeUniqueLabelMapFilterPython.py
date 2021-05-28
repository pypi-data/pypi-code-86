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
    from . import _itkShapeUniqueLabelMapFilterPython
else:
    import _itkShapeUniqueLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapeUniqueLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapeUniqueLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkLabelMapFilterPython
import itk.itkStatisticsLabelObjectPython
import itk.itkPointPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkArrayPython
import itk.itkShapeLabelObjectPython
import itk.itkLabelObjectPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkLabelObjectLinePython
import itk.itkImageRegionPython
import itk.itkAffineTransformPython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkTransformBasePython
import itk.itkVariableLengthVectorPython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkOptimizerParametersPython
import itk.itkArray2DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.ITKLabelMapBasePython
import itk.itkImageSourceCommonPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkImageToImageFilterCommonPython

def itkShapeUniqueLabelMapFilterLM2_New():
    return itkShapeUniqueLabelMapFilterLM2.New()

class itkShapeUniqueLabelMapFilterLM2(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    r"""


    Remove some pixels in the label object according to the value of their
    shape attribute to ensure that a pixel is not in to objects.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   ShapeLabelObject, BinaryShapeOpeningImageFilter,
    LabelStatisticsOpeningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2_Clone)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2_SetAttribute)
    __swig_destroy__ = _itkShapeUniqueLabelMapFilterPython.delete_itkShapeUniqueLabelMapFilterLM2
    cast = _swig_new_static_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkShapeUniqueLabelMapFilterLM2

        Create a new object of the class itkShapeUniqueLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeUniqueLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeUniqueLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeUniqueLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeUniqueLabelMapFilterLM2 in _itkShapeUniqueLabelMapFilterPython:
_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2_swigregister(itkShapeUniqueLabelMapFilterLM2)
itkShapeUniqueLabelMapFilterLM2___New_orig__ = _itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2___New_orig__
itkShapeUniqueLabelMapFilterLM2_cast = _itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM2_cast


def itkShapeUniqueLabelMapFilterLM3_New():
    return itkShapeUniqueLabelMapFilterLM3.New()

class itkShapeUniqueLabelMapFilterLM3(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    r"""


    Remove some pixels in the label object according to the value of their
    shape attribute to ensure that a pixel is not in to objects.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   ShapeLabelObject, BinaryShapeOpeningImageFilter,
    LabelStatisticsOpeningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3_Clone)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3_SetAttribute)
    __swig_destroy__ = _itkShapeUniqueLabelMapFilterPython.delete_itkShapeUniqueLabelMapFilterLM3
    cast = _swig_new_static_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkShapeUniqueLabelMapFilterLM3

        Create a new object of the class itkShapeUniqueLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeUniqueLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeUniqueLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeUniqueLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeUniqueLabelMapFilterLM3 in _itkShapeUniqueLabelMapFilterPython:
_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3_swigregister(itkShapeUniqueLabelMapFilterLM3)
itkShapeUniqueLabelMapFilterLM3___New_orig__ = _itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3___New_orig__
itkShapeUniqueLabelMapFilterLM3_cast = _itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM3_cast


def itkShapeUniqueLabelMapFilterLM4_New():
    return itkShapeUniqueLabelMapFilterLM4.New()

class itkShapeUniqueLabelMapFilterLM4(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4):
    r"""


    Remove some pixels in the label object according to the value of their
    shape attribute to ensure that a pixel is not in to objects.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   ShapeLabelObject, BinaryShapeOpeningImageFilter,
    LabelStatisticsOpeningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4_Clone)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4_GetReverseOrdering)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4_SetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4_SetAttribute)
    __swig_destroy__ = _itkShapeUniqueLabelMapFilterPython.delete_itkShapeUniqueLabelMapFilterLM4
    cast = _swig_new_static_method(_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkShapeUniqueLabelMapFilterLM4

        Create a new object of the class itkShapeUniqueLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeUniqueLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeUniqueLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeUniqueLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeUniqueLabelMapFilterLM4 in _itkShapeUniqueLabelMapFilterPython:
_itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4_swigregister(itkShapeUniqueLabelMapFilterLM4)
itkShapeUniqueLabelMapFilterLM4___New_orig__ = _itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4___New_orig__
itkShapeUniqueLabelMapFilterLM4_cast = _itkShapeUniqueLabelMapFilterPython.itkShapeUniqueLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def shape_unique_label_map_filter(*args: itkt.ImageLike,  reverse_ordering: bool=..., attribute: Union[str, int]=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for ShapeUniqueLabelMapFilter"""
    import itk

    kwarg_typehints = { 'reverse_ordering':reverse_ordering,'attribute':attribute }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ShapeUniqueLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def shape_unique_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.ShapeUniqueLabelMapFilter
    shape_unique_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    shape_unique_label_map_filter.__doc__ = filter_object.__doc__




