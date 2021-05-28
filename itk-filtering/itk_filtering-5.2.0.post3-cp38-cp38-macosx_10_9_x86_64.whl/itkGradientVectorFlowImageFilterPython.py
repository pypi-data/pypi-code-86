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
    from . import _itkGradientVectorFlowImageFilterPython
else:
    import _itkGradientVectorFlowImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGradientVectorFlowImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGradientVectorFlowImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkLaplacianImageFilterPython

def itkGradientVectorFlowImageFilterICVF22ICVF22F_New():
    return itkGradientVectorFlowImageFilterICVF22ICVF22F.New()

class itkGradientVectorFlowImageFilterICVF22ICVF22F(itk.itkImageToImageFilterAPython.itkImageToImageFilterICVF22ICVF22):
    r"""


    This class computes a diffusion of the gradient vectors for graylevel
    or binary edge map derive from the image. It enlarges the capture
    range of the gradient force and make external force derived from the
    gradient work effectively in the framework of deformable model.

    This implementation of GVF closely follows this paper:http://ww.vavlab
    .ee.boun.edu.tr/courses/574/materialx/Active%20Contour s/xu_GVF.pdf

    dx and dy are assumed to be 1 and the CFL restriction for convergence
    has been modified for multi-dimensional images 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_Clone)
    SetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_SetLaplacianFilter)
    GetModifiableLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_GetModifiableLaplacianFilter)
    GetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_GetLaplacianFilter)
    SetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_GetTimeStep)
    SetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_SetNoiseLevel)
    GetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_GetNoiseLevel)
    SetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_SetIterationNum)
    GetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_GetIterationNum)
    SameDimensionCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_SameDimensionCheck
    
    InputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_InputHasNumericTraitsCheck
    
    OutputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientVectorFlowImageFilterPython.delete_itkGradientVectorFlowImageFilterICVF22ICVF22F
    cast = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_cast)

    def New(*args, **kargs):
        """New() -> itkGradientVectorFlowImageFilterICVF22ICVF22F

        Create a new object of the class itkGradientVectorFlowImageFilterICVF22ICVF22F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientVectorFlowImageFilterICVF22ICVF22F.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientVectorFlowImageFilterICVF22ICVF22F.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientVectorFlowImageFilterICVF22ICVF22F.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientVectorFlowImageFilterICVF22ICVF22F in _itkGradientVectorFlowImageFilterPython:
_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_swigregister(itkGradientVectorFlowImageFilterICVF22ICVF22F)
itkGradientVectorFlowImageFilterICVF22ICVF22F___New_orig__ = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F___New_orig__
itkGradientVectorFlowImageFilterICVF22ICVF22F_cast = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF22ICVF22F_cast


def itkGradientVectorFlowImageFilterICVF33ICVF33F_New():
    return itkGradientVectorFlowImageFilterICVF33ICVF33F.New()

class itkGradientVectorFlowImageFilterICVF33ICVF33F(itk.itkImageToImageFilterAPython.itkImageToImageFilterICVF33ICVF33):
    r"""


    This class computes a diffusion of the gradient vectors for graylevel
    or binary edge map derive from the image. It enlarges the capture
    range of the gradient force and make external force derived from the
    gradient work effectively in the framework of deformable model.

    This implementation of GVF closely follows this paper:http://ww.vavlab
    .ee.boun.edu.tr/courses/574/materialx/Active%20Contour s/xu_GVF.pdf

    dx and dy are assumed to be 1 and the CFL restriction for convergence
    has been modified for multi-dimensional images 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_Clone)
    SetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_SetLaplacianFilter)
    GetModifiableLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_GetModifiableLaplacianFilter)
    GetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_GetLaplacianFilter)
    SetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_GetTimeStep)
    SetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_SetNoiseLevel)
    GetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_GetNoiseLevel)
    SetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_SetIterationNum)
    GetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_GetIterationNum)
    SameDimensionCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_SameDimensionCheck
    
    InputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_InputHasNumericTraitsCheck
    
    OutputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientVectorFlowImageFilterPython.delete_itkGradientVectorFlowImageFilterICVF33ICVF33F
    cast = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_cast)

    def New(*args, **kargs):
        """New() -> itkGradientVectorFlowImageFilterICVF33ICVF33F

        Create a new object of the class itkGradientVectorFlowImageFilterICVF33ICVF33F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientVectorFlowImageFilterICVF33ICVF33F.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientVectorFlowImageFilterICVF33ICVF33F.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientVectorFlowImageFilterICVF33ICVF33F.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientVectorFlowImageFilterICVF33ICVF33F in _itkGradientVectorFlowImageFilterPython:
_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_swigregister(itkGradientVectorFlowImageFilterICVF33ICVF33F)
itkGradientVectorFlowImageFilterICVF33ICVF33F___New_orig__ = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F___New_orig__
itkGradientVectorFlowImageFilterICVF33ICVF33F_cast = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF33ICVF33F_cast


