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
    from . import _itkSpatialObjectPointPython
else:
    import _itkSpatialObjectPointPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSpatialObjectPointPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSpatialObjectPointPython.SWIG_PyStaticMethod_New

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
import itk.itkPointPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkFixedArrayPython
import itk.itkRGBAPixelPython
import itk.ITKCommonBasePython
import itk.itkSpatialObjectBasePython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSpatialObjectPropertyPython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkVariableLengthVectorPython
import itk.itkArray2DPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.itkDiffusionTensor3DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkBoundingBoxPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkMapContainerPython
class vectoritkSpatialObjectPoint2(collections.abc.MutableSequence):
    r"""Proxy of C++ std::vector< itkSpatialObjectPoint2 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2___nonzero__)
    __bool__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2___bool__)
    __len__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2___len__)
    __getslice__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2___getslice__)
    __setslice__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2___setslice__)
    __delslice__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2___delslice__)
    __delitem__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2___delitem__)
    __getitem__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2___getitem__)
    __setitem__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2___setitem__)
    pop = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_pop)
    append = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_append)
    empty = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_empty)
    size = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_size)
    swap = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_swap)
    begin = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_begin)
    end = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_end)
    rbegin = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_rbegin)
    rend = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_rend)
    clear = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_clear)
    get_allocator = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_get_allocator)
    pop_back = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_pop_back)
    erase = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> vectoritkSpatialObjectPoint2
        __init__(self, other) -> vectoritkSpatialObjectPoint2

        Parameters
        ----------
        other: std::vector< itkSpatialObjectPoint2 > const &

        __init__(self, size) -> vectoritkSpatialObjectPoint2

        Parameters
        ----------
        size: std::vector< itkSpatialObjectPoint2 >::size_type

        __init__(self, size, value) -> vectoritkSpatialObjectPoint2

        Parameters
        ----------
        size: std::vector< itkSpatialObjectPoint2 >::size_type
        value: std::vector< itkSpatialObjectPoint2 >::value_type const &

        """
        _itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_swiginit(self, _itkSpatialObjectPointPython.new_vectoritkSpatialObjectPoint2(*args))
    push_back = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_push_back)
    front = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_front)
    back = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_back)
    assign = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_assign)
    resize = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_resize)
    insert = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_insert)
    reserve = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_reserve)
    capacity = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_capacity)
    __swig_destroy__ = _itkSpatialObjectPointPython.delete_vectoritkSpatialObjectPoint2

# Register vectoritkSpatialObjectPoint2 in _itkSpatialObjectPointPython:
_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint2_swigregister(vectoritkSpatialObjectPoint2)

class vectoritkSpatialObjectPoint3(collections.abc.MutableSequence):
    r"""Proxy of C++ std::vector< itkSpatialObjectPoint3 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3___nonzero__)
    __bool__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3___bool__)
    __len__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3___len__)
    __getslice__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3___getslice__)
    __setslice__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3___setslice__)
    __delslice__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3___delslice__)
    __delitem__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3___delitem__)
    __getitem__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3___getitem__)
    __setitem__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3___setitem__)
    pop = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_pop)
    append = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_append)
    empty = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_empty)
    size = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_size)
    swap = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_swap)
    begin = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_begin)
    end = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_end)
    rbegin = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_rbegin)
    rend = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_rend)
    clear = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_clear)
    get_allocator = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_get_allocator)
    pop_back = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_pop_back)
    erase = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> vectoritkSpatialObjectPoint3
        __init__(self, other) -> vectoritkSpatialObjectPoint3

        Parameters
        ----------
        other: std::vector< itkSpatialObjectPoint3 > const &

        __init__(self, size) -> vectoritkSpatialObjectPoint3

        Parameters
        ----------
        size: std::vector< itkSpatialObjectPoint3 >::size_type

        __init__(self, size, value) -> vectoritkSpatialObjectPoint3

        Parameters
        ----------
        size: std::vector< itkSpatialObjectPoint3 >::size_type
        value: std::vector< itkSpatialObjectPoint3 >::value_type const &

        """
        _itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_swiginit(self, _itkSpatialObjectPointPython.new_vectoritkSpatialObjectPoint3(*args))
    push_back = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_push_back)
    front = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_front)
    back = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_back)
    assign = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_assign)
    resize = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_resize)
    insert = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_insert)
    reserve = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_reserve)
    capacity = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_capacity)
    __swig_destroy__ = _itkSpatialObjectPointPython.delete_vectoritkSpatialObjectPoint3

