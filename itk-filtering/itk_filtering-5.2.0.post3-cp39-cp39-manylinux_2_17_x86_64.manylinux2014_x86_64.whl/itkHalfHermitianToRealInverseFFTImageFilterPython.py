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
    from . import _itkHalfHermitianToRealInverseFFTImageFilterPython
else:
    import _itkHalfHermitianToRealInverseFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHalfHermitianToRealInverseFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHalfHermitianToRealInverseFFTImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageFilterBPython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkPointPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBPixelPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterCommonPython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkArrayPython

def itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_New():
    return itkHalfHermitianToRealInverseFFTImageFilterICD2ID2.New()

class itkHalfHermitianToRealInverseFFTImageFilterICD2ID2(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD2ID2):
    r"""


    Base class for specialized complex-to-real inverse Fast Fourier
    Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    The input to this filter is assumed to have the same format as the
    output of the RealToHalfHermitianForwardFFTImageFilter. That is, the
    input is assumed to consist of roughly half the full complex image
    resulting from a real-to-complex discrete Fourier transform. This half
    is expected to be the first half of the image in the X-dimension.
    Because this filter assumes that the input stores only about half of
    the non-redundant complex pixels, the output is larger in the
    X-dimension than it is in the input. To determine the actual size of
    the output image, this filter needs additional information in the form
    of a flag indicating whether the output image has an odd size in the
    X-dimension. Use SetActualXDimensionIsOdd() to set this flag.

    See:   ForwardFFTImageFilter, HalfHermitianToRealInverseFFTImageFilter

    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2___New_orig__)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_ActualXDimensionIsOddOff)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.delete_itkHalfHermitianToRealInverseFFTImageFilterICD2ID2
    cast = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkHalfHermitianToRealInverseFFTImageFilterICD2ID2

        Create a new object of the class itkHalfHermitianToRealInverseFFTImageFilterICD2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfHermitianToRealInverseFFTImageFilterICD2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfHermitianToRealInverseFFTImageFilterICD2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfHermitianToRealInverseFFTImageFilterICD2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfHermitianToRealInverseFFTImageFilterICD2ID2 in _itkHalfHermitianToRealInverseFFTImageFilterPython:
_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_swigregister(itkHalfHermitianToRealInverseFFTImageFilterICD2ID2)
itkHalfHermitianToRealInverseFFTImageFilterICD2ID2___New_orig__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2___New_orig__
itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_cast = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2_cast


def itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_New():
    return itkHalfHermitianToRealInverseFFTImageFilterICD3ID3.New()

class itkHalfHermitianToRealInverseFFTImageFilterICD3ID3(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD3ID3):
    r"""


    Base class for specialized complex-to-real inverse Fast Fourier
    Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    The input to this filter is assumed to have the same format as the
    output of the RealToHalfHermitianForwardFFTImageFilter. That is, the
    input is assumed to consist of roughly half the full complex image
    resulting from a real-to-complex discrete Fourier transform. This half
    is expected to be the first half of the image in the X-dimension.
    Because this filter assumes that the input stores only about half of
    the non-redundant complex pixels, the output is larger in the
    X-dimension than it is in the input. To determine the actual size of
    the output image, this filter needs additional information in the form
    of a flag indicating whether the output image has an odd size in the
    X-dimension. Use SetActualXDimensionIsOdd() to set this flag.

    See:   ForwardFFTImageFilter, HalfHermitianToRealInverseFFTImageFilter

    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3___New_orig__)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_ActualXDimensionIsOddOff)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.delete_itkHalfHermitianToRealInverseFFTImageFilterICD3ID3
    cast = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkHalfHermitianToRealInverseFFTImageFilterICD3ID3

        Create a new object of the class itkHalfHermitianToRealInverseFFTImageFilterICD3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfHermitianToRealInverseFFTImageFilterICD3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfHermitianToRealInverseFFTImageFilterICD3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfHermitianToRealInverseFFTImageFilterICD3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfHermitianToRealInverseFFTImageFilterICD3ID3 in _itkHalfHermitianToRealInverseFFTImageFilterPython:
_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_swigregister(itkHalfHermitianToRealInverseFFTImageFilterICD3ID3)
itkHalfHermitianToRealInverseFFTImageFilterICD3ID3___New_orig__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3___New_orig__
itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_cast = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3_cast


def itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_New():
    return itkHalfHermitianToRealInverseFFTImageFilterICD4ID4.New()

class itkHalfHermitianToRealInverseFFTImageFilterICD4ID4(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD4ID4):
    r"""


    Base class for specialized complex-to-real inverse Fast Fourier
    Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    The input to this filter is assumed to have the same format as the
    output of the RealToHalfHermitianForwardFFTImageFilter. That is, the
    input is assumed to consist of roughly half the full complex image
    resulting from a real-to-complex discrete Fourier transform. This half
    is expected to be the first half of the image in the X-dimension.
    Because this filter assumes that the input stores only about half of
    the non-redundant complex pixels, the output is larger in the
    X-dimension than it is in the input. To determine the actual size of
    the output image, this filter needs additional information in the form
    of a flag indicating whether the output image has an odd size in the
    X-dimension. Use SetActualXDimensionIsOdd() to set this flag.

    See:   ForwardFFTImageFilter, HalfHermitianToRealInverseFFTImageFilter

    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4___New_orig__)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_ActualXDimensionIsOddOff)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.delete_itkHalfHermitianToRealInverseFFTImageFilterICD4ID4
    cast = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkHalfHermitianToRealInverseFFTImageFilterICD4ID4

        Create a new object of the class itkHalfHermitianToRealInverseFFTImageFilterICD4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfHermitianToRealInverseFFTImageFilterICD4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfHermitianToRealInverseFFTImageFilterICD4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfHermitianToRealInverseFFTImageFilterICD4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfHermitianToRealInverseFFTImageFilterICD4ID4 in _itkHalfHermitianToRealInverseFFTImageFilterPython:
_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_swigregister(itkHalfHermitianToRealInverseFFTImageFilterICD4ID4)
itkHalfHermitianToRealInverseFFTImageFilterICD4ID4___New_orig__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4___New_orig__
itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_cast = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4_cast


def itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_New():
    return itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.New()

class itkHalfHermitianToRealInverseFFTImageFilterICF2IF2(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF2IF2):
    r"""


    Base class for specialized complex-to-real inverse Fast Fourier
    Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    The input to this filter is assumed to have the same format as the
    output of the RealToHalfHermitianForwardFFTImageFilter. That is, the
    input is assumed to consist of roughly half the full complex image
    resulting from a real-to-complex discrete Fourier transform. This half
    is expected to be the first half of the image in the X-dimension.
    Because this filter assumes that the input stores only about half of
    the non-redundant complex pixels, the output is larger in the
    X-dimension than it is in the input. To determine the actual size of
    the output image, this filter needs additional information in the form
    of a flag indicating whether the output image has an odd size in the
    X-dimension. Use SetActualXDimensionIsOdd() to set this flag.

    See:   ForwardFFTImageFilter, HalfHermitianToRealInverseFFTImageFilter

    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2___New_orig__)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_ActualXDimensionIsOddOff)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.delete_itkHalfHermitianToRealInverseFFTImageFilterICF2IF2
    cast = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkHalfHermitianToRealInverseFFTImageFilterICF2IF2

        Create a new object of the class itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfHermitianToRealInverseFFTImageFilterICF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfHermitianToRealInverseFFTImageFilterICF2IF2 in _itkHalfHermitianToRealInverseFFTImageFilterPython:
_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_swigregister(itkHalfHermitianToRealInverseFFTImageFilterICF2IF2)
itkHalfHermitianToRealInverseFFTImageFilterICF2IF2___New_orig__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2___New_orig__
itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_cast = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2_cast


def itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_New():
    return itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.New()

