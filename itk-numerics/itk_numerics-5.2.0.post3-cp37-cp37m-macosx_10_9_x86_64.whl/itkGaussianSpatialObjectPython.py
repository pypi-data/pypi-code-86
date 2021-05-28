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
    from . import _itkGaussianSpatialObjectPython
else:
    import _itkGaussianSpatialObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGaussianSpatialObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGaussianSpatialObjectPython.SWIG_PyStaticMethod_New

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
import itk.itkEllipseSpatialObjectPython
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
class listitkGaussianSpatialObject2_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkGaussianSpatialObject2_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_pop)
    append = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_append)
    empty = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_empty)
    size = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_size)
    swap = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_swap)
    begin = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_begin)
    end = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_end)
    rbegin = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_rend)
    clear = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkGaussianSpatialObject2_Pointer
        __init__(self, other) -> listitkGaussianSpatialObject2_Pointer

        Parameters
        ----------
        other: std::list< itkGaussianSpatialObject2_Pointer > const &

        __init__(self, size) -> listitkGaussianSpatialObject2_Pointer

        Parameters
        ----------
        size: std::list< itkGaussianSpatialObject2_Pointer >::size_type

        __init__(self, size, value) -> listitkGaussianSpatialObject2_Pointer

        Parameters
        ----------
        size: std::list< itkGaussianSpatialObject2_Pointer >::size_type
        value: std::list< itkGaussianSpatialObject2_Pointer >::value_type const &

        """
        _itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_swiginit(self, _itkGaussianSpatialObjectPython.new_listitkGaussianSpatialObject2_Pointer(*args))
    push_back = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_push_back)
    front = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_front)
    back = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_back)
    assign = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_assign)
    resize = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_resize)
    insert = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_reverse)
    __swig_destroy__ = _itkGaussianSpatialObjectPython.delete_listitkGaussianSpatialObject2_Pointer

# Register listitkGaussianSpatialObject2_Pointer in _itkGaussianSpatialObjectPython:
_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject2_Pointer_swigregister(listitkGaussianSpatialObject2_Pointer)

class listitkGaussianSpatialObject3_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkGaussianSpatialObject3_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_pop)
    append = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_append)
    empty = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_empty)
    size = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_size)
    swap = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_swap)
    begin = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_begin)
    end = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_end)
    rbegin = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_rend)
    clear = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkGaussianSpatialObject3_Pointer
        __init__(self, other) -> listitkGaussianSpatialObject3_Pointer

        Parameters
        ----------
        other: std::list< itkGaussianSpatialObject3_Pointer > const &

        __init__(self, size) -> listitkGaussianSpatialObject3_Pointer

        Parameters
        ----------
        size: std::list< itkGaussianSpatialObject3_Pointer >::size_type

        __init__(self, size, value) -> listitkGaussianSpatialObject3_Pointer

        Parameters
        ----------
        size: std::list< itkGaussianSpatialObject3_Pointer >::size_type
        value: std::list< itkGaussianSpatialObject3_Pointer >::value_type const &

        """
        _itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_swiginit(self, _itkGaussianSpatialObjectPython.new_listitkGaussianSpatialObject3_Pointer(*args))
    push_back = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_push_back)
    front = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_front)
    back = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_back)
    assign = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_assign)
    resize = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_resize)
    insert = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_reverse)
    __swig_destroy__ = _itkGaussianSpatialObjectPython.delete_listitkGaussianSpatialObject3_Pointer

# Register listitkGaussianSpatialObject3_Pointer in _itkGaussianSpatialObjectPython:
_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject3_Pointer_swigregister(listitkGaussianSpatialObject3_Pointer)

