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
    from . import _itkShapePriorSegmentationLevelSetImageFilterPython
else:
    import _itkShapePriorSegmentationLevelSetImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapePriorSegmentationLevelSetImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapePriorSegmentationLevelSetImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkOptimizerParametersPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkArrayPython
import itk.ITKFastMarchingBasePython
import itk.itkLevelSetNodePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkRGBAPixelPython
import itk.itkImageRegionPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkImageToImageFilterAPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkNodePairPython
import itk.itkFastMarchingStoppingCriterionBasePython
import itk.ITKOptimizersBasePython
import itk.ITKCostFunctionsPython
import itk.vnl_cost_functionPython
import itk.vnl_unary_functionPython
import itk.vnl_least_squares_functionPython
import itk.itkArray2DPython
import itk.itkCostFunctionPython
import itk.itkShapePriorMAPCostFunctionBasePython
import itk.itkShapeSignedDistanceFunctionPython
import itk.itkSpatialFunctionPython
import itk.itkFunctionBasePython
import itk.itkContinuousIndexPython
import itk.itkSegmentationLevelSetImageFilterPython
import itk.itkSegmentationLevelSetFunctionPython
import itk.itkLevelSetFunctionPython
import itk.itkFiniteDifferenceFunctionPython
import itk.itkSparseFieldLevelSetImageFilterPython
import itk.itkFiniteDifferenceImageFilterPython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterBPython
class itkShapePriorSegmentationLevelSetImageFilterID2ID2D(itk.itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterID2ID2D):
    r"""


    A base class which defines the API for implementing a level set
    segmentation filter with statistical shape influence.

    OVERVIEW This class extends the functionality of
    SegmentationLevelSetImageFilter with an additional statistical shape
    influence term in the level set evolution as developed in [1].
    TEMPLATE PARAMETERS There are two required and one optional template
    parameter for these filters.  TInputImage is the image type of the
    initial model you will input to the filter using SetInput() or
    SetInitialImage().

    TFeatureImage is the image type of the image from which the filter
    will calculate the speed term for segmentation (see INPUTS).

    TOutputPixelType is the data type used for the output image phi, the
    implicit level set image. This should really only ever be set as float
    (default) or double.

    PARAMETERS

    From a level set evolution point of view, the shape is represented by
    a signed distance function from the shape encapsulated in a
    ShapeSignedDistanceFunction object.

    See:  ShapeSignedDistanceFunction

    See:  ShapePriorSegmentationLevelSetFunction REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetShapeFunction)
    SetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetCostFunction)
    GetModifiableCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetModifiableCostFunction)
    GetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetCostFunction)
    SetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetOptimizer)
    GetModifiableOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetModifiableOptimizer)
    GetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetOptimizer)
    SetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetInitialParameters)
    GetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetInitialParameters)
    SetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetShapePriorScaling)
    GetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetShapePriorScaling)
    SetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_SetShapePriorSegmentationFunction)
    GetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetShapePriorSegmentationFunction)
    GetCurrentParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_GetCurrentParameters)
    __swig_destroy__ = _itkShapePriorSegmentationLevelSetImageFilterPython.delete_itkShapePriorSegmentationLevelSetImageFilterID2ID2D
    cast = _swig_new_static_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_cast)

# Register itkShapePriorSegmentationLevelSetImageFilterID2ID2D in _itkShapePriorSegmentationLevelSetImageFilterPython:
_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_swigregister(itkShapePriorSegmentationLevelSetImageFilterID2ID2D)
itkShapePriorSegmentationLevelSetImageFilterID2ID2D_cast = _itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID2ID2D_cast

class itkShapePriorSegmentationLevelSetImageFilterID3ID3D(itk.itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterID3ID3D):
    r"""


    A base class which defines the API for implementing a level set
    segmentation filter with statistical shape influence.

    OVERVIEW This class extends the functionality of
    SegmentationLevelSetImageFilter with an additional statistical shape
    influence term in the level set evolution as developed in [1].
    TEMPLATE PARAMETERS There are two required and one optional template
    parameter for these filters.  TInputImage is the image type of the
    initial model you will input to the filter using SetInput() or
    SetInitialImage().

    TFeatureImage is the image type of the image from which the filter
    will calculate the speed term for segmentation (see INPUTS).

    TOutputPixelType is the data type used for the output image phi, the
    implicit level set image. This should really only ever be set as float
    (default) or double.

    PARAMETERS

    From a level set evolution point of view, the shape is represented by
    a signed distance function from the shape encapsulated in a
    ShapeSignedDistanceFunction object.

    See:  ShapeSignedDistanceFunction

    See:  ShapePriorSegmentationLevelSetFunction REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetShapeFunction)
    SetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetCostFunction)
    GetModifiableCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetModifiableCostFunction)
    GetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetCostFunction)
    SetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetOptimizer)
    GetModifiableOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetModifiableOptimizer)
    GetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetOptimizer)
    SetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetInitialParameters)
    GetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetInitialParameters)
    SetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetShapePriorScaling)
    GetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetShapePriorScaling)
    SetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_SetShapePriorSegmentationFunction)
    GetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetShapePriorSegmentationFunction)
    GetCurrentParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_GetCurrentParameters)
    __swig_destroy__ = _itkShapePriorSegmentationLevelSetImageFilterPython.delete_itkShapePriorSegmentationLevelSetImageFilterID3ID3D
    cast = _swig_new_static_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_cast)

