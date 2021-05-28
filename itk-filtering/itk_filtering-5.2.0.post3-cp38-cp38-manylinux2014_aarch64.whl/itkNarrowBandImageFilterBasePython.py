# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKNarrowBandPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkNarrowBandImageFilterBasePython
else:
    import _itkNarrowBandImageFilterBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkNarrowBandImageFilterBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkNarrowBandImageFilterBasePython.SWIG_PyStaticMethod_New

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
import itk.itkFiniteDifferenceImageFilterPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterAPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.stdcomplexPython
import itk.itkImagePython
import itk.itkSizePython
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
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkRGBAPixelPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterBPython
import itk.itkFiniteDifferenceFunctionPython
import itk.ITKNarrowBandBasePython
class itkNarrowBandImageFilterBaseID2ID2(itk.itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterID2ID2):
    r"""


    This class implements a multi-threaded finite difference image to
    image solver that can be applied to an arbitrary list of pixels.

    This class is intended as a common base class for classical narrowband
    solvers and manifold solvers. This base class implements a common
    memory management and multi-threaded architecture for applying a
    finite difference function to a list of pixels in an image. The
    specifics of narrowband solvers such as re-initialization and the use
    of land-mines are not implemented. INPUTS This filter takes an
    itk::Image as input. The appropriate type of input image is entirely
    determined by the application. As a rule, however, the input type is
    immediately converted to the output type before processing. This is
    because the input is not assumed to be a real value type and must be
    converted to signed, real values for the calculations. OUTPUTS The
    output is an itk::Image and is the solution of the pde. The embedding
    of the interface may vary with the application, but the usual ITK
    convention is that it is the zero level set in the output image.
    IMPORTANT! Read the documentation for FiniteDifferenceImageFilter
    before attempting to use this filter. The solver requires that you
    specify a FiniteDifferenceFunction to use for calculations. This is
    set using the method SetDifferenceFunction in the parent class.
    REFERENCES Sethian, J.A. Level Set Methods. Cambridge University
    Press. 1996. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_GetIsoSurfaceValue)
    InsertNarrowBandNode = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_InsertNarrowBandNode)
    SetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_SetNarrowBandTotalRadius)
    GetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_GetNarrowBandTotalRadius)
    SetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_SetNarrowBandInnerRadius)
    GetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_GetNarrowBandInnerRadius)
    CreateNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_CreateNarrowBand)
    SetNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_SetNarrowBand)
    CopyInputToOutput = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_CopyInputToOutput)
    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseID2ID2
    cast = _swig_new_static_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_cast)

# Register itkNarrowBandImageFilterBaseID2ID2 in _itkNarrowBandImageFilterBasePython:
_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_swigregister(itkNarrowBandImageFilterBaseID2ID2)
itkNarrowBandImageFilterBaseID2ID2_cast = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID2ID2_cast

class itkNarrowBandImageFilterBaseID3ID3(itk.itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterID3ID3):
    r"""


    This class implements a multi-threaded finite difference image to
    image solver that can be applied to an arbitrary list of pixels.

    This class is intended as a common base class for classical narrowband
    solvers and manifold solvers. This base class implements a common
    memory management and multi-threaded architecture for applying a
    finite difference function to a list of pixels in an image. The
    specifics of narrowband solvers such as re-initialization and the use
    of land-mines are not implemented. INPUTS This filter takes an
    itk::Image as input. The appropriate type of input image is entirely
    determined by the application. As a rule, however, the input type is
    immediately converted to the output type before processing. This is
    because the input is not assumed to be a real value type and must be
    converted to signed, real values for the calculations. OUTPUTS The
    output is an itk::Image and is the solution of the pde. The embedding
    of the interface may vary with the application, but the usual ITK
    convention is that it is the zero level set in the output image.
    IMPORTANT! Read the documentation for FiniteDifferenceImageFilter
    before attempting to use this filter. The solver requires that you
    specify a FiniteDifferenceFunction to use for calculations. This is
    set using the method SetDifferenceFunction in the parent class.
    REFERENCES Sethian, J.A. Level Set Methods. Cambridge University
    Press. 1996. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_GetIsoSurfaceValue)
    InsertNarrowBandNode = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_InsertNarrowBandNode)
    SetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_SetNarrowBandTotalRadius)
    GetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_GetNarrowBandTotalRadius)
    SetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_SetNarrowBandInnerRadius)
    GetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_GetNarrowBandInnerRadius)
    CreateNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_CreateNarrowBand)
    SetNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_SetNarrowBand)
    CopyInputToOutput = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_CopyInputToOutput)
    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseID3ID3
    cast = _swig_new_static_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_cast)

# Register itkNarrowBandImageFilterBaseID3ID3 in _itkNarrowBandImageFilterBasePython:
_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_swigregister(itkNarrowBandImageFilterBaseID3ID3)
itkNarrowBandImageFilterBaseID3ID3_cast = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID3ID3_cast

