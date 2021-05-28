# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKAnisotropicSmoothingPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkCurvatureAnisotropicDiffusionImageFilterPython
else:
    import _itkCurvatureAnisotropicDiffusionImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCurvatureAnisotropicDiffusionImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCurvatureAnisotropicDiffusionImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkAnisotropicDiffusionImageFilterPython
import itk.itkDenseFiniteDifferenceImageFilterPython
import itk.itkFiniteDifferenceImageFilterPython
import itk.itkInPlaceImageFilterAPython
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
import itk.itkImageToImageFilterAPython
import itk.itkFiniteDifferenceFunctionPython

def itkCurvatureAnisotropicDiffusionImageFilterID2ID2_New():
    return itkCurvatureAnisotropicDiffusionImageFilterID2ID2.New()

class itkCurvatureAnisotropicDiffusionImageFilterID2ID2(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterID2ID2):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the modified curvature diffusion equation (MCDE).

    For detailed information on anisotropic diffusion and the MCDE see
    itkAnisotropicDiffusionFunction and
    itkCurvatureNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input and output to this filter must be a
    scalar itk::Image with numerical pixel types (float or double). A user
    defined type which correctly defines arithmetic operations with
    floating point accuracy should also give correct results. Parameters
    Please first read all the documentation found in
    AnisotropicDiffusionImageFilter and AnisotropicDiffusionFunction. Also
    see CurvatureNDAnisotropicDiffusionFunction.  The default time step
    for this filter is set to the maximum theoretically stable value: 0.5
    / 2^N, where N is the dimensionality of the image. For a 2D image,
    this means valid time steps are below 0.1250. For a 3D image, valid
    time steps are below 0.0625.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  CurvatureNDAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2_Clone)
    OutputHasNumericTraitsCheck = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.delete_itkCurvatureAnisotropicDiffusionImageFilterID2ID2
    cast = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureAnisotropicDiffusionImageFilterID2ID2

        Create a new object of the class itkCurvatureAnisotropicDiffusionImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureAnisotropicDiffusionImageFilterID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCurvatureAnisotropicDiffusionImageFilterID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCurvatureAnisotropicDiffusionImageFilterID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvatureAnisotropicDiffusionImageFilterID2ID2 in _itkCurvatureAnisotropicDiffusionImageFilterPython:
_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2_swigregister(itkCurvatureAnisotropicDiffusionImageFilterID2ID2)
itkCurvatureAnisotropicDiffusionImageFilterID2ID2___New_orig__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2___New_orig__
itkCurvatureAnisotropicDiffusionImageFilterID2ID2_cast = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID2ID2_cast


def itkCurvatureAnisotropicDiffusionImageFilterID3ID3_New():
    return itkCurvatureAnisotropicDiffusionImageFilterID3ID3.New()

class itkCurvatureAnisotropicDiffusionImageFilterID3ID3(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterID3ID3):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the modified curvature diffusion equation (MCDE).

    For detailed information on anisotropic diffusion and the MCDE see
    itkAnisotropicDiffusionFunction and
    itkCurvatureNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input and output to this filter must be a
    scalar itk::Image with numerical pixel types (float or double). A user
    defined type which correctly defines arithmetic operations with
    floating point accuracy should also give correct results. Parameters
    Please first read all the documentation found in
    AnisotropicDiffusionImageFilter and AnisotropicDiffusionFunction. Also
    see CurvatureNDAnisotropicDiffusionFunction.  The default time step
    for this filter is set to the maximum theoretically stable value: 0.5
    / 2^N, where N is the dimensionality of the image. For a 2D image,
    this means valid time steps are below 0.1250. For a 3D image, valid
    time steps are below 0.0625.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  CurvatureNDAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3_Clone)
    OutputHasNumericTraitsCheck = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.delete_itkCurvatureAnisotropicDiffusionImageFilterID3ID3
    cast = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureAnisotropicDiffusionImageFilterID3ID3

        Create a new object of the class itkCurvatureAnisotropicDiffusionImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureAnisotropicDiffusionImageFilterID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCurvatureAnisotropicDiffusionImageFilterID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCurvatureAnisotropicDiffusionImageFilterID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvatureAnisotropicDiffusionImageFilterID3ID3 in _itkCurvatureAnisotropicDiffusionImageFilterPython:
_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3_swigregister(itkCurvatureAnisotropicDiffusionImageFilterID3ID3)
itkCurvatureAnisotropicDiffusionImageFilterID3ID3___New_orig__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3___New_orig__
itkCurvatureAnisotropicDiffusionImageFilterID3ID3_cast = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID3ID3_cast