# Register itkShapePriorSegmentationLevelSetImageFilterID3ID3D in _itkShapePriorSegmentationLevelSetImageFilterPython:
_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_swigregister(itkShapePriorSegmentationLevelSetImageFilterID3ID3D)
itkShapePriorSegmentationLevelSetImageFilterID3ID3D_cast = _itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID3ID3D_cast

class itkShapePriorSegmentationLevelSetImageFilterID4ID4D(itk.itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterID4ID4D):
    r"""


    A base class which defines the API for implementing a level set
    segmentation filter with statistical shape influence.

    OVERVIEW This class extends the functionality of
    SegmentationLevelSetImageFilter with an additional statistical shape
    influence term in the level set evolution as developed in [1].
    TEMPLATE PARAMETERS There are two required and one optional template
    parameter for these filters.  TInputImage is the image type of the
    initial model you will input to the filter using SetInput() or
    SetInitialImage().

    TFeatureImage is the image type of the image from which the filter
    will calculate the speed term for segmentation (see INPUTS).

    TOutputPixelType is the data type used for the output image phi, the
    implicit level set image. This should really only ever be set as float
    (default) or double.

    PARAMETERS

    From a level set evolution point of view, the shape is represented by
    a signed distance function from the shape encapsulated in a
    ShapeSignedDistanceFunction object.

    See:  ShapeSignedDistanceFunction

    See:  ShapePriorSegmentationLevelSetFunction REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_GetShapeFunction)
    SetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_SetCostFunction)
    GetModifiableCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_GetModifiableCostFunction)
    GetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_GetCostFunction)
    SetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_SetOptimizer)
    GetModifiableOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_GetModifiableOptimizer)
    GetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_GetOptimizer)
    SetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_SetInitialParameters)
    GetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_GetInitialParameters)
    SetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_SetShapePriorScaling)
    GetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_GetShapePriorScaling)
    SetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_SetShapePriorSegmentationFunction)
    GetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_GetShapePriorSegmentationFunction)
    GetCurrentParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_GetCurrentParameters)
    __swig_destroy__ = _itkShapePriorSegmentationLevelSetImageFilterPython.delete_itkShapePriorSegmentationLevelSetImageFilterID4ID4D
    cast = _swig_new_static_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_cast)

# Register itkShapePriorSegmentationLevelSetImageFilterID4ID4D in _itkShapePriorSegmentationLevelSetImageFilterPython:
_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_swigregister(itkShapePriorSegmentationLevelSetImageFilterID4ID4D)
itkShapePriorSegmentationLevelSetImageFilterID4ID4D_cast = _itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterID4ID4D_cast

class itkShapePriorSegmentationLevelSetImageFilterIF2IF2F(itk.itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF2IF2F):
    r"""


    A base class which defines the API for implementing a level set
    segmentation filter with statistical shape influence.

    OVERVIEW This class extends the functionality of
    SegmentationLevelSetImageFilter with an additional statistical shape
    influence term in the level set evolution as developed in [1].
    TEMPLATE PARAMETERS There are two required and one optional template
    parameter for these filters.  TInputImage is the image type of the
    initial model you will input to the filter using SetInput() or
    SetInitialImage().

    TFeatureImage is the image type of the image from which the filter
    will calculate the speed term for segmentation (see INPUTS).

    TOutputPixelType is the data type used for the output image phi, the
    implicit level set image. This should really only ever be set as float
    (default) or double.

    PARAMETERS

    From a level set evolution point of view, the shape is represented by
    a signed distance function from the shape encapsulated in a
    ShapeSignedDistanceFunction object.

    See:  ShapeSignedDistanceFunction

    See:  ShapePriorSegmentationLevelSetFunction REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetShapeFunction)
    SetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetCostFunction)
    GetModifiableCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetModifiableCostFunction)
    GetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetCostFunction)
    SetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetOptimizer)
    GetModifiableOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetModifiableOptimizer)
    GetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetOptimizer)
    SetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetInitialParameters)
    GetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetInitialParameters)
    SetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetShapePriorScaling)
    GetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetShapePriorScaling)
    SetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_SetShapePriorSegmentationFunction)
    GetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetShapePriorSegmentationFunction)
    GetCurrentParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_GetCurrentParameters)
    __swig_destroy__ = _itkShapePriorSegmentationLevelSetImageFilterPython.delete_itkShapePriorSegmentationLevelSetImageFilterIF2IF2F
    cast = _swig_new_static_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_cast)

