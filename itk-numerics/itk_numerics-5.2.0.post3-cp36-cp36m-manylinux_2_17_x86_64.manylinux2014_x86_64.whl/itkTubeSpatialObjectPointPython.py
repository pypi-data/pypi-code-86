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
    from . import _itkTubeSpatialObjectPointPython
else:
    import _itkTubeSpatialObjectPointPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTubeSpatialObjectPointPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTubeSpatialObjectPointPython.SWIG_PyStaticMethod_New

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
import itk.itkCovariantVectorPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.ITKCommonBasePython
import itk.itkSpatialObjectPointPython
import itk.itkPointPython
import itk.itkSpatialObjectBasePython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkVectorContainerPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSpatialObjectPropertyPython
import itk.itkRGBAPixelPython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkVariableLengthVectorPython
import itk.itkArrayPython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkOptimizerParametersPython
import itk.itkArray2DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkImageRegionPython
class vectoritkTubeSpatialObjectPoint2(collections.abc.MutableSequence):
    r"""Proxy of C++ std::vector< itkTubeSpatialObjectPoint2 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2___nonzero__)
    __bool__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2___bool__)
    __len__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2___len__)
    __getslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2___getslice__)
    __setslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2___setslice__)
    __delslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2___delslice__)
    __delitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2___delitem__)
    __getitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2___getitem__)
    __setitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2___setitem__)
    pop = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_pop)
    append = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_append)
    empty = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_empty)
    size = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_size)
    swap = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_swap)
    begin = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_begin)
    end = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_end)
    rbegin = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_rbegin)
    rend = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_rend)
    clear = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_clear)
    get_allocator = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_get_allocator)
    pop_back = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_pop_back)
    erase = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> vectoritkTubeSpatialObjectPoint2
        __init__(self, other) -> vectoritkTubeSpatialObjectPoint2

        Parameters
        ----------
        other: std::vector< itkTubeSpatialObjectPoint2 > const &

        __init__(self, size) -> vectoritkTubeSpatialObjectPoint2

        Parameters
        ----------
        size: std::vector< itkTubeSpatialObjectPoint2 >::size_type

        __init__(self, size, value) -> vectoritkTubeSpatialObjectPoint2

        Parameters
        ----------
        size: std::vector< itkTubeSpatialObjectPoint2 >::size_type
        value: std::vector< itkTubeSpatialObjectPoint2 >::value_type const &

        """
        _itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_swiginit(self, _itkTubeSpatialObjectPointPython.new_vectoritkTubeSpatialObjectPoint2(*args))
    push_back = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_push_back)
    front = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_front)
    back = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_back)
    assign = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_assign)
    resize = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_resize)
    insert = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_insert)
    reserve = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_reserve)
    capacity = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_capacity)
    __swig_destroy__ = _itkTubeSpatialObjectPointPython.delete_vectoritkTubeSpatialObjectPoint2

# Register vectoritkTubeSpatialObjectPoint2 in _itkTubeSpatialObjectPointPython:
_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint2_swigregister(vectoritkTubeSpatialObjectPoint2)

class vectoritkTubeSpatialObjectPoint3(collections.abc.MutableSequence):
    r"""Proxy of C++ std::vector< itkTubeSpatialObjectPoint3 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3___nonzero__)
    __bool__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3___bool__)
    __len__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3___len__)
    __getslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3___getslice__)
    __setslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3___setslice__)
    __delslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3___delslice__)
    __delitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3___delitem__)
    __getitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3___getitem__)
    __setitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3___setitem__)
    pop = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_pop)
    append = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_append)
    empty = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_empty)
    size = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_size)
    swap = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_swap)
    begin = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_begin)
    end = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_end)
    rbegin = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_rbegin)
    rend = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_rend)
    clear = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_clear)
    get_allocator = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_get_allocator)
    pop_back = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_pop_back)
    erase = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> vectoritkTubeSpatialObjectPoint3
        __init__(self, other) -> vectoritkTubeSpatialObjectPoint3

        Parameters
        ----------
        other: std::vector< itkTubeSpatialObjectPoint3 > const &

        __init__(self, size) -> vectoritkTubeSpatialObjectPoint3

        Parameters
        ----------
        size: std::vector< itkTubeSpatialObjectPoint3 >::size_type

        __init__(self, size, value) -> vectoritkTubeSpatialObjectPoint3

        Parameters
        ----------
        size: std::vector< itkTubeSpatialObjectPoint3 >::size_type
        value: std::vector< itkTubeSpatialObjectPoint3 >::value_type const &

        """
        _itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_swiginit(self, _itkTubeSpatialObjectPointPython.new_vectoritkTubeSpatialObjectPoint3(*args))
    push_back = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_push_back)
    front = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_front)
    back = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_back)
    assign = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_assign)
    resize = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_resize)
    insert = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_insert)
    reserve = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_reserve)
    capacity = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_capacity)
    __swig_destroy__ = _itkTubeSpatialObjectPointPython.delete_vectoritkTubeSpatialObjectPoint3

# Register vectoritkTubeSpatialObjectPoint3 in _itkTubeSpatialObjectPointPython:
_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint3_swigregister(vectoritkTubeSpatialObjectPoint3)