class listitkGaussianSpatialObject4_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkGaussianSpatialObject4_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_pop)
    append = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_append)
    empty = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_empty)
    size = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_size)
    swap = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_swap)
    begin = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_begin)
    end = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_end)
    rbegin = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_rend)
    clear = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkGaussianSpatialObject4_Pointer
        __init__(self, other) -> listitkGaussianSpatialObject4_Pointer

        Parameters
        ----------
        other: std::list< itkGaussianSpatialObject4_Pointer > const &

        __init__(self, size) -> listitkGaussianSpatialObject4_Pointer

        Parameters
        ----------
        size: std::list< itkGaussianSpatialObject4_Pointer >::size_type

        __init__(self, size, value) -> listitkGaussianSpatialObject4_Pointer

        Parameters
        ----------
        size: std::list< itkGaussianSpatialObject4_Pointer >::size_type
        value: std::list< itkGaussianSpatialObject4_Pointer >::value_type const &

        """
        _itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_swiginit(self, _itkGaussianSpatialObjectPython.new_listitkGaussianSpatialObject4_Pointer(*args))
    push_back = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_push_back)
    front = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_front)
    back = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_back)
    assign = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_assign)
    resize = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_resize)
    insert = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_reverse)
    __swig_destroy__ = _itkGaussianSpatialObjectPython.delete_listitkGaussianSpatialObject4_Pointer

# Register listitkGaussianSpatialObject4_Pointer in _itkGaussianSpatialObjectPython:
_itkGaussianSpatialObjectPython.listitkGaussianSpatialObject4_Pointer_swigregister(listitkGaussianSpatialObject4_Pointer)


def itkGaussianSpatialObject2_New():
    return itkGaussianSpatialObject2.New()

class itkGaussianSpatialObject2(itk.itkSpatialObjectBasePython.itkSpatialObject2):
    r"""


    Represents a multivariate Gaussian function.

    The Gaussian function G(x) is given by \\[ G(\\vec{x}) = m
    e^{-\\|\\S^{-1} \\vec{x}\\|^2 / 2}, \\] where m is a scaling
    factor set by SetMaximum(), and $\\S$ is the (invertible) matrix
    associated to the IndexToObjectTransform of the object multiplied by
    the Sigma parameter. If $\\S$ is symmetric and positive definite,
    and m is chosen so that the integral of G(x) is 1, then G will denote
    a normal distribution with mean 0 and covariance matrix $\\S
    \\times Sigma$. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_Clone)
    SetRadiusInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_SetRadiusInObjectSpace)
    GetRadiusInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_GetRadiusInObjectSpace)
    SetSigmaInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_SetSigmaInObjectSpace)
    GetSigmaInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_GetSigmaInObjectSpace)
    SetCenterInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_SetCenterInObjectSpace)
    GetCenterInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_GetCenterInObjectSpace)
    SetMaximum = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_SetMaximum)
    GetMaximum = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_GetMaximum)
    SquaredZScoreInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_SquaredZScoreInObjectSpace)
    SquaredZScoreInWorldSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_SquaredZScoreInWorldSpace)
    ValueAtInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_ValueAtInObjectSpace)
    GetEllipsoid = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_GetEllipsoid)
    __swig_destroy__ = _itkGaussianSpatialObjectPython.delete_itkGaussianSpatialObject2
    cast = _swig_new_static_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianSpatialObject2

        Create a new object of the class itkGaussianSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSpatialObject2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianSpatialObject2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianSpatialObject2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianSpatialObject2 in _itkGaussianSpatialObjectPython:
_itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_swigregister(itkGaussianSpatialObject2)
itkGaussianSpatialObject2___New_orig__ = _itkGaussianSpatialObjectPython.itkGaussianSpatialObject2___New_orig__
itkGaussianSpatialObject2_cast = _itkGaussianSpatialObjectPython.itkGaussianSpatialObject2_cast


def itkGaussianSpatialObject3_New():
    return itkGaussianSpatialObject3.New()

