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
    from . import _itkHalfToFullHermitianImageFilterPython
else:
    import _itkHalfToFullHermitianImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHalfToFullHermitianImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHalfToFullHermitianImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageFilterBPython
import itk.itkImageToImageFilterCommonPython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
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
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkArrayPython

def itkHalfToFullHermitianImageFilterICD2_New():
    return itkHalfToFullHermitianImageFilterICD2.New()

class itkHalfToFullHermitianImageFilterICD2(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD2ICD2):
    r"""


    Expands a half image produced from a real-to-complex discrete Fourier
    transform (DFT) to the full complex image.

    The subclasses of RealToHalfHermitianForwardFFTImageFilter produce
    only the non-redundant half of the image resulting from a real-to-
    complex DFT. This filter takes the non-redundant half image and
    generates the full complex image that includes the redundant half. It
    requires additional information about the output image size, namely,
    whether the size in the first dimension of the output image is odd.

    See:   RealToHalfHermitianForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2___New_orig__)
    Clone = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2_Clone)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkHalfToFullHermitianImageFilterPython.delete_itkHalfToFullHermitianImageFilterICD2
    cast = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2_cast)

    def New(*args, **kargs):
        """New() -> itkHalfToFullHermitianImageFilterICD2

        Create a new object of the class itkHalfToFullHermitianImageFilterICD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfToFullHermitianImageFilterICD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfToFullHermitianImageFilterICD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfToFullHermitianImageFilterICD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfToFullHermitianImageFilterICD2 in _itkHalfToFullHermitianImageFilterPython:
_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2_swigregister(itkHalfToFullHermitianImageFilterICD2)
itkHalfToFullHermitianImageFilterICD2___New_orig__ = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2___New_orig__
itkHalfToFullHermitianImageFilterICD2_cast = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD2_cast


def itkHalfToFullHermitianImageFilterICD3_New():
    return itkHalfToFullHermitianImageFilterICD3.New()

class itkHalfToFullHermitianImageFilterICD3(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD3ICD3):
    r"""


    Expands a half image produced from a real-to-complex discrete Fourier
    transform (DFT) to the full complex image.

    The subclasses of RealToHalfHermitianForwardFFTImageFilter produce
    only the non-redundant half of the image resulting from a real-to-
    complex DFT. This filter takes the non-redundant half image and
    generates the full complex image that includes the redundant half. It
    requires additional information about the output image size, namely,
    whether the size in the first dimension of the output image is odd.

    See:   RealToHalfHermitianForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3___New_orig__)
    Clone = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3_Clone)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkHalfToFullHermitianImageFilterPython.delete_itkHalfToFullHermitianImageFilterICD3
    cast = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3_cast)

    def New(*args, **kargs):
        """New() -> itkHalfToFullHermitianImageFilterICD3

        Create a new object of the class itkHalfToFullHermitianImageFilterICD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfToFullHermitianImageFilterICD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfToFullHermitianImageFilterICD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfToFullHermitianImageFilterICD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfToFullHermitianImageFilterICD3 in _itkHalfToFullHermitianImageFilterPython:
_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3_swigregister(itkHalfToFullHermitianImageFilterICD3)
itkHalfToFullHermitianImageFilterICD3___New_orig__ = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3___New_orig__
itkHalfToFullHermitianImageFilterICD3_cast = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD3_cast


def itkHalfToFullHermitianImageFilterICD4_New():
    return itkHalfToFullHermitianImageFilterICD4.New()

class itkHalfToFullHermitianImageFilterICD4(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD4ICD4):
    r"""


    Expands a half image produced from a real-to-complex discrete Fourier
    transform (DFT) to the full complex image.

    The subclasses of RealToHalfHermitianForwardFFTImageFilter produce
    only the non-redundant half of the image resulting from a real-to-
    complex DFT. This filter takes the non-redundant half image and
    generates the full complex image that includes the redundant half. It
    requires additional information about the output image size, namely,
    whether the size in the first dimension of the output image is odd.

    See:   RealToHalfHermitianForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4___New_orig__)
    Clone = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4_Clone)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkHalfToFullHermitianImageFilterPython.delete_itkHalfToFullHermitianImageFilterICD4
    cast = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4_cast)

    def New(*args, **kargs):
        """New() -> itkHalfToFullHermitianImageFilterICD4

        Create a new object of the class itkHalfToFullHermitianImageFilterICD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfToFullHermitianImageFilterICD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfToFullHermitianImageFilterICD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfToFullHermitianImageFilterICD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfToFullHermitianImageFilterICD4 in _itkHalfToFullHermitianImageFilterPython:
_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4_swigregister(itkHalfToFullHermitianImageFilterICD4)
itkHalfToFullHermitianImageFilterICD4___New_orig__ = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4___New_orig__
itkHalfToFullHermitianImageFilterICD4_cast = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICD4_cast


def itkHalfToFullHermitianImageFilterICF2_New():
    return itkHalfToFullHermitianImageFilterICF2.New()

