# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKStatisticsPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkKdTreeBasedKmeansEstimatorPython
else:
    import _itkKdTreeBasedKmeansEstimatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkKdTreeBasedKmeansEstimatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkKdTreeBasedKmeansEstimatorPython.SWIG_PyStaticMethod_New

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
import itk.itkKdTreePython
import itk.itkListSamplePython
import itk.itkSamplePython
import itk.itkFixedArrayPython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkEuclideanDistanceMetricPython
import itk.itkDistanceMetricPython
import itk.itkFunctionBasePython
import itk.itkContinuousIndexPython
import itk.itkPointPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkImagePython
import itk.itkImageRegionPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython

def itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_New():
    return itkKdTreeBasedKmeansEstimatorKdTreeLSVF2.New()

class itkKdTreeBasedKmeansEstimatorKdTreeLSVF2(itk.ITKCommonBasePython.itkObject):
    r"""


    fast k-means algorithm implementation using k-d tree structure

    It returns k mean vectors that are centroids of k-clusters using pre-
    generated k-d tree. k-d tree generation is done by the
    WeightedCentroidKdTreeGenerator. The tree construction needs to be
    done only once. The resulting k-d tree's non-terminal nodes that have
    their children nodes have vector sums of measurement vectors that
    belong to the nodes and the number of measurement vectors in addition
    to the typical node boundary information and pointers to children
    nodes. Instead of reassigning every measurement vector to the nearest
    cluster centroid and recalculating centroid, it maintain a set of
    cluster centroid candidates and using pruning algorithm that utilizes
    k-d tree, it updates the means of only relevant candidates at each
    iterations. It would be faster than traditional implementation of
    k-means algorithm. However, the k-d tree consumes a large amount of
    memory. The tree construction time and pruning algorithm's performance
    are important factors to the whole process's performance. If users
    want to use k-d tree for some purpose other than k-means estimation,
    they can use the KdTreeGenerator instead of the
    WeightedCentroidKdTreeGenerator. It will save the tree construction
    time and memory usage.

    Note: There is a second implementation of k-means algorithm in ITK
    under the While the Kd tree based implementation is more time
    efficient, the GLA/LBG based algorithm is more memory efficient.

    Recent API changes: The static const macro to get the length of a
    measurement vector, MeasurementVectorSize has been removed to allow
    the length of a measurement vector to be specified at run time. It is
    now obtained from the KdTree set as input. You may query this length
    using the function GetMeasurementVectorSize().

    See:  ImageKmeansModelEstimator

    See:   WeightedCentroidKdTreeGenerator, KdTree 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2___New_orig__)
    Clone = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_Clone)
    GetOutput = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_GetOutput)
    SetParameters = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_SetParameters)
    GetParameters = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_GetParameters)
    SetMaximumIteration = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_SetMaximumIteration)
    GetMaximumIteration = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_GetMaximumIteration)
    SetCentroidPositionChangesThreshold = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_SetCentroidPositionChangesThreshold)
    GetCentroidPositionChangesThreshold = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_GetCentroidPositionChangesThreshold)
    SetKdTree = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_SetKdTree)
    GetKdTree = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_GetKdTree)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_GetMeasurementVectorSize)
    GetCurrentIteration = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_GetCurrentIteration)
    GetCentroidPositionChanges = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_GetCentroidPositionChanges)
    StartOptimization = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_StartOptimization)
    SetUseClusterLabels = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_SetUseClusterLabels)
    GetUseClusterLabels = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_GetUseClusterLabels)
    __swig_destroy__ = _itkKdTreeBasedKmeansEstimatorPython.delete_itkKdTreeBasedKmeansEstimatorKdTreeLSVF2
    cast = _swig_new_static_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeBasedKmeansEstimatorKdTreeLSVF2

        Create a new object of the class itkKdTreeBasedKmeansEstimatorKdTreeLSVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeBasedKmeansEstimatorKdTreeLSVF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKdTreeBasedKmeansEstimatorKdTreeLSVF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKdTreeBasedKmeansEstimatorKdTreeLSVF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKdTreeBasedKmeansEstimatorKdTreeLSVF2 in _itkKdTreeBasedKmeansEstimatorPython:
_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_swigregister(itkKdTreeBasedKmeansEstimatorKdTreeLSVF2)
itkKdTreeBasedKmeansEstimatorKdTreeLSVF2___New_orig__ = _itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2___New_orig__
itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_cast = _itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF2_cast


def itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_New():
    return itkKdTreeBasedKmeansEstimatorKdTreeLSVF3.New()

class itkKdTreeBasedKmeansEstimatorKdTreeLSVF3(itk.ITKCommonBasePython.itkObject):
    r"""


    fast k-means algorithm implementation using k-d tree structure

    It returns k mean vectors that are centroids of k-clusters using pre-
    generated k-d tree. k-d tree generation is done by the
    WeightedCentroidKdTreeGenerator. The tree construction needs to be
    done only once. The resulting k-d tree's non-terminal nodes that have
    their children nodes have vector sums of measurement vectors that
    belong to the nodes and the number of measurement vectors in addition
    to the typical node boundary information and pointers to children
    nodes. Instead of reassigning every measurement vector to the nearest
    cluster centroid and recalculating centroid, it maintain a set of
    cluster centroid candidates and using pruning algorithm that utilizes
    k-d tree, it updates the means of only relevant candidates at each
    iterations. It would be faster than traditional implementation of
    k-means algorithm. However, the k-d tree consumes a large amount of
    memory. The tree construction time and pruning algorithm's performance
    are important factors to the whole process's performance. If users
    want to use k-d tree for some purpose other than k-means estimation,
    they can use the KdTreeGenerator instead of the
    WeightedCentroidKdTreeGenerator. It will save the tree construction
    time and memory usage.

    Note: There is a second implementation of k-means algorithm in ITK
    under the While the Kd tree based implementation is more time
    efficient, the GLA/LBG based algorithm is more memory efficient.

    Recent API changes: The static const macro to get the length of a
    measurement vector, MeasurementVectorSize has been removed to allow
    the length of a measurement vector to be specified at run time. It is
    now obtained from the KdTree set as input. You may query this length
    using the function GetMeasurementVectorSize().

    See:  ImageKmeansModelEstimator

    See:   WeightedCentroidKdTreeGenerator, KdTree 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3___New_orig__)
    Clone = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_Clone)
    GetOutput = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_GetOutput)
    SetParameters = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_SetParameters)
    GetParameters = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_GetParameters)
    SetMaximumIteration = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_SetMaximumIteration)
    GetMaximumIteration = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_GetMaximumIteration)
    SetCentroidPositionChangesThreshold = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_SetCentroidPositionChangesThreshold)
    GetCentroidPositionChangesThreshold = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_GetCentroidPositionChangesThreshold)
    SetKdTree = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_SetKdTree)
    GetKdTree = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_GetKdTree)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_GetMeasurementVectorSize)
    GetCurrentIteration = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_GetCurrentIteration)
    GetCentroidPositionChanges = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_GetCentroidPositionChanges)
    StartOptimization = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_StartOptimization)
    SetUseClusterLabels = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_SetUseClusterLabels)
    GetUseClusterLabels = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_GetUseClusterLabels)
    __swig_destroy__ = _itkKdTreeBasedKmeansEstimatorPython.delete_itkKdTreeBasedKmeansEstimatorKdTreeLSVF3
    cast = _swig_new_static_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeBasedKmeansEstimatorKdTreeLSVF3

        Create a new object of the class itkKdTreeBasedKmeansEstimatorKdTreeLSVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeBasedKmeansEstimatorKdTreeLSVF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKdTreeBasedKmeansEstimatorKdTreeLSVF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKdTreeBasedKmeansEstimatorKdTreeLSVF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKdTreeBasedKmeansEstimatorKdTreeLSVF3 in _itkKdTreeBasedKmeansEstimatorPython:
_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_swigregister(itkKdTreeBasedKmeansEstimatorKdTreeLSVF3)
itkKdTreeBasedKmeansEstimatorKdTreeLSVF3___New_orig__ = _itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3___New_orig__
itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_cast = _itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF3_cast


def itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_New():
    return itkKdTreeBasedKmeansEstimatorKdTreeLSVF4.New()

class itkKdTreeBasedKmeansEstimatorKdTreeLSVF4(itk.ITKCommonBasePython.itkObject):
    r"""


    fast k-means algorithm implementation using k-d tree structure

    It returns k mean vectors that are centroids of k-clusters using pre-
    generated k-d tree. k-d tree generation is done by the
    WeightedCentroidKdTreeGenerator. The tree construction needs to be
    done only once. The resulting k-d tree's non-terminal nodes that have
    their children nodes have vector sums of measurement vectors that
    belong to the nodes and the number of measurement vectors in addition
    to the typical node boundary information and pointers to children
    nodes. Instead of reassigning every measurement vector to the nearest
    cluster centroid and recalculating centroid, it maintain a set of
    cluster centroid candidates and using pruning algorithm that utilizes
    k-d tree, it updates the means of only relevant candidates at each
    iterations. It would be faster than traditional implementation of
    k-means algorithm. However, the k-d tree consumes a large amount of
    memory. The tree construction time and pruning algorithm's performance
    are important factors to the whole process's performance. If users
    want to use k-d tree for some purpose other than k-means estimation,
    they can use the KdTreeGenerator instead of the
    WeightedCentroidKdTreeGenerator. It will save the tree construction
    time and memory usage.

    Note: There is a second implementation of k-means algorithm in ITK
    under the While the Kd tree based implementation is more time
    efficient, the GLA/LBG based algorithm is more memory efficient.

    Recent API changes: The static const macro to get the length of a
    measurement vector, MeasurementVectorSize has been removed to allow
    the length of a measurement vector to be specified at run time. It is
    now obtained from the KdTree set as input. You may query this length
    using the function GetMeasurementVectorSize().

    See:  ImageKmeansModelEstimator

    See:   WeightedCentroidKdTreeGenerator, KdTree 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4___New_orig__)
    Clone = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_Clone)
    GetOutput = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_GetOutput)
    SetParameters = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_SetParameters)
    GetParameters = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_GetParameters)
    SetMaximumIteration = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_SetMaximumIteration)
    GetMaximumIteration = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_GetMaximumIteration)
    SetCentroidPositionChangesThreshold = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_SetCentroidPositionChangesThreshold)
    GetCentroidPositionChangesThreshold = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_GetCentroidPositionChangesThreshold)
    SetKdTree = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_SetKdTree)
    GetKdTree = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_GetKdTree)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_GetMeasurementVectorSize)
    GetCurrentIteration = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_GetCurrentIteration)
    GetCentroidPositionChanges = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_GetCentroidPositionChanges)
    StartOptimization = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_StartOptimization)
    SetUseClusterLabels = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_SetUseClusterLabels)
    GetUseClusterLabels = _swig_new_instance_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_GetUseClusterLabels)
    __swig_destroy__ = _itkKdTreeBasedKmeansEstimatorPython.delete_itkKdTreeBasedKmeansEstimatorKdTreeLSVF4
    cast = _swig_new_static_method(_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeBasedKmeansEstimatorKdTreeLSVF4

        Create a new object of the class itkKdTreeBasedKmeansEstimatorKdTreeLSVF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeBasedKmeansEstimatorKdTreeLSVF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKdTreeBasedKmeansEstimatorKdTreeLSVF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKdTreeBasedKmeansEstimatorKdTreeLSVF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKdTreeBasedKmeansEstimatorKdTreeLSVF4 in _itkKdTreeBasedKmeansEstimatorPython:
_itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_swigregister(itkKdTreeBasedKmeansEstimatorKdTreeLSVF4)
itkKdTreeBasedKmeansEstimatorKdTreeLSVF4___New_orig__ = _itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4___New_orig__
itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_cast = _itkKdTreeBasedKmeansEstimatorPython.itkKdTreeBasedKmeansEstimatorKdTreeLSVF4_cast



