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
    from . import _itkVnlComplexToComplexFFTImageFilterPython
else:
    import _itkVnlComplexToComplexFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVnlComplexToComplexFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVnlComplexToComplexFFTImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkComplexToComplexFFTImageFilterPython
import itk.itkImageToImageFilterBPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.stdcomplexPython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython

def itkVnlComplexToComplexFFTImageFilterICD2_New():
    return itkVnlComplexToComplexFFTImageFilterICD2.New()

class itkVnlComplexToComplexFFTImageFilterICD2(itk.itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICD2):
    r"""


    VNL based complex to complex Fast Fourier Transform.

    This filter requires input images with sizes which are a power of two.

    See:   ComplexToComplexFFTImageFilter

    See:  FFTWComplexToComplexFFTImageFilter

    See:   VnlForwardFFTImageFilter

    See:   VnlInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD2___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD2_Clone)
    __swig_destroy__ = _itkVnlComplexToComplexFFTImageFilterPython.delete_itkVnlComplexToComplexFFTImageFilterICD2
    cast = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD2_cast)

    def New(*args, **kargs):
        """New() -> itkVnlComplexToComplexFFTImageFilterICD2

        Create a new object of the class itkVnlComplexToComplexFFTImageFilterICD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlComplexToComplexFFTImageFilterICD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlComplexToComplexFFTImageFilterICD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlComplexToComplexFFTImageFilterICD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlComplexToComplexFFTImageFilterICD2 in _itkVnlComplexToComplexFFTImageFilterPython:
_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD2_swigregister(itkVnlComplexToComplexFFTImageFilterICD2)
itkVnlComplexToComplexFFTImageFilterICD2___New_orig__ = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD2___New_orig__
itkVnlComplexToComplexFFTImageFilterICD2_cast = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD2_cast


def itkVnlComplexToComplexFFTImageFilterICD3_New():
    return itkVnlComplexToComplexFFTImageFilterICD3.New()

class itkVnlComplexToComplexFFTImageFilterICD3(itk.itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICD3):
    r"""


    VNL based complex to complex Fast Fourier Transform.

    This filter requires input images with sizes which are a power of two.

    See:   ComplexToComplexFFTImageFilter

    See:  FFTWComplexToComplexFFTImageFilter

    See:   VnlForwardFFTImageFilter

    See:   VnlInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD3___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD3_Clone)
    __swig_destroy__ = _itkVnlComplexToComplexFFTImageFilterPython.delete_itkVnlComplexToComplexFFTImageFilterICD3
    cast = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD3_cast)

    def New(*args, **kargs):
        """New() -> itkVnlComplexToComplexFFTImageFilterICD3

        Create a new object of the class itkVnlComplexToComplexFFTImageFilterICD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlComplexToComplexFFTImageFilterICD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlComplexToComplexFFTImageFilterICD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlComplexToComplexFFTImageFilterICD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlComplexToComplexFFTImageFilterICD3 in _itkVnlComplexToComplexFFTImageFilterPython:
_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD3_swigregister(itkVnlComplexToComplexFFTImageFilterICD3)
itkVnlComplexToComplexFFTImageFilterICD3___New_orig__ = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD3___New_orig__
itkVnlComplexToComplexFFTImageFilterICD3_cast = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD3_cast


def itkVnlComplexToComplexFFTImageFilterICD4_New():
    return itkVnlComplexToComplexFFTImageFilterICD4.New()

class itkVnlComplexToComplexFFTImageFilterICD4(itk.itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICD4):
    r"""


    VNL based complex to complex Fast Fourier Transform.

    This filter requires input images with sizes which are a power of two.

    See:   ComplexToComplexFFTImageFilter

    See:  FFTWComplexToComplexFFTImageFilter

    See:   VnlForwardFFTImageFilter

    See:   VnlInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD4___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD4_Clone)
    __swig_destroy__ = _itkVnlComplexToComplexFFTImageFilterPython.delete_itkVnlComplexToComplexFFTImageFilterICD4
    cast = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD4_cast)

    def New(*args, **kargs):
        """New() -> itkVnlComplexToComplexFFTImageFilterICD4

        Create a new object of the class itkVnlComplexToComplexFFTImageFilterICD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlComplexToComplexFFTImageFilterICD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlComplexToComplexFFTImageFilterICD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlComplexToComplexFFTImageFilterICD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlComplexToComplexFFTImageFilterICD4 in _itkVnlComplexToComplexFFTImageFilterPython:
_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD4_swigregister(itkVnlComplexToComplexFFTImageFilterICD4)
itkVnlComplexToComplexFFTImageFilterICD4___New_orig__ = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD4___New_orig__
itkVnlComplexToComplexFFTImageFilterICD4_cast = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICD4_cast


def itkVnlComplexToComplexFFTImageFilterICF2_New():
    return itkVnlComplexToComplexFFTImageFilterICF2.New()

