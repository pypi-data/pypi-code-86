# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageFeaturePython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkLaplacianImageFilterPython
else:
    import _itkLaplacianImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLaplacianImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLaplacianImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageFilterAPython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.stdcomplexPython
import itk.itkVariableLengthVectorPython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkCovariantVectorPython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBAPixelPython
import itk.itkImageToImageFilterCommonPython

def itkLaplacianImageFilterID2ID2_New():
    return itkLaplacianImageFilterID2ID2.New()

class itkLaplacianImageFilterID2ID2(itk.itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""


    This filter computes the Laplacian of a scalar-valued image.

    The Laplacian is an isotropic measure of the 2nd spatial derivative of
    an image. The Laplacian of an image highlights regions of rapid
    intensity change and is therefore often used for edge detection.
    Often, the Laplacian is applied to an image that has first been
    smoothed with a Gaussian filter in order to reduce its sensitivity to
    noise.

    The Laplacian at each pixel location is computed by convolution with
    the itk::LaplacianOperator. Inputs and Outputs The input to this
    filter is a scalar-valued itk::Image of arbitrary dimension. The
    output is a scalar-valued itk::Image.

    WARNING:  The pixel type of the input and output images must be of
    real type (float or double). ConceptChecking is used here to enforce
    the input pixel type. You will get a compilation error if the pixel
    type of the input and output images is not float or double.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    See:  LaplacianOperator
    example{Filtering/ImageFeature/ComputeLaplacian,Compute Laplacian} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_GenerateInputRequestedRegion)
    UseImageSpacingOn = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_UseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_GetUseImageSpacing)
    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_SameDimensionCheck
    
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_InputPixelTypeIsFloatingPointCheck
    
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_OutputPixelTypeIsFloatingPointCheck
    
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterID2ID2
    cast = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterID2ID2

        Create a new object of the class itkLaplacianImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLaplacianImageFilterID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLaplacianImageFilterID2ID2 in _itkLaplacianImageFilterPython:
_itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_swigregister(itkLaplacianImageFilterID2ID2)
itkLaplacianImageFilterID2ID2___New_orig__ = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2___New_orig__
itkLaplacianImageFilterID2ID2_cast = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID2ID2_cast


def itkLaplacianImageFilterID3ID3_New():
    return itkLaplacianImageFilterID3ID3.New()

class itkLaplacianImageFilterID3ID3(itk.itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""


    This filter computes the Laplacian of a scalar-valued image.

    The Laplacian is an isotropic measure of the 2nd spatial derivative of
    an image. The Laplacian of an image highlights regions of rapid
    intensity change and is therefore often used for edge detection.
    Often, the Laplacian is applied to an image that has first been
    smoothed with a Gaussian filter in order to reduce its sensitivity to
    noise.

    The Laplacian at each pixel location is computed by convolution with
    the itk::LaplacianOperator. Inputs and Outputs The input to this
    filter is a scalar-valued itk::Image of arbitrary dimension. The
    output is a scalar-valued itk::Image.

    WARNING:  The pixel type of the input and output images must be of
    real type (float or double). ConceptChecking is used here to enforce
    the input pixel type. You will get a compilation error if the pixel
    type of the input and output images is not float or double.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    See:  LaplacianOperator
    example{Filtering/ImageFeature/ComputeLaplacian,Compute Laplacian} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_GenerateInputRequestedRegion)
    UseImageSpacingOn = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_UseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_GetUseImageSpacing)
    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_SameDimensionCheck
    
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_InputPixelTypeIsFloatingPointCheck
    
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_OutputPixelTypeIsFloatingPointCheck
    
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterID3ID3
    cast = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterID3ID3

        Create a new object of the class itkLaplacianImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLaplacianImageFilterID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLaplacianImageFilterID3ID3 in _itkLaplacianImageFilterPython:
_itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_swigregister(itkLaplacianImageFilterID3ID3)
itkLaplacianImageFilterID3ID3___New_orig__ = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3___New_orig__
itkLaplacianImageFilterID3ID3_cast = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID3ID3_cast


def itkLaplacianImageFilterID4ID4_New():
    return itkLaplacianImageFilterID4ID4.New()

