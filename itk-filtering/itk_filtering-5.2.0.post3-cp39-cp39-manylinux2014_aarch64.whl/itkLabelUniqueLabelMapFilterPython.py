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
    from . import _itkLabelUniqueLabelMapFilterPython
else:
    import _itkLabelUniqueLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelUniqueLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelUniqueLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkInPlaceLabelMapFilterPython
import itk.ITKCommonBasePython
import itk.pyBasePython
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

def itkLabelUniqueLabelMapFilterLM2_Superclass_New():
    return itkLabelUniqueLabelMapFilterLM2_Superclass.New()

class itkLabelUniqueLabelMapFilterLM2_Superclass(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    r"""Proxy of C++ itkLabelUniqueLabelMapFilterLM2_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_ReverseOrderingOff)
    __swig_destroy__ = _itkLabelUniqueLabelMapFilterPython.delete_itkLabelUniqueLabelMapFilterLM2_Superclass
    cast = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkLabelUniqueLabelMapFilterLM2_Superclass

        Create a new object of the class itkLabelUniqueLabelMapFilterLM2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelUniqueLabelMapFilterLM2_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelUniqueLabelMapFilterLM2_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelUniqueLabelMapFilterLM2_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelUniqueLabelMapFilterLM2_Superclass in _itkLabelUniqueLabelMapFilterPython:
_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_swigregister(itkLabelUniqueLabelMapFilterLM2_Superclass)
itkLabelUniqueLabelMapFilterLM2_Superclass___New_orig__ = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass___New_orig__
itkLabelUniqueLabelMapFilterLM2_Superclass_cast = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Superclass_cast


def itkLabelUniqueLabelMapFilterLM3_Superclass_New():
    return itkLabelUniqueLabelMapFilterLM3_Superclass.New()

class itkLabelUniqueLabelMapFilterLM3_Superclass(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    r"""Proxy of C++ itkLabelUniqueLabelMapFilterLM3_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_ReverseOrderingOff)
    __swig_destroy__ = _itkLabelUniqueLabelMapFilterPython.delete_itkLabelUniqueLabelMapFilterLM3_Superclass
    cast = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkLabelUniqueLabelMapFilterLM3_Superclass

        Create a new object of the class itkLabelUniqueLabelMapFilterLM3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelUniqueLabelMapFilterLM3_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelUniqueLabelMapFilterLM3_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelUniqueLabelMapFilterLM3_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelUniqueLabelMapFilterLM3_Superclass in _itkLabelUniqueLabelMapFilterPython:
_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_swigregister(itkLabelUniqueLabelMapFilterLM3_Superclass)
itkLabelUniqueLabelMapFilterLM3_Superclass___New_orig__ = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass___New_orig__
itkLabelUniqueLabelMapFilterLM3_Superclass_cast = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Superclass_cast


def itkLabelUniqueLabelMapFilterLM4_Superclass_New():
    return itkLabelUniqueLabelMapFilterLM4_Superclass.New()

class itkLabelUniqueLabelMapFilterLM4_Superclass(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4):
    r"""Proxy of C++ itkLabelUniqueLabelMapFilterLM4_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_Superclass_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_Superclass_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_Superclass_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_Superclass_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_Superclass_ReverseOrderingOff)
    __swig_destroy__ = _itkLabelUniqueLabelMapFilterPython.delete_itkLabelUniqueLabelMapFilterLM4_Superclass
    cast = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkLabelUniqueLabelMapFilterLM4_Superclass

        Create a new object of the class itkLabelUniqueLabelMapFilterLM4_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelUniqueLabelMapFilterLM4_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelUniqueLabelMapFilterLM4_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelUniqueLabelMapFilterLM4_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelUniqueLabelMapFilterLM4_Superclass in _itkLabelUniqueLabelMapFilterPython:
_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_Superclass_swigregister(itkLabelUniqueLabelMapFilterLM4_Superclass)
itkLabelUniqueLabelMapFilterLM4_Superclass___New_orig__ = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_Superclass___New_orig__
itkLabelUniqueLabelMapFilterLM4_Superclass_cast = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_Superclass_cast


def itkLabelUniqueLabelMapFilterLM2_New():
    return itkLabelUniqueLabelMapFilterLM2.New()

class itkLabelUniqueLabelMapFilterLM2(itkLabelUniqueLabelMapFilterLM2_Superclass):
    r"""


    Make sure that the objects are not overlapping.

    AttributeUniqueLabelMapFilter search the overlapping zones in the
    overlapping objects and keeps only a single object on all the pixels
    of the image. The object to keep is selected according to their label.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:  AttributeLabelObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_Clone)
    __swig_destroy__ = _itkLabelUniqueLabelMapFilterPython.delete_itkLabelUniqueLabelMapFilterLM2
    cast = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelUniqueLabelMapFilterLM2

        Create a new object of the class itkLabelUniqueLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelUniqueLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelUniqueLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelUniqueLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelUniqueLabelMapFilterLM2 in _itkLabelUniqueLabelMapFilterPython:
_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_swigregister(itkLabelUniqueLabelMapFilterLM2)
itkLabelUniqueLabelMapFilterLM2___New_orig__ = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2___New_orig__
itkLabelUniqueLabelMapFilterLM2_cast = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM2_cast


def itkLabelUniqueLabelMapFilterLM3_New():
    return itkLabelUniqueLabelMapFilterLM3.New()

class itkLabelUniqueLabelMapFilterLM3(itkLabelUniqueLabelMapFilterLM3_Superclass):
    r"""


    Make sure that the objects are not overlapping.

    AttributeUniqueLabelMapFilter search the overlapping zones in the
    overlapping objects and keeps only a single object on all the pixels
    of the image. The object to keep is selected according to their label.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:  AttributeLabelObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_Clone)
    __swig_destroy__ = _itkLabelUniqueLabelMapFilterPython.delete_itkLabelUniqueLabelMapFilterLM3
    cast = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelUniqueLabelMapFilterLM3

        Create a new object of the class itkLabelUniqueLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelUniqueLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelUniqueLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelUniqueLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelUniqueLabelMapFilterLM3 in _itkLabelUniqueLabelMapFilterPython:
_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_swigregister(itkLabelUniqueLabelMapFilterLM3)
itkLabelUniqueLabelMapFilterLM3___New_orig__ = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3___New_orig__
itkLabelUniqueLabelMapFilterLM3_cast = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM3_cast


def itkLabelUniqueLabelMapFilterLM4_New():
    return itkLabelUniqueLabelMapFilterLM4.New()

class itkLabelUniqueLabelMapFilterLM4(itkLabelUniqueLabelMapFilterLM4_Superclass):
    r"""


    Make sure that the objects are not overlapping.

    AttributeUniqueLabelMapFilter search the overlapping zones in the
    overlapping objects and keeps only a single object on all the pixels
    of the image. The object to keep is selected according to their label.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:  AttributeLabelObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_Clone)
    __swig_destroy__ = _itkLabelUniqueLabelMapFilterPython.delete_itkLabelUniqueLabelMapFilterLM4
    cast = _swig_new_static_method(_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkLabelUniqueLabelMapFilterLM4

        Create a new object of the class itkLabelUniqueLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelUniqueLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelUniqueLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelUniqueLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelUniqueLabelMapFilterLM4 in _itkLabelUniqueLabelMapFilterPython:
_itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_swigregister(itkLabelUniqueLabelMapFilterLM4)
itkLabelUniqueLabelMapFilterLM4___New_orig__ = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4___New_orig__
itkLabelUniqueLabelMapFilterLM4_cast = _itkLabelUniqueLabelMapFilterPython.itkLabelUniqueLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def label_unique_label_map_filter(*args: itkt.ImageLike,  reverse_ordering: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for LabelUniqueLabelMapFilter"""
    import itk

    kwarg_typehints = { 'reverse_ordering':reverse_ordering }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.LabelUniqueLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_unique_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.LabelUniqueLabelMapFilter
    label_unique_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    label_unique_label_map_filter.__doc__ = filter_object.__doc__

from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def attribute_unique_label_map_filter(*args: itkt.ImageLike,  reverse_ordering: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for AttributeUniqueLabelMapFilter"""
    import itk

    kwarg_typehints = { 'reverse_ordering':reverse_ordering }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.AttributeUniqueLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def attribute_unique_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.AttributeUniqueLabelMapFilter
    attribute_unique_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    attribute_unique_label_map_filter.__doc__ = filter_object.__doc__




