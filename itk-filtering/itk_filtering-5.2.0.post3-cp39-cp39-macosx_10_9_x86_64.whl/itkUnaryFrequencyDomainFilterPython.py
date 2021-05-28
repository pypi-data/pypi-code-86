# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageFrequencyPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkUnaryFrequencyDomainFilterPython
else:
    import _itkUnaryFrequencyDomainFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkUnaryFrequencyDomainFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkUnaryFrequencyDomainFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.ITKCommonBasePython
import itk.itkInPlaceImageFilterBPython
import itk.itkImageToImageFilterBPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.stdcomplexPython
import itk.itkImagePython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkVariableLengthVectorPython

def itkUnaryFrequencyDomainFilterICD2_New():
    return itkUnaryFrequencyDomainFilterICD2.New()

class itkUnaryFrequencyDomainFilterICD2(itk.itkInPlaceImageFilterBPython.itkInPlaceImageFilterICD2ICD2):
    r"""


    Performs a unary operation on a frequency domain image.

    A frequency filtering functor needs to be supplied via one of
    SetFunctor() overloads. The functor should take FrequencyIteratorType
    reference as its only parameter. If functor configurability is
    required, those parameters should be passed directly to the functor at
    the place of definition.

    Filters in the module ITKImageFrequency work with input images in the
    frequency domain. This filter is templated over a TFrequencyIterator
    depending on the frequency layout of the input image.

    Images in the dual space can be acquired experimentally, from
    scattering experiments or other techniques. In that case use
    FrequencyImageRegionIteratorWithIndex because the layout of dual space
    images is the same as spatial domain images.

    Frequency-domain images can be computed from any spatial-domain
    applying a Fourier Transform. If ForwardFFTImageFilter was used,
    template this filter with the
    FrequencyFFTLayoutImageRegionIteratorWithIndex. Please note that
    FrequencyFFTLayoutImageRegionIteratorWithIndex requires a full FFT,
    and is not compatible with the Hermitian optimization.

    To use this filter with Hermitian (halved-frequency) FFTs, use
    FrequencyHalfHermitianFFTLayoutImageRegionIteratorWithIndex or its
    const version.

    If the output of the FFT is shifted, for example after applying
    FFTShiftImageFilter, use
    FrequencyShiftedFFTLayoutImageRegionIteratorWithIndex.

    See:  UnaryGeneratorImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD2___New_orig__)
    Clone = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD2_Clone)
    ImageTypeHasNumericTraitsCheck = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD2_ImageTypeHasNumericTraitsCheck
    
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD2_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD2_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD2_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD2_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkUnaryFrequencyDomainFilterPython.delete_itkUnaryFrequencyDomainFilterICD2
    cast = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD2_cast)

    def New(*args, **kargs):
        """New() -> itkUnaryFrequencyDomainFilterICD2

        Create a new object of the class itkUnaryFrequencyDomainFilterICD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnaryFrequencyDomainFilterICD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnaryFrequencyDomainFilterICD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnaryFrequencyDomainFilterICD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnaryFrequencyDomainFilterICD2 in _itkUnaryFrequencyDomainFilterPython:
_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD2_swigregister(itkUnaryFrequencyDomainFilterICD2)
itkUnaryFrequencyDomainFilterICD2___New_orig__ = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD2___New_orig__
itkUnaryFrequencyDomainFilterICD2_cast = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD2_cast


def itkUnaryFrequencyDomainFilterICD3_New():
    return itkUnaryFrequencyDomainFilterICD3.New()