# Register vectoritkSpatialObjectPoint3 in _itkSpatialObjectPointPython:
_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint3_swigregister(vectoritkSpatialObjectPoint3)

class vectoritkSpatialObjectPoint4(collections.abc.MutableSequence):
    r"""Proxy of C++ std::vector< itkSpatialObjectPoint4 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4___nonzero__)
    __bool__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4___bool__)
    __len__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4___len__)
    __getslice__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4___getslice__)
    __setslice__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4___setslice__)
    __delslice__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4___delslice__)
    __delitem__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4___delitem__)
    __getitem__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4___getitem__)
    __setitem__ = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4___setitem__)
    pop = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_pop)
    append = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_append)
    empty = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_empty)
    size = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_size)
    swap = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_swap)
    begin = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_begin)
    end = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_end)
    rbegin = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_rbegin)
    rend = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_rend)
    clear = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_clear)
    get_allocator = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_get_allocator)
    pop_back = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_pop_back)
    erase = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> vectoritkSpatialObjectPoint4
        __init__(self, other) -> vectoritkSpatialObjectPoint4

        Parameters
        ----------
        other: std::vector< itkSpatialObjectPoint4 > const &

        __init__(self, size) -> vectoritkSpatialObjectPoint4

        Parameters
        ----------
        size: std::vector< itkSpatialObjectPoint4 >::size_type

        __init__(self, size, value) -> vectoritkSpatialObjectPoint4

        Parameters
        ----------
        size: std::vector< itkSpatialObjectPoint4 >::size_type
        value: std::vector< itkSpatialObjectPoint4 >::value_type const &

        """
        _itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_swiginit(self, _itkSpatialObjectPointPython.new_vectoritkSpatialObjectPoint4(*args))
    push_back = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_push_back)
    front = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_front)
    back = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_back)
    assign = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_assign)
    resize = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_resize)
    insert = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_insert)
    reserve = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_reserve)
    capacity = _swig_new_instance_method(_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_capacity)
    __swig_destroy__ = _itkSpatialObjectPointPython.delete_vectoritkSpatialObjectPoint4

# Register vectoritkSpatialObjectPoint4 in _itkSpatialObjectPointPython:
_itkSpatialObjectPointPython.vectoritkSpatialObjectPoint4_swigregister(vectoritkSpatialObjectPoint4)

class itkSpatialObjectPoint2(object):
    r"""


    Point used for spatial objets.

    This class contains all the functions necessary to define a point

    See:   TubeSpatialObjectPoint SurfaceSpatialObjectPoint 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkSpatialObjectPoint2
        __init__(self, other) -> itkSpatialObjectPoint2

        Parameters
        ----------
        other: itkSpatialObjectPoint2 const &



        Point used for spatial objets.

        This class contains all the functions necessary to define a point

        See:   TubeSpatialObjectPoint SurfaceSpatialObjectPoint 
        """
        _itkSpatialObjectPointPython.itkSpatialObjectPoint2_swiginit(self, _itkSpatialObjectPointPython.new_itkSpatialObjectPoint2(*args))
    __swig_destroy__ = _itkSpatialObjectPointPython.delete_itkSpatialObjectPoint2
    GetNameOfClass = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetNameOfClass)
    SetId = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_SetId)
    GetId = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetId)
    SetPositionInObjectSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_SetPositionInObjectSpace)
    GetPositionInObjectSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetPositionInObjectSpace)
    SetSpatialObject = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_SetSpatialObject)
    GetSpatialObject = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetSpatialObject)
    SetPositionInWorldSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_SetPositionInWorldSpace)
    GetPositionInWorldSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetPositionInWorldSpace)
    GetColor = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetColor)
    SetColor = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_SetColor)
    SetRed = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_SetRed)
    GetRed = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetRed)
    SetGreen = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_SetGreen)
    GetGreen = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetGreen)
    SetBlue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_SetBlue)
    GetBlue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetBlue)
    SetAlpha = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetAlpha)
    SetTagScalarValue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_SetTagScalarValue)
    GetTagScalarValue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetTagScalarValue)
    GetTagScalarDictionary = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_GetTagScalarDictionary)
    SetTagScalarDictionary = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_SetTagScalarDictionary)
    Print = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2_Print)
    __str__ = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint2___str__)

# Register itkSpatialObjectPoint2 in _itkSpatialObjectPointPython:
_itkSpatialObjectPointPython.itkSpatialObjectPoint2_swigregister(itkSpatialObjectPoint2)