class itkHalfHermitianToRealInverseFFTImageFilterICF3IF3(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF3IF3):
    r"""


    Base class for specialized complex-to-real inverse Fast Fourier
    Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    The input to this filter is assumed to have the same format as the
    output of the RealToHalfHermitianForwardFFTImageFilter. That is, the
    input is assumed to consist of roughly half the full complex image
    resulting from a real-to-complex discrete Fourier transform. This half
    is expected to be the first half of the image in the X-dimension.
    Because this filter assumes that the input stores only about half of
    the non-redundant complex pixels, the output is larger in the
    X-dimension than it is in the input. To determine the actual size of
    the output image, this filter needs additional information in the form
    of a flag indicating whether the output image has an odd size in the
    X-dimension. Use SetActualXDimensionIsOdd() to set this flag.

    See:   ForwardFFTImageFilter, HalfHermitianToRealInverseFFTImageFilter

    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3___New_orig__)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_ActualXDimensionIsOddOff)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.delete_itkHalfHermitianToRealInverseFFTImageFilterICF3IF3
    cast = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkHalfHermitianToRealInverseFFTImageFilterICF3IF3

        Create a new object of the class itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfHermitianToRealInverseFFTImageFilterICF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfHermitianToRealInverseFFTImageFilterICF3IF3 in _itkHalfHermitianToRealInverseFFTImageFilterPython:
_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_swigregister(itkHalfHermitianToRealInverseFFTImageFilterICF3IF3)
itkHalfHermitianToRealInverseFFTImageFilterICF3IF3___New_orig__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3___New_orig__
itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_cast = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3_cast


def itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_New():
    return itkHalfHermitianToRealInverseFFTImageFilterICF4IF4.New()

class itkHalfHermitianToRealInverseFFTImageFilterICF4IF4(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF4IF4):
    r"""


    Base class for specialized complex-to-real inverse Fast Fourier
    Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    The input to this filter is assumed to have the same format as the
    output of the RealToHalfHermitianForwardFFTImageFilter. That is, the
    input is assumed to consist of roughly half the full complex image
    resulting from a real-to-complex discrete Fourier transform. This half
    is expected to be the first half of the image in the X-dimension.
    Because this filter assumes that the input stores only about half of
    the non-redundant complex pixels, the output is larger in the
    X-dimension than it is in the input. To determine the actual size of
    the output image, this filter needs additional information in the form
    of a flag indicating whether the output image has an odd size in the
    X-dimension. Use SetActualXDimensionIsOdd() to set this flag.

    See:   ForwardFFTImageFilter, HalfHermitianToRealInverseFFTImageFilter

    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4___New_orig__)
    SetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_SetActualXDimensionIsOddInput)
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOddInput = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_GetActualXDimensionIsOddInput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_ActualXDimensionIsOddOff)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.delete_itkHalfHermitianToRealInverseFFTImageFilterICF4IF4
    cast = _swig_new_static_method(_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkHalfHermitianToRealInverseFFTImageFilterICF4IF4

        Create a new object of the class itkHalfHermitianToRealInverseFFTImageFilterICF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHalfHermitianToRealInverseFFTImageFilterICF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHalfHermitianToRealInverseFFTImageFilterICF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHalfHermitianToRealInverseFFTImageFilterICF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHalfHermitianToRealInverseFFTImageFilterICF4IF4 in _itkHalfHermitianToRealInverseFFTImageFilterPython:
_itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_swigregister(itkHalfHermitianToRealInverseFFTImageFilterICF4IF4)
itkHalfHermitianToRealInverseFFTImageFilterICF4IF4___New_orig__ = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4___New_orig__
itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_cast = _itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def half_hermitian_to_real_inverse_fft_image_filter(*args: itkt.ImageLike,  actual_x_dimension_is_odd_input=..., actual_x_dimension_is_odd: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for HalfHermitianToRealInverseFFTImageFilter"""
    import itk

    kwarg_typehints = { 'actual_x_dimension_is_odd_input':actual_x_dimension_is_odd_input,'actual_x_dimension_is_odd':actual_x_dimension_is_odd }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.HalfHermitianToRealInverseFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def half_hermitian_to_real_inverse_fft_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKFFT.HalfHermitianToRealInverseFFTImageFilter
    half_hermitian_to_real_inverse_fft_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    half_hermitian_to_real_inverse_fft_image_filter.__doc__ = filter_object.__doc__