class itkUnaryFrequencyDomainFilterICD3(itk.itkInPlaceImageFilterBPython.itkInPlaceImageFilterICD3ICD3):
    r"""


    Performs a unary operation on a frequency domain image.

    A frequency filtering functor needs to be supplied via one of
    SetFunctor() overloads. The functor should take FrequencyIteratorType
    reference as its only parameter. If functor configurability is
    required, those parameters should be passed directly to the functor at
    the place of definition.

    Filters in the module ITKImageFrequency work with input images in the
    frequency domain. This filter is templated over a TFrequencyIterator
    depending on the frequency layout of the input image.

    Images in the dual space can be acquired experimentally, from
    scattering experiments or other techniques. In that case use
    FrequencyImageRegionIteratorWithIndex because the layout of dual space
    images is the same as spatial domain images.

    Frequency-domain images can be computed from any spatial-domain
    applying a Fourier Transform. If ForwardFFTImageFilter was used,
    template this filter with the
    FrequencyFFTLayoutImageRegionIteratorWithIndex. Please note that
    FrequencyFFTLayoutImageRegionIteratorWithIndex requires a full FFT,
    and is not compatible with the Hermitian optimization.

    To use this filter with Hermitian (halved-frequency) FFTs, use
    FrequencyHalfHermitianFFTLayoutImageRegionIteratorWithIndex or its
    const version.

    If the output of the FFT is shifted, for example after applying
    FFTShiftImageFilter, use
    FrequencyShiftedFFTLayoutImageRegionIteratorWithIndex.

    See:  UnaryGeneratorImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD3___New_orig__)
    Clone = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD3_Clone)
    ImageTypeHasNumericTraitsCheck = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD3_ImageTypeHasNumericTraitsCheck
    
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD3_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD3_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD3_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD3_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkUnaryFrequencyDomainFilterPython.delete_itkUnaryFrequencyDomainFilterICD3
    cast = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD3_cast)

    def New(*args, **kargs):
        """New() -> itkUnaryFrequencyDomainFilterICD3

        Create a new object of the class itkUnaryFrequencyDomainFilterICD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnaryFrequencyDomainFilterICD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnaryFrequencyDomainFilterICD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnaryFrequencyDomainFilterICD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnaryFrequencyDomainFilterICD3 in _itkUnaryFrequencyDomainFilterPython:
_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD3_swigregister(itkUnaryFrequencyDomainFilterICD3)
itkUnaryFrequencyDomainFilterICD3___New_orig__ = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD3___New_orig__
itkUnaryFrequencyDomainFilterICD3_cast = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD3_cast


def itkUnaryFrequencyDomainFilterICD4_New():
    return itkUnaryFrequencyDomainFilterICD4.New()

class itkUnaryFrequencyDomainFilterICD4(itk.itkInPlaceImageFilterBPython.itkInPlaceImageFilterICD4ICD4):
    r"""


    Performs a unary operation on a frequency domain image.

    A frequency filtering functor needs to be supplied via one of
    SetFunctor() overloads. The functor should take FrequencyIteratorType
    reference as its only parameter. If functor configurability is
    required, those parameters should be passed directly to the functor at
    the place of definition.

    Filters in the module ITKImageFrequency work with input images in the
    frequency domain. This filter is templated over a TFrequencyIterator
    depending on the frequency layout of the input image.

    Images in the dual space can be acquired experimentally, from
    scattering experiments or other techniques. In that case use
    FrequencyImageRegionIteratorWithIndex because the layout of dual space
    images is the same as spatial domain images.

    Frequency-domain images can be computed from any spatial-domain
    applying a Fourier Transform. If ForwardFFTImageFilter was used,
    template this filter with the
    FrequencyFFTLayoutImageRegionIteratorWithIndex. Please note that
    FrequencyFFTLayoutImageRegionIteratorWithIndex requires a full FFT,
    and is not compatible with the Hermitian optimization.

    To use this filter with Hermitian (halved-frequency) FFTs, use
    FrequencyHalfHermitianFFTLayoutImageRegionIteratorWithIndex or its
    const version.

    If the output of the FFT is shifted, for example after applying
    FFTShiftImageFilter, use
    FrequencyShiftedFFTLayoutImageRegionIteratorWithIndex.

    See:  UnaryGeneratorImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD4___New_orig__)
    Clone = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD4_Clone)
    ImageTypeHasNumericTraitsCheck = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD4_ImageTypeHasNumericTraitsCheck
    
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD4_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD4_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD4_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD4_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkUnaryFrequencyDomainFilterPython.delete_itkUnaryFrequencyDomainFilterICD4
    cast = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD4_cast)

    def New(*args, **kargs):
        """New() -> itkUnaryFrequencyDomainFilterICD4

        Create a new object of the class itkUnaryFrequencyDomainFilterICD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnaryFrequencyDomainFilterICD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnaryFrequencyDomainFilterICD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnaryFrequencyDomainFilterICD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnaryFrequencyDomainFilterICD4 in _itkUnaryFrequencyDomainFilterPython:
_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD4_swigregister(itkUnaryFrequencyDomainFilterICD4)
itkUnaryFrequencyDomainFilterICD4___New_orig__ = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD4___New_orig__
itkUnaryFrequencyDomainFilterICD4_cast = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICD4_cast


