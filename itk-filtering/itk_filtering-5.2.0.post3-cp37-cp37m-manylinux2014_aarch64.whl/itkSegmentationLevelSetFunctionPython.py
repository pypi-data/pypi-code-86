# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKLevelSetsPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkSegmentationLevelSetFunctionPython
else:
    import _itkSegmentationLevelSetFunctionPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSegmentationLevelSetFunctionPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSegmentationLevelSetFunctionPython.SWIG_PyStaticMethod_New

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
import itk.itkLevelSetFunctionPython
import itk.itkFiniteDifferenceFunctionPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vector_refPython
import itk.itkSizePython
import itk.itkCovariantVectorPython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkOffsetPython
import itk.itkIndexPython
import itk.itkRGBPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
class itkSegmentationLevelSetFunctionID2ID2(itk.itkLevelSetFunctionPython.itkLevelSetFunctionID2):
    r"""


    This object defines the API for a class of function objects which
    perform level set based segmentations. The
    SegmentationLevelSetImageFilter objects use these
    SegmentationLevelSetFunction objects to perform the numerical
    calculations which move a level set front to lock onto image features.

    In order to create a working function object, you must subclass the
    CalculateSpeedImage method to produce a "feature image" that is used
    by the parent LevelSetFunction class as the PropagationSpeed for its
    calculations.

    See:   SegmentationLevelSetImageFilter

    See:   LevelSetFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    GetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_GetFeatureImage)
    SetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_SetFeatureImage)
    GetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_GetSpeedImage)
    SetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_SetSpeedImage)
    GetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_GetAdvectionImage)
    SetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_SetAdvectionImage)
    CalculateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_CalculateSpeedImage)
    CalculateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_CalculateAdvectionImage)
    AllocateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_AllocateSpeedImage)
    AllocateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_AllocateAdvectionImage)
    ReverseExpansionDirection = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_ReverseExpansionDirection)
    __swig_destroy__ = _itkSegmentationLevelSetFunctionPython.delete_itkSegmentationLevelSetFunctionID2ID2
    cast = _swig_new_static_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_cast)

# Register itkSegmentationLevelSetFunctionID2ID2 in _itkSegmentationLevelSetFunctionPython:
_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_swigregister(itkSegmentationLevelSetFunctionID2ID2)
itkSegmentationLevelSetFunctionID2ID2_cast = _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID2ID2_cast

class itkSegmentationLevelSetFunctionID3ID3(itk.itkLevelSetFunctionPython.itkLevelSetFunctionID3):
    r"""


    This object defines the API for a class of function objects which
    perform level set based segmentations. The
    SegmentationLevelSetImageFilter objects use these
    SegmentationLevelSetFunction objects to perform the numerical
    calculations which move a level set front to lock onto image features.

    In order to create a working function object, you must subclass the
    CalculateSpeedImage method to produce a "feature image" that is used
    by the parent LevelSetFunction class as the PropagationSpeed for its
    calculations.

    See:   SegmentationLevelSetImageFilter

    See:   LevelSetFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    GetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_GetFeatureImage)
    SetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_SetFeatureImage)
    GetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_GetSpeedImage)
    SetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_SetSpeedImage)
    GetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_GetAdvectionImage)
    SetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_SetAdvectionImage)
    CalculateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_CalculateSpeedImage)
    CalculateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_CalculateAdvectionImage)
    AllocateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_AllocateSpeedImage)
    AllocateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_AllocateAdvectionImage)
    ReverseExpansionDirection = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_ReverseExpansionDirection)
    __swig_destroy__ = _itkSegmentationLevelSetFunctionPython.delete_itkSegmentationLevelSetFunctionID3ID3
    cast = _swig_new_static_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_cast)

# Register itkSegmentationLevelSetFunctionID3ID3 in _itkSegmentationLevelSetFunctionPython:
_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_swigregister(itkSegmentationLevelSetFunctionID3ID3)
itkSegmentationLevelSetFunctionID3ID3_cast = _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID3ID3_cast

