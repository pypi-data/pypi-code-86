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
    from . import _itkPointBasedSpatialObjectPython
else:
    import _itkPointBasedSpatialObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkPointBasedSpatialObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkPointBasedSpatialObjectPython.SWIG_PyStaticMethod_New

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
import itk.itkSpatialObjectPointPython
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.itkSpatialObjectBasePython
import itk.itkAffineTransformPython
import itk.itkMatrixPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkCovariantVectorPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkTransformBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkArray2DPython
import itk.itkArrayPython
import itk.itkVariableLengthVectorPython
import itk.itkOptimizerParametersPython
import itk.itkDiffusionTensor3DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkSpatialObjectPropertyPython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkBoundingBoxPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkMapContainerPython
class listitkPointBasedSpatialObject2_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkPointBasedSpatialObject2_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_pop)
    append = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_append)
    empty = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_empty)
    size = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_size)
    swap = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_swap)
    begin = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_begin)
    end = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_end)
    rbegin = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_rend)
    clear = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkPointBasedSpatialObject2_Pointer
        __init__(self, other) -> listitkPointBasedSpatialObject2_Pointer

        Parameters
        ----------
        other: std::list< itkPointBasedSpatialObject2_Pointer > const &

        __init__(self, size) -> listitkPointBasedSpatialObject2_Pointer

        Parameters
        ----------
        size: std::list< itkPointBasedSpatialObject2_Pointer >::size_type

        __init__(self, size, value) -> listitkPointBasedSpatialObject2_Pointer

        Parameters
        ----------
        size: std::list< itkPointBasedSpatialObject2_Pointer >::size_type
        value: std::list< itkPointBasedSpatialObject2_Pointer >::value_type const &

        """
        _itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_swiginit(self, _itkPointBasedSpatialObjectPython.new_listitkPointBasedSpatialObject2_Pointer(*args))
    push_back = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_push_back)
    front = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_front)
    back = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_back)
    assign = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_assign)
    resize = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_resize)
    insert = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_reverse)
    __swig_destroy__ = _itkPointBasedSpatialObjectPython.delete_listitkPointBasedSpatialObject2_Pointer

# Register listitkPointBasedSpatialObject2_Pointer in _itkPointBasedSpatialObjectPython:
_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject2_Pointer_swigregister(listitkPointBasedSpatialObject2_Pointer)

class listitkPointBasedSpatialObject3_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkPointBasedSpatialObject3_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_pop)
    append = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_append)
    empty = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_empty)
    size = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_size)
    swap = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_swap)
    begin = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_begin)
    end = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_end)
    rbegin = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_rend)
    clear = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkPointBasedSpatialObject3_Pointer
        __init__(self, other) -> listitkPointBasedSpatialObject3_Pointer

        Parameters
        ----------
        other: std::list< itkPointBasedSpatialObject3_Pointer > const &

        __init__(self, size) -> listitkPointBasedSpatialObject3_Pointer

        Parameters
        ----------
        size: std::list< itkPointBasedSpatialObject3_Pointer >::size_type

        __init__(self, size, value) -> listitkPointBasedSpatialObject3_Pointer

        Parameters
        ----------
        size: std::list< itkPointBasedSpatialObject3_Pointer >::size_type
        value: std::list< itkPointBasedSpatialObject3_Pointer >::value_type const &

        """
        _itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_swiginit(self, _itkPointBasedSpatialObjectPython.new_listitkPointBasedSpatialObject3_Pointer(*args))
    push_back = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_push_back)
    front = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_front)
    back = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_back)
    assign = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_assign)
    resize = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_resize)
    insert = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_reverse)
    __swig_destroy__ = _itkPointBasedSpatialObjectPython.delete_listitkPointBasedSpatialObject3_Pointer

# Register listitkPointBasedSpatialObject3_Pointer in _itkPointBasedSpatialObjectPython:
_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject3_Pointer_swigregister(listitkPointBasedSpatialObject3_Pointer)