class itkHalfToFullHermitianImageFilterICF2(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF2ICF2):
    r"""


    Expands a half image produced from a real-to-complex discrete Fourier
    transform (DFT) to the full complex image.

    The subclasses of RealToHalfHermitianForwardFFTImageFilter produce
    only the non-redundant half of the image resulting from a real-to-
    complex DFT. This filter takes the non-redundant half image and
    generates the full complex image that includes the redundant half. It
    requires additional information about the output image size, namely,
    whether the size in the first dimension of the output image is odd.

    See:   RealToHalfHermitianForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2___New_orig__)
    Clone = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_Clone)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkHalfToFullHermitianImageFilterPython.delete_itkHalfToFullHermitianImageFilterICF2
    cast = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_cast)

    def New(*args, **kargs):
        """New() -> itkHalfToFullHermitianImageFilterICF2

        Create a new object of the class itkHalfToFullHermitianImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfToFullHermitianImageFilterICF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfToFullHermitianImageFilterICF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfToFullHermitianImageFilterICF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfToFullHermitianImageFilterICF2 in _itkHalfToFullHermitianImageFilterPython:
_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_swigregister(itkHalfToFullHermitianImageFilterICF2)
itkHalfToFullHermitianImageFilterICF2___New_orig__ = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2___New_orig__
itkHalfToFullHermitianImageFilterICF2_cast = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF2_cast


def itkHalfToFullHermitianImageFilterICF3_New():
    return itkHalfToFullHermitianImageFilterICF3.New()

class itkHalfToFullHermitianImageFilterICF3(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF3ICF3):
    r"""


    Expands a half image produced from a real-to-complex discrete Fourier
    transform (DFT) to the full complex image.

    The subclasses of RealToHalfHermitianForwardFFTImageFilter produce
    only the non-redundant half of the image resulting from a real-to-
    complex DFT. This filter takes the non-redundant half image and
    generates the full complex image that includes the redundant half. It
    requires additional information about the output image size, namely,
    whether the size in the first dimension of the output image is odd.

    See:   RealToHalfHermitianForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3___New_orig__)
    Clone = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_Clone)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkHalfToFullHermitianImageFilterPython.delete_itkHalfToFullHermitianImageFilterICF3
    cast = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_cast)

    def New(*args, **kargs):
        """New() -> itkHalfToFullHermitianImageFilterICF3

        Create a new object of the class itkHalfToFullHermitianImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfToFullHermitianImageFilterICF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfToFullHermitianImageFilterICF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfToFullHermitianImageFilterICF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfToFullHermitianImageFilterICF3 in _itkHalfToFullHermitianImageFilterPython:
_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_swigregister(itkHalfToFullHermitianImageFilterICF3)
itkHalfToFullHermitianImageFilterICF3___New_orig__ = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3___New_orig__
itkHalfToFullHermitianImageFilterICF3_cast = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF3_cast


def itkHalfToFullHermitianImageFilterICF4_New():
    return itkHalfToFullHermitianImageFilterICF4.New()

class itkHalfToFullHermitianImageFilterICF4(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF4ICF4):
    r"""


    Expands a half image produced from a real-to-complex discrete Fourier
    transform (DFT) to the full complex image.

    The subclasses of RealToHalfHermitianForwardFFTImageFilter produce
    only the non-redundant half of the image resulting from a real-to-
    complex DFT. This filter takes the non-redundant half image and
    generates the full complex image that includes the redundant half. It
    requires additional information about the output image size, namely,
    whether the size in the first dimension of the output image is odd.

    See:   RealToHalfHermitianForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4___New_orig__)
    Clone = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4_Clone)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkHalfToFullHermitianImageFilterPython.delete_itkHalfToFullHermitianImageFilterICF4
    cast = _swig_new_static_method(_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4_cast)

    def New(*args, **kargs):
        """New() -> itkHalfToFullHermitianImageFilterICF4

        Create a new object of the class itkHalfToFullHermitianImageFilterICF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfToFullHermitianImageFilterICF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfToFullHermitianImageFilterICF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfToFullHermitianImageFilterICF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfToFullHermitianImageFilterICF4 in _itkHalfToFullHermitianImageFilterPython:
_itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4_swigregister(itkHalfToFullHermitianImageFilterICF4)
itkHalfToFullHermitianImageFilterICF4___New_orig__ = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4___New_orig__
itkHalfToFullHermitianImageFilterICF4_cast = _itkHalfToFullHermitianImageFilterPython.itkHalfToFullHermitianImageFilterICF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def half_to_full_hermitian_image_filter(*args: itkt.ImageLike,  actual_x_dimension_is_odd_input=..., actual_x_dimension_is_odd: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for HalfToFullHermitianImageFilter"""
    import itk

    kwarg_typehints = { 'actual_x_dimension_is_odd_input':actual_x_dimension_is_odd_input,'actual_x_dimension_is_odd':actual_x_dimension_is_odd }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.HalfToFullHermitianImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def half_to_full_hermitian_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKFFT.HalfToFullHermitianImageFilter
    half_to_full_hermitian_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    half_to_full_hermitian_image_filter.__doc__ = filter_object.__doc__




