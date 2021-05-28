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
    from . import _itkShapePositionLabelMapFilterPython
else:
    import _itkShapePositionLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapePositionLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapePositionLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkStatisticsLabelObjectPython
import itk.itkHistogramPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkSamplePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkAffineTransformPython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkArray2DPython
import itk.itkTransformBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkOptimizerParametersPython
import itk.itkDiffusionTensor3DPython
import itk.itkVariableLengthVectorPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkShapeLabelObjectPython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.itkImageRegionPython
import itk.itkInPlaceLabelMapFilterPython
import itk.ITKLabelMapBasePython
import itk.itkImageToImageFilterCommonPython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython
import itk.itkImageSourceCommonPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkLabelMapFilterPython

def itkShapePositionLabelMapFilterLM2_New():
    return itkShapePositionLabelMapFilterLM2.New()

class itkShapePositionLabelMapFilterLM2(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    r"""


    Mark a single pixel in the label object which correspond to a position
    given by an attribute.

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
    __New_orig__ = _swig_new_static_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_Clone)
    GetAttribute = _swig_new_instance_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_SetAttribute)
    __swig_destroy__ = _itkShapePositionLabelMapFilterPython.delete_itkShapePositionLabelMapFilterLM2
    cast = _swig_new_static_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkShapePositionLabelMapFilterLM2

        Create a new object of the class itkShapePositionLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePositionLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapePositionLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapePositionLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapePositionLabelMapFilterLM2 in _itkShapePositionLabelMapFilterPython:
_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_swigregister(itkShapePositionLabelMapFilterLM2)
itkShapePositionLabelMapFilterLM2___New_orig__ = _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2___New_orig__
itkShapePositionLabelMapFilterLM2_cast = _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2_cast


def itkShapePositionLabelMapFilterLM3_New():
    return itkShapePositionLabelMapFilterLM3.New()

class itkShapePositionLabelMapFilterLM3(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    r"""


    Mark a single pixel in the label object which correspond to a position
    given by an attribute.

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
    __New_orig__ = _swig_new_static_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_Clone)
    GetAttribute = _swig_new_instance_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_SetAttribute)
    __swig_destroy__ = _itkShapePositionLabelMapFilterPython.delete_itkShapePositionLabelMapFilterLM3
    cast = _swig_new_static_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkShapePositionLabelMapFilterLM3

        Create a new object of the class itkShapePositionLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePositionLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapePositionLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapePositionLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapePositionLabelMapFilterLM3 in _itkShapePositionLabelMapFilterPython:
_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_swigregister(itkShapePositionLabelMapFilterLM3)
itkShapePositionLabelMapFilterLM3___New_orig__ = _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3___New_orig__
itkShapePositionLabelMapFilterLM3_cast = _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3_cast


def itkShapePositionLabelMapFilterLM4_New():
    return itkShapePositionLabelMapFilterLM4.New()

class itkShapePositionLabelMapFilterLM4(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4):
    r"""


    Mark a single pixel in the label object which correspond to a position
    given by an attribute.

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
    __New_orig__ = _swig_new_static_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM4_Clone)
    GetAttribute = _swig_new_instance_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM4_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM4_SetAttribute)
    __swig_destroy__ = _itkShapePositionLabelMapFilterPython.delete_itkShapePositionLabelMapFilterLM4
    cast = _swig_new_static_method(_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkShapePositionLabelMapFilterLM4

        Create a new object of the class itkShapePositionLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapePositionLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapePositionLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapePositionLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapePositionLabelMapFilterLM4 in _itkShapePositionLabelMapFilterPython:
_itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM4_swigregister(itkShapePositionLabelMapFilterLM4)
itkShapePositionLabelMapFilterLM4___New_orig__ = _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM4___New_orig__
itkShapePositionLabelMapFilterLM4_cast = _itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def shape_position_label_map_filter(*args: itkt.ImageLike,  attribute: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for ShapePositionLabelMapFilter"""
    import itk

    kwarg_typehints = { 'attribute':attribute }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ShapePositionLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def shape_position_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.ShapePositionLabelMapFilter
    shape_position_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    shape_position_label_map_filter.__doc__ = filter_object.__doc__