class itkNarrowBandImageFilterBaseID4ID4(itk.itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterID4ID4):
    r"""


    This class implements a multi-threaded finite difference image to
    image solver that can be applied to an arbitrary list of pixels.

    This class is intended as a common base class for classical narrowband
    solvers and manifold solvers. This base class implements a common
    memory management and multi-threaded architecture for applying a
    finite difference function to a list of pixels in an image. The
    specifics of narrowband solvers such as re-initialization and the use
    of land-mines are not implemented. INPUTS This filter takes an
    itk::Image as input. The appropriate type of input image is entirely
    determined by the application. As a rule, however, the input type is
    immediately converted to the output type before processing. This is
    because the input is not assumed to be a real value type and must be
    converted to signed, real values for the calculations. OUTPUTS The
    output is an itk::Image and is the solution of the pde. The embedding
    of the interface may vary with the application, but the usual ITK
    convention is that it is the zero level set in the output image.
    IMPORTANT! Read the documentation for FiniteDifferenceImageFilter
    before attempting to use this filter. The solver requires that you
    specify a FiniteDifferenceFunction to use for calculations. This is
    set using the method SetDifferenceFunction in the parent class.
    REFERENCES Sethian, J.A. Level Set Methods. Cambridge University
    Press. 1996. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_GetIsoSurfaceValue)
    InsertNarrowBandNode = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_InsertNarrowBandNode)
    SetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_SetNarrowBandTotalRadius)
    GetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_GetNarrowBandTotalRadius)
    SetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_SetNarrowBandInnerRadius)
    GetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_GetNarrowBandInnerRadius)
    CreateNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_CreateNarrowBand)
    SetNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_SetNarrowBand)
    CopyInputToOutput = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_CopyInputToOutput)
    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseID4ID4
    cast = _swig_new_static_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_cast)

# Register itkNarrowBandImageFilterBaseID4ID4 in _itkNarrowBandImageFilterBasePython:
_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_swigregister(itkNarrowBandImageFilterBaseID4ID4)
itkNarrowBandImageFilterBaseID4ID4_cast = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseID4ID4_cast

class itkNarrowBandImageFilterBaseIF2IF2(itk.itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF2IF2):
    r"""


    This class implements a multi-threaded finite difference image to
    image solver that can be applied to an arbitrary list of pixels.

    This class is intended as a common base class for classical narrowband
    solvers and manifold solvers. This base class implements a common
    memory management and multi-threaded architecture for applying a
    finite difference function to a list of pixels in an image. The
    specifics of narrowband solvers such as re-initialization and the use
    of land-mines are not implemented. INPUTS This filter takes an
    itk::Image as input. The appropriate type of input image is entirely
    determined by the application. As a rule, however, the input type is
    immediately converted to the output type before processing. This is
    because the input is not assumed to be a real value type and must be
    converted to signed, real values for the calculations. OUTPUTS The
    output is an itk::Image and is the solution of the pde. The embedding
    of the interface may vary with the application, but the usual ITK
    convention is that it is the zero level set in the output image.
    IMPORTANT! Read the documentation for FiniteDifferenceImageFilter
    before attempting to use this filter. The solver requires that you
    specify a FiniteDifferenceFunction to use for calculations. This is
    set using the method SetDifferenceFunction in the parent class.
    REFERENCES Sethian, J.A. Level Set Methods. Cambridge University
    Press. 1996. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetIsoSurfaceValue)
    InsertNarrowBandNode = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_InsertNarrowBandNode)
    SetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBandTotalRadius)
    GetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetNarrowBandTotalRadius)
    SetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBandInnerRadius)
    GetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_GetNarrowBandInnerRadius)
    CreateNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_CreateNarrowBand)
    SetNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_SetNarrowBand)
    CopyInputToOutput = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_CopyInputToOutput)
    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseIF2IF2
    cast = _swig_new_static_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_cast)

# Register itkNarrowBandImageFilterBaseIF2IF2 in _itkNarrowBandImageFilterBasePython:
_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_swigregister(itkNarrowBandImageFilterBaseIF2IF2)
itkNarrowBandImageFilterBaseIF2IF2_cast = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2_cast

