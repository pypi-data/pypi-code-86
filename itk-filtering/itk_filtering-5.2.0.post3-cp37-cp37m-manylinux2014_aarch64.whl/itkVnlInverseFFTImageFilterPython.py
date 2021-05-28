# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKFFTPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkVnlInverseFFTImageFilterPython
else:
    import _itkVnlInverseFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVnlInverseFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVnlInverseFFTImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkInverseFFTImageFilterPython
import itk.itkImageToImageFilterBPython
import itk.itkVectorImagePython
import itk.stdcomplexPython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
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
import itk.itkVariableLengthVectorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython

def itkVnlInverseFFTImageFilterICD2ID2_New():
    return itkVnlInverseFFTImageFilterICD2ID2.New()

class itkVnlInverseFFTImageFilterICD2ID2(itk.itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD2ID2):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   InverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD2ID2_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD2ID2_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD2ID2_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlInverseFFTImageFilterPython.delete_itkVnlInverseFFTImageFilterICD2ID2
    cast = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkVnlInverseFFTImageFilterICD2ID2

        Create a new object of the class itkVnlInverseFFTImageFilterICD2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlInverseFFTImageFilterICD2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlInverseFFTImageFilterICD2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlInverseFFTImageFilterICD2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlInverseFFTImageFilterICD2ID2 in _itkVnlInverseFFTImageFilterPython:
_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD2ID2_swigregister(itkVnlInverseFFTImageFilterICD2ID2)
itkVnlInverseFFTImageFilterICD2ID2___New_orig__ = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD2ID2___New_orig__
itkVnlInverseFFTImageFilterICD2ID2_cast = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD2ID2_cast


def itkVnlInverseFFTImageFilterICD3ID3_New():
    return itkVnlInverseFFTImageFilterICD3ID3.New()

class itkVnlInverseFFTImageFilterICD3ID3(itk.itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD3ID3):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   InverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD3ID3_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD3ID3_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD3ID3_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlInverseFFTImageFilterPython.delete_itkVnlInverseFFTImageFilterICD3ID3
    cast = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkVnlInverseFFTImageFilterICD3ID3

        Create a new object of the class itkVnlInverseFFTImageFilterICD3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlInverseFFTImageFilterICD3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlInverseFFTImageFilterICD3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlInverseFFTImageFilterICD3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlInverseFFTImageFilterICD3ID3 in _itkVnlInverseFFTImageFilterPython:
_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD3ID3_swigregister(itkVnlInverseFFTImageFilterICD3ID3)
itkVnlInverseFFTImageFilterICD3ID3___New_orig__ = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD3ID3___New_orig__
itkVnlInverseFFTImageFilterICD3ID3_cast = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD3ID3_cast


def itkVnlInverseFFTImageFilterICD4ID4_New():
    return itkVnlInverseFFTImageFilterICD4ID4.New()

class itkVnlInverseFFTImageFilterICD4ID4(itk.itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD4ID4):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   InverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD4ID4_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD4ID4_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD4ID4_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlInverseFFTImageFilterPython.delete_itkVnlInverseFFTImageFilterICD4ID4
    cast = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkVnlInverseFFTImageFilterICD4ID4

        Create a new object of the class itkVnlInverseFFTImageFilterICD4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlInverseFFTImageFilterICD4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlInverseFFTImageFilterICD4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlInverseFFTImageFilterICD4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlInverseFFTImageFilterICD4ID4 in _itkVnlInverseFFTImageFilterPython:
_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD4ID4_swigregister(itkVnlInverseFFTImageFilterICD4ID4)
itkVnlInverseFFTImageFilterICD4ID4___New_orig__ = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD4ID4___New_orig__
itkVnlInverseFFTImageFilterICD4ID4_cast = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICD4ID4_cast


def itkVnlInverseFFTImageFilterICF2IF2_New():
    return itkVnlInverseFFTImageFilterICF2IF2.New()

class itkVnlInverseFFTImageFilterICF2IF2(itk.itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   InverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlInverseFFTImageFilterPython.delete_itkVnlInverseFFTImageFilterICF2IF2
    cast = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkVnlInverseFFTImageFilterICF2IF2

        Create a new object of the class itkVnlInverseFFTImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlInverseFFTImageFilterICF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlInverseFFTImageFilterICF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlInverseFFTImageFilterICF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlInverseFFTImageFilterICF2IF2 in _itkVnlInverseFFTImageFilterPython:
_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_swigregister(itkVnlInverseFFTImageFilterICF2IF2)
itkVnlInverseFFTImageFilterICF2IF2___New_orig__ = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2___New_orig__
itkVnlInverseFFTImageFilterICF2IF2_cast = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF2IF2_cast


def itkVnlInverseFFTImageFilterICF3IF3_New():
    return itkVnlInverseFFTImageFilterICF3IF3.New()

class itkVnlInverseFFTImageFilterICF3IF3(itk.itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   InverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlInverseFFTImageFilterPython.delete_itkVnlInverseFFTImageFilterICF3IF3
    cast = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkVnlInverseFFTImageFilterICF3IF3

        Create a new object of the class itkVnlInverseFFTImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlInverseFFTImageFilterICF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlInverseFFTImageFilterICF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlInverseFFTImageFilterICF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlInverseFFTImageFilterICF3IF3 in _itkVnlInverseFFTImageFilterPython:
_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_swigregister(itkVnlInverseFFTImageFilterICF3IF3)
itkVnlInverseFFTImageFilterICF3IF3___New_orig__ = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3___New_orig__
itkVnlInverseFFTImageFilterICF3IF3_cast = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF3IF3_cast


def itkVnlInverseFFTImageFilterICF4IF4_New():
    return itkVnlInverseFFTImageFilterICF4IF4.New()

class itkVnlInverseFFTImageFilterICF4IF4(itk.itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF4IF4):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   InverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF4IF4_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF4IF4_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF4IF4_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlInverseFFTImageFilterPython.delete_itkVnlInverseFFTImageFilterICF4IF4
    cast = _swig_new_static_method(_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkVnlInverseFFTImageFilterICF4IF4

        Create a new object of the class itkVnlInverseFFTImageFilterICF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlInverseFFTImageFilterICF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlInverseFFTImageFilterICF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlInverseFFTImageFilterICF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlInverseFFTImageFilterICF4IF4 in _itkVnlInverseFFTImageFilterPython:
_itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF4IF4_swigregister(itkVnlInverseFFTImageFilterICF4IF4)
itkVnlInverseFFTImageFilterICF4IF4___New_orig__ = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF4IF4___New_orig__
itkVnlInverseFFTImageFilterICF4IF4_cast = _itkVnlInverseFFTImageFilterPython.itkVnlInverseFFTImageFilterICF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def vnl_inverse_fft_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for VnlInverseFFTImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.VnlInverseFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def vnl_inverse_fft_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKFFT.VnlInverseFFTImageFilter
    vnl_inverse_fft_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    vnl_inverse_fft_image_filter.__doc__ = filter_object.__doc__




