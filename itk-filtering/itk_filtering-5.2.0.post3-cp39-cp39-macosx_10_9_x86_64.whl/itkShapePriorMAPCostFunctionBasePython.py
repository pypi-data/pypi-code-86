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
    from . import _itkShapePriorMAPCostFunctionBasePython
else:
    import _itkShapePriorMAPCostFunctionBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapePriorMAPCostFunctionBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapePriorMAPCostFunctionBasePython.SWIG_PyStaticMethod_New

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
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkImagePython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkShapeSignedDistanceFunctionPython
import itk.itkSpatialFunctionPython
import itk.itkFunctionBasePython
import itk.itkContinuousIndexPython
import itk.ITKCostFunctionsPython
import itk.vnl_least_squares_functionPython
import itk.itkCostFunctionPython
import itk.itkArray2DPython
import itk.vnl_cost_functionPython
import itk.vnl_unary_functionPython
import itk.ITKFastMarchingBasePython
import itk.itkNodePairPython
import itk.itkImageToImageFilterAPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkFastMarchingStoppingCriterionBasePython
import itk.itkLevelSetNodePython
class itkShapePriorMAPCostFunctionBaseID2D(itk.ITKCostFunctionsPython.itkSingleValuedCostFunction):
    r"""


    Represents the base class of maximum aprior (MAP) cost function used
    ShapePriorSegmentationLevelSetImageFilter to estimate the shape
    parameters.

    This class follows the shape and pose parameters estimation developed
    in [1].

    This class has two template parameters, the feature image type
    representing the edge potential map and the pixel type used to
    represent the output level set in the
    ShapePriorSegmentationLevelSetImageFilter.

    See:   ShapePriorSegmentationLevelSetImageFilter REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_GetShapeFunction)
    SetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_SetActiveRegion)
    GetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_GetActiveRegion)
    SetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_GetFeatureImage)
    ComputeLogInsideTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_ComputeLogInsideTerm)
    ComputeLogGradientTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_ComputeLogGradientTerm)
    ComputeLogShapePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_ComputeLogShapePriorTerm)
    ComputeLogPosePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_ComputeLogPosePriorTerm)
    Initialize = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_Initialize)
    __swig_destroy__ = _itkShapePriorMAPCostFunctionBasePython.delete_itkShapePriorMAPCostFunctionBaseID2D
    cast = _swig_new_static_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_cast)

# Register itkShapePriorMAPCostFunctionBaseID2D in _itkShapePriorMAPCostFunctionBasePython:
_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_swigregister(itkShapePriorMAPCostFunctionBaseID2D)
itkShapePriorMAPCostFunctionBaseID2D_cast = _itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID2D_cast

class itkShapePriorMAPCostFunctionBaseID3D(itk.ITKCostFunctionsPython.itkSingleValuedCostFunction):
    r"""


    Represents the base class of maximum aprior (MAP) cost function used
    ShapePriorSegmentationLevelSetImageFilter to estimate the shape
    parameters.

    This class follows the shape and pose parameters estimation developed
    in [1].

    This class has two template parameters, the feature image type
    representing the edge potential map and the pixel type used to
    represent the output level set in the
    ShapePriorSegmentationLevelSetImageFilter.

    See:   ShapePriorSegmentationLevelSetImageFilter REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_GetShapeFunction)
    SetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_SetActiveRegion)
    GetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_GetActiveRegion)
    SetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_GetFeatureImage)
    ComputeLogInsideTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_ComputeLogInsideTerm)
    ComputeLogGradientTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_ComputeLogGradientTerm)
    ComputeLogShapePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_ComputeLogShapePriorTerm)
    ComputeLogPosePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_ComputeLogPosePriorTerm)
    Initialize = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_Initialize)
    __swig_destroy__ = _itkShapePriorMAPCostFunctionBasePython.delete_itkShapePriorMAPCostFunctionBaseID3D
    cast = _swig_new_static_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_cast)

# Register itkShapePriorMAPCostFunctionBaseID3D in _itkShapePriorMAPCostFunctionBasePython:
_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_swigregister(itkShapePriorMAPCostFunctionBaseID3D)
itkShapePriorMAPCostFunctionBaseID3D_cast = _itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID3D_cast