def itkGradientVectorFlowImageFilterICVF44ICVF44F_New():
    return itkGradientVectorFlowImageFilterICVF44ICVF44F.New()

class itkGradientVectorFlowImageFilterICVF44ICVF44F(itk.itkImageToImageFilterAPython.itkImageToImageFilterICVF44ICVF44):
    r"""


    This class computes a diffusion of the gradient vectors for graylevel
    or binary edge map derive from the image. It enlarges the capture
    range of the gradient force and make external force derived from the
    gradient work effectively in the framework of deformable model.

    This implementation of GVF closely follows this paper:http://ww.vavlab
    .ee.boun.edu.tr/courses/574/materialx/Active%20Contour s/xu_GVF.pdf

    dx and dy are assumed to be 1 and the CFL restriction for convergence
    has been modified for multi-dimensional images 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_Clone)
    SetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_SetLaplacianFilter)
    GetModifiableLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_GetModifiableLaplacianFilter)
    GetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_GetLaplacianFilter)
    SetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_GetTimeStep)
    SetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_SetNoiseLevel)
    GetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_GetNoiseLevel)
    SetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_SetIterationNum)
    GetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_GetIterationNum)
    SameDimensionCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_SameDimensionCheck
    
    InputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_InputHasNumericTraitsCheck
    
    OutputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientVectorFlowImageFilterPython.delete_itkGradientVectorFlowImageFilterICVF44ICVF44F
    cast = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_cast)

    def New(*args, **kargs):
        """New() -> itkGradientVectorFlowImageFilterICVF44ICVF44F

        Create a new object of the class itkGradientVectorFlowImageFilterICVF44ICVF44F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientVectorFlowImageFilterICVF44ICVF44F.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientVectorFlowImageFilterICVF44ICVF44F.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientVectorFlowImageFilterICVF44ICVF44F.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientVectorFlowImageFilterICVF44ICVF44F in _itkGradientVectorFlowImageFilterPython:
_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_swigregister(itkGradientVectorFlowImageFilterICVF44ICVF44F)
itkGradientVectorFlowImageFilterICVF44ICVF44F___New_orig__ = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F___New_orig__
itkGradientVectorFlowImageFilterICVF44ICVF44F_cast = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterICVF44ICVF44F_cast


def itkGradientVectorFlowImageFilterIVF22IVF22F_New():
    return itkGradientVectorFlowImageFilterIVF22IVF22F.New()

class itkGradientVectorFlowImageFilterIVF22IVF22F(itk.itkImageToImageFilterAPython.itkImageToImageFilterIVF22IVF22):
    r"""


    This class computes a diffusion of the gradient vectors for graylevel
    or binary edge map derive from the image. It enlarges the capture
    range of the gradient force and make external force derived from the
    gradient work effectively in the framework of deformable model.

    This implementation of GVF closely follows this paper:http://ww.vavlab
    .ee.boun.edu.tr/courses/574/materialx/Active%20Contour s/xu_GVF.pdf

    dx and dy are assumed to be 1 and the CFL restriction for convergence
    has been modified for multi-dimensional images 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_Clone)
    SetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_SetLaplacianFilter)
    GetModifiableLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_GetModifiableLaplacianFilter)
    GetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_GetLaplacianFilter)
    SetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_GetTimeStep)
    SetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_SetNoiseLevel)
    GetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_GetNoiseLevel)
    SetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_SetIterationNum)
    GetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_GetIterationNum)
    SameDimensionCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_SameDimensionCheck
    
    InputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_InputHasNumericTraitsCheck
    
    OutputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientVectorFlowImageFilterPython.delete_itkGradientVectorFlowImageFilterIVF22IVF22F
    cast = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_cast)

    def New(*args, **kargs):
        """New() -> itkGradientVectorFlowImageFilterIVF22IVF22F

        Create a new object of the class itkGradientVectorFlowImageFilterIVF22IVF22F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientVectorFlowImageFilterIVF22IVF22F.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientVectorFlowImageFilterIVF22IVF22F.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientVectorFlowImageFilterIVF22IVF22F.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientVectorFlowImageFilterIVF22IVF22F in _itkGradientVectorFlowImageFilterPython:
_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_swigregister(itkGradientVectorFlowImageFilterIVF22IVF22F)
itkGradientVectorFlowImageFilterIVF22IVF22F___New_orig__ = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F___New_orig__
itkGradientVectorFlowImageFilterIVF22IVF22F_cast = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF22IVF22F_cast


def itkGradientVectorFlowImageFilterIVF33IVF33F_New():
    return itkGradientVectorFlowImageFilterIVF33IVF33F.New()