class listitkPointBasedSpatialObject4_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkPointBasedSpatialObject4_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_pop)
    append = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_append)
    empty = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_empty)
    size = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_size)
    swap = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_swap)
    begin = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_begin)
    end = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_end)
    rbegin = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_rend)
    clear = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkPointBasedSpatialObject4_Pointer
        __init__(self, other) -> listitkPointBasedSpatialObject4_Pointer

        Parameters
        ----------
        other: std::list< itkPointBasedSpatialObject4_Pointer > const &

        __init__(self, size) -> listitkPointBasedSpatialObject4_Pointer

        Parameters
        ----------
        size: std::list< itkPointBasedSpatialObject4_Pointer >::size_type

        __init__(self, size, value) -> listitkPointBasedSpatialObject4_Pointer

        Parameters
        ----------
        size: std::list< itkPointBasedSpatialObject4_Pointer >::size_type
        value: std::list< itkPointBasedSpatialObject4_Pointer >::value_type const &

        """
        _itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_swiginit(self, _itkPointBasedSpatialObjectPython.new_listitkPointBasedSpatialObject4_Pointer(*args))
    push_back = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_push_back)
    front = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_front)
    back = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_back)
    assign = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_assign)
    resize = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_resize)
    insert = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_reverse)
    __swig_destroy__ = _itkPointBasedSpatialObjectPython.delete_listitkPointBasedSpatialObject4_Pointer

# Register listitkPointBasedSpatialObject4_Pointer in _itkPointBasedSpatialObjectPython:
_itkPointBasedSpatialObjectPython.listitkPointBasedSpatialObject4_Pointer_swigregister(listitkPointBasedSpatialObject4_Pointer)


def itkPointBasedSpatialObject2_New():
    return itkPointBasedSpatialObject2.New()

class itkPointBasedSpatialObject2(itk.itkSpatialObjectBasePython.itkSpatialObject2):
    r"""


    This class serves as the base class for point-based spatial objects.

    A PointBasedSpatialObject is an abstract class to support
    PointBasedSpatialObject filters and algorithms. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2___New_orig__)
    Clone = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_Clone)
    AddPoint = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_AddPoint)
    RemovePoint = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_RemovePoint)
    SetPoints = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_SetPoints)
    GetPoints = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_GetPoints)
    GetPoint = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_GetPoint)
    GetNumberOfPoints = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_GetNumberOfPoints)
    ClosestPointInWorldSpace = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_ClosestPointInWorldSpace)
    ClosestPointInObjectSpace = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_ClosestPointInObjectSpace)
    __swig_destroy__ = _itkPointBasedSpatialObjectPython.delete_itkPointBasedSpatialObject2
    cast = _swig_new_static_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_cast)

    def New(*args, **kargs):
        """New() -> itkPointBasedSpatialObject2

        Create a new object of the class itkPointBasedSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPointBasedSpatialObject2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPointBasedSpatialObject2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPointBasedSpatialObject2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPointBasedSpatialObject2 in _itkPointBasedSpatialObjectPython:
_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_swigregister(itkPointBasedSpatialObject2)
itkPointBasedSpatialObject2___New_orig__ = _itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2___New_orig__
itkPointBasedSpatialObject2_cast = _itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2_cast


def itkPointBasedSpatialObject3_New():
    return itkPointBasedSpatialObject3.New()

class itkPointBasedSpatialObject3(itk.itkSpatialObjectBasePython.itkSpatialObject3):
    r"""


    This class serves as the base class for point-based spatial objects.

    A PointBasedSpatialObject is an abstract class to support
    PointBasedSpatialObject filters and algorithms. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3___New_orig__)
    Clone = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_Clone)
    AddPoint = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_AddPoint)
    RemovePoint = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_RemovePoint)
    SetPoints = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_SetPoints)
    GetPoints = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_GetPoints)
    GetPoint = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_GetPoint)
    GetNumberOfPoints = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_GetNumberOfPoints)
    ClosestPointInWorldSpace = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_ClosestPointInWorldSpace)
    ClosestPointInObjectSpace = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_ClosestPointInObjectSpace)
    __swig_destroy__ = _itkPointBasedSpatialObjectPython.delete_itkPointBasedSpatialObject3
    cast = _swig_new_static_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_cast)

    def New(*args, **kargs):
        """New() -> itkPointBasedSpatialObject3

        Create a new object of the class itkPointBasedSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPointBasedSpatialObject3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPointBasedSpatialObject3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPointBasedSpatialObject3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPointBasedSpatialObject3 in _itkPointBasedSpatialObjectPython:
_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_swigregister(itkPointBasedSpatialObject3)
itkPointBasedSpatialObject3___New_orig__ = _itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3___New_orig__
itkPointBasedSpatialObject3_cast = _itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3_cast


def itkPointBasedSpatialObject4_New():
    return itkPointBasedSpatialObject4.New()

class itkPointBasedSpatialObject4(itk.itkSpatialObjectBasePython.itkSpatialObject4):
    r"""


    This class serves as the base class for point-based spatial objects.

    A PointBasedSpatialObject is an abstract class to support
    PointBasedSpatialObject filters and algorithms. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4___New_orig__)
    Clone = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_Clone)
    AddPoint = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_AddPoint)
    RemovePoint = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_RemovePoint)
    SetPoints = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_SetPoints)
    GetPoints = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_GetPoints)
    GetPoint = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_GetPoint)
    GetNumberOfPoints = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_GetNumberOfPoints)
    ClosestPointInWorldSpace = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_ClosestPointInWorldSpace)
    ClosestPointInObjectSpace = _swig_new_instance_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_ClosestPointInObjectSpace)
    __swig_destroy__ = _itkPointBasedSpatialObjectPython.delete_itkPointBasedSpatialObject4
    cast = _swig_new_static_method(_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_cast)

    def New(*args, **kargs):
        """New() -> itkPointBasedSpatialObject4

        Create a new object of the class itkPointBasedSpatialObject4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPointBasedSpatialObject4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPointBasedSpatialObject4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPointBasedSpatialObject4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPointBasedSpatialObject4 in _itkPointBasedSpatialObjectPython:
_itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_swigregister(itkPointBasedSpatialObject4)
itkPointBasedSpatialObject4___New_orig__ = _itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4___New_orig__
itkPointBasedSpatialObject4_cast = _itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4_cast



