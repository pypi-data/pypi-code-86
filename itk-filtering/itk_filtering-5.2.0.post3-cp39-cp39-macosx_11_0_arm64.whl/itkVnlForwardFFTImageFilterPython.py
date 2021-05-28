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
    from . import _itkVnlForwardFFTImageFilterPython
else:
    import _itkVnlForwardFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVnlForwardFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVnlForwardFFTImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkForwardFFTImageFilterPython
import itk.itkImageToImageFilterBPython
import itk.itkImageSourcePython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkImagePython
import itk.stdcomplexPython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkRGBAPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython

def itkVnlForwardFFTImageFilterID2ICD2_New():
    return itkVnlForwardFFTImageFilterID2ICD2.New()

class itkVnlForwardFFTImageFilterID2ICD2(itk.itkForwardFFTImageFilterPython.itkForwardFFTImageFilterID2ICD2):
    r"""


    VNL based forward Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID2ICD2___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID2ICD2_Clone)
    ImageDimensionsMatchCheck = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID2ICD2_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlForwardFFTImageFilterPython.delete_itkVnlForwardFFTImageFilterID2ICD2
    cast = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID2ICD2_cast)

    def New(*args, **kargs):
        """New() -> itkVnlForwardFFTImageFilterID2ICD2

        Create a new object of the class itkVnlForwardFFTImageFilterID2ICD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlForwardFFTImageFilterID2ICD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlForwardFFTImageFilterID2ICD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlForwardFFTImageFilterID2ICD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlForwardFFTImageFilterID2ICD2 in _itkVnlForwardFFTImageFilterPython:
_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID2ICD2_swigregister(itkVnlForwardFFTImageFilterID2ICD2)
itkVnlForwardFFTImageFilterID2ICD2___New_orig__ = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID2ICD2___New_orig__
itkVnlForwardFFTImageFilterID2ICD2_cast = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID2ICD2_cast


def itkVnlForwardFFTImageFilterID3ICD3_New():
    return itkVnlForwardFFTImageFilterID3ICD3.New()

class itkVnlForwardFFTImageFilterID3ICD3(itk.itkForwardFFTImageFilterPython.itkForwardFFTImageFilterID3ICD3):
    r"""


    VNL based forward Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID3ICD3___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID3ICD3_Clone)
    ImageDimensionsMatchCheck = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID3ICD3_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlForwardFFTImageFilterPython.delete_itkVnlForwardFFTImageFilterID3ICD3
    cast = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID3ICD3_cast)

    def New(*args, **kargs):
        """New() -> itkVnlForwardFFTImageFilterID3ICD3

        Create a new object of the class itkVnlForwardFFTImageFilterID3ICD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlForwardFFTImageFilterID3ICD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlForwardFFTImageFilterID3ICD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlForwardFFTImageFilterID3ICD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlForwardFFTImageFilterID3ICD3 in _itkVnlForwardFFTImageFilterPython:
_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID3ICD3_swigregister(itkVnlForwardFFTImageFilterID3ICD3)
itkVnlForwardFFTImageFilterID3ICD3___New_orig__ = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID3ICD3___New_orig__
itkVnlForwardFFTImageFilterID3ICD3_cast = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID3ICD3_cast


def itkVnlForwardFFTImageFilterID4ICD4_New():
    return itkVnlForwardFFTImageFilterID4ICD4.New()

class itkVnlForwardFFTImageFilterID4ICD4(itk.itkForwardFFTImageFilterPython.itkForwardFFTImageFilterID4ICD4):
    r"""


    VNL based forward Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID4ICD4___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID4ICD4_Clone)
    ImageDimensionsMatchCheck = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID4ICD4_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlForwardFFTImageFilterPython.delete_itkVnlForwardFFTImageFilterID4ICD4
    cast = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID4ICD4_cast)

    def New(*args, **kargs):
        """New() -> itkVnlForwardFFTImageFilterID4ICD4

        Create a new object of the class itkVnlForwardFFTImageFilterID4ICD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlForwardFFTImageFilterID4ICD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlForwardFFTImageFilterID4ICD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlForwardFFTImageFilterID4ICD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlForwardFFTImageFilterID4ICD4 in _itkVnlForwardFFTImageFilterPython:
_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID4ICD4_swigregister(itkVnlForwardFFTImageFilterID4ICD4)
itkVnlForwardFFTImageFilterID4ICD4___New_orig__ = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID4ICD4___New_orig__
itkVnlForwardFFTImageFilterID4ICD4_cast = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterID4ICD4_cast


def itkVnlForwardFFTImageFilterIF2ICF2_New():
    return itkVnlForwardFFTImageFilterIF2ICF2.New()

class itkVnlForwardFFTImageFilterIF2ICF2(itk.itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF2ICF2):
    r"""


    VNL based forward Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2_Clone)
    ImageDimensionsMatchCheck = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlForwardFFTImageFilterPython.delete_itkVnlForwardFFTImageFilterIF2ICF2
    cast = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2_cast)

    def New(*args, **kargs):
        """New() -> itkVnlForwardFFTImageFilterIF2ICF2

        Create a new object of the class itkVnlForwardFFTImageFilterIF2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlForwardFFTImageFilterIF2ICF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlForwardFFTImageFilterIF2ICF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlForwardFFTImageFilterIF2ICF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlForwardFFTImageFilterIF2ICF2 in _itkVnlForwardFFTImageFilterPython:
_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2_swigregister(itkVnlForwardFFTImageFilterIF2ICF2)
itkVnlForwardFFTImageFilterIF2ICF2___New_orig__ = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2___New_orig__
itkVnlForwardFFTImageFilterIF2ICF2_cast = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF2ICF2_cast


def itkVnlForwardFFTImageFilterIF3ICF3_New():
    return itkVnlForwardFFTImageFilterIF3ICF3.New()

class itkVnlForwardFFTImageFilterIF3ICF3(itk.itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF3ICF3):
    r"""


    VNL based forward Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3_Clone)
    ImageDimensionsMatchCheck = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlForwardFFTImageFilterPython.delete_itkVnlForwardFFTImageFilterIF3ICF3
    cast = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3_cast)

    def New(*args, **kargs):
        """New() -> itkVnlForwardFFTImageFilterIF3ICF3

        Create a new object of the class itkVnlForwardFFTImageFilterIF3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlForwardFFTImageFilterIF3ICF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlForwardFFTImageFilterIF3ICF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlForwardFFTImageFilterIF3ICF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlForwardFFTImageFilterIF3ICF3 in _itkVnlForwardFFTImageFilterPython:
_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3_swigregister(itkVnlForwardFFTImageFilterIF3ICF3)
itkVnlForwardFFTImageFilterIF3ICF3___New_orig__ = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3___New_orig__
itkVnlForwardFFTImageFilterIF3ICF3_cast = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF3ICF3_cast


def itkVnlForwardFFTImageFilterIF4ICF4_New():
    return itkVnlForwardFFTImageFilterIF4ICF4.New()

class itkVnlForwardFFTImageFilterIF4ICF4(itk.itkForwardFFTImageFilterPython.itkForwardFFTImageFilterIF4ICF4):
    r"""


    VNL based forward Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF4ICF4___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF4ICF4_Clone)
    ImageDimensionsMatchCheck = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF4ICF4_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlForwardFFTImageFilterPython.delete_itkVnlForwardFFTImageFilterIF4ICF4
    cast = _swig_new_static_method(_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF4ICF4_cast)

    def New(*args, **kargs):
        """New() -> itkVnlForwardFFTImageFilterIF4ICF4

        Create a new object of the class itkVnlForwardFFTImageFilterIF4ICF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlForwardFFTImageFilterIF4ICF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlForwardFFTImageFilterIF4ICF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlForwardFFTImageFilterIF4ICF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlForwardFFTImageFilterIF4ICF4 in _itkVnlForwardFFTImageFilterPython:
_itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF4ICF4_swigregister(itkVnlForwardFFTImageFilterIF4ICF4)
itkVnlForwardFFTImageFilterIF4ICF4___New_orig__ = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF4ICF4___New_orig__
itkVnlForwardFFTImageFilterIF4ICF4_cast = _itkVnlForwardFFTImageFilterPython.itkVnlForwardFFTImageFilterIF4ICF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def vnl_forward_fft_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for VnlForwardFFTImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.VnlForwardFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def vnl_forward_fft_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKFFT.VnlForwardFFTImageFilter
    vnl_forward_fft_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    vnl_forward_fft_image_filter.__doc__ = filter_object.__doc__




