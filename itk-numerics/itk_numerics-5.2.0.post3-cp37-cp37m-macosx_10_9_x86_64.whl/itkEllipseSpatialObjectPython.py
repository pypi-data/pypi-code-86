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
    from . import _itkEllipseSpatialObjectPython
else:
    import _itkEllipseSpatialObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkEllipseSpatialObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkEllipseSpatialObjectPython.SWIG_PyStaticMethod_New

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
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkSpatialObjectBasePython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkSpatialObjectPropertyPython
import itk.itkRGBAPixelPython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkArray2DPython
import itk.itkArrayPython
import itk.itkPointPython
import itk.itkVariableLengthVectorPython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkOptimizerParametersPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkImageRegionPython
class listitkEllipseSpatialObject2_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkEllipseSpatialObject2_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_pop)
    append = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_append)
    empty = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_empty)
    size = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_size)
    swap = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_swap)
    begin = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_begin)
    end = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_end)
    rbegin = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_rend)
    clear = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkEllipseSpatialObject2_Pointer
        __init__(self, other) -> listitkEllipseSpatialObject2_Pointer

        Parameters
        ----------
        other: std::list< itkEllipseSpatialObject2_Pointer > const &

        __init__(self, size) -> listitkEllipseSpatialObject2_Pointer

        Parameters
        ----------
        size: std::list< itkEllipseSpatialObject2_Pointer >::size_type

        __init__(self, size, value) -> listitkEllipseSpatialObject2_Pointer

        Parameters
        ----------
        size: std::list< itkEllipseSpatialObject2_Pointer >::size_type
        value: std::list< itkEllipseSpatialObject2_Pointer >::value_type const &

        """
        _itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_swiginit(self, _itkEllipseSpatialObjectPython.new_listitkEllipseSpatialObject2_Pointer(*args))
    push_back = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_push_back)
    front = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_front)
    back = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_back)
    assign = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_assign)
    resize = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_resize)
    insert = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_reverse)
    __swig_destroy__ = _itkEllipseSpatialObjectPython.delete_listitkEllipseSpatialObject2_Pointer

# Register listitkEllipseSpatialObject2_Pointer in _itkEllipseSpatialObjectPython:
_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject2_Pointer_swigregister(listitkEllipseSpatialObject2_Pointer)

class listitkEllipseSpatialObject3_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkEllipseSpatialObject3_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_pop)
    append = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_append)
    empty = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_empty)
    size = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_size)
    swap = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_swap)
    begin = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_begin)
    end = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_end)
    rbegin = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_rend)
    clear = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkEllipseSpatialObject3_Pointer
        __init__(self, other) -> listitkEllipseSpatialObject3_Pointer

        Parameters
        ----------
        other: std::list< itkEllipseSpatialObject3_Pointer > const &

        __init__(self, size) -> listitkEllipseSpatialObject3_Pointer

        Parameters
        ----------
        size: std::list< itkEllipseSpatialObject3_Pointer >::size_type

        __init__(self, size, value) -> listitkEllipseSpatialObject3_Pointer

        Parameters
        ----------
        size: std::list< itkEllipseSpatialObject3_Pointer >::size_type
        value: std::list< itkEllipseSpatialObject3_Pointer >::value_type const &

        """
        _itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_swiginit(self, _itkEllipseSpatialObjectPython.new_listitkEllipseSpatialObject3_Pointer(*args))
    push_back = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_push_back)
    front = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_front)
    back = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_back)
    assign = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_assign)
    resize = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_resize)
    insert = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_reverse)
    __swig_destroy__ = _itkEllipseSpatialObjectPython.delete_listitkEllipseSpatialObject3_Pointer

# Register listitkEllipseSpatialObject3_Pointer in _itkEllipseSpatialObjectPython:
_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject3_Pointer_swigregister(listitkEllipseSpatialObject3_Pointer)

