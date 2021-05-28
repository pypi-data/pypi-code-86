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
    from . import _itkKdTreePython
else:
    import _itkKdTreePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkKdTreePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkKdTreePython.SWIG_PyStaticMethod_New

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
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkListSamplePython
import itk.itkSamplePython
import itk.ITKCommonBasePython
import itk.itkEuclideanDistanceMetricPython
import itk.itkDistanceMetricPython
import itk.itkFunctionBasePython
import itk.itkRGBPixelPython
import itk.itkCovariantVectorPython
import itk.itkPointPython
import itk.itkImagePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
import itk.itkContinuousIndexPython

def itkKdTreeLSVF2_New():
    return itkKdTreeLSVF2.New()

class itkKdTreeLSVF2(itk.ITKCommonBasePython.itkObject):
    r"""


    This class provides methods for k-nearest neighbor search and related
    data structures for a k-d tree.

    An object of this class stores instance identifiers in a k-d tree that
    is a binary tree with childrens split along a dimension among
    k-dimensions. The dimension of the split (or partition) is determined
    for each nonterminal node that has two children. The split process is
    terminated when the node has no children (when the number of
    measurement vectors is less than or equal to the size set by the
    SetBucketSize. That is The split process is a recursive process in
    nature and in implementation. This implementation doesn't support
    dynamic insert and delete operations for the tree. Instead, we can use
    the KdTreeGenerator or WeightedCentroidKdTreeGenerator to generate a
    static KdTree object.

    To search k-nearest neighbor, call the Search method with the query
    point in a k-d space and the number of nearest neighbors. The
    GetSearchResult method returns a pointer to a NearestNeighbors object
    with k-nearest neighbors.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. Please
    use the function GetMeasurementVectorSize() instead.

    See:   KdTreeNode, KdTreeNonterminalNode,
    KdTreeWeightedCentroidNonterminalNode, KdTreeTerminalNode,
    KdTreeGenerator, WeightedCentroidKdTreeNode 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKdTreePython.itkKdTreeLSVF2___New_orig__)
    Clone = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_Clone)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_GetMeasurementVectorSize)
    SetBucketSize = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_SetBucketSize)
    SetSample = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_SetSample)
    GetSample = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_GetSample)
    Size = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_Size)
    GetEmptyTerminalNode = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_GetEmptyTerminalNode)
    SetRoot = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_SetRoot)
    GetRoot = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_GetRoot)
    GetMeasurementVector = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_GetMeasurementVector)
    GetFrequency = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_GetFrequency)
    GetDistanceMetric = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_GetDistanceMetric)
    Search = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_Search)
    BallWithinBounds = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_BallWithinBounds)
    BoundsOverlapBall = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_BoundsOverlapBall)
    DeleteNode = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_DeleteNode)
    PrintTree = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_PrintTree)
    PlotTree = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF2_PlotTree)
    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeLSVF2
    cast = _swig_new_static_method(_itkKdTreePython.itkKdTreeLSVF2_cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeLSVF2

        Create a new object of the class itkKdTreeLSVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeLSVF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKdTreeLSVF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKdTreeLSVF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKdTreeLSVF2 in _itkKdTreePython:
_itkKdTreePython.itkKdTreeLSVF2_swigregister(itkKdTreeLSVF2)
itkKdTreeLSVF2___New_orig__ = _itkKdTreePython.itkKdTreeLSVF2___New_orig__
itkKdTreeLSVF2_cast = _itkKdTreePython.itkKdTreeLSVF2_cast


def itkKdTreeLSVF3_New():
    return itkKdTreeLSVF3.New()

class itkKdTreeLSVF3(itk.ITKCommonBasePython.itkObject):
    r"""


    This class provides methods for k-nearest neighbor search and related
    data structures for a k-d tree.

    An object of this class stores instance identifiers in a k-d tree that
    is a binary tree with childrens split along a dimension among
    k-dimensions. The dimension of the split (or partition) is determined
    for each nonterminal node that has two children. The split process is
    terminated when the node has no children (when the number of
    measurement vectors is less than or equal to the size set by the
    SetBucketSize. That is The split process is a recursive process in
    nature and in implementation. This implementation doesn't support
    dynamic insert and delete operations for the tree. Instead, we can use
    the KdTreeGenerator or WeightedCentroidKdTreeGenerator to generate a
    static KdTree object.

    To search k-nearest neighbor, call the Search method with the query
    point in a k-d space and the number of nearest neighbors. The
    GetSearchResult method returns a pointer to a NearestNeighbors object
    with k-nearest neighbors.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. Please
    use the function GetMeasurementVectorSize() instead.

    See:   KdTreeNode, KdTreeNonterminalNode,
    KdTreeWeightedCentroidNonterminalNode, KdTreeTerminalNode,
    KdTreeGenerator, WeightedCentroidKdTreeNode 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKdTreePython.itkKdTreeLSVF3___New_orig__)
    Clone = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_Clone)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_GetMeasurementVectorSize)
    SetBucketSize = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_SetBucketSize)
    SetSample = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_SetSample)
    GetSample = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_GetSample)
    Size = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_Size)
    GetEmptyTerminalNode = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_GetEmptyTerminalNode)
    SetRoot = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_SetRoot)
    GetRoot = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_GetRoot)
    GetMeasurementVector = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_GetMeasurementVector)
    GetFrequency = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_GetFrequency)
    GetDistanceMetric = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_GetDistanceMetric)
    Search = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_Search)
    BallWithinBounds = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_BallWithinBounds)
    BoundsOverlapBall = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_BoundsOverlapBall)
    DeleteNode = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_DeleteNode)
    PrintTree = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_PrintTree)
    PlotTree = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF3_PlotTree)
    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeLSVF3
    cast = _swig_new_static_method(_itkKdTreePython.itkKdTreeLSVF3_cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeLSVF3

        Create a new object of the class itkKdTreeLSVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeLSVF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKdTreeLSVF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKdTreeLSVF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKdTreeLSVF3 in _itkKdTreePython:
_itkKdTreePython.itkKdTreeLSVF3_swigregister(itkKdTreeLSVF3)
itkKdTreeLSVF3___New_orig__ = _itkKdTreePython.itkKdTreeLSVF3___New_orig__
itkKdTreeLSVF3_cast = _itkKdTreePython.itkKdTreeLSVF3_cast


def itkKdTreeLSVF4_New():
    return itkKdTreeLSVF4.New()

class itkKdTreeLSVF4(itk.ITKCommonBasePython.itkObject):
    r"""


    This class provides methods for k-nearest neighbor search and related
    data structures for a k-d tree.

    An object of this class stores instance identifiers in a k-d tree that
    is a binary tree with childrens split along a dimension among
    k-dimensions. The dimension of the split (or partition) is determined
    for each nonterminal node that has two children. The split process is
    terminated when the node has no children (when the number of
    measurement vectors is less than or equal to the size set by the
    SetBucketSize. That is The split process is a recursive process in
    nature and in implementation. This implementation doesn't support
    dynamic insert and delete operations for the tree. Instead, we can use
    the KdTreeGenerator or WeightedCentroidKdTreeGenerator to generate a
    static KdTree object.

    To search k-nearest neighbor, call the Search method with the query
    point in a k-d space and the number of nearest neighbors. The
    GetSearchResult method returns a pointer to a NearestNeighbors object
    with k-nearest neighbors.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. Please
    use the function GetMeasurementVectorSize() instead.

    See:   KdTreeNode, KdTreeNonterminalNode,
    KdTreeWeightedCentroidNonterminalNode, KdTreeTerminalNode,
    KdTreeGenerator, WeightedCentroidKdTreeNode 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKdTreePython.itkKdTreeLSVF4___New_orig__)
    Clone = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_Clone)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_GetMeasurementVectorSize)
    SetBucketSize = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_SetBucketSize)
    SetSample = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_SetSample)
    GetSample = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_GetSample)
    Size = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_Size)
    GetEmptyTerminalNode = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_GetEmptyTerminalNode)
    SetRoot = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_SetRoot)
    GetRoot = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_GetRoot)
    GetMeasurementVector = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_GetMeasurementVector)
    GetFrequency = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_GetFrequency)
    GetDistanceMetric = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_GetDistanceMetric)
    Search = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_Search)
    BallWithinBounds = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_BallWithinBounds)
    BoundsOverlapBall = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_BoundsOverlapBall)
    DeleteNode = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_DeleteNode)
    PrintTree = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_PrintTree)
    PlotTree = _swig_new_instance_method(_itkKdTreePython.itkKdTreeLSVF4_PlotTree)
    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeLSVF4
    cast = _swig_new_static_method(_itkKdTreePython.itkKdTreeLSVF4_cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeLSVF4

        Create a new object of the class itkKdTreeLSVF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeLSVF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKdTreeLSVF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKdTreeLSVF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKdTreeLSVF4 in _itkKdTreePython:
_itkKdTreePython.itkKdTreeLSVF4_swigregister(itkKdTreeLSVF4)
itkKdTreeLSVF4___New_orig__ = _itkKdTreePython.itkKdTreeLSVF4___New_orig__
itkKdTreeLSVF4_cast = _itkKdTreePython.itkKdTreeLSVF4_cast

class itkKdTreeNodeLSVF2(object):
    r"""Proxy of C++ itkKdTreeNodeLSVF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    IsTerminal = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF2_IsTerminal)
    GetParameters = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF2_GetParameters)
    Left = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF2_Left)
    Right = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF2_Right)
    Size = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF2_Size)
    GetWeightedCentroid = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF2_GetWeightedCentroid)
    GetCentroid = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF2_GetCentroid)
    GetInstanceIdentifier = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF2_GetInstanceIdentifier)
    AddInstanceIdentifier = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF2_AddInstanceIdentifier)
    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeNodeLSVF2