# Register itkShapePriorSegmentationLevelSetImageFilterIF2IF2F in _itkShapePriorSegmentationLevelSetImageFilterPython:
_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_swigregister(itkShapePriorSegmentationLevelSetImageFilterIF2IF2F)
itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_cast = _itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_cast

class itkShapePriorSegmentationLevelSetImageFilterIF3IF3F(itk.itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF3IF3F):
    r"""


    A base class which defines the API for implementing a level set
    segmentation filter with statistical shape influence.

    OVERVIEW This class extends the functionality of
    SegmentationLevelSetImageFilter with an additional statistical shape
    influence term in the level set evolution as developed in [1].
    TEMPLATE PARAMETERS There are two required and one optional template
    parameter for these filters.  TInputImage is the image type of the
    initial model you will input to the filter using SetInput() or
    SetInitialImage().

    TFeatureImage is the image type of the image from which the filter
    will calculate the speed term for segmentation (see INPUTS).

    TOutputPixelType is the data type used for the output image phi, the
    implicit level set image. This should really only ever be set as float
    (default) or double.

    PARAMETERS

    From a level set evolution point of view, the shape is represented by
    a signed distance function from the shape encapsulated in a
    ShapeSignedDistanceFunction object.

    See:  ShapeSignedDistanceFunction

    See:  ShapePriorSegmentationLevelSetFunction REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetShapeFunction)
    SetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetCostFunction)
    GetModifiableCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetModifiableCostFunction)
    GetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetCostFunction)
    SetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetOptimizer)
    GetModifiableOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetModifiableOptimizer)
    GetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetOptimizer)
    SetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetInitialParameters)
    GetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetInitialParameters)
    SetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetShapePriorScaling)
    GetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetShapePriorScaling)
    SetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_SetShapePriorSegmentationFunction)
    GetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetShapePriorSegmentationFunction)
    GetCurrentParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_GetCurrentParameters)
    __swig_destroy__ = _itkShapePriorSegmentationLevelSetImageFilterPython.delete_itkShapePriorSegmentationLevelSetImageFilterIF3IF3F
    cast = _swig_new_static_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_cast)

# Register itkShapePriorSegmentationLevelSetImageFilterIF3IF3F in _itkShapePriorSegmentationLevelSetImageFilterPython:
_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_swigregister(itkShapePriorSegmentationLevelSetImageFilterIF3IF3F)
itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_cast = _itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_cast

class itkShapePriorSegmentationLevelSetImageFilterIF4IF4F(itk.itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF4IF4F):
    r"""


    A base class which defines the API for implementing a level set
    segmentation filter with statistical shape influence.

    OVERVIEW This class extends the functionality of
    SegmentationLevelSetImageFilter with an additional statistical shape
    influence term in the level set evolution as developed in [1].
    TEMPLATE PARAMETERS There are two required and one optional template
    parameter for these filters.  TInputImage is the image type of the
    initial model you will input to the filter using SetInput() or
    SetInitialImage().

    TFeatureImage is the image type of the image from which the filter
    will calculate the speed term for segmentation (see INPUTS).

    TOutputPixelType is the data type used for the output image phi, the
    implicit level set image. This should really only ever be set as float
    (default) or double.

    PARAMETERS

    From a level set evolution point of view, the shape is represented by
    a signed distance function from the shape encapsulated in a
    ShapeSignedDistanceFunction object.

    See:  ShapeSignedDistanceFunction

    See:  ShapePriorSegmentationLevelSetFunction REFERENCES

    [1] Leventon, M.E. et al. "Statistical Shape Influence in Geodesic
    Active Contours", CVPR 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_SetShapeFunction)
    GetModifiableShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_GetModifiableShapeFunction)
    GetShapeFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_GetShapeFunction)
    SetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_SetCostFunction)
    GetModifiableCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_GetModifiableCostFunction)
    GetCostFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_GetCostFunction)
    SetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_SetOptimizer)
    GetModifiableOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_GetModifiableOptimizer)
    GetOptimizer = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_GetOptimizer)
    SetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_SetInitialParameters)
    GetInitialParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_GetInitialParameters)
    SetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_SetShapePriorScaling)
    GetShapePriorScaling = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_GetShapePriorScaling)
    SetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_SetShapePriorSegmentationFunction)
    GetShapePriorSegmentationFunction = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_GetShapePriorSegmentationFunction)
    GetCurrentParameters = _swig_new_instance_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_GetCurrentParameters)
    __swig_destroy__ = _itkShapePriorSegmentationLevelSetImageFilterPython.delete_itkShapePriorSegmentationLevelSetImageFilterIF4IF4F
    cast = _swig_new_static_method(_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_cast)

