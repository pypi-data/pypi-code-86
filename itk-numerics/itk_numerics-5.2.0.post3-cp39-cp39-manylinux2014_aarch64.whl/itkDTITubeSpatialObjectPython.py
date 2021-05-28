# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKSpatialObjectsPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkDTITubeSpatialObjectPython
else:
    import _itkDTITubeSpatialObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDTITubeSpatialObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDTITubeSpatialObjectPython.SWIG_PyStaticMethod_New

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
import itk.itkSpatialObjectBasePython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkImageRegionPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkArray2DPython
import itk.itkVariableLengthVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkDiffusionTensor3DPython
import itk.itkTransformBasePython
import itk.itkSpatialObjectPropertyPython
import itk.itkRGBAPixelPython
import itk.itkDTITubeSpatialObjectPointPython
import itk.itkTubeSpatialObjectPointPython
import itk.itkSpatialObjectPointPython
class listitkPointBasedSpatialObjectDTITube3_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkPointBasedSpatialObjectDTITube3_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_pop)
    append = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_append)
    empty = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_empty)
    size = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_size)
    swap = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_swap)
    begin = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_begin)
    end = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_end)
    rbegin = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_rend)
    clear = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkPointBasedSpatialObjectDTITube3_Pointer
        __init__(self, other) -> listitkPointBasedSpatialObjectDTITube3_Pointer

        Parameters
        ----------
        other: std::list< itkPointBasedSpatialObjectDTITube3_Pointer > const &

        __init__(self, size) -> listitkPointBasedSpatialObjectDTITube3_Pointer

        Parameters
        ----------
        size: std::list< itkPointBasedSpatialObjectDTITube3_Pointer >::size_type

        __init__(self, size, value) -> listitkPointBasedSpatialObjectDTITube3_Pointer

        Parameters
        ----------
        size: std::list< itkPointBasedSpatialObjectDTITube3_Pointer >::size_type
        value: std::list< itkPointBasedSpatialObjectDTITube3_Pointer >::value_type const &

        """
        _itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_swiginit(self, _itkDTITubeSpatialObjectPython.new_listitkPointBasedSpatialObjectDTITube3_Pointer(*args))
    push_back = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_push_back)
    front = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_front)
    back = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_back)
    assign = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_assign)
    resize = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_resize)
    insert = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_reverse)
    __swig_destroy__ = _itkDTITubeSpatialObjectPython.delete_listitkPointBasedSpatialObjectDTITube3_Pointer

# Register listitkPointBasedSpatialObjectDTITube3_Pointer in _itkDTITubeSpatialObjectPython:
_itkDTITubeSpatialObjectPython.listitkPointBasedSpatialObjectDTITube3_Pointer_swigregister(listitkPointBasedSpatialObjectDTITube3_Pointer)


def itkPointBasedSpatialObjectDTITube3_New():
    return itkPointBasedSpatialObjectDTITube3.New()

class itkPointBasedSpatialObjectDTITube3(itk.itkSpatialObjectBasePython.itkSpatialObject3):
    r"""


    This class serves as the base class for point-based spatial objects.

    A PointBasedSpatialObject is an abstract class to support
    PointBasedSpatialObject filters and algorithms. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3___New_orig__)
    Clone = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_Clone)
    AddPoint = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_AddPoint)
    RemovePoint = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_RemovePoint)
    SetPoints = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_SetPoints)
    GetPoints = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_GetPoints)
    GetPoint = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_GetPoint)
    GetNumberOfPoints = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_GetNumberOfPoints)
    ClosestPointInWorldSpace = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_ClosestPointInWorldSpace)
    ClosestPointInObjectSpace = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_ClosestPointInObjectSpace)
    __swig_destroy__ = _itkDTITubeSpatialObjectPython.delete_itkPointBasedSpatialObjectDTITube3
    cast = _swig_new_static_method(_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_cast)

    def New(*args, **kargs):
        """New() -> itkPointBasedSpatialObjectDTITube3

        Create a new object of the class itkPointBasedSpatialObjectDTITube3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPointBasedSpatialObjectDTITube3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPointBasedSpatialObjectDTITube3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPointBasedSpatialObjectDTITube3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPointBasedSpatialObjectDTITube3 in _itkDTITubeSpatialObjectPython:
_itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_swigregister(itkPointBasedSpatialObjectDTITube3)
itkPointBasedSpatialObjectDTITube3___New_orig__ = _itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3___New_orig__
itkPointBasedSpatialObjectDTITube3_cast = _itkDTITubeSpatialObjectPython.itkPointBasedSpatialObjectDTITube3_cast


def itkDTITubeSpatialObject3_Superclass_New():
    return itkDTITubeSpatialObject3_Superclass.New()

class itkDTITubeSpatialObject3_Superclass(itkPointBasedSpatialObjectDTITube3):
    r"""Proxy of C++ itkDTITubeSpatialObject3_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_Clone)
    SetEndRounded = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetEndRounded)
    GetEndRounded = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetEndRounded)
    EndRoundedOn = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_EndRoundedOn)
    EndRoundedOff = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_EndRoundedOff)
    ComputeTangentsAndNormals = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_ComputeTangentsAndNormals)
    RemoveDuplicatePointsInObjectSpace = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_RemoveDuplicatePointsInObjectSpace)
    SetParentPoint = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetParentPoint)
    GetParentPoint = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetParentPoint)
    SetRoot = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_SetRoot)
    GetRoot = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_GetRoot)
    RootOn = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_RootOn)
    RootOff = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_RootOff)
    __swig_destroy__ = _itkDTITubeSpatialObjectPython.delete_itkDTITubeSpatialObject3_Superclass
    cast = _swig_new_static_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkDTITubeSpatialObject3_Superclass

        Create a new object of the class itkDTITubeSpatialObject3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDTITubeSpatialObject3_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDTITubeSpatialObject3_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDTITubeSpatialObject3_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDTITubeSpatialObject3_Superclass in _itkDTITubeSpatialObjectPython:
_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_swigregister(itkDTITubeSpatialObject3_Superclass)
itkDTITubeSpatialObject3_Superclass___New_orig__ = _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass___New_orig__
itkDTITubeSpatialObject3_Superclass_cast = _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Superclass_cast


def itkDTITubeSpatialObject3_New():
    return itkDTITubeSpatialObject3.New()

class itkDTITubeSpatialObject3(itkDTITubeSpatialObject3_Superclass):
    r"""


    Representation of a tube based on the spatial object classes.

    The tube is basically defined by a set of points. Each tube can be
    connected to a tube network, by using the AddChild() methods of a
    DTITubeSpatialObject Object. A tube is also identified by an id number
    when connected to a network.

    See:   DTITubeSpatialObjectPoint 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3___New_orig__)
    Clone = _swig_new_instance_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_Clone)
    __swig_destroy__ = _itkDTITubeSpatialObjectPython.delete_itkDTITubeSpatialObject3
    cast = _swig_new_static_method(_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_cast)

    def New(*args, **kargs):
        """New() -> itkDTITubeSpatialObject3

        Create a new object of the class itkDTITubeSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDTITubeSpatialObject3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDTITubeSpatialObject3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDTITubeSpatialObject3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDTITubeSpatialObject3 in _itkDTITubeSpatialObjectPython:
_itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_swigregister(itkDTITubeSpatialObject3)
itkDTITubeSpatialObject3___New_orig__ = _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3___New_orig__
itkDTITubeSpatialObject3_cast = _itkDTITubeSpatialObjectPython.itkDTITubeSpatialObject3_cast