class itkGradientVectorFlowImageFilterIVF33IVF33F(itk.itkImageToImageFilterAPython.itkImageToImageFilterIVF33IVF33):
    r"""


    This class computes a diffusion of the gradient vectors for graylevel
    or binary edge map derive from the image. It enlarges the capture
    range of the gradient force and make external force derived from the
    gradient work effectively in the framework of deformable model.

    This implementation of GVF closely follows this paper:http://ww.vavlab
    .ee.boun.edu.tr/courses/574/materialx/Active%20Contour s/xu_GVF.pdf

    dx and dy are assumed to be 1 and the CFL restriction for convergence
    has been modified for multi-dimensional images 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_Clone)
    SetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_SetLaplacianFilter)
    GetModifiableLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_GetModifiableLaplacianFilter)
    GetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_GetLaplacianFilter)
    SetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_GetTimeStep)
    SetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_SetNoiseLevel)
    GetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_GetNoiseLevel)
    SetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_SetIterationNum)
    GetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_GetIterationNum)
    SameDimensionCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_SameDimensionCheck
    
    InputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_InputHasNumericTraitsCheck
    
    OutputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientVectorFlowImageFilterPython.delete_itkGradientVectorFlowImageFilterIVF33IVF33F
    cast = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_cast)

    def New(*args, **kargs):
        """New() -> itkGradientVectorFlowImageFilterIVF33IVF33F

        Create a new object of the class itkGradientVectorFlowImageFilterIVF33IVF33F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientVectorFlowImageFilterIVF33IVF33F.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientVectorFlowImageFilterIVF33IVF33F.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientVectorFlowImageFilterIVF33IVF33F.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientVectorFlowImageFilterIVF33IVF33F in _itkGradientVectorFlowImageFilterPython:
_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_swigregister(itkGradientVectorFlowImageFilterIVF33IVF33F)
itkGradientVectorFlowImageFilterIVF33IVF33F___New_orig__ = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F___New_orig__
itkGradientVectorFlowImageFilterIVF33IVF33F_cast = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF33IVF33F_cast


def itkGradientVectorFlowImageFilterIVF44IVF44F_New():
    return itkGradientVectorFlowImageFilterIVF44IVF44F.New()

class itkGradientVectorFlowImageFilterIVF44IVF44F(itk.itkImageToImageFilterAPython.itkImageToImageFilterIVF44IVF44):
    r"""


    This class computes a diffusion of the gradient vectors for graylevel
    or binary edge map derive from the image. It enlarges the capture
    range of the gradient force and make external force derived from the
    gradient work effectively in the framework of deformable model.

    This implementation of GVF closely follows this paper:http://ww.vavlab
    .ee.boun.edu.tr/courses/574/materialx/Active%20Contour s/xu_GVF.pdf

    dx and dy are assumed to be 1 and the CFL restriction for convergence
    has been modified for multi-dimensional images 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_Clone)
    SetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_SetLaplacianFilter)
    GetModifiableLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_GetModifiableLaplacianFilter)
    GetLaplacianFilter = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_GetLaplacianFilter)
    SetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_GetTimeStep)
    SetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_SetNoiseLevel)
    GetNoiseLevel = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_GetNoiseLevel)
    SetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_SetIterationNum)
    GetIterationNum = _swig_new_instance_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_GetIterationNum)
    SameDimensionCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_SameDimensionCheck
    
    InputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_InputHasNumericTraitsCheck
    
    OutputHasNumericTraitsCheck = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_OutputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientVectorFlowImageFilterPython.delete_itkGradientVectorFlowImageFilterIVF44IVF44F
    cast = _swig_new_static_method(_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_cast)

    def New(*args, **kargs):
        """New() -> itkGradientVectorFlowImageFilterIVF44IVF44F

        Create a new object of the class itkGradientVectorFlowImageFilterIVF44IVF44F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientVectorFlowImageFilterIVF44IVF44F.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientVectorFlowImageFilterIVF44IVF44F.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientVectorFlowImageFilterIVF44IVF44F.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientVectorFlowImageFilterIVF44IVF44F in _itkGradientVectorFlowImageFilterPython:
_itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_swigregister(itkGradientVectorFlowImageFilterIVF44IVF44F)
itkGradientVectorFlowImageFilterIVF44IVF44F___New_orig__ = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F___New_orig__
itkGradientVectorFlowImageFilterIVF44IVF44F_cast = _itkGradientVectorFlowImageFilterPython.itkGradientVectorFlowImageFilterIVF44IVF44F_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def gradient_vector_flow_image_filter(*args: itkt.ImageLike,  laplacian_filter=..., time_step: float=..., noise_level: float=..., iteration_num: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for GradientVectorFlowImageFilter"""
    import itk

    kwarg_typehints = { 'laplacian_filter':laplacian_filter,'time_step':time_step,'noise_level':noise_level,'iteration_num':iteration_num }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.GradientVectorFlowImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def gradient_vector_flow_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageFeature.GradientVectorFlowImageFilter
    gradient_vector_flow_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    gradient_vector_flow_image_filter.__doc__ = filter_object.__doc__