class vectoritkTubeSpatialObjectPoint4(collections.abc.MutableSequence):
    r"""Proxy of C++ std::vector< itkTubeSpatialObjectPoint4 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4___nonzero__)
    __bool__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4___bool__)
    __len__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4___len__)
    __getslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4___getslice__)
    __setslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4___setslice__)
    __delslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4___delslice__)
    __delitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4___delitem__)
    __getitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4___getitem__)
    __setitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4___setitem__)
    pop = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_pop)
    append = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_append)
    empty = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_empty)
    size = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_size)
    swap = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_swap)
    begin = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_begin)
    end = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_end)
    rbegin = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_rbegin)
    rend = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_rend)
    clear = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_clear)
    get_allocator = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_get_allocator)
    pop_back = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_pop_back)
    erase = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> vectoritkTubeSpatialObjectPoint4
        __init__(self, other) -> vectoritkTubeSpatialObjectPoint4

        Parameters
        ----------
        other: std::vector< itkTubeSpatialObjectPoint4 > const &

        __init__(self, size) -> vectoritkTubeSpatialObjectPoint4

        Parameters
        ----------
        size: std::vector< itkTubeSpatialObjectPoint4 >::size_type

        __init__(self, size, value) -> vectoritkTubeSpatialObjectPoint4

        Parameters
        ----------
        size: std::vector< itkTubeSpatialObjectPoint4 >::size_type
        value: std::vector< itkTubeSpatialObjectPoint4 >::value_type const &

        """
        _itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_swiginit(self, _itkTubeSpatialObjectPointPython.new_vectoritkTubeSpatialObjectPoint4(*args))
    push_back = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_push_back)
    front = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_front)
    back = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_back)
    assign = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_assign)
    resize = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_resize)
    insert = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_insert)
    reserve = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_reserve)
    capacity = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_capacity)
    __swig_destroy__ = _itkTubeSpatialObjectPointPython.delete_vectoritkTubeSpatialObjectPoint4

# Register vectoritkTubeSpatialObjectPoint4 in _itkTubeSpatialObjectPointPython:
_itkTubeSpatialObjectPointPython.vectoritkTubeSpatialObjectPoint4_swigregister(vectoritkTubeSpatialObjectPoint4)

class itkTubeSpatialObjectPoint2(itk.itkSpatialObjectPointPython.itkSpatialObjectPoint2):
    r"""


    Point used for a tube definition.

    This class contains all the functions necessary to define a point that
    can be used to build tubes.

    See:   TubeSpatialObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkTubeSpatialObjectPoint2
        __init__(self, other) -> itkTubeSpatialObjectPoint2

        Parameters
        ----------
        other: itkTubeSpatialObjectPoint2 const &



        Point used for a tube definition.

        This class contains all the functions necessary to define a point that
        can be used to build tubes.

        See:   TubeSpatialObject 
        """
        _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_swiginit(self, _itkTubeSpatialObjectPointPython.new_itkTubeSpatialObjectPoint2(*args))
    __swig_destroy__ = _itkTubeSpatialObjectPointPython.delete_itkTubeSpatialObjectPoint2
    GetRadiusInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetRadiusInObjectSpace)
    GetRadiusInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetRadiusInWorldSpace)
    SetRadiusInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetRadiusInObjectSpace)
    SetRadiusInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetRadiusInWorldSpace)
    GetTangentInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetTangentInObjectSpace)
    GetTangentInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetTangentInWorldSpace)
    SetTangentInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetTangentInObjectSpace)
    SetTangentInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetTangentInWorldSpace)
    GetNormal1InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetNormal1InObjectSpace)
    GetNormal1InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetNormal1InWorldSpace)
    SetNormal1InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetNormal1InObjectSpace)
    SetNormal1InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetNormal1InWorldSpace)
    GetNormal2InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetNormal2InObjectSpace)
    GetNormal2InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetNormal2InWorldSpace)
    SetNormal2InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetNormal2InObjectSpace)
    SetNormal2InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetNormal2InWorldSpace)
    SetRidgeness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetRidgeness)
    GetRidgeness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetRidgeness)
    SetCurvature = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetCurvature)
    GetCurvature = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetCurvature)
    SetLevelness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetLevelness)
    GetLevelness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetLevelness)
    SetRoundness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetRoundness)
    GetRoundness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetRoundness)
    SetIntensity = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetIntensity)
    GetIntensity = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetIntensity)
    SetMedialness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetMedialness)
    GetMedialness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetMedialness)
    SetBranchness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetBranchness)
    GetBranchness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetBranchness)
    SetAlpha1 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetAlpha2)
    SetAlpha3 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_SetAlpha3)
    GetAlpha3 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_GetAlpha3)

# Register itkTubeSpatialObjectPoint2 in _itkTubeSpatialObjectPointPython:
_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint2_swigregister(itkTubeSpatialObjectPoint2)

