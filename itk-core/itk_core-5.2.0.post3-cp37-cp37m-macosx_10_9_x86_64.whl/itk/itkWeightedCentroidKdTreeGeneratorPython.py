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
    from . import _itkWeightedCentroidKdTreeGeneratorPython
else:
    import _itkWeightedCentroidKdTreeGeneratorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkWeightedCentroidKdTreeGeneratorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkWeightedCentroidKdTreeGeneratorPython.SWIG_PyStaticMethod_New

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
import itk.itkKdTreeGeneratorPython

def itkWeightedCentroidKdTreeGeneratorLSVF2_New():
    return itkWeightedCentroidKdTreeGeneratorLSVF2.New()

class itkWeightedCentroidKdTreeGeneratorLSVF2(itk.itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2):
    r"""


    This class generates a KdTree object with centroid information.

    The KdTree object stores measurement vectors in a k-d tree structure
    that is a binary tree. The partition value is the median value of one
    of the k dimension (partition dimension). The partition dimension is
    determined by the spread of measurement values in each dimension. The
    partition dimension is the dimension has the widest spread. Our
    implementation of k-d tree doesn't have any construction or insertion
    logic. Users should use this class or the KdTreeGenerator class.

    This class is derived from the KdTreeGenerator class. The only
    difference between this class and the KdTreeGenerator class is that
    the nonterminal node type of this class is
    KdTreeWeightedCentroidNonterminalNode and that of the KdTreeGenerator
    is KdTreeNonterminalNode. Therefore, the public interface is identical
    to each other. The nonterminal node generation routines differ.

    To run this generator, users should provides the bucket size
    (SetBucketSize method) and the input sample (SetSample method). The
    Update method will run this generator. To get the resulting KdTree
    object, call the GetOutput method.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. It is
    now obtained from the sample set as input. You may query this length
    using the function GetMeasurementVectorSize().

    See:   KdTree, KdTreeNode, KdTreeWeightedCentroidNonterminalNode,
    KdTreeTerminalNode, KdTreeGenerator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF2___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF2_Clone)
    __swig_destroy__ = _itkWeightedCentroidKdTreeGeneratorPython.delete_itkWeightedCentroidKdTreeGeneratorLSVF2
    cast = _swig_new_static_method(_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF2_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedCentroidKdTreeGeneratorLSVF2

        Create a new object of the class itkWeightedCentroidKdTreeGeneratorLSVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedCentroidKdTreeGeneratorLSVF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkWeightedCentroidKdTreeGeneratorLSVF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkWeightedCentroidKdTreeGeneratorLSVF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedCentroidKdTreeGeneratorLSVF2 in _itkWeightedCentroidKdTreeGeneratorPython:
_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF2_swigregister(itkWeightedCentroidKdTreeGeneratorLSVF2)
itkWeightedCentroidKdTreeGeneratorLSVF2___New_orig__ = _itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF2___New_orig__
itkWeightedCentroidKdTreeGeneratorLSVF2_cast = _itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF2_cast


def itkWeightedCentroidKdTreeGeneratorLSVF3_New():
    return itkWeightedCentroidKdTreeGeneratorLSVF3.New()

class itkWeightedCentroidKdTreeGeneratorLSVF3(itk.itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3):
    r"""


    This class generates a KdTree object with centroid information.

    The KdTree object stores measurement vectors in a k-d tree structure
    that is a binary tree. The partition value is the median value of one
    of the k dimension (partition dimension). The partition dimension is
    determined by the spread of measurement values in each dimension. The
    partition dimension is the dimension has the widest spread. Our
    implementation of k-d tree doesn't have any construction or insertion
    logic. Users should use this class or the KdTreeGenerator class.

    This class is derived from the KdTreeGenerator class. The only
    difference between this class and the KdTreeGenerator class is that
    the nonterminal node type of this class is
    KdTreeWeightedCentroidNonterminalNode and that of the KdTreeGenerator
    is KdTreeNonterminalNode. Therefore, the public interface is identical
    to each other. The nonterminal node generation routines differ.

    To run this generator, users should provides the bucket size
    (SetBucketSize method) and the input sample (SetSample method). The
    Update method will run this generator. To get the resulting KdTree
    object, call the GetOutput method.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. It is
    now obtained from the sample set as input. You may query this length
    using the function GetMeasurementVectorSize().

    See:   KdTree, KdTreeNode, KdTreeWeightedCentroidNonterminalNode,
    KdTreeTerminalNode, KdTreeGenerator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF3___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF3_Clone)
    __swig_destroy__ = _itkWeightedCentroidKdTreeGeneratorPython.delete_itkWeightedCentroidKdTreeGeneratorLSVF3
    cast = _swig_new_static_method(_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF3_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedCentroidKdTreeGeneratorLSVF3

        Create a new object of the class itkWeightedCentroidKdTreeGeneratorLSVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedCentroidKdTreeGeneratorLSVF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkWeightedCentroidKdTreeGeneratorLSVF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkWeightedCentroidKdTreeGeneratorLSVF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedCentroidKdTreeGeneratorLSVF3 in _itkWeightedCentroidKdTreeGeneratorPython:
_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF3_swigregister(itkWeightedCentroidKdTreeGeneratorLSVF3)
itkWeightedCentroidKdTreeGeneratorLSVF3___New_orig__ = _itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF3___New_orig__
itkWeightedCentroidKdTreeGeneratorLSVF3_cast = _itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF3_cast


def itkWeightedCentroidKdTreeGeneratorLSVF4_New():
    return itkWeightedCentroidKdTreeGeneratorLSVF4.New()

class itkWeightedCentroidKdTreeGeneratorLSVF4(itk.itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4):
    r"""


    This class generates a KdTree object with centroid information.

    The KdTree object stores measurement vectors in a k-d tree structure
    that is a binary tree. The partition value is the median value of one
    of the k dimension (partition dimension). The partition dimension is
    determined by the spread of measurement values in each dimension. The
    partition dimension is the dimension has the widest spread. Our
    implementation of k-d tree doesn't have any construction or insertion
    logic. Users should use this class or the KdTreeGenerator class.

    This class is derived from the KdTreeGenerator class. The only
    difference between this class and the KdTreeGenerator class is that
    the nonterminal node type of this class is
    KdTreeWeightedCentroidNonterminalNode and that of the KdTreeGenerator
    is KdTreeNonterminalNode. Therefore, the public interface is identical
    to each other. The nonterminal node generation routines differ.

    To run this generator, users should provides the bucket size
    (SetBucketSize method) and the input sample (SetSample method). The
    Update method will run this generator. To get the resulting KdTree
    object, call the GetOutput method.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. It is
    now obtained from the sample set as input. You may query this length
    using the function GetMeasurementVectorSize().

    See:   KdTree, KdTreeNode, KdTreeWeightedCentroidNonterminalNode,
    KdTreeTerminalNode, KdTreeGenerator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF4___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF4_Clone)
    __swig_destroy__ = _itkWeightedCentroidKdTreeGeneratorPython.delete_itkWeightedCentroidKdTreeGeneratorLSVF4
    cast = _swig_new_static_method(_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF4_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedCentroidKdTreeGeneratorLSVF4

        Create a new object of the class itkWeightedCentroidKdTreeGeneratorLSVF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedCentroidKdTreeGeneratorLSVF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkWeightedCentroidKdTreeGeneratorLSVF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkWeightedCentroidKdTreeGeneratorLSVF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedCentroidKdTreeGeneratorLSVF4 in _itkWeightedCentroidKdTreeGeneratorPython:
_itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF4_swigregister(itkWeightedCentroidKdTreeGeneratorLSVF4)
itkWeightedCentroidKdTreeGeneratorLSVF4___New_orig__ = _itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF4___New_orig__
itkWeightedCentroidKdTreeGeneratorLSVF4_cast = _itkWeightedCentroidKdTreeGeneratorPython.itkWeightedCentroidKdTreeGeneratorLSVF4_cast