# Register itkShapePriorSegmentationLevelSetImageFilterIF4IF4F in _itkShapePriorSegmentationLevelSetImageFilterPython:
_itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_swigregister(itkShapePriorSegmentationLevelSetImageFilterIF4IF4F)
itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_cast = _itkShapePriorSegmentationLevelSetImageFilterPython.itkShapePriorSegmentationLevelSetImageFilterIF4IF4F_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def shape_prior_segmentation_level_set_image_filter(*args: itkt.ImageLike,  shape_function=..., cost_function=..., optimizer=..., initial_parameters=..., shape_prior_scaling: float=..., shape_prior_segmentation_function=..., maximum_iterations: int=..., feature_image: itkt.Image=..., initial_image: itkt.Image=..., speed_image: itkt.Image=..., advection_image: itkt.Image=..., use_negative_features: bool=..., reverse_expansion_direction: bool=..., auto_generate_speed_advection: bool=..., feature_scaling: float=..., propagation_scaling: float=..., advection_scaling: float=..., curvature_scaling: float=..., use_minimal_curvature: bool=..., segmentation_function=..., maximum_curvature_time_step: float=..., maximum_propagation_time_step: float=..., number_of_layers: int=..., iso_surface_value: float=..., interpolate_surface_location: bool=..., difference_function=..., number_of_iterations: int=..., use_image_spacing: bool=..., maximum_rms_error: float=..., rms_change: float=..., manual_reinitialization: bool=..., is_initialized: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for ShapePriorSegmentationLevelSetImageFilter"""
    import itk

    kwarg_typehints = { 'shape_function':shape_function,'cost_function':cost_function,'optimizer':optimizer,'initial_parameters':initial_parameters,'shape_prior_scaling':shape_prior_scaling,'shape_prior_segmentation_function':shape_prior_segmentation_function,'maximum_iterations':maximum_iterations,'feature_image':feature_image,'initial_image':initial_image,'speed_image':speed_image,'advection_image':advection_image,'use_negative_features':use_negative_features,'reverse_expansion_direction':reverse_expansion_direction,'auto_generate_speed_advection':auto_generate_speed_advection,'feature_scaling':feature_scaling,'propagation_scaling':propagation_scaling,'advection_scaling':advection_scaling,'curvature_scaling':curvature_scaling,'use_minimal_curvature':use_minimal_curvature,'segmentation_function':segmentation_function,'maximum_curvature_time_step':maximum_curvature_time_step,'maximum_propagation_time_step':maximum_propagation_time_step,'number_of_layers':number_of_layers,'iso_surface_value':iso_surface_value,'interpolate_surface_location':interpolate_surface_location,'difference_function':difference_function,'number_of_iterations':number_of_iterations,'use_image_spacing':use_image_spacing,'maximum_rms_error':maximum_rms_error,'rms_change':rms_change,'manual_reinitialization':manual_reinitialization,'is_initialized':is_initialized }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ShapePriorSegmentationLevelSetImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def shape_prior_segmentation_level_set_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLevelSets.ShapePriorSegmentationLevelSetImageFilter
    shape_prior_segmentation_level_set_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    shape_prior_segmentation_level_set_image_filter.__doc__ = filter_object.__doc__