class itkShapePriorMAPCostFunctionBaseID4D(itk.ITKCostFunctionsPython.itkSingleValuedCostFunction):
    r"""


    Represents the base class of maximum aprior (MAP) cost function used
    ShapePriorSegmentationLevelSetImageFilter to estimate the shape
    parameters.

    This class follows the shape and pose parameters estimation developed
    in [1].

    This class has two template parameters, the feature image type
    representing the edge potential map and the pixel type used to
    represent the output level set in the
    ShapePriorSegmentationLevelSetImageFilter.

    See:   ShapePriorSegmentationLevelSetImageFilter REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_GetShapeFunction)
    SetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_SetActiveRegion)
    GetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_GetActiveRegion)
    SetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_GetFeatureImage)
    ComputeLogInsideTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_ComputeLogInsideTerm)
    ComputeLogGradientTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_ComputeLogGradientTerm)
    ComputeLogShapePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_ComputeLogShapePriorTerm)
    ComputeLogPosePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_ComputeLogPosePriorTerm)
    Initialize = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_Initialize)
    __swig_destroy__ = _itkShapePriorMAPCostFunctionBasePython.delete_itkShapePriorMAPCostFunctionBaseID4D
    cast = _swig_new_static_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_cast)

# Register itkShapePriorMAPCostFunctionBaseID4D in _itkShapePriorMAPCostFunctionBasePython:
_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_swigregister(itkShapePriorMAPCostFunctionBaseID4D)
itkShapePriorMAPCostFunctionBaseID4D_cast = _itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseID4D_cast

class itkShapePriorMAPCostFunctionBaseIF2F(itk.ITKCostFunctionsPython.itkSingleValuedCostFunction):
    r"""


    Represents the base class of maximum aprior (MAP) cost function used
    ShapePriorSegmentationLevelSetImageFilter to estimate the shape
    parameters.

    This class follows the shape and pose parameters estimation developed
    in [1].

    This class has two template parameters, the feature image type
    representing the edge potential map and the pixel type used to
    represent the output level set in the
    ShapePriorSegmentationLevelSetImageFilter.

    See:   ShapePriorSegmentationLevelSetImageFilter REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_GetShapeFunction)
    SetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_SetActiveRegion)
    GetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_GetActiveRegion)
    SetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_GetFeatureImage)
    ComputeLogInsideTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_ComputeLogInsideTerm)
    ComputeLogGradientTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_ComputeLogGradientTerm)
    ComputeLogShapePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_ComputeLogShapePriorTerm)
    ComputeLogPosePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_ComputeLogPosePriorTerm)
    Initialize = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_Initialize)
    __swig_destroy__ = _itkShapePriorMAPCostFunctionBasePython.delete_itkShapePriorMAPCostFunctionBaseIF2F
    cast = _swig_new_static_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_cast)

# Register itkShapePriorMAPCostFunctionBaseIF2F in _itkShapePriorMAPCostFunctionBasePython:
_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_swigregister(itkShapePriorMAPCostFunctionBaseIF2F)
itkShapePriorMAPCostFunctionBaseIF2F_cast = _itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF2F_cast

class itkShapePriorMAPCostFunctionBaseIF3F(itk.ITKCostFunctionsPython.itkSingleValuedCostFunction):
    r"""


    Represents the base class of maximum aprior (MAP) cost function used
    ShapePriorSegmentationLevelSetImageFilter to estimate the shape
    parameters.

    This class follows the shape and pose parameters estimation developed
    in [1].

    This class has two template parameters, the feature image type
    representing the edge potential map and the pixel type used to
    represent the output level set in the
    ShapePriorSegmentationLevelSetImageFilter.

    See:   ShapePriorSegmentationLevelSetImageFilter REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_GetShapeFunction)
    SetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_SetActiveRegion)
    GetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_GetActiveRegion)
    SetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_GetFeatureImage)
    ComputeLogInsideTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_ComputeLogInsideTerm)
    ComputeLogGradientTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_ComputeLogGradientTerm)
    ComputeLogShapePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_ComputeLogShapePriorTerm)
    ComputeLogPosePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_ComputeLogPosePriorTerm)
    Initialize = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_Initialize)
    __swig_destroy__ = _itkShapePriorMAPCostFunctionBasePython.delete_itkShapePriorMAPCostFunctionBaseIF3F
    cast = _swig_new_static_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_cast)

# Register itkShapePriorMAPCostFunctionBaseIF3F in _itkShapePriorMAPCostFunctionBasePython:
_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_swigregister(itkShapePriorMAPCostFunctionBaseIF3F)
itkShapePriorMAPCostFunctionBaseIF3F_cast = _itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF3F_cast

class itkShapePriorMAPCostFunctionBaseIF4F(itk.ITKCostFunctionsPython.itkSingleValuedCostFunction):
    r"""


    Represents the base class of maximum aprior (MAP) cost function used
    ShapePriorSegmentationLevelSetImageFilter to estimate the shape
    parameters.

    This class follows the shape and pose parameters estimation developed
    in [1].

    This class has two template parameters, the feature image type
    representing the edge potential map and the pixel type used to
    represent the output level set in the
    ShapePriorSegmentationLevelSetImageFilter.

    See:   ShapePriorSegmentationLevelSetImageFilter REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_GetShapeFunction)
    SetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_SetActiveRegion)
    GetActiveRegion = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_GetActiveRegion)
    SetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_GetFeatureImage)
    ComputeLogInsideTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_ComputeLogInsideTerm)
    ComputeLogGradientTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_ComputeLogGradientTerm)
    ComputeLogShapePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_ComputeLogShapePriorTerm)
    ComputeLogPosePriorTerm = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_ComputeLogPosePriorTerm)
    Initialize = _swig_new_instance_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_Initialize)
    __swig_destroy__ = _itkShapePriorMAPCostFunctionBasePython.delete_itkShapePriorMAPCostFunctionBaseIF4F
    cast = _swig_new_static_method(_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_cast)

# Register itkShapePriorMAPCostFunctionBaseIF4F in _itkShapePriorMAPCostFunctionBasePython:
_itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_swigregister(itkShapePriorMAPCostFunctionBaseIF4F)
itkShapePriorMAPCostFunctionBaseIF4F_cast = _itkShapePriorMAPCostFunctionBasePython.itkShapePriorMAPCostFunctionBaseIF4F_cast