# Register itkKdTreeNodeLSVF2 in _itkKdTreePython:
_itkKdTreePython.itkKdTreeNodeLSVF2_swigregister(itkKdTreeNodeLSVF2)

class itkKdTreeNodeLSVF3(object):
    r"""Proxy of C++ itkKdTreeNodeLSVF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    IsTerminal = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF3_IsTerminal)
    GetParameters = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF3_GetParameters)
    Left = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF3_Left)
    Right = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF3_Right)
    Size = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF3_Size)
    GetWeightedCentroid = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF3_GetWeightedCentroid)
    GetCentroid = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF3_GetCentroid)
    GetInstanceIdentifier = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF3_GetInstanceIdentifier)
    AddInstanceIdentifier = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF3_AddInstanceIdentifier)
    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeNodeLSVF3

# Register itkKdTreeNodeLSVF3 in _itkKdTreePython:
_itkKdTreePython.itkKdTreeNodeLSVF3_swigregister(itkKdTreeNodeLSVF3)

class itkKdTreeNodeLSVF4(object):
    r"""Proxy of C++ itkKdTreeNodeLSVF4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    IsTerminal = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF4_IsTerminal)
    GetParameters = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF4_GetParameters)
    Left = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF4_Left)
    Right = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF4_Right)
    Size = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF4_Size)
    GetWeightedCentroid = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF4_GetWeightedCentroid)
    GetCentroid = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF4_GetCentroid)
    GetInstanceIdentifier = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF4_GetInstanceIdentifier)
    AddInstanceIdentifier = _swig_new_instance_method(_itkKdTreePython.itkKdTreeNodeLSVF4_AddInstanceIdentifier)
    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeNodeLSVF4

# Register itkKdTreeNodeLSVF4 in _itkKdTreePython:
_itkKdTreePython.itkKdTreeNodeLSVF4_swigregister(itkKdTreeNodeLSVF4)



