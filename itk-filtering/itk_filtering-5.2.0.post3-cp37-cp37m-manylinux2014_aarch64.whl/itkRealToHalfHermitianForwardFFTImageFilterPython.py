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
    from . import _itkRealToHalfHermitianForwardFFTImageFilterPython
else:
    import _itkRealToHalfHermitianForwardFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRealToHalfHermitianForwardFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRealToHalfHermitianForwardFFTImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkVectorImagePython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkImagePython
import itk.ITKCommonBasePython
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
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkArrayPython

def itkRealToHalfHermitianForwardFFTImageFilterID2ICD2_New():
    return itkRealToHalfHermitianForwardFFTImageFilterID2ICD2.New()

class itkRealToHalfHermitianForwardFFTImageFilterID2ICD2(itk.itkImageToImageFilterBPython.itkImageToImageFilterID2ICD2):
    r"""


    Base class for specialized real-to-complex forward Fast Fourier
    Transform.

    This is a base class for the "forward" or "direct" discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    This class transforms a real input image into its complex Fourier
    transform. The Fourier transform of a real input image has Hermitian
    symmetry: $ f(\\mathbf{x}) = f^*(-\\mathbf{x}) $. That is, when
    the result of the transform is split in half along the X-dimension,
    the values in the second half of the transform are the complex
    conjugates of values in the first half reflected about the center of
    the image in each dimension. This filter takes advantage of the
    Hermitian symmetry property and reduces the size of the output in the
    first dimension to N/2+1, where N is the size of the input image in
    that dimension and the division by 2 is rounded down.

    See:   HalfHermitianToRealInverseFFTImageFilter

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID2ICD2___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID2ICD2_GetSizeGreatestPrimeFactor)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID2ICD2_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID2ICD2_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkRealToHalfHermitianForwardFFTImageFilterID2ICD2
    cast = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID2ICD2_cast)

    def New(*args, **kargs):
        """New() -> itkRealToHalfHermitianForwardFFTImageFilterID2ICD2

        Create a new object of the class itkRealToHalfHermitianForwardFFTImageFilterID2ICD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRealToHalfHermitianForwardFFTImageFilterID2ICD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRealToHalfHermitianForwardFFTImageFilterID2ICD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRealToHalfHermitianForwardFFTImageFilterID2ICD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRealToHalfHermitianForwardFFTImageFilterID2ICD2 in _itkRealToHalfHermitianForwardFFTImageFilterPython:
_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID2ICD2_swigregister(itkRealToHalfHermitianForwardFFTImageFilterID2ICD2)
itkRealToHalfHermitianForwardFFTImageFilterID2ICD2___New_orig__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID2ICD2___New_orig__
itkRealToHalfHermitianForwardFFTImageFilterID2ICD2_cast = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID2ICD2_cast


def itkRealToHalfHermitianForwardFFTImageFilterID3ICD3_New():
    return itkRealToHalfHermitianForwardFFTImageFilterID3ICD3.New()

class itkRealToHalfHermitianForwardFFTImageFilterID3ICD3(itk.itkImageToImageFilterBPython.itkImageToImageFilterID3ICD3):
    r"""


    Base class for specialized real-to-complex forward Fast Fourier
    Transform.

    This is a base class for the "forward" or "direct" discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    This class transforms a real input image into its complex Fourier
    transform. The Fourier transform of a real input image has Hermitian
    symmetry: $ f(\\mathbf{x}) = f^*(-\\mathbf{x}) $. That is, when
    the result of the transform is split in half along the X-dimension,
    the values in the second half of the transform are the complex
    conjugates of values in the first half reflected about the center of
    the image in each dimension. This filter takes advantage of the
    Hermitian symmetry property and reduces the size of the output in the
    first dimension to N/2+1, where N is the size of the input image in
    that dimension and the division by 2 is rounded down.

    See:   HalfHermitianToRealInverseFFTImageFilter

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID3ICD3___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID3ICD3_GetSizeGreatestPrimeFactor)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID3ICD3_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID3ICD3_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkRealToHalfHermitianForwardFFTImageFilterID3ICD3
    cast = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID3ICD3_cast)

    def New(*args, **kargs):
        """New() -> itkRealToHalfHermitianForwardFFTImageFilterID3ICD3

        Create a new object of the class itkRealToHalfHermitianForwardFFTImageFilterID3ICD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRealToHalfHermitianForwardFFTImageFilterID3ICD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRealToHalfHermitianForwardFFTImageFilterID3ICD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRealToHalfHermitianForwardFFTImageFilterID3ICD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRealToHalfHermitianForwardFFTImageFilterID3ICD3 in _itkRealToHalfHermitianForwardFFTImageFilterPython:
_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID3ICD3_swigregister(itkRealToHalfHermitianForwardFFTImageFilterID3ICD3)
itkRealToHalfHermitianForwardFFTImageFilterID3ICD3___New_orig__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID3ICD3___New_orig__
itkRealToHalfHermitianForwardFFTImageFilterID3ICD3_cast = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID3ICD3_cast


def itkRealToHalfHermitianForwardFFTImageFilterID4ICD4_New():
    return itkRealToHalfHermitianForwardFFTImageFilterID4ICD4.New()

class itkRealToHalfHermitianForwardFFTImageFilterID4ICD4(itk.itkImageToImageFilterBPython.itkImageToImageFilterID4ICD4):
    r"""


    Base class for specialized real-to-complex forward Fast Fourier
    Transform.

    This is a base class for the "forward" or "direct" discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    This class transforms a real input image into its complex Fourier
    transform. The Fourier transform of a real input image has Hermitian
    symmetry: $ f(\\mathbf{x}) = f^*(-\\mathbf{x}) $. That is, when
    the result of the transform is split in half along the X-dimension,
    the values in the second half of the transform are the complex
    conjugates of values in the first half reflected about the center of
    the image in each dimension. This filter takes advantage of the
    Hermitian symmetry property and reduces the size of the output in the
    first dimension to N/2+1, where N is the size of the input image in
    that dimension and the division by 2 is rounded down.

    See:   HalfHermitianToRealInverseFFTImageFilter

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID4ICD4___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID4ICD4_GetSizeGreatestPrimeFactor)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID4ICD4_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID4ICD4_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkRealToHalfHermitianForwardFFTImageFilterID4ICD4
    cast = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID4ICD4_cast)

    def New(*args, **kargs):
        """New() -> itkRealToHalfHermitianForwardFFTImageFilterID4ICD4

        Create a new object of the class itkRealToHalfHermitianForwardFFTImageFilterID4ICD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRealToHalfHermitianForwardFFTImageFilterID4ICD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRealToHalfHermitianForwardFFTImageFilterID4ICD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRealToHalfHermitianForwardFFTImageFilterID4ICD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRealToHalfHermitianForwardFFTImageFilterID4ICD4 in _itkRealToHalfHermitianForwardFFTImageFilterPython:
_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID4ICD4_swigregister(itkRealToHalfHermitianForwardFFTImageFilterID4ICD4)
itkRealToHalfHermitianForwardFFTImageFilterID4ICD4___New_orig__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID4ICD4___New_orig__
itkRealToHalfHermitianForwardFFTImageFilterID4ICD4_cast = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterID4ICD4_cast


def itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_New():
    return itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.New()

class itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2(itk.itkImageToImageFilterBPython.itkImageToImageFilterIF2ICF2):
    r"""


    Base class for specialized real-to-complex forward Fast Fourier
    Transform.

    This is a base class for the "forward" or "direct" discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    This class transforms a real input image into its complex Fourier
    transform. The Fourier transform of a real input image has Hermitian
    symmetry: $ f(\\mathbf{x}) = f^*(-\\mathbf{x}) $. That is, when
    the result of the transform is split in half along the X-dimension,
    the values in the second half of the transform are the complex
    conjugates of values in the first half reflected about the center of
    the image in each dimension. This filter takes advantage of the
    Hermitian symmetry property and reduces the size of the output in the
    first dimension to N/2+1, where N is the size of the input image in
    that dimension and the division by 2 is rounded down.

    See:   HalfHermitianToRealInverseFFTImageFilter

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetSizeGreatestPrimeFactor)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2
    cast = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_cast)

    def New(*args, **kargs):
        """New() -> itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2

        Create a new object of the class itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2 in _itkRealToHalfHermitianForwardFFTImageFilterPython:
_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_swigregister(itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2)
itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2___New_orig__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2___New_orig__
itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_cast = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2_cast


def itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_New():
    return itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.New()

class itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3(itk.itkImageToImageFilterBPython.itkImageToImageFilterIF3ICF3):
    r"""


    Base class for specialized real-to-complex forward Fast Fourier
    Transform.

    This is a base class for the "forward" or "direct" discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    This class transforms a real input image into its complex Fourier
    transform. The Fourier transform of a real input image has Hermitian
    symmetry: $ f(\\mathbf{x}) = f^*(-\\mathbf{x}) $. That is, when
    the result of the transform is split in half along the X-dimension,
    the values in the second half of the transform are the complex
    conjugates of values in the first half reflected about the center of
    the image in each dimension. This filter takes advantage of the
    Hermitian symmetry property and reduces the size of the output in the
    first dimension to N/2+1, where N is the size of the input image in
    that dimension and the division by 2 is rounded down.

    See:   HalfHermitianToRealInverseFFTImageFilter

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetSizeGreatestPrimeFactor)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3
    cast = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_cast)

    def New(*args, **kargs):
        """New() -> itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3

        Create a new object of the class itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3 in _itkRealToHalfHermitianForwardFFTImageFilterPython:
_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_swigregister(itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3)
itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3___New_orig__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3___New_orig__
itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_cast = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3_cast


def itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4_New():
    return itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4.New()

class itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4(itk.itkImageToImageFilterBPython.itkImageToImageFilterIF4ICF4):
    r"""


    Base class for specialized real-to-complex forward Fast Fourier
    Transform.

    This is a base class for the "forward" or "direct" discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child class available on the
    system when the object is created via the object factory system.

    This class transforms a real input image into its complex Fourier
    transform. The Fourier transform of a real input image has Hermitian
    symmetry: $ f(\\mathbf{x}) = f^*(-\\mathbf{x}) $. That is, when
    the result of the transform is split in half along the X-dimension,
    the values in the second half of the transform are the complex
    conjugates of values in the first half reflected about the center of
    the image in each dimension. This filter takes advantage of the
    Hermitian symmetry property and reduces the size of the output in the
    first dimension to N/2+1, where N is the size of the input image in
    that dimension and the division by 2 is rounded down.

    See:   HalfHermitianToRealInverseFFTImageFilter

    See:   ForwardFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4_GetSizeGreatestPrimeFactor)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.delete_itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4
    cast = _swig_new_static_method(_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4_cast)

    def New(*args, **kargs):
        """New() -> itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4

        Create a new object of the class itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4 in _itkRealToHalfHermitianForwardFFTImageFilterPython:
_itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4_swigregister(itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4)
itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4___New_orig__ = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4___New_orig__
itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4_cast = _itkRealToHalfHermitianForwardFFTImageFilterPython.itkRealToHalfHermitianForwardFFTImageFilterIF4ICF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def real_to_half_hermitian_forward_fft_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for RealToHalfHermitianForwardFFTImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.RealToHalfHermitianForwardFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def real_to_half_hermitian_forward_fft_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKFFT.RealToHalfHermitianForwardFFTImageFilter
    real_to_half_hermitian_forward_fft_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    real_to_half_hermitian_forward_fft_image_filter.__doc__ = filter_object.__doc__