class itkLaplacianImageFilterID4ID4(itk.itkImageToImageFilterAPython.itkImageToImageFilterID4ID4):
    r"""


    This filter computes the Laplacian of a scalar-valued image.

    The Laplacian is an isotropic measure of the 2nd spatial derivative of
    an image. The Laplacian of an image highlights regions of rapid
    intensity change and is therefore often used for edge detection.
    Often, the Laplacian is applied to an image that has first been
    smoothed with a Gaussian filter in order to reduce its sensitivity to
    noise.

    The Laplacian at each pixel location is computed by convolution with
    the itk::LaplacianOperator. Inputs and Outputs The input to this
    filter is a scalar-valued itk::Image of arbitrary dimension. The
    output is a scalar-valued itk::Image.

    WARNING:  The pixel type of the input and output images must be of
    real type (float or double). ConceptChecking is used here to enforce
    the input pixel type. You will get a compilation error if the pixel
    type of the input and output images is not float or double.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    See:  LaplacianOperator
    example{Filtering/ImageFeature/ComputeLaplacian,Compute Laplacian} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_GenerateInputRequestedRegion)
    UseImageSpacingOn = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_UseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_GetUseImageSpacing)
    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_SameDimensionCheck
    
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_InputPixelTypeIsFloatingPointCheck
    
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_OutputPixelTypeIsFloatingPointCheck
    
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterID4ID4
    cast = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterID4ID4

        Create a new object of the class itkLaplacianImageFilterID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLaplacianImageFilterID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLaplacianImageFilterID4ID4 in _itkLaplacianImageFilterPython:
_itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_swigregister(itkLaplacianImageFilterID4ID4)
itkLaplacianImageFilterID4ID4___New_orig__ = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4___New_orig__
itkLaplacianImageFilterID4ID4_cast = _itkLaplacianImageFilterPython.itkLaplacianImageFilterID4ID4_cast


def itkLaplacianImageFilterIF2IF2_New():
    return itkLaplacianImageFilterIF2IF2.New()

class itkLaplacianImageFilterIF2IF2(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""


    This filter computes the Laplacian of a scalar-valued image.

    The Laplacian is an isotropic measure of the 2nd spatial derivative of
    an image. The Laplacian of an image highlights regions of rapid
    intensity change and is therefore often used for edge detection.
    Often, the Laplacian is applied to an image that has first been
    smoothed with a Gaussian filter in order to reduce its sensitivity to
    noise.

    The Laplacian at each pixel location is computed by convolution with
    the itk::LaplacianOperator. Inputs and Outputs The input to this
    filter is a scalar-valued itk::Image of arbitrary dimension. The
    output is a scalar-valued itk::Image.

    WARNING:  The pixel type of the input and output images must be of
    real type (float or double). ConceptChecking is used here to enforce
    the input pixel type. You will get a compilation error if the pixel
    type of the input and output images is not float or double.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    See:  LaplacianOperator
    example{Filtering/ImageFeature/ComputeLaplacian,Compute Laplacian} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GenerateInputRequestedRegion)
    UseImageSpacingOn = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_UseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_GetUseImageSpacing)
    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_SameDimensionCheck
    
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_InputPixelTypeIsFloatingPointCheck
    
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_OutputPixelTypeIsFloatingPointCheck
    
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterIF2IF2
    cast = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterIF2IF2

        Create a new object of the class itkLaplacianImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLaplacianImageFilterIF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLaplacianImageFilterIF2IF2 in _itkLaplacianImageFilterPython:
_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_swigregister(itkLaplacianImageFilterIF2IF2)
itkLaplacianImageFilterIF2IF2___New_orig__ = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2___New_orig__
itkLaplacianImageFilterIF2IF2_cast = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF2IF2_cast


def itkLaplacianImageFilterIF3IF3_New():
    return itkLaplacianImageFilterIF3IF3.New()

class itkLaplacianImageFilterIF3IF3(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""


    This filter computes the Laplacian of a scalar-valued image.

    The Laplacian is an isotropic measure of the 2nd spatial derivative of
    an image. The Laplacian of an image highlights regions of rapid
    intensity change and is therefore often used for edge detection.
    Often, the Laplacian is applied to an image that has first been
    smoothed with a Gaussian filter in order to reduce its sensitivity to
    noise.

    The Laplacian at each pixel location is computed by convolution with
    the itk::LaplacianOperator. Inputs and Outputs The input to this
    filter is a scalar-valued itk::Image of arbitrary dimension. The
    output is a scalar-valued itk::Image.

    WARNING:  The pixel type of the input and output images must be of
    real type (float or double). ConceptChecking is used here to enforce
    the input pixel type. You will get a compilation error if the pixel
    type of the input and output images is not float or double.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    See:  LaplacianOperator
    example{Filtering/ImageFeature/ComputeLaplacian,Compute Laplacian} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GenerateInputRequestedRegion)
    UseImageSpacingOn = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_UseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_GetUseImageSpacing)
    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_SameDimensionCheck
    
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_InputPixelTypeIsFloatingPointCheck
    
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_OutputPixelTypeIsFloatingPointCheck
    
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterIF3IF3
    cast = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterIF3IF3

        Create a new object of the class itkLaplacianImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLaplacianImageFilterIF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLaplacianImageFilterIF3IF3 in _itkLaplacianImageFilterPython:
_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_swigregister(itkLaplacianImageFilterIF3IF3)
itkLaplacianImageFilterIF3IF3___New_orig__ = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3___New_orig__
itkLaplacianImageFilterIF3IF3_cast = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF3IF3_cast


def itkLaplacianImageFilterIF4IF4_New():
    return itkLaplacianImageFilterIF4IF4.New()

class itkLaplacianImageFilterIF4IF4(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF4IF4):
    r"""


    This filter computes the Laplacian of a scalar-valued image.

    The Laplacian is an isotropic measure of the 2nd spatial derivative of
    an image. The Laplacian of an image highlights regions of rapid
    intensity change and is therefore often used for edge detection.
    Often, the Laplacian is applied to an image that has first been
    smoothed with a Gaussian filter in order to reduce its sensitivity to
    noise.

    The Laplacian at each pixel location is computed by convolution with
    the itk::LaplacianOperator. Inputs and Outputs The input to this
    filter is a scalar-valued itk::Image of arbitrary dimension. The
    output is a scalar-valued itk::Image.

    WARNING:  The pixel type of the input and output images must be of
    real type (float or double). ConceptChecking is used here to enforce
    the input pixel type. You will get a compilation error if the pixel
    type of the input and output images is not float or double.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    See:  LaplacianOperator
    example{Filtering/ImageFeature/ComputeLaplacian,Compute Laplacian} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_Clone)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_GenerateInputRequestedRegion)
    UseImageSpacingOn = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_UseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_GetUseImageSpacing)
    SameDimensionCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_SameDimensionCheck
    
    InputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_InputPixelTypeIsFloatingPointCheck
    
    OutputPixelTypeIsFloatingPointCheck = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_OutputPixelTypeIsFloatingPointCheck
    
    __swig_destroy__ = _itkLaplacianImageFilterPython.delete_itkLaplacianImageFilterIF4IF4
    cast = _swig_new_static_method(_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkLaplacianImageFilterIF4IF4

        Create a new object of the class itkLaplacianImageFilterIF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLaplacianImageFilterIF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLaplacianImageFilterIF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLaplacianImageFilterIF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLaplacianImageFilterIF4IF4 in _itkLaplacianImageFilterPython:
_itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_swigregister(itkLaplacianImageFilterIF4IF4)
itkLaplacianImageFilterIF4IF4___New_orig__ = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4___New_orig__
itkLaplacianImageFilterIF4IF4_cast = _itkLaplacianImageFilterPython.itkLaplacianImageFilterIF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def laplacian_image_filter(*args: itkt.ImageLike,  use_image_spacing: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for LaplacianImageFilter"""
    import itk

    kwarg_typehints = { 'use_image_spacing':use_image_spacing }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.LaplacianImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def laplacian_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageFeature.LaplacianImageFilter
    laplacian_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    laplacian_image_filter.__doc__ = filter_object.__doc__




