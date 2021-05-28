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
    from . import _itkShapeRelabelLabelMapFilterPython
else:
    import _itkShapeRelabelLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapeRelabelLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapeRelabelLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageFilterCommonPython
import itk.itkImagePython
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
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkRGBPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourceCommonPython
import itk.itkStatisticsLabelObjectPython
import itk.itkShapeLabelObjectPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkArray2DPython
import itk.itkTransformBasePython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkLabelMapFilterPython

def itkShapeRelabelLabelMapFilterLM2_New():
    return itkShapeRelabelLabelMapFilterLM2.New()

class itkShapeRelabelLabelMapFilterLM2(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    r"""


    Relabels objects according to their shape attributes.

    The ShapeRelabelImageFilter relabels a label collection image
    according to the shape attributes of the objects. The label produced
    are always consecutives.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_SetAttribute)
    __swig_destroy__ = _itkShapeRelabelLabelMapFilterPython.delete_itkShapeRelabelLabelMapFilterLM2
    cast = _swig_new_static_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkShapeRelabelLabelMapFilterLM2

        Create a new object of the class itkShapeRelabelLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeRelabelLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeRelabelLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeRelabelLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeRelabelLabelMapFilterLM2 in _itkShapeRelabelLabelMapFilterPython:
_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_swigregister(itkShapeRelabelLabelMapFilterLM2)
itkShapeRelabelLabelMapFilterLM2___New_orig__ = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2___New_orig__
itkShapeRelabelLabelMapFilterLM2_cast = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2_cast


def itkShapeRelabelLabelMapFilterLM3_New():
    return itkShapeRelabelLabelMapFilterLM3.New()

class itkShapeRelabelLabelMapFilterLM3(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    r"""


    Relabels objects according to their shape attributes.

    The ShapeRelabelImageFilter relabels a label collection image
    according to the shape attributes of the objects. The label produced
    are always consecutives.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_SetAttribute)
    __swig_destroy__ = _itkShapeRelabelLabelMapFilterPython.delete_itkShapeRelabelLabelMapFilterLM3
    cast = _swig_new_static_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkShapeRelabelLabelMapFilterLM3

        Create a new object of the class itkShapeRelabelLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeRelabelLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeRelabelLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeRelabelLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeRelabelLabelMapFilterLM3 in _itkShapeRelabelLabelMapFilterPython:
_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_swigregister(itkShapeRelabelLabelMapFilterLM3)
itkShapeRelabelLabelMapFilterLM3___New_orig__ = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3___New_orig__
itkShapeRelabelLabelMapFilterLM3_cast = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3_cast


def itkShapeRelabelLabelMapFilterLM4_New():
    return itkShapeRelabelLabelMapFilterLM4.New()

class itkShapeRelabelLabelMapFilterLM4(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4):
    r"""


    Relabels objects according to their shape attributes.

    The ShapeRelabelImageFilter relabels a label collection image
    according to the shape attributes of the objects. The label produced
    are always consecutives.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4_ReverseOrderingOff)
    GetAttribute = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4_SetAttribute)
    __swig_destroy__ = _itkShapeRelabelLabelMapFilterPython.delete_itkShapeRelabelLabelMapFilterLM4
    cast = _swig_new_static_method(_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkShapeRelabelLabelMapFilterLM4

        Create a new object of the class itkShapeRelabelLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeRelabelLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeRelabelLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeRelabelLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeRelabelLabelMapFilterLM4 in _itkShapeRelabelLabelMapFilterPython:
_itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4_swigregister(itkShapeRelabelLabelMapFilterLM4)
itkShapeRelabelLabelMapFilterLM4___New_orig__ = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4___New_orig__
itkShapeRelabelLabelMapFilterLM4_cast = _itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def shape_relabel_label_map_filter(*args: itkt.ImageLike,  reverse_ordering: bool=..., attribute: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for ShapeRelabelLabelMapFilter"""
    import itk

    kwarg_typehints = { 'reverse_ordering':reverse_ordering,'attribute':attribute }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ShapeRelabelLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def shape_relabel_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.ShapeRelabelLabelMapFilter
    shape_relabel_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    shape_relabel_label_map_filter.__doc__ = filter_object.__doc__