class itkGaussianSpatialObject3(itk.itkSpatialObjectBasePython.itkSpatialObject3):
    r"""


    Represents a multivariate Gaussian function.

    The Gaussian function G(x) is given by \\[ G(\\vec{x}) = m
    e^{-\\|\\S^{-1} \\vec{x}\\|^2 / 2}, \\] where m is a scaling
    factor set by SetMaximum(), and $\\S$ is the (invertible) matrix
    associated to the IndexToObjectTransform of the object multiplied by
    the Sigma parameter. If $\\S$ is symmetric and positive definite,
    and m is chosen so that the integral of G(x) is 1, then G will denote
    a normal distribution with mean 0 and covariance matrix $\\S
    \\times Sigma$. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_Clone)
    SetRadiusInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_SetRadiusInObjectSpace)
    GetRadiusInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_GetRadiusInObjectSpace)
    SetSigmaInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_SetSigmaInObjectSpace)
    GetSigmaInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_GetSigmaInObjectSpace)
    SetCenterInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_SetCenterInObjectSpace)
    GetCenterInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_GetCenterInObjectSpace)
    SetMaximum = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_SetMaximum)
    GetMaximum = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_GetMaximum)
    SquaredZScoreInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_SquaredZScoreInObjectSpace)
    SquaredZScoreInWorldSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_SquaredZScoreInWorldSpace)
    ValueAtInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_ValueAtInObjectSpace)
    GetEllipsoid = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_GetEllipsoid)
    __swig_destroy__ = _itkGaussianSpatialObjectPython.delete_itkGaussianSpatialObject3
    cast = _swig_new_static_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianSpatialObject3

        Create a new object of the class itkGaussianSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSpatialObject3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianSpatialObject3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianSpatialObject3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianSpatialObject3 in _itkGaussianSpatialObjectPython:
_itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_swigregister(itkGaussianSpatialObject3)
itkGaussianSpatialObject3___New_orig__ = _itkGaussianSpatialObjectPython.itkGaussianSpatialObject3___New_orig__
itkGaussianSpatialObject3_cast = _itkGaussianSpatialObjectPython.itkGaussianSpatialObject3_cast


def itkGaussianSpatialObject4_New():
    return itkGaussianSpatialObject4.New()

class itkGaussianSpatialObject4(itk.itkSpatialObjectBasePython.itkSpatialObject4):
    r"""


    Represents a multivariate Gaussian function.

    The Gaussian function G(x) is given by \\[ G(\\vec{x}) = m
    e^{-\\|\\S^{-1} \\vec{x}\\|^2 / 2}, \\] where m is a scaling
    factor set by SetMaximum(), and $\\S$ is the (invertible) matrix
    associated to the IndexToObjectTransform of the object multiplied by
    the Sigma parameter. If $\\S$ is symmetric and positive definite,
    and m is chosen so that the integral of G(x) is 1, then G will denote
    a normal distribution with mean 0 and covariance matrix $\\S
    \\times Sigma$. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_Clone)
    SetRadiusInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_SetRadiusInObjectSpace)
    GetRadiusInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_GetRadiusInObjectSpace)
    SetSigmaInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_SetSigmaInObjectSpace)
    GetSigmaInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_GetSigmaInObjectSpace)
    SetCenterInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_SetCenterInObjectSpace)
    GetCenterInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_GetCenterInObjectSpace)
    SetMaximum = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_SetMaximum)
    GetMaximum = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_GetMaximum)
    SquaredZScoreInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_SquaredZScoreInObjectSpace)
    SquaredZScoreInWorldSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_SquaredZScoreInWorldSpace)
    ValueAtInObjectSpace = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_ValueAtInObjectSpace)
    GetEllipsoid = _swig_new_instance_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_GetEllipsoid)
    __swig_destroy__ = _itkGaussianSpatialObjectPython.delete_itkGaussianSpatialObject4
    cast = _swig_new_static_method(_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianSpatialObject4

        Create a new object of the class itkGaussianSpatialObject4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSpatialObject4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianSpatialObject4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianSpatialObject4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianSpatialObject4 in _itkGaussianSpatialObjectPython:
_itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_swigregister(itkGaussianSpatialObject4)
itkGaussianSpatialObject4___New_orig__ = _itkGaussianSpatialObjectPython.itkGaussianSpatialObject4___New_orig__
itkGaussianSpatialObject4_cast = _itkGaussianSpatialObjectPython.itkGaussianSpatialObject4_cast