class itkSpatialObjectPoint3(object):
    r"""


    Point used for spatial objets.

    This class contains all the functions necessary to define a point

    See:   TubeSpatialObjectPoint SurfaceSpatialObjectPoint 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkSpatialObjectPoint3
        __init__(self, other) -> itkSpatialObjectPoint3

        Parameters
        ----------
        other: itkSpatialObjectPoint3 const &



        Point used for spatial objets.

        This class contains all the functions necessary to define a point

        See:   TubeSpatialObjectPoint SurfaceSpatialObjectPoint 
        """
        _itkSpatialObjectPointPython.itkSpatialObjectPoint3_swiginit(self, _itkSpatialObjectPointPython.new_itkSpatialObjectPoint3(*args))
    __swig_destroy__ = _itkSpatialObjectPointPython.delete_itkSpatialObjectPoint3
    GetNameOfClass = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetNameOfClass)
    SetId = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_SetId)
    GetId = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetId)
    SetPositionInObjectSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_SetPositionInObjectSpace)
    GetPositionInObjectSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetPositionInObjectSpace)
    SetSpatialObject = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_SetSpatialObject)
    GetSpatialObject = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetSpatialObject)
    SetPositionInWorldSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_SetPositionInWorldSpace)
    GetPositionInWorldSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetPositionInWorldSpace)
    GetColor = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetColor)
    SetColor = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_SetColor)
    SetRed = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_SetRed)
    GetRed = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetRed)
    SetGreen = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_SetGreen)
    GetGreen = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetGreen)
    SetBlue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_SetBlue)
    GetBlue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetBlue)
    SetAlpha = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetAlpha)
    SetTagScalarValue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_SetTagScalarValue)
    GetTagScalarValue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetTagScalarValue)
    GetTagScalarDictionary = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_GetTagScalarDictionary)
    SetTagScalarDictionary = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_SetTagScalarDictionary)
    Print = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3_Print)
    __str__ = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint3___str__)

# Register itkSpatialObjectPoint3 in _itkSpatialObjectPointPython:
_itkSpatialObjectPointPython.itkSpatialObjectPoint3_swigregister(itkSpatialObjectPoint3)

class itkSpatialObjectPoint4(object):
    r"""


    Point used for spatial objets.

    This class contains all the functions necessary to define a point

    See:   TubeSpatialObjectPoint SurfaceSpatialObjectPoint 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkSpatialObjectPoint4
        __init__(self, other) -> itkSpatialObjectPoint4

        Parameters
        ----------
        other: itkSpatialObjectPoint4 const &



        Point used for spatial objets.

        This class contains all the functions necessary to define a point

        See:   TubeSpatialObjectPoint SurfaceSpatialObjectPoint 
        """
        _itkSpatialObjectPointPython.itkSpatialObjectPoint4_swiginit(self, _itkSpatialObjectPointPython.new_itkSpatialObjectPoint4(*args))
    __swig_destroy__ = _itkSpatialObjectPointPython.delete_itkSpatialObjectPoint4
    GetNameOfClass = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetNameOfClass)
    SetId = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_SetId)
    GetId = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetId)
    SetPositionInObjectSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_SetPositionInObjectSpace)
    GetPositionInObjectSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetPositionInObjectSpace)
    SetSpatialObject = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_SetSpatialObject)
    GetSpatialObject = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetSpatialObject)
    SetPositionInWorldSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_SetPositionInWorldSpace)
    GetPositionInWorldSpace = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetPositionInWorldSpace)
    GetColor = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetColor)
    SetColor = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_SetColor)
    SetRed = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_SetRed)
    GetRed = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetRed)
    SetGreen = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_SetGreen)
    GetGreen = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetGreen)
    SetBlue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_SetBlue)
    GetBlue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetBlue)
    SetAlpha = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetAlpha)
    SetTagScalarValue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_SetTagScalarValue)
    GetTagScalarValue = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetTagScalarValue)
    GetTagScalarDictionary = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_GetTagScalarDictionary)
    SetTagScalarDictionary = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_SetTagScalarDictionary)
    Print = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4_Print)
    __str__ = _swig_new_instance_method(_itkSpatialObjectPointPython.itkSpatialObjectPoint4___str__)

# Register itkSpatialObjectPoint4 in _itkSpatialObjectPointPython:
_itkSpatialObjectPointPython.itkSpatialObjectPoint4_swigregister(itkSpatialObjectPoint4)