class itkTubeSpatialObjectPoint3(itk.itkSpatialObjectPointPython.itkSpatialObjectPoint3):
    r"""


    Point used for a tube definition.

    This class contains all the functions necessary to define a point that
    can be used to build tubes.

    See:   TubeSpatialObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkTubeSpatialObjectPoint3
        __init__(self, other) -> itkTubeSpatialObjectPoint3

        Parameters
        ----------
        other: itkTubeSpatialObjectPoint3 const &



        Point used for a tube definition.

        This class contains all the functions necessary to define a point that
        can be used to build tubes.

        See:   TubeSpatialObject 
        """
        _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_swiginit(self, _itkTubeSpatialObjectPointPython.new_itkTubeSpatialObjectPoint3(*args))
    __swig_destroy__ = _itkTubeSpatialObjectPointPython.delete_itkTubeSpatialObjectPoint3
    GetRadiusInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetRadiusInObjectSpace)
    GetRadiusInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetRadiusInWorldSpace)
    SetRadiusInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetRadiusInObjectSpace)
    SetRadiusInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetRadiusInWorldSpace)
    GetTangentInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetTangentInObjectSpace)
    GetTangentInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetTangentInWorldSpace)
    SetTangentInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetTangentInObjectSpace)
    SetTangentInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetTangentInWorldSpace)
    GetNormal1InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetNormal1InObjectSpace)
    GetNormal1InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetNormal1InWorldSpace)
    SetNormal1InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetNormal1InObjectSpace)
    SetNormal1InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetNormal1InWorldSpace)
    GetNormal2InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetNormal2InObjectSpace)
    GetNormal2InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetNormal2InWorldSpace)
    SetNormal2InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetNormal2InObjectSpace)
    SetNormal2InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetNormal2InWorldSpace)
    SetRidgeness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetRidgeness)
    GetRidgeness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetRidgeness)
    SetCurvature = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetCurvature)
    GetCurvature = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetCurvature)
    SetLevelness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetLevelness)
    GetLevelness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetLevelness)
    SetRoundness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetRoundness)
    GetRoundness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetRoundness)
    SetIntensity = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetIntensity)
    GetIntensity = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetIntensity)
    SetMedialness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetMedialness)
    GetMedialness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetMedialness)
    SetBranchness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetBranchness)
    GetBranchness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetBranchness)
    SetAlpha1 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetAlpha2)
    SetAlpha3 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_SetAlpha3)
    GetAlpha3 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_GetAlpha3)

# Register itkTubeSpatialObjectPoint3 in _itkTubeSpatialObjectPointPython:
_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3_swigregister(itkTubeSpatialObjectPoint3)

class itkTubeSpatialObjectPoint4(itk.itkSpatialObjectPointPython.itkSpatialObjectPoint4):
    r"""


    Point used for a tube definition.

    This class contains all the functions necessary to define a point that
    can be used to build tubes.

    See:   TubeSpatialObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkTubeSpatialObjectPoint4
        __init__(self, other) -> itkTubeSpatialObjectPoint4

        Parameters
        ----------
        other: itkTubeSpatialObjectPoint4 const &



        Point used for a tube definition.

        This class contains all the functions necessary to define a point that
        can be used to build tubes.

        See:   TubeSpatialObject 
        """
        _itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_swiginit(self, _itkTubeSpatialObjectPointPython.new_itkTubeSpatialObjectPoint4(*args))
    __swig_destroy__ = _itkTubeSpatialObjectPointPython.delete_itkTubeSpatialObjectPoint4
    GetRadiusInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetRadiusInObjectSpace)
    GetRadiusInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetRadiusInWorldSpace)
    SetRadiusInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetRadiusInObjectSpace)
    SetRadiusInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetRadiusInWorldSpace)
    GetTangentInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetTangentInObjectSpace)
    GetTangentInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetTangentInWorldSpace)
    SetTangentInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetTangentInObjectSpace)
    SetTangentInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetTangentInWorldSpace)
    GetNormal1InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetNormal1InObjectSpace)
    GetNormal1InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetNormal1InWorldSpace)
    SetNormal1InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetNormal1InObjectSpace)
    SetNormal1InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetNormal1InWorldSpace)
    GetNormal2InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetNormal2InObjectSpace)
    GetNormal2InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetNormal2InWorldSpace)
    SetNormal2InObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetNormal2InObjectSpace)
    SetNormal2InWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetNormal2InWorldSpace)
    SetRidgeness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetRidgeness)
    GetRidgeness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetRidgeness)
    SetCurvature = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetCurvature)
    GetCurvature = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetCurvature)
    SetLevelness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetLevelness)
    GetLevelness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetLevelness)
    SetRoundness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetRoundness)
    GetRoundness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetRoundness)
    SetIntensity = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetIntensity)
    GetIntensity = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetIntensity)
    SetMedialness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetMedialness)
    GetMedialness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetMedialness)
    SetBranchness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetBranchness)
    GetBranchness = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetBranchness)
    SetAlpha1 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetAlpha2)
    SetAlpha3 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_SetAlpha3)
    GetAlpha3 = _swig_new_instance_method(_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_GetAlpha3)

# Register itkTubeSpatialObjectPoint4 in _itkTubeSpatialObjectPointPython:
_itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint4_swigregister(itkTubeSpatialObjectPoint4)



