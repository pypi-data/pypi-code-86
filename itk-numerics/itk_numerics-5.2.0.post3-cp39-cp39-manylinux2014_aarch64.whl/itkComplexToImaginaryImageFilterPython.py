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
    from . import _itkComplexToImaginaryImageFilterPython
else:
    import _itkComplexToImaginaryImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkComplexToImaginaryImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkComplexToImaginaryImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkUnaryGeneratorImageFilterPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkInPlaceImageFilterBPython
import itk.itkImageToImageFilterBPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.itkRGBPixelPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterAPython

def itkComplexToImaginaryImageFilterICD2ID2_New():
    return itkComplexToImaginaryImageFilterICD2ID2.New()

class itkComplexToImaginaryImageFilterICD2ID2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICD2ID2):
    r"""


    Computes pixel-wise the imaginary part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD2ID2_Clone)
    InputConvertibleToOutputCheck = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD2ID2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToImaginaryImageFilterPython.delete_itkComplexToImaginaryImageFilterICD2ID2
    cast = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToImaginaryImageFilterICD2ID2

        Create a new object of the class itkComplexToImaginaryImageFilterICD2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToImaginaryImageFilterICD2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToImaginaryImageFilterICD2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToImaginaryImageFilterICD2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToImaginaryImageFilterICD2ID2 in _itkComplexToImaginaryImageFilterPython:
_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD2ID2_swigregister(itkComplexToImaginaryImageFilterICD2ID2)
itkComplexToImaginaryImageFilterICD2ID2___New_orig__ = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD2ID2___New_orig__
itkComplexToImaginaryImageFilterICD2ID2_cast = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD2ID2_cast


def itkComplexToImaginaryImageFilterICD3ID3_New():
    return itkComplexToImaginaryImageFilterICD3ID3.New()

class itkComplexToImaginaryImageFilterICD3ID3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICD3ID3):
    r"""


    Computes pixel-wise the imaginary part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD3ID3_Clone)
    InputConvertibleToOutputCheck = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD3ID3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToImaginaryImageFilterPython.delete_itkComplexToImaginaryImageFilterICD3ID3
    cast = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToImaginaryImageFilterICD3ID3

        Create a new object of the class itkComplexToImaginaryImageFilterICD3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToImaginaryImageFilterICD3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToImaginaryImageFilterICD3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToImaginaryImageFilterICD3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToImaginaryImageFilterICD3ID3 in _itkComplexToImaginaryImageFilterPython:
_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD3ID3_swigregister(itkComplexToImaginaryImageFilterICD3ID3)
itkComplexToImaginaryImageFilterICD3ID3___New_orig__ = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD3ID3___New_orig__
itkComplexToImaginaryImageFilterICD3ID3_cast = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD3ID3_cast


def itkComplexToImaginaryImageFilterICD4ID4_New():
    return itkComplexToImaginaryImageFilterICD4ID4.New()

class itkComplexToImaginaryImageFilterICD4ID4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICD4ID4):
    r"""


    Computes pixel-wise the imaginary part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD4ID4_Clone)
    InputConvertibleToOutputCheck = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD4ID4_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToImaginaryImageFilterPython.delete_itkComplexToImaginaryImageFilterICD4ID4
    cast = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToImaginaryImageFilterICD4ID4

        Create a new object of the class itkComplexToImaginaryImageFilterICD4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToImaginaryImageFilterICD4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToImaginaryImageFilterICD4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToImaginaryImageFilterICD4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToImaginaryImageFilterICD4ID4 in _itkComplexToImaginaryImageFilterPython:
_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD4ID4_swigregister(itkComplexToImaginaryImageFilterICD4ID4)
itkComplexToImaginaryImageFilterICD4ID4___New_orig__ = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD4ID4___New_orig__
itkComplexToImaginaryImageFilterICD4ID4_cast = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICD4ID4_cast


def itkComplexToImaginaryImageFilterICF2IF2_New():
    return itkComplexToImaginaryImageFilterICF2IF2.New()

class itkComplexToImaginaryImageFilterICF2IF2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICF2IF2):
    r"""


    Computes pixel-wise the imaginary part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_Clone)
    InputConvertibleToOutputCheck = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToImaginaryImageFilterPython.delete_itkComplexToImaginaryImageFilterICF2IF2
    cast = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToImaginaryImageFilterICF2IF2

        Create a new object of the class itkComplexToImaginaryImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToImaginaryImageFilterICF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToImaginaryImageFilterICF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToImaginaryImageFilterICF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToImaginaryImageFilterICF2IF2 in _itkComplexToImaginaryImageFilterPython:
_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_swigregister(itkComplexToImaginaryImageFilterICF2IF2)
itkComplexToImaginaryImageFilterICF2IF2___New_orig__ = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2___New_orig__
itkComplexToImaginaryImageFilterICF2IF2_cast = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF2IF2_cast


def itkComplexToImaginaryImageFilterICF3IF3_New():
    return itkComplexToImaginaryImageFilterICF3IF3.New()

class itkComplexToImaginaryImageFilterICF3IF3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICF3IF3):
    r"""


    Computes pixel-wise the imaginary part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_Clone)
    InputConvertibleToOutputCheck = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToImaginaryImageFilterPython.delete_itkComplexToImaginaryImageFilterICF3IF3
    cast = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToImaginaryImageFilterICF3IF3

        Create a new object of the class itkComplexToImaginaryImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToImaginaryImageFilterICF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToImaginaryImageFilterICF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToImaginaryImageFilterICF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToImaginaryImageFilterICF3IF3 in _itkComplexToImaginaryImageFilterPython:
_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_swigregister(itkComplexToImaginaryImageFilterICF3IF3)
itkComplexToImaginaryImageFilterICF3IF3___New_orig__ = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3___New_orig__
itkComplexToImaginaryImageFilterICF3IF3_cast = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF3IF3_cast


def itkComplexToImaginaryImageFilterICF4IF4_New():
    return itkComplexToImaginaryImageFilterICF4IF4.New()

class itkComplexToImaginaryImageFilterICF4IF4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterICF4IF4):
    r"""


    Computes pixel-wise the imaginary part of a complex image. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF4IF4_Clone)
    InputConvertibleToOutputCheck = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF4IF4_InputConvertibleToOutputCheck
    
    __swig_destroy__ = _itkComplexToImaginaryImageFilterPython.delete_itkComplexToImaginaryImageFilterICF4IF4
    cast = _swig_new_static_method(_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkComplexToImaginaryImageFilterICF4IF4

        Create a new object of the class itkComplexToImaginaryImageFilterICF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComplexToImaginaryImageFilterICF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComplexToImaginaryImageFilterICF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComplexToImaginaryImageFilterICF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComplexToImaginaryImageFilterICF4IF4 in _itkComplexToImaginaryImageFilterPython:
_itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF4IF4_swigregister(itkComplexToImaginaryImageFilterICF4IF4)
itkComplexToImaginaryImageFilterICF4IF4___New_orig__ = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF4IF4___New_orig__
itkComplexToImaginaryImageFilterICF4IF4_cast = _itkComplexToImaginaryImageFilterPython.itkComplexToImaginaryImageFilterICF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def complex_to_imaginary_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for ComplexToImaginaryImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ComplexToImaginaryImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def complex_to_imaginary_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.ComplexToImaginaryImageFilter
    complex_to_imaginary_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    complex_to_imaginary_image_filter.__doc__ = filter_object.__doc__