class listitkEllipseSpatialObject4_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkEllipseSpatialObject4_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_pop)
    append = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_append)
    empty = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_empty)
    size = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_size)
    swap = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_swap)
    begin = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_begin)
    end = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_end)
    rbegin = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_rend)
    clear = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkEllipseSpatialObject4_Pointer
        __init__(self, other) -> listitkEllipseSpatialObject4_Pointer

        Parameters
        ----------
        other: std::list< itkEllipseSpatialObject4_Pointer > const &

        __init__(self, size) -> listitkEllipseSpatialObject4_Pointer

        Parameters
        ----------
        size: std::list< itkEllipseSpatialObject4_Pointer >::size_type

        __init__(self, size, value) -> listitkEllipseSpatialObject4_Pointer

        Parameters
        ----------
        size: std::list< itkEllipseSpatialObject4_Pointer >::size_type
        value: std::list< itkEllipseSpatialObject4_Pointer >::value_type const &

        """
        _itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_swiginit(self, _itkEllipseSpatialObjectPython.new_listitkEllipseSpatialObject4_Pointer(*args))
    push_back = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_push_back)
    front = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_front)
    back = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_back)
    assign = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_assign)
    resize = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_resize)
    insert = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_reverse)
    __swig_destroy__ = _itkEllipseSpatialObjectPython.delete_listitkEllipseSpatialObject4_Pointer

# Register listitkEllipseSpatialObject4_Pointer in _itkEllipseSpatialObjectPython:
_itkEllipseSpatialObjectPython.listitkEllipseSpatialObject4_Pointer_swigregister(listitkEllipseSpatialObject4_Pointer)


def itkEllipseSpatialObject2_New():
    return itkEllipseSpatialObject2.New()

class itkEllipseSpatialObject2(itk.itkSpatialObjectBasePython.itkSpatialObject2):
    r"""


    example{Core/SpatialObjects/Ellipse,Ellipse} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject2___New_orig__)
    Clone = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject2_Clone)
    SetRadiusInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject2_SetRadiusInObjectSpace)
    GetRadiusInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject2_GetRadiusInObjectSpace)
    SetCenterInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject2_SetCenterInObjectSpace)
    GetCenterInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject2_GetCenterInObjectSpace)
    __swig_destroy__ = _itkEllipseSpatialObjectPython.delete_itkEllipseSpatialObject2
    cast = _swig_new_static_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject2_cast)

    def New(*args, **kargs):
        """New() -> itkEllipseSpatialObject2

        Create a new object of the class itkEllipseSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEllipseSpatialObject2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkEllipseSpatialObject2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkEllipseSpatialObject2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEllipseSpatialObject2 in _itkEllipseSpatialObjectPython:
_itkEllipseSpatialObjectPython.itkEllipseSpatialObject2_swigregister(itkEllipseSpatialObject2)
itkEllipseSpatialObject2___New_orig__ = _itkEllipseSpatialObjectPython.itkEllipseSpatialObject2___New_orig__
itkEllipseSpatialObject2_cast = _itkEllipseSpatialObjectPython.itkEllipseSpatialObject2_cast


def itkEllipseSpatialObject3_New():
    return itkEllipseSpatialObject3.New()

class itkEllipseSpatialObject3(itk.itkSpatialObjectBasePython.itkSpatialObject3):
    r"""


    example{Core/SpatialObjects/Ellipse,Ellipse} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject3___New_orig__)
    Clone = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject3_Clone)
    SetRadiusInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject3_SetRadiusInObjectSpace)
    GetRadiusInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject3_GetRadiusInObjectSpace)
    SetCenterInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject3_SetCenterInObjectSpace)
    GetCenterInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject3_GetCenterInObjectSpace)
    __swig_destroy__ = _itkEllipseSpatialObjectPython.delete_itkEllipseSpatialObject3
    cast = _swig_new_static_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject3_cast)

    def New(*args, **kargs):
        """New() -> itkEllipseSpatialObject3

        Create a new object of the class itkEllipseSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEllipseSpatialObject3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkEllipseSpatialObject3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkEllipseSpatialObject3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEllipseSpatialObject3 in _itkEllipseSpatialObjectPython:
_itkEllipseSpatialObjectPython.itkEllipseSpatialObject3_swigregister(itkEllipseSpatialObject3)
itkEllipseSpatialObject3___New_orig__ = _itkEllipseSpatialObjectPython.itkEllipseSpatialObject3___New_orig__
itkEllipseSpatialObject3_cast = _itkEllipseSpatialObjectPython.itkEllipseSpatialObject3_cast


def itkEllipseSpatialObject4_New():
    return itkEllipseSpatialObject4.New()

class itkEllipseSpatialObject4(itk.itkSpatialObjectBasePython.itkSpatialObject4):
    r"""


    example{Core/SpatialObjects/Ellipse,Ellipse} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject4___New_orig__)
    Clone = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject4_Clone)
    SetRadiusInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject4_SetRadiusInObjectSpace)
    GetRadiusInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject4_GetRadiusInObjectSpace)
    SetCenterInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject4_SetCenterInObjectSpace)
    GetCenterInObjectSpace = _swig_new_instance_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject4_GetCenterInObjectSpace)
    __swig_destroy__ = _itkEllipseSpatialObjectPython.delete_itkEllipseSpatialObject4
    cast = _swig_new_static_method(_itkEllipseSpatialObjectPython.itkEllipseSpatialObject4_cast)

    def New(*args, **kargs):
        """New() -> itkEllipseSpatialObject4

        Create a new object of the class itkEllipseSpatialObject4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEllipseSpatialObject4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkEllipseSpatialObject4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkEllipseSpatialObject4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEllipseSpatialObject4 in _itkEllipseSpatialObjectPython:
_itkEllipseSpatialObjectPython.itkEllipseSpatialObject4_swigregister(itkEllipseSpatialObject4)
itkEllipseSpatialObject4___New_orig__ = _itkEllipseSpatialObjectPython.itkEllipseSpatialObject4___New_orig__
itkEllipseSpatialObject4_cast = _itkEllipseSpatialObjectPython.itkEllipseSpatialObject4_cast