def itkUnaryFrequencyDomainFilterICF2_New():
    return itkUnaryFrequencyDomainFilterICF2.New()

class itkUnaryFrequencyDomainFilterICF2(itk.itkInPlaceImageFilterBPython.itkInPlaceImageFilterICF2ICF2):
    r"""


    Performs a unary operation on a frequency domain image.

    A frequency filtering functor needs to be supplied via one of
    SetFunctor() overloads. The functor should take FrequencyIteratorType
    reference as its only parameter. If functor configurability is
    required, those parameters should be passed directly to the functor at
    the place of definition.

    Filters in the module ITKImageFrequency work with input images in the
    frequency domain. This filter is templated over a TFrequencyIterator
    depending on the frequency layout of the input image.

    Images in the dual space can be acquired experimentally, from
    scattering experiments or other techniques. In that case use
    FrequencyImageRegionIteratorWithIndex because the layout of dual space
    images is the same as spatial domain images.

    Frequency-domain images can be computed from any spatial-domain
    applying a Fourier Transform. If ForwardFFTImageFilter was used,
    template this filter with the
    FrequencyFFTLayoutImageRegionIteratorWithIndex. Please note that
    FrequencyFFTLayoutImageRegionIteratorWithIndex requires a full FFT,
    and is not compatible with the Hermitian optimization.

    To use this filter with Hermitian (halved-frequency) FFTs, use
    FrequencyHalfHermitianFFTLayoutImageRegionIteratorWithIndex or its
    const version.

    If the output of the FFT is shifted, for example after applying
    FFTShiftImageFilter, use
    FrequencyShiftedFFTLayoutImageRegionIteratorWithIndex.

    See:  UnaryGeneratorImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2___New_orig__)
    Clone = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_Clone)
    ImageTypeHasNumericTraitsCheck = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_ImageTypeHasNumericTraitsCheck
    
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkUnaryFrequencyDomainFilterPython.delete_itkUnaryFrequencyDomainFilterICF2
    cast = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_cast)

    def New(*args, **kargs):
        """New() -> itkUnaryFrequencyDomainFilterICF2

        Create a new object of the class itkUnaryFrequencyDomainFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnaryFrequencyDomainFilterICF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnaryFrequencyDomainFilterICF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnaryFrequencyDomainFilterICF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnaryFrequencyDomainFilterICF2 in _itkUnaryFrequencyDomainFilterPython:
_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_swigregister(itkUnaryFrequencyDomainFilterICF2)
itkUnaryFrequencyDomainFilterICF2___New_orig__ = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2___New_orig__
itkUnaryFrequencyDomainFilterICF2_cast = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF2_cast


def itkUnaryFrequencyDomainFilterICF3_New():
    return itkUnaryFrequencyDomainFilterICF3.New()

class itkUnaryFrequencyDomainFilterICF3(itk.itkInPlaceImageFilterBPython.itkInPlaceImageFilterICF3ICF3):
    r"""


    Performs a unary operation on a frequency domain image.

    A frequency filtering functor needs to be supplied via one of
    SetFunctor() overloads. The functor should take FrequencyIteratorType
    reference as its only parameter. If functor configurability is
    required, those parameters should be passed directly to the functor at
    the place of definition.

    Filters in the module ITKImageFrequency work with input images in the
    frequency domain. This filter is templated over a TFrequencyIterator
    depending on the frequency layout of the input image.

    Images in the dual space can be acquired experimentally, from
    scattering experiments or other techniques. In that case use
    FrequencyImageRegionIteratorWithIndex because the layout of dual space
    images is the same as spatial domain images.

    Frequency-domain images can be computed from any spatial-domain
    applying a Fourier Transform. If ForwardFFTImageFilter was used,
    template this filter with the
    FrequencyFFTLayoutImageRegionIteratorWithIndex. Please note that
    FrequencyFFTLayoutImageRegionIteratorWithIndex requires a full FFT,
    and is not compatible with the Hermitian optimization.

    To use this filter with Hermitian (halved-frequency) FFTs, use
    FrequencyHalfHermitianFFTLayoutImageRegionIteratorWithIndex or its
    const version.

    If the output of the FFT is shifted, for example after applying
    FFTShiftImageFilter, use
    FrequencyShiftedFFTLayoutImageRegionIteratorWithIndex.

    See:  UnaryGeneratorImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3___New_orig__)
    Clone = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_Clone)
    ImageTypeHasNumericTraitsCheck = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_ImageTypeHasNumericTraitsCheck
    
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkUnaryFrequencyDomainFilterPython.delete_itkUnaryFrequencyDomainFilterICF3
    cast = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_cast)

    def New(*args, **kargs):
        """New() -> itkUnaryFrequencyDomainFilterICF3

        Create a new object of the class itkUnaryFrequencyDomainFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnaryFrequencyDomainFilterICF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnaryFrequencyDomainFilterICF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnaryFrequencyDomainFilterICF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnaryFrequencyDomainFilterICF3 in _itkUnaryFrequencyDomainFilterPython:
_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_swigregister(itkUnaryFrequencyDomainFilterICF3)
itkUnaryFrequencyDomainFilterICF3___New_orig__ = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3___New_orig__
itkUnaryFrequencyDomainFilterICF3_cast = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF3_cast


def itkUnaryFrequencyDomainFilterICF4_New():
    return itkUnaryFrequencyDomainFilterICF4.New()

class itkUnaryFrequencyDomainFilterICF4(itk.itkInPlaceImageFilterBPython.itkInPlaceImageFilterICF4ICF4):
    r"""


    Performs a unary operation on a frequency domain image.

    A frequency filtering functor needs to be supplied via one of
    SetFunctor() overloads. The functor should take FrequencyIteratorType
    reference as its only parameter. If functor configurability is
    required, those parameters should be passed directly to the functor at
    the place of definition.

    Filters in the module ITKImageFrequency work with input images in the
    frequency domain. This filter is templated over a TFrequencyIterator
    depending on the frequency layout of the input image.

    Images in the dual space can be acquired experimentally, from
    scattering experiments or other techniques. In that case use
    FrequencyImageRegionIteratorWithIndex because the layout of dual space
    images is the same as spatial domain images.

    Frequency-domain images can be computed from any spatial-domain
    applying a Fourier Transform. If ForwardFFTImageFilter was used,
    template this filter with the
    FrequencyFFTLayoutImageRegionIteratorWithIndex. Please note that
    FrequencyFFTLayoutImageRegionIteratorWithIndex requires a full FFT,
    and is not compatible with the Hermitian optimization.

    To use this filter with Hermitian (halved-frequency) FFTs, use
    FrequencyHalfHermitianFFTLayoutImageRegionIteratorWithIndex or its
    const version.

    If the output of the FFT is shifted, for example after applying
    FFTShiftImageFilter, use
    FrequencyShiftedFFTLayoutImageRegionIteratorWithIndex.

    See:  UnaryGeneratorImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF4___New_orig__)
    Clone = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF4_Clone)
    ImageTypeHasNumericTraitsCheck = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF4_ImageTypeHasNumericTraitsCheck
    
    SetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF4_SetActualXDimensionIsOdd)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF4_GetActualXDimensionIsOdd)
    ActualXDimensionIsOddOn = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF4_ActualXDimensionIsOddOn)
    ActualXDimensionIsOddOff = _swig_new_instance_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF4_ActualXDimensionIsOddOff)
    __swig_destroy__ = _itkUnaryFrequencyDomainFilterPython.delete_itkUnaryFrequencyDomainFilterICF4
    cast = _swig_new_static_method(_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF4_cast)

    def New(*args, **kargs):
        """New() -> itkUnaryFrequencyDomainFilterICF4

        Create a new object of the class itkUnaryFrequencyDomainFilterICF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnaryFrequencyDomainFilterICF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnaryFrequencyDomainFilterICF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnaryFrequencyDomainFilterICF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnaryFrequencyDomainFilterICF4 in _itkUnaryFrequencyDomainFilterPython:
_itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF4_swigregister(itkUnaryFrequencyDomainFilterICF4)
itkUnaryFrequencyDomainFilterICF4___New_orig__ = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF4___New_orig__
itkUnaryFrequencyDomainFilterICF4_cast = _itkUnaryFrequencyDomainFilterPython.itkUnaryFrequencyDomainFilterICF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def unary_frequency_domain_filter(*args: itkt.ImageLike,  actual_x_dimension_is_odd: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for UnaryFrequencyDomainFilter"""
    import itk

    kwarg_typehints = { 'actual_x_dimension_is_odd':actual_x_dimension_is_odd }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.UnaryFrequencyDomainFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def unary_frequency_domain_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageFrequency.UnaryFrequencyDomainFilter
    unary_frequency_domain_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    unary_frequency_domain_filter.__doc__ = filter_object.__doc__