class itkSegmentationLevelSetFunctionID4ID4(itk.itkLevelSetFunctionPython.itkLevelSetFunctionID4):
    r"""


    This object defines the API for a class of function objects which
    perform level set based segmentations. The
    SegmentationLevelSetImageFilter objects use these
    SegmentationLevelSetFunction objects to perform the numerical
    calculations which move a level set front to lock onto image features.

    In order to create a working function object, you must subclass the
    CalculateSpeedImage method to produce a "feature image" that is used
    by the parent LevelSetFunction class as the PropagationSpeed for its
    calculations.

    See:   SegmentationLevelSetImageFilter

    See:   LevelSetFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    GetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_GetFeatureImage)
    SetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_SetFeatureImage)
    GetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_GetSpeedImage)
    SetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_SetSpeedImage)
    GetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_GetAdvectionImage)
    SetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_SetAdvectionImage)
    CalculateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_CalculateSpeedImage)
    CalculateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_CalculateAdvectionImage)
    AllocateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_AllocateSpeedImage)
    AllocateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_AllocateAdvectionImage)
    ReverseExpansionDirection = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_ReverseExpansionDirection)
    __swig_destroy__ = _itkSegmentationLevelSetFunctionPython.delete_itkSegmentationLevelSetFunctionID4ID4
    cast = _swig_new_static_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_cast)

# Register itkSegmentationLevelSetFunctionID4ID4 in _itkSegmentationLevelSetFunctionPython:
_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_swigregister(itkSegmentationLevelSetFunctionID4ID4)
itkSegmentationLevelSetFunctionID4ID4_cast = _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionID4ID4_cast

class itkSegmentationLevelSetFunctionIF2IF2(itk.itkLevelSetFunctionPython.itkLevelSetFunctionIF2):
    r"""


    This object defines the API for a class of function objects which
    perform level set based segmentations. The
    SegmentationLevelSetImageFilter objects use these
    SegmentationLevelSetFunction objects to perform the numerical
    calculations which move a level set front to lock onto image features.

    In order to create a working function object, you must subclass the
    CalculateSpeedImage method to produce a "feature image" that is used
    by the parent LevelSetFunction class as the PropagationSpeed for its
    calculations.

    See:   SegmentationLevelSetImageFilter

    See:   LevelSetFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    GetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_GetFeatureImage)
    SetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_SetFeatureImage)
    GetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_GetSpeedImage)
    SetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_SetSpeedImage)
    GetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_GetAdvectionImage)
    SetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_SetAdvectionImage)
    CalculateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_CalculateSpeedImage)
    CalculateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_CalculateAdvectionImage)
    AllocateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_AllocateSpeedImage)
    AllocateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_AllocateAdvectionImage)
    ReverseExpansionDirection = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_ReverseExpansionDirection)
    __swig_destroy__ = _itkSegmentationLevelSetFunctionPython.delete_itkSegmentationLevelSetFunctionIF2IF2
    cast = _swig_new_static_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_cast)

# Register itkSegmentationLevelSetFunctionIF2IF2 in _itkSegmentationLevelSetFunctionPython:
_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_swigregister(itkSegmentationLevelSetFunctionIF2IF2)
itkSegmentationLevelSetFunctionIF2IF2_cast = _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF2IF2_cast

class itkSegmentationLevelSetFunctionIF3IF3(itk.itkLevelSetFunctionPython.itkLevelSetFunctionIF3):
    r"""


    This object defines the API for a class of function objects which
    perform level set based segmentations. The
    SegmentationLevelSetImageFilter objects use these
    SegmentationLevelSetFunction objects to perform the numerical
    calculations which move a level set front to lock onto image features.

    In order to create a working function object, you must subclass the
    CalculateSpeedImage method to produce a "feature image" that is used
    by the parent LevelSetFunction class as the PropagationSpeed for its
    calculations.

    See:   SegmentationLevelSetImageFilter

    See:   LevelSetFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    GetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_GetFeatureImage)
    SetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_SetFeatureImage)
    GetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_GetSpeedImage)
    SetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_SetSpeedImage)
    GetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_GetAdvectionImage)
    SetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_SetAdvectionImage)
    CalculateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_CalculateSpeedImage)
    CalculateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_CalculateAdvectionImage)
    AllocateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_AllocateSpeedImage)
    AllocateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_AllocateAdvectionImage)
    ReverseExpansionDirection = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_ReverseExpansionDirection)
    __swig_destroy__ = _itkSegmentationLevelSetFunctionPython.delete_itkSegmentationLevelSetFunctionIF3IF3
    cast = _swig_new_static_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_cast)

# Register itkSegmentationLevelSetFunctionIF3IF3 in _itkSegmentationLevelSetFunctionPython:
_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_swigregister(itkSegmentationLevelSetFunctionIF3IF3)
itkSegmentationLevelSetFunctionIF3IF3_cast = _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF3IF3_cast

class itkSegmentationLevelSetFunctionIF4IF4(itk.itkLevelSetFunctionPython.itkLevelSetFunctionIF4):
    r"""


    This object defines the API for a class of function objects which
    perform level set based segmentations. The
    SegmentationLevelSetImageFilter objects use these
    SegmentationLevelSetFunction objects to perform the numerical
    calculations which move a level set front to lock onto image features.

    In order to create a working function object, you must subclass the
    CalculateSpeedImage method to produce a "feature image" that is used
    by the parent LevelSetFunction class as the PropagationSpeed for its
    calculations.

    See:   SegmentationLevelSetImageFilter

    See:   LevelSetFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    GetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_GetFeatureImage)
    SetFeatureImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_SetFeatureImage)
    GetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_GetSpeedImage)
    SetSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_SetSpeedImage)
    GetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_GetAdvectionImage)
    SetAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_SetAdvectionImage)
    CalculateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_CalculateSpeedImage)
    CalculateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_CalculateAdvectionImage)
    AllocateSpeedImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_AllocateSpeedImage)
    AllocateAdvectionImage = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_AllocateAdvectionImage)
    ReverseExpansionDirection = _swig_new_instance_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_ReverseExpansionDirection)
    __swig_destroy__ = _itkSegmentationLevelSetFunctionPython.delete_itkSegmentationLevelSetFunctionIF4IF4
    cast = _swig_new_static_method(_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_cast)

# Register itkSegmentationLevelSetFunctionIF4IF4 in _itkSegmentationLevelSetFunctionPython:
_itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_swigregister(itkSegmentationLevelSetFunctionIF4IF4)
itkSegmentationLevelSetFunctionIF4IF4_cast = _itkSegmentationLevelSetFunctionPython.itkSegmentationLevelSetFunctionIF4IF4_cast