class itkVnlComplexToComplexFFTImageFilterICF2(itk.itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF2):
    r"""


    VNL based complex to complex Fast Fourier Transform.

    This filter requires input images with sizes which are a power of two.

    See:   ComplexToComplexFFTImageFilter

    See:  FFTWComplexToComplexFFTImageFilter

    See:   VnlForwardFFTImageFilter

    See:   VnlInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF2___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF2_Clone)
    __swig_destroy__ = _itkVnlComplexToComplexFFTImageFilterPython.delete_itkVnlComplexToComplexFFTImageFilterICF2
    cast = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF2_cast)

    def New(*args, **kargs):
        """New() -> itkVnlComplexToComplexFFTImageFilterICF2

        Create a new object of the class itkVnlComplexToComplexFFTImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlComplexToComplexFFTImageFilterICF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlComplexToComplexFFTImageFilterICF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlComplexToComplexFFTImageFilterICF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlComplexToComplexFFTImageFilterICF2 in _itkVnlComplexToComplexFFTImageFilterPython:
_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF2_swigregister(itkVnlComplexToComplexFFTImageFilterICF2)
itkVnlComplexToComplexFFTImageFilterICF2___New_orig__ = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF2___New_orig__
itkVnlComplexToComplexFFTImageFilterICF2_cast = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF2_cast


def itkVnlComplexToComplexFFTImageFilterICF3_New():
    return itkVnlComplexToComplexFFTImageFilterICF3.New()

class itkVnlComplexToComplexFFTImageFilterICF3(itk.itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF3):
    r"""


    VNL based complex to complex Fast Fourier Transform.

    This filter requires input images with sizes which are a power of two.

    See:   ComplexToComplexFFTImageFilter

    See:  FFTWComplexToComplexFFTImageFilter

    See:   VnlForwardFFTImageFilter

    See:   VnlInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF3___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF3_Clone)
    __swig_destroy__ = _itkVnlComplexToComplexFFTImageFilterPython.delete_itkVnlComplexToComplexFFTImageFilterICF3
    cast = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF3_cast)

    def New(*args, **kargs):
        """New() -> itkVnlComplexToComplexFFTImageFilterICF3

        Create a new object of the class itkVnlComplexToComplexFFTImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlComplexToComplexFFTImageFilterICF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlComplexToComplexFFTImageFilterICF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlComplexToComplexFFTImageFilterICF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlComplexToComplexFFTImageFilterICF3 in _itkVnlComplexToComplexFFTImageFilterPython:
_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF3_swigregister(itkVnlComplexToComplexFFTImageFilterICF3)
itkVnlComplexToComplexFFTImageFilterICF3___New_orig__ = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF3___New_orig__
itkVnlComplexToComplexFFTImageFilterICF3_cast = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF3_cast


def itkVnlComplexToComplexFFTImageFilterICF4_New():
    return itkVnlComplexToComplexFFTImageFilterICF4.New()

class itkVnlComplexToComplexFFTImageFilterICF4(itk.itkComplexToComplexFFTImageFilterPython.itkComplexToComplexFFTImageFilterICF4):
    r"""


    VNL based complex to complex Fast Fourier Transform.

    This filter requires input images with sizes which are a power of two.

    See:   ComplexToComplexFFTImageFilter

    See:  FFTWComplexToComplexFFTImageFilter

    See:   VnlForwardFFTImageFilter

    See:   VnlInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF4___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF4_Clone)
    __swig_destroy__ = _itkVnlComplexToComplexFFTImageFilterPython.delete_itkVnlComplexToComplexFFTImageFilterICF4
    cast = _swig_new_static_method(_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF4_cast)

    def New(*args, **kargs):
        """New() -> itkVnlComplexToComplexFFTImageFilterICF4

        Create a new object of the class itkVnlComplexToComplexFFTImageFilterICF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlComplexToComplexFFTImageFilterICF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlComplexToComplexFFTImageFilterICF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlComplexToComplexFFTImageFilterICF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlComplexToComplexFFTImageFilterICF4 in _itkVnlComplexToComplexFFTImageFilterPython:
_itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF4_swigregister(itkVnlComplexToComplexFFTImageFilterICF4)
itkVnlComplexToComplexFFTImageFilterICF4___New_orig__ = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF4___New_orig__
itkVnlComplexToComplexFFTImageFilterICF4_cast = _itkVnlComplexToComplexFFTImageFilterPython.itkVnlComplexToComplexFFTImageFilterICF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def vnl_complex_to_complex_fft_image_filter(*args: itkt.ImageLike,  transform_direction=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for VnlComplexToComplexFFTImageFilter"""
    import itk

    kwarg_typehints = { 'transform_direction':transform_direction }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.VnlComplexToComplexFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def vnl_complex_to_complex_fft_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKFFT.VnlComplexToComplexFFTImageFilter
    vnl_complex_to_complex_fft_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    vnl_complex_to_complex_fft_image_filter.__doc__ = filter_object.__doc__




