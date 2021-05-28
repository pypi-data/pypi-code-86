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
    from . import _itkImageMaskSpatialObjectPython
else:
    import _itkImageMaskSpatialObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkImageMaskSpatialObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkImageMaskSpatialObjectPython.SWIG_PyStaticMethod_New

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
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkImageSpatialObjectPython
import itk.itkInterpolateImageFunctionPython
import itk.itkSizePython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkImageFunctionBasePython
import itk.itkImagePython
import itk.itkImageRegionPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBPixelPython
import itk.itkFunctionBasePython
import itk.itkArrayPython
import itk.itkSpatialObjectBasePython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkOptimizerParametersPython
import itk.itkVariableLengthVectorPython
import itk.itkArray2DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkBoundingBoxPython
import itk.itkVectorContainerPython
import itk.itkMapContainerPython
import itk.itkSpatialObjectPropertyPython
class listitkImageMaskSpatialObject2_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkImageMaskSpatialObject2_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_pop)
    append = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_append)
    empty = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_empty)
    size = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_size)
    swap = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_swap)
    begin = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_begin)
    end = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_end)
    rbegin = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_rend)
    clear = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkImageMaskSpatialObject2_Pointer
        __init__(self, other) -> listitkImageMaskSpatialObject2_Pointer

        Parameters
        ----------
        other: std::list< itkImageMaskSpatialObject2_Pointer > const &

        __init__(self, size) -> listitkImageMaskSpatialObject2_Pointer

        Parameters
        ----------
        size: std::list< itkImageMaskSpatialObject2_Pointer >::size_type

        __init__(self, size, value) -> listitkImageMaskSpatialObject2_Pointer

        Parameters
        ----------
        size: std::list< itkImageMaskSpatialObject2_Pointer >::size_type
        value: std::list< itkImageMaskSpatialObject2_Pointer >::value_type const &

        """
        _itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_swiginit(self, _itkImageMaskSpatialObjectPython.new_listitkImageMaskSpatialObject2_Pointer(*args))
    push_back = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_push_back)
    front = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_front)
    back = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_back)
    assign = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_assign)
    resize = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_resize)
    insert = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_reverse)
    __swig_destroy__ = _itkImageMaskSpatialObjectPython.delete_listitkImageMaskSpatialObject2_Pointer

# Register listitkImageMaskSpatialObject2_Pointer in _itkImageMaskSpatialObjectPython:
_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject2_Pointer_swigregister(listitkImageMaskSpatialObject2_Pointer)

class listitkImageMaskSpatialObject3_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkImageMaskSpatialObject3_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_pop)
    append = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_append)
    empty = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_empty)
    size = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_size)
    swap = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_swap)
    begin = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_begin)
    end = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_end)
    rbegin = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_rend)
    clear = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkImageMaskSpatialObject3_Pointer
        __init__(self, other) -> listitkImageMaskSpatialObject3_Pointer

        Parameters
        ----------
        other: std::list< itkImageMaskSpatialObject3_Pointer > const &

        __init__(self, size) -> listitkImageMaskSpatialObject3_Pointer

        Parameters
        ----------
        size: std::list< itkImageMaskSpatialObject3_Pointer >::size_type

        __init__(self, size, value) -> listitkImageMaskSpatialObject3_Pointer

        Parameters
        ----------
        size: std::list< itkImageMaskSpatialObject3_Pointer >::size_type
        value: std::list< itkImageMaskSpatialObject3_Pointer >::value_type const &

        """
        _itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_swiginit(self, _itkImageMaskSpatialObjectPython.new_listitkImageMaskSpatialObject3_Pointer(*args))
    push_back = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_push_back)
    front = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_front)
    back = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_back)
    assign = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_assign)
    resize = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_resize)
    insert = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_reverse)
    __swig_destroy__ = _itkImageMaskSpatialObjectPython.delete_listitkImageMaskSpatialObject3_Pointer

# Register listitkImageMaskSpatialObject3_Pointer in _itkImageMaskSpatialObjectPython:
_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject3_Pointer_swigregister(listitkImageMaskSpatialObject3_Pointer)