class itkNarrowBandImageFilterBaseIF3IF3(itk.itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF3IF3):
    r"""


    This class implements a multi-threaded finite difference image to
    image solver that can be applied to an arbitrary list of pixels.

    This class is intended as a common base class for classical narrowband
    solvers and manifold solvers. This base class implements a common
    memory management and multi-threaded architecture for applying a
    finite difference function to a list of pixels in an image. The
    specifics of narrowband solvers such as re-initialization and the use
    of land-mines are not implemented. INPUTS This filter takes an
    itk::Image as input. The appropriate type of input image is entirely
    determined by the application. As a rule, however, the input type is
    immediately converted to the output type before processing. This is
    because the input is not assumed to be a real value type and must be
    converted to signed, real values for the calculations. OUTPUTS The
    output is an itk::Image and is the solution of the pde. The embedding
    of the interface may vary with the application, but the usual ITK
    convention is that it is the zero level set in the output image.
    IMPORTANT! Read the documentation for FiniteDifferenceImageFilter
    before attempting to use this filter. The solver requires that you
    specify a FiniteDifferenceFunction to use for calculations. This is
    set using the method SetDifferenceFunction in the parent class.
    REFERENCES Sethian, J.A. Level Set Methods. Cambridge University
    Press. 1996. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetIsoSurfaceValue)
    InsertNarrowBandNode = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_InsertNarrowBandNode)
    SetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBandTotalRadius)
    GetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetNarrowBandTotalRadius)
    SetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBandInnerRadius)
    GetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_GetNarrowBandInnerRadius)
    CreateNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_CreateNarrowBand)
    SetNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_SetNarrowBand)
    CopyInputToOutput = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_CopyInputToOutput)
    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseIF3IF3
    cast = _swig_new_static_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_cast)

# Register itkNarrowBandImageFilterBaseIF3IF3 in _itkNarrowBandImageFilterBasePython:
_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_swigregister(itkNarrowBandImageFilterBaseIF3IF3)
itkNarrowBandImageFilterBaseIF3IF3_cast = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3_cast

class itkNarrowBandImageFilterBaseIF4IF4(itk.itkFiniteDifferenceImageFilterPython.itkFiniteDifferenceImageFilterIF4IF4):
    r"""


    This class implements a multi-threaded finite difference image to
    image solver that can be applied to an arbitrary list of pixels.

    This class is intended as a common base class for classical narrowband
    solvers and manifold solvers. This base class implements a common
    memory management and multi-threaded architecture for applying a
    finite difference function to a list of pixels in an image. The
    specifics of narrowband solvers such as re-initialization and the use
    of land-mines are not implemented. INPUTS This filter takes an
    itk::Image as input. The appropriate type of input image is entirely
    determined by the application. As a rule, however, the input type is
    immediately converted to the output type before processing. This is
    because the input is not assumed to be a real value type and must be
    converted to signed, real values for the calculations. OUTPUTS The
    output is an itk::Image and is the solution of the pde. The embedding
    of the interface may vary with the application, but the usual ITK
    convention is that it is the zero level set in the output image.
    IMPORTANT! Read the documentation for FiniteDifferenceImageFilter
    before attempting to use this filter. The solver requires that you
    specify a FiniteDifferenceFunction to use for calculations. This is
    set using the method SetDifferenceFunction in the parent class.
    REFERENCES Sethian, J.A. Level Set Methods. Cambridge University
    Press. 1996. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_SetIsoSurfaceValue)
    GetIsoSurfaceValue = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_GetIsoSurfaceValue)
    InsertNarrowBandNode = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_InsertNarrowBandNode)
    SetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_SetNarrowBandTotalRadius)
    GetNarrowBandTotalRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_GetNarrowBandTotalRadius)
    SetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_SetNarrowBandInnerRadius)
    GetNarrowBandInnerRadius = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_GetNarrowBandInnerRadius)
    CreateNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_CreateNarrowBand)
    SetNarrowBand = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_SetNarrowBand)
    CopyInputToOutput = _swig_new_instance_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_CopyInputToOutput)
    __swig_destroy__ = _itkNarrowBandImageFilterBasePython.delete_itkNarrowBandImageFilterBaseIF4IF4
    cast = _swig_new_static_method(_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_cast)

# Register itkNarrowBandImageFilterBaseIF4IF4 in _itkNarrowBandImageFilterBasePython:
_itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_swigregister(itkNarrowBandImageFilterBaseIF4IF4)
itkNarrowBandImageFilterBaseIF4IF4_cast = _itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def narrow_band_image_filter_base(*args: itkt.ImageLike,  iso_surface_value: float=..., narrow_band_total_radius: float=..., narrow_band_inner_radius: float=..., narrow_band=..., difference_function=..., number_of_iterations: int=..., use_image_spacing: bool=..., maximum_rms_error: float=..., rms_change: float=..., manual_reinitialization: bool=..., is_initialized: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for NarrowBandImageFilterBase"""
    import itk

    kwarg_typehints = { 'iso_surface_value':iso_surface_value,'narrow_band_total_radius':narrow_band_total_radius,'narrow_band_inner_radius':narrow_band_inner_radius,'narrow_band':narrow_band,'difference_function':difference_function,'number_of_iterations':number_of_iterations,'use_image_spacing':use_image_spacing,'maximum_rms_error':maximum_rms_error,'rms_change':rms_change,'manual_reinitialization':manual_reinitialization,'is_initialized':is_initialized }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.NarrowBandImageFilterBase.New(*args, **kwargs)
    return instance.__internal_call__()

def narrow_band_image_filter_base_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKNarrowBand.NarrowBandImageFilterBase
    narrow_band_image_filter_base.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    narrow_band_image_filter_base.__doc__ = filter_object.__doc__