def itkCurvatureAnisotropicDiffusionImageFilterID4ID4_New():
    return itkCurvatureAnisotropicDiffusionImageFilterID4ID4.New()

class itkCurvatureAnisotropicDiffusionImageFilterID4ID4(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterID4ID4):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the modified curvature diffusion equation (MCDE).

    For detailed information on anisotropic diffusion and the MCDE see
    itkAnisotropicDiffusionFunction and
    itkCurvatureNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input and output to this filter must be a
    scalar itk::Image with numerical pixel types (float or double). A user
    defined type which correctly defines arithmetic operations with
    floating point accuracy should also give correct results. Parameters
    Please first read all the documentation found in
    AnisotropicDiffusionImageFilter and AnisotropicDiffusionFunction. Also
    see CurvatureNDAnisotropicDiffusionFunction.  The default time step
    for this filter is set to the maximum theoretically stable value: 0.5
    / 2^N, where N is the dimensionality of the image. For a 2D image,
    this means valid time steps are below 0.1250. For a 3D image, valid
    time steps are below 0.0625.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  CurvatureNDAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID4ID4_Clone)
    OutputHasNumericTraitsCheck = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID4ID4_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.delete_itkCurvatureAnisotropicDiffusionImageFilterID4ID4
    cast = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureAnisotropicDiffusionImageFilterID4ID4

        Create a new object of the class itkCurvatureAnisotropicDiffusionImageFilterID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureAnisotropicDiffusionImageFilterID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCurvatureAnisotropicDiffusionImageFilterID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCurvatureAnisotropicDiffusionImageFilterID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvatureAnisotropicDiffusionImageFilterID4ID4 in _itkCurvatureAnisotropicDiffusionImageFilterPython:
_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID4ID4_swigregister(itkCurvatureAnisotropicDiffusionImageFilterID4ID4)
itkCurvatureAnisotropicDiffusionImageFilterID4ID4___New_orig__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID4ID4___New_orig__
itkCurvatureAnisotropicDiffusionImageFilterID4ID4_cast = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterID4ID4_cast


def itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_New():
    return itkCurvatureAnisotropicDiffusionImageFilterIF2IF2.New()

class itkCurvatureAnisotropicDiffusionImageFilterIF2IF2(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF2IF2):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the modified curvature diffusion equation (MCDE).

    For detailed information on anisotropic diffusion and the MCDE see
    itkAnisotropicDiffusionFunction and
    itkCurvatureNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input and output to this filter must be a
    scalar itk::Image with numerical pixel types (float or double). A user
    defined type which correctly defines arithmetic operations with
    floating point accuracy should also give correct results. Parameters
    Please first read all the documentation found in
    AnisotropicDiffusionImageFilter and AnisotropicDiffusionFunction. Also
    see CurvatureNDAnisotropicDiffusionFunction.  The default time step
    for this filter is set to the maximum theoretically stable value: 0.5
    / 2^N, where N is the dimensionality of the image. For a 2D image,
    this means valid time steps are below 0.1250. For a 3D image, valid
    time steps are below 0.0625.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  CurvatureNDAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_Clone)
    OutputHasNumericTraitsCheck = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.delete_itkCurvatureAnisotropicDiffusionImageFilterIF2IF2
    cast = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureAnisotropicDiffusionImageFilterIF2IF2

        Create a new object of the class itkCurvatureAnisotropicDiffusionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureAnisotropicDiffusionImageFilterIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCurvatureAnisotropicDiffusionImageFilterIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCurvatureAnisotropicDiffusionImageFilterIF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvatureAnisotropicDiffusionImageFilterIF2IF2 in _itkCurvatureAnisotropicDiffusionImageFilterPython:
_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_swigregister(itkCurvatureAnisotropicDiffusionImageFilterIF2IF2)
itkCurvatureAnisotropicDiffusionImageFilterIF2IF2___New_orig__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2___New_orig__
itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_cast = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF2IF2_cast


def itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_New():
    return itkCurvatureAnisotropicDiffusionImageFilterIF3IF3.New()

