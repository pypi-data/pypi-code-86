# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageIntensityPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkComplexToRealImageFilterPython
else:
    import _itkComplexToRealImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkComplexToRealImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkComplexToRealImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkUnaryGeneratorImageFilterPython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterBPython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.stdcomplexPython
import itk.itkImagePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkFixedArrayPython
import itk.itkMatrixPython
import itk.vnl_matrixPython
import itk.vnl_vectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterAPython
import itk.itkInPlaceImageFilterBPython

def itkComplexToRealImageFilterICD2ID2_New():
    return itkComplexToRealImageFilterICD2ID2.New()

class itkComplexToRealImageFilterICD2ID2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICD2ID2):
    r"""


    Computes pixel-wise the real(x) part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD2ID2_Clone)
    InputConvertibleToOutputCheck = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD2ID2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToRealImageFilterPython.delete_itkComplexToRealImageFilterICD2ID2
    cast = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToRealImageFilterICD2ID2

        Create a new object of the class itkComplexToRealImageFilterICD2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToRealImageFilterICD2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToRealImageFilterICD2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToRealImageFilterICD2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToRealImageFilterICD2ID2 in _itkComplexToRealImageFilterPython:
_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD2ID2_swigregister(itkComplexToRealImageFilterICD2ID2)
itkComplexToRealImageFilterICD2ID2___New_orig__ = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD2ID2___New_orig__
itkComplexToRealImageFilterICD2ID2_cast = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD2ID2_cast


def itkComplexToRealImageFilterICD3ID3_New():
    return itkComplexToRealImageFilterICD3ID3.New()

class itkComplexToRealImageFilterICD3ID3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICD3ID3):
    r"""


    Computes pixel-wise the real(x) part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD3ID3_Clone)
    InputConvertibleToOutputCheck = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD3ID3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToRealImageFilterPython.delete_itkComplexToRealImageFilterICD3ID3
    cast = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToRealImageFilterICD3ID3

        Create a new object of the class itkComplexToRealImageFilterICD3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToRealImageFilterICD3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToRealImageFilterICD3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToRealImageFilterICD3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToRealImageFilterICD3ID3 in _itkComplexToRealImageFilterPython:
_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD3ID3_swigregister(itkComplexToRealImageFilterICD3ID3)
itkComplexToRealImageFilterICD3ID3___New_orig__ = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD3ID3___New_orig__
itkComplexToRealImageFilterICD3ID3_cast = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD3ID3_cast


def itkComplexToRealImageFilterICD4ID4_New():
    return itkComplexToRealImageFilterICD4ID4.New()

class itkComplexToRealImageFilterICD4ID4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICD4ID4):
    r"""


    Computes pixel-wise the real(x) part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD4ID4_Clone)
    InputConvertibleToOutputCheck = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD4ID4_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToRealImageFilterPython.delete_itkComplexToRealImageFilterICD4ID4
    cast = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToRealImageFilterICD4ID4

        Create a new object of the class itkComplexToRealImageFilterICD4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToRealImageFilterICD4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToRealImageFilterICD4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToRealImageFilterICD4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToRealImageFilterICD4ID4 in _itkComplexToRealImageFilterPython:
_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD4ID4_swigregister(itkComplexToRealImageFilterICD4ID4)
itkComplexToRealImageFilterICD4ID4___New_orig__ = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD4ID4___New_orig__
itkComplexToRealImageFilterICD4ID4_cast = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICD4ID4_cast


def itkComplexToRealImageFilterICF2IF2_New():
    return itkComplexToRealImageFilterICF2IF2.New()

class itkComplexToRealImageFilterICF2IF2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICF2IF2):
    r"""


    Computes pixel-wise the real(x) part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF2IF2_Clone)
    InputConvertibleToOutputCheck = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF2IF2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToRealImageFilterPython.delete_itkComplexToRealImageFilterICF2IF2
    cast = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToRealImageFilterICF2IF2

        Create a new object of the class itkComplexToRealImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToRealImageFilterICF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToRealImageFilterICF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToRealImageFilterICF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToRealImageFilterICF2IF2 in _itkComplexToRealImageFilterPython:
_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF2IF2_swigregister(itkComplexToRealImageFilterICF2IF2)
itkComplexToRealImageFilterICF2IF2___New_orig__ = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF2IF2___New_orig__
itkComplexToRealImageFilterICF2IF2_cast = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF2IF2_cast


def itkComplexToRealImageFilterICF3IF3_New():
    return itkComplexToRealImageFilterICF3IF3.New()

class itkComplexToRealImageFilterICF3IF3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICF3IF3):
    r"""


    Computes pixel-wise the real(x) part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF3IF3_Clone)
    InputConvertibleToOutputCheck = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF3IF3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToRealImageFilterPython.delete_itkComplexToRealImageFilterICF3IF3
    cast = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToRealImageFilterICF3IF3

        Create a new object of the class itkComplexToRealImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToRealImageFilterICF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToRealImageFilterICF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToRealImageFilterICF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToRealImageFilterICF3IF3 in _itkComplexToRealImageFilterPython:
_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF3IF3_swigregister(itkComplexToRealImageFilterICF3IF3)
itkComplexToRealImageFilterICF3IF3___New_orig__ = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF3IF3___New_orig__
itkComplexToRealImageFilterICF3IF3_cast = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF3IF3_cast


def itkComplexToRealImageFilterICF4IF4_New():
    return itkComplexToRealImageFilterICF4IF4.New()

class itkComplexToRealImageFilterICF4IF4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICF4IF4):
    r"""


    Computes pixel-wise the real(x) part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF4IF4_Clone)
    InputConvertibleToOutputCheck = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF4IF4_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToRealImageFilterPython.delete_itkComplexToRealImageFilterICF4IF4
    cast = _swig_new_static_method(_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToRealImageFilterICF4IF4

        Create a new object of the class itkComplexToRealImageFilterICF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToRealImageFilterICF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToRealImageFilterICF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToRealImageFilterICF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToRealImageFilterICF4IF4 in _itkComplexToRealImageFilterPython:
_itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF4IF4_swigregister(itkComplexToRealImageFilterICF4IF4)
itkComplexToRealImageFilterICF4IF4___New_orig__ = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF4IF4___New_orig__
itkComplexToRealImageFilterICF4IF4_cast = _itkComplexToRealImageFilterPython.itkComplexToRealImageFilterICF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def complex_to_real_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for ComplexToRealImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ComplexToRealImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def complex_to_real_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.ComplexToRealImageFilter
    complex_to_real_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    complex_to_real_image_filter.__doc__ = filter_object.__doc__




