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
    from . import _itkKdTreeGeneratorPython
else:
    import _itkKdTreeGeneratorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkKdTreeGeneratorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkKdTreeGeneratorPython.SWIG_PyStaticMethod_New

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
import itk.itkKdTreePython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkEuclideanDistanceMetricPython
import itk.itkDistanceMetricPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkFunctionBasePython
import itk.itkContinuousIndexPython
import itk.itkPointPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkArrayPython
import itk.itkImagePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkImageRegionPython
import itk.itkListSamplePython
import itk.itkSamplePython

def itkKdTreeGeneratorLSVF2_New():
    return itkKdTreeGeneratorLSVF2.New()

class itkKdTreeGeneratorLSVF2(itk.ITKCommonBasePython.itkObject):
    r"""


    This class generates a KdTree object without centroid information.

    The KdTree object stores measurement vectors in a k-d tree structure
    that is a binary tree. The partition value is the median value of one
    of the k dimension (partition dimension). The partition dimension is
    determined by the spread of measurement values in each dimension. The
    partition dimension is the dimension has the widest spread. Our
    implementation of k-d tree doesn't have any construction or insertion
    logic. Users should use this class or the
    WeightedCentroidKdTreeGenerator class.

    The number of the measurement vectors in a terminal node is set by the
    SetBucketSize method. If we use too small number for this, it might
    cause computational overhead to calculate bound conditions. However,
    too large number will cause more distance calculation between the
    measurement vectors in a terminal node and the query point.

    To run this generator, users should provides the bucket size
    (SetBucketSize method) and the input sample (SetSample method). The
    Update method will run this generator. To get the resulting KdTree
    object, call the GetOutput method.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. It is
    now obtained from the sample set as input. You may query this length
    using the function GetMeasurementVectorSize().

    See:   KdTree, KdTreeNode, KdTreeNonterminalNode, KdTreeTerminalNode,
    WeightedCentroidKdTreeGenerator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2___New_orig__)
    Clone = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_Clone)
    SetSample = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_SetSample)
    SetBucketSize = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_SetBucketSize)
    GetOutput = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_GetOutput)
    Update = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_Update)
    GenerateData = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_GenerateData)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_GetMeasurementVectorSize)
    __swig_destroy__ = _itkKdTreeGeneratorPython.delete_itkKdTreeGeneratorLSVF2
    cast = _swig_new_static_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeGeneratorLSVF2

        Create a new object of the class itkKdTreeGeneratorLSVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeGeneratorLSVF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKdTreeGeneratorLSVF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKdTreeGeneratorLSVF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKdTreeGeneratorLSVF2 in _itkKdTreeGeneratorPython:
_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_swigregister(itkKdTreeGeneratorLSVF2)
itkKdTreeGeneratorLSVF2___New_orig__ = _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2___New_orig__
itkKdTreeGeneratorLSVF2_cast = _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_cast


def itkKdTreeGeneratorLSVF3_New():
    return itkKdTreeGeneratorLSVF3.New()

class itkKdTreeGeneratorLSVF3(itk.ITKCommonBasePython.itkObject):
    r"""


    This class generates a KdTree object without centroid information.

    The KdTree object stores measurement vectors in a k-d tree structure
    that is a binary tree. The partition value is the median value of one
    of the k dimension (partition dimension). The partition dimension is
    determined by the spread of measurement values in each dimension. The
    partition dimension is the dimension has the widest spread. Our
    implementation of k-d tree doesn't have any construction or insertion
    logic. Users should use this class or the
    WeightedCentroidKdTreeGenerator class.

    The number of the measurement vectors in a terminal node is set by the
    SetBucketSize method. If we use too small number for this, it might
    cause computational overhead to calculate bound conditions. However,
    too large number will cause more distance calculation between the
    measurement vectors in a terminal node and the query point.

    To run this generator, users should provides the bucket size
    (SetBucketSize method) and the input sample (SetSample method). The
    Update method will run this generator. To get the resulting KdTree
    object, call the GetOutput method.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. It is
    now obtained from the sample set as input. You may query this length
    using the function GetMeasurementVectorSize().

    See:   KdTree, KdTreeNode, KdTreeNonterminalNode, KdTreeTerminalNode,
    WeightedCentroidKdTreeGenerator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3___New_orig__)
    Clone = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_Clone)
    SetSample = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_SetSample)
    SetBucketSize = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_SetBucketSize)
    GetOutput = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_GetOutput)
    Update = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_Update)
    GenerateData = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_GenerateData)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_GetMeasurementVectorSize)
    __swig_destroy__ = _itkKdTreeGeneratorPython.delete_itkKdTreeGeneratorLSVF3
    cast = _swig_new_static_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeGeneratorLSVF3

        Create a new object of the class itkKdTreeGeneratorLSVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeGeneratorLSVF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKdTreeGeneratorLSVF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKdTreeGeneratorLSVF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKdTreeGeneratorLSVF3 in _itkKdTreeGeneratorPython:
_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_swigregister(itkKdTreeGeneratorLSVF3)
itkKdTreeGeneratorLSVF3___New_orig__ = _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3___New_orig__
itkKdTreeGeneratorLSVF3_cast = _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_cast


def itkKdTreeGeneratorLSVF4_New():
    return itkKdTreeGeneratorLSVF4.New()

class itkKdTreeGeneratorLSVF4(itk.ITKCommonBasePython.itkObject):
    r"""


    This class generates a KdTree object without centroid information.

    The KdTree object stores measurement vectors in a k-d tree structure
    that is a binary tree. The partition value is the median value of one
    of the k dimension (partition dimension). The partition dimension is
    determined by the spread of measurement values in each dimension. The
    partition dimension is the dimension has the widest spread. Our
    implementation of k-d tree doesn't have any construction or insertion
    logic. Users should use this class or the
    WeightedCentroidKdTreeGenerator class.

    The number of the measurement vectors in a terminal node is set by the
    SetBucketSize method. If we use too small number for this, it might
    cause computational overhead to calculate bound conditions. However,
    too large number will cause more distance calculation between the
    measurement vectors in a terminal node and the query point.

    To run this generator, users should provides the bucket size
    (SetBucketSize method) and the input sample (SetSample method). The
    Update method will run this generator. To get the resulting KdTree
    object, call the GetOutput method.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. It is
    now obtained from the sample set as input. You may query this length
    using the function GetMeasurementVectorSize().

    See:   KdTree, KdTreeNode, KdTreeNonterminalNode, KdTreeTerminalNode,
    WeightedCentroidKdTreeGenerator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4___New_orig__)
    Clone = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4_Clone)
    SetSample = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4_SetSample)
    SetBucketSize = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4_SetBucketSize)
    GetOutput = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4_GetOutput)
    Update = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4_Update)
    GenerateData = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4_GenerateData)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4_GetMeasurementVectorSize)
    __swig_destroy__ = _itkKdTreeGeneratorPython.delete_itkKdTreeGeneratorLSVF4
    cast = _swig_new_static_method(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4_cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeGeneratorLSVF4

        Create a new object of the class itkKdTreeGeneratorLSVF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeGeneratorLSVF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKdTreeGeneratorLSVF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKdTreeGeneratorLSVF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKdTreeGeneratorLSVF4 in _itkKdTreeGeneratorPython:
_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4_swigregister(itkKdTreeGeneratorLSVF4)
itkKdTreeGeneratorLSVF4___New_orig__ = _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4___New_orig__
itkKdTreeGeneratorLSVF4_cast = _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF4_cast