class itkCurvatureAnisotropicDiffusionImageFilterIF3IF3(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF3IF3):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the modified curvature diffusion equation (MCDE).

    For detailed information on anisotropic diffusion and the MCDE see
    itkAnisotropicDiffusionFunction and
    itkCurvatureNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input and output to this filter must be a
    scalar itk::Image with numerical pixel types (float or double). A user
    defined type which correctly defines arithmetic operations with
    floating point accuracy should also give correct results. Parameters
    Please first read all the documentation found in
    AnisotropicDiffusionImageFilter and AnisotropicDiffusionFunction. Also
    see CurvatureNDAnisotropicDiffusionFunction.  The default time step
    for this filter is set to the maximum theoretically stable value: 0.5
    / 2^N, where N is the dimensionality of the image. For a 2D image,
    this means valid time steps are below 0.1250. For a 3D image, valid
    time steps are below 0.0625.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  CurvatureNDAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_Clone)
    OutputHasNumericTraitsCheck = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.delete_itkCurvatureAnisotropicDiffusionImageFilterIF3IF3
    cast = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureAnisotropicDiffusionImageFilterIF3IF3

        Create a new object of the class itkCurvatureAnisotropicDiffusionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureAnisotropicDiffusionImageFilterIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCurvatureAnisotropicDiffusionImageFilterIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCurvatureAnisotropicDiffusionImageFilterIF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvatureAnisotropicDiffusionImageFilterIF3IF3 in _itkCurvatureAnisotropicDiffusionImageFilterPython:
_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_swigregister(itkCurvatureAnisotropicDiffusionImageFilterIF3IF3)
itkCurvatureAnisotropicDiffusionImageFilterIF3IF3___New_orig__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3___New_orig__
itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_cast = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF3IF3_cast


def itkCurvatureAnisotropicDiffusionImageFilterIF4IF4_New():
    return itkCurvatureAnisotropicDiffusionImageFilterIF4IF4.New()

class itkCurvatureAnisotropicDiffusionImageFilterIF4IF4(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF4IF4):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the modified curvature diffusion equation (MCDE).

    For detailed information on anisotropic diffusion and the MCDE see
    itkAnisotropicDiffusionFunction and
    itkCurvatureNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input and output to this filter must be a
    scalar itk::Image with numerical pixel types (float or double). A user
    defined type which correctly defines arithmetic operations with
    floating point accuracy should also give correct results. Parameters
    Please first read all the documentation found in
    AnisotropicDiffusionImageFilter and AnisotropicDiffusionFunction. Also
    see CurvatureNDAnisotropicDiffusionFunction.  The default time step
    for this filter is set to the maximum theoretically stable value: 0.5
    / 2^N, where N is the dimensionality of the image. For a 2D image,
    this means valid time steps are below 0.1250. For a 3D image, valid
    time steps are below 0.0625.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  CurvatureNDAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF4IF4_Clone)
    OutputHasNumericTraitsCheck = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF4IF4_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.delete_itkCurvatureAnisotropicDiffusionImageFilterIF4IF4
    cast = _swig_new_static_method(_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureAnisotropicDiffusionImageFilterIF4IF4

        Create a new object of the class itkCurvatureAnisotropicDiffusionImageFilterIF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureAnisotropicDiffusionImageFilterIF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCurvatureAnisotropicDiffusionImageFilterIF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCurvatureAnisotropicDiffusionImageFilterIF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvatureAnisotropicDiffusionImageFilterIF4IF4 in _itkCurvatureAnisotropicDiffusionImageFilterPython:
_itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF4IF4_swigregister(itkCurvatureAnisotropicDiffusionImageFilterIF4IF4)
itkCurvatureAnisotropicDiffusionImageFilterIF4IF4___New_orig__ = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF4IF4___New_orig__
itkCurvatureAnisotropicDiffusionImageFilterIF4IF4_cast = _itkCurvatureAnisotropicDiffusionImageFilterPython.itkCurvatureAnisotropicDiffusionImageFilterIF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def curvature_anisotropic_diffusion_image_filter(*args: itkt.ImageLike,  time_step: float=..., conductance_parameter: float=..., conductance_scaling_update_interval: int=..., conductance_scaling_parameter: float=..., fixed_average_gradient_magnitude: float=..., difference_function=..., number_of_iterations: int=..., use_image_spacing: bool=..., maximum_rms_error: float=..., rms_change: float=..., manual_reinitialization: bool=..., is_initialized: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for CurvatureAnisotropicDiffusionImageFilter"""
    import itk

    kwarg_typehints = { 'time_step':time_step,'conductance_parameter':conductance_parameter,'conductance_scaling_update_interval':conductance_scaling_update_interval,'conductance_scaling_parameter':conductance_scaling_parameter,'fixed_average_gradient_magnitude':fixed_average_gradient_magnitude,'difference_function':difference_function,'number_of_iterations':number_of_iterations,'use_image_spacing':use_image_spacing,'maximum_rms_error':maximum_rms_error,'rms_change':rms_change,'manual_reinitialization':manual_reinitialization,'is_initialized':is_initialized }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.CurvatureAnisotropicDiffusionImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def curvature_anisotropic_diffusion_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKAnisotropicSmoothing.CurvatureAnisotropicDiffusionImageFilter
    curvature_anisotropic_diffusion_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    curvature_anisotropic_diffusion_image_filter.__doc__ = filter_object.__doc__