class listitkImageMaskSpatialObject4_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkImageMaskSpatialObject4_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_pop)
    append = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_append)
    empty = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_empty)
    size = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_size)
    swap = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_swap)
    begin = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_begin)
    end = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_end)
    rbegin = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_rend)
    clear = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkImageMaskSpatialObject4_Pointer
        __init__(self, other) -> listitkImageMaskSpatialObject4_Pointer

        Parameters
        ----------
        other: std::list< itkImageMaskSpatialObject4_Pointer > const &

        __init__(self, size) -> listitkImageMaskSpatialObject4_Pointer

        Parameters
        ----------
        size: std::list< itkImageMaskSpatialObject4_Pointer >::size_type

        __init__(self, size, value) -> listitkImageMaskSpatialObject4_Pointer

        Parameters
        ----------
        size: std::list< itkImageMaskSpatialObject4_Pointer >::size_type
        value: std::list< itkImageMaskSpatialObject4_Pointer >::value_type const &

        """
        _itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_swiginit(self, _itkImageMaskSpatialObjectPython.new_listitkImageMaskSpatialObject4_Pointer(*args))
    push_back = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_push_back)
    front = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_front)
    back = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_back)
    assign = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_assign)
    resize = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_resize)
    insert = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_reverse)
    __swig_destroy__ = _itkImageMaskSpatialObjectPython.delete_listitkImageMaskSpatialObject4_Pointer

# Register listitkImageMaskSpatialObject4_Pointer in _itkImageMaskSpatialObjectPython:
_itkImageMaskSpatialObjectPython.listitkImageMaskSpatialObject4_Pointer_swigregister(listitkImageMaskSpatialObject4_Pointer)


def itkImageMaskSpatialObject2_New():
    return itkImageMaskSpatialObject2.New()

class itkImageMaskSpatialObject2(itk.itkImageSpatialObjectPython.itkImageSpatialObject2UC):
    r"""


    Implementation of an image mask as spatial object.

    This class derives from the ImageSpatialObject and overloads the
    IsInsideInObjectSpace() method. One of the common uses of this class
    is to serve as Mask for the Image Registration Metrics.

    The bounding box of an image mask is defined in such a way that any
    point whose nearest pixel has a non-zero value is inside the bounding
    box. When all the pixels of an image are zero, the bounding box of the
    image mask is empty, and its bounds are all zero.

    See:   ImageSpatialObject SpatialObject CompositeSpatialObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject2___New_orig__)
    Clone = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject2_Clone)
    ComputeMyBoundingBoxInIndexSpace = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject2_ComputeMyBoundingBoxInIndexSpace)
    __swig_destroy__ = _itkImageMaskSpatialObjectPython.delete_itkImageMaskSpatialObject2
    cast = _swig_new_static_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject2_cast)

    def New(*args, **kargs):
        """New() -> itkImageMaskSpatialObject2

        Create a new object of the class itkImageMaskSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageMaskSpatialObject2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageMaskSpatialObject2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageMaskSpatialObject2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageMaskSpatialObject2 in _itkImageMaskSpatialObjectPython:
_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject2_swigregister(itkImageMaskSpatialObject2)
itkImageMaskSpatialObject2___New_orig__ = _itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject2___New_orig__
itkImageMaskSpatialObject2_cast = _itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject2_cast


def itkImageMaskSpatialObject3_New():
    return itkImageMaskSpatialObject3.New()

class itkImageMaskSpatialObject3(itk.itkImageSpatialObjectPython.itkImageSpatialObject3UC):
    r"""


    Implementation of an image mask as spatial object.

    This class derives from the ImageSpatialObject and overloads the
    IsInsideInObjectSpace() method. One of the common uses of this class
    is to serve as Mask for the Image Registration Metrics.

    The bounding box of an image mask is defined in such a way that any
    point whose nearest pixel has a non-zero value is inside the bounding
    box. When all the pixels of an image are zero, the bounding box of the
    image mask is empty, and its bounds are all zero.

    See:   ImageSpatialObject SpatialObject CompositeSpatialObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject3___New_orig__)
    Clone = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject3_Clone)
    ComputeMyBoundingBoxInIndexSpace = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject3_ComputeMyBoundingBoxInIndexSpace)
    __swig_destroy__ = _itkImageMaskSpatialObjectPython.delete_itkImageMaskSpatialObject3
    cast = _swig_new_static_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject3_cast)

    def New(*args, **kargs):
        """New() -> itkImageMaskSpatialObject3

        Create a new object of the class itkImageMaskSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageMaskSpatialObject3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageMaskSpatialObject3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageMaskSpatialObject3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageMaskSpatialObject3 in _itkImageMaskSpatialObjectPython:
_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject3_swigregister(itkImageMaskSpatialObject3)
itkImageMaskSpatialObject3___New_orig__ = _itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject3___New_orig__
itkImageMaskSpatialObject3_cast = _itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject3_cast


def itkImageMaskSpatialObject4_New():
    return itkImageMaskSpatialObject4.New()

class itkImageMaskSpatialObject4(itk.itkImageSpatialObjectPython.itkImageSpatialObject4UC):
    r"""


    Implementation of an image mask as spatial object.

    This class derives from the ImageSpatialObject and overloads the
    IsInsideInObjectSpace() method. One of the common uses of this class
    is to serve as Mask for the Image Registration Metrics.

    The bounding box of an image mask is defined in such a way that any
    point whose nearest pixel has a non-zero value is inside the bounding
    box. When all the pixels of an image are zero, the bounding box of the
    image mask is empty, and its bounds are all zero.

    See:   ImageSpatialObject SpatialObject CompositeSpatialObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject4___New_orig__)
    Clone = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject4_Clone)
    ComputeMyBoundingBoxInIndexSpace = _swig_new_instance_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject4_ComputeMyBoundingBoxInIndexSpace)
    __swig_destroy__ = _itkImageMaskSpatialObjectPython.delete_itkImageMaskSpatialObject4
    cast = _swig_new_static_method(_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject4_cast)

    def New(*args, **kargs):
        """New() -> itkImageMaskSpatialObject4

        Create a new object of the class itkImageMaskSpatialObject4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageMaskSpatialObject4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageMaskSpatialObject4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageMaskSpatialObject4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageMaskSpatialObject4 in _itkImageMaskSpatialObjectPython:
_itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject4_swigregister(itkImageMaskSpatialObject4)
itkImageMaskSpatialObject4___New_orig__ = _itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject4___New_orig__
itkImageMaskSpatialObject4_cast = _itkImageMaskSpatialObjectPython.itkImageMaskSpatialObject4_cast



