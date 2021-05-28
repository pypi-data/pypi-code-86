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
    from . import _itkDTITubeSpatialObjectPointPython
else:
    import _itkDTITubeSpatialObjectPointPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDTITubeSpatialObjectPointPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDTITubeSpatialObjectPointPython.SWIG_PyStaticMethod_New

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
import itk.itkTubeSpatialObjectPointPython
import itk.itkCovariantVectorPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.ITKCommonBasePython
import itk.itkSpatialObjectPointPython
import itk.itkRGBAPixelPython
import itk.itkSpatialObjectBasePython
import itk.itkAffineTransformPython
import itk.itkMatrixPython
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
class vectoritkDTITubeSpatialObjectPoint3(collections.abc.MutableSequence):
    r"""Proxy of C++ std::vector< itkDTITubeSpatialObjectPoint3 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___nonzero__)
    __bool__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___bool__)
    __len__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___len__)
    __getslice__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___getslice__)
    __setslice__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___setslice__)
    __delslice__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___delslice__)
    __delitem__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___delitem__)
    __getitem__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___getitem__)
    __setitem__ = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___setitem__)
    pop = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_pop)
    append = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_append)
    empty = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_empty)
    size = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_size)
    swap = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_swap)
    begin = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_begin)
    end = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_end)
    rbegin = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_rbegin)
    rend = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_rend)
    clear = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_clear)
    get_allocator = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_get_allocator)
    pop_back = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_pop_back)
    erase = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> vectoritkDTITubeSpatialObjectPoint3
        __init__(self, other) -> vectoritkDTITubeSpatialObjectPoint3

        Parameters
        ----------
        other: std::vector< itkDTITubeSpatialObjectPoint3 > const &

        __init__(self, size) -> vectoritkDTITubeSpatialObjectPoint3

        Parameters
        ----------
        size: std::vector< itkDTITubeSpatialObjectPoint3 >::size_type

        __init__(self, size, value) -> vectoritkDTITubeSpatialObjectPoint3

        Parameters
        ----------
        size: std::vector< itkDTITubeSpatialObjectPoint3 >::size_type
        value: std::vector< itkDTITubeSpatialObjectPoint3 >::value_type const &

        """
        _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_swiginit(self, _itkDTITubeSpatialObjectPointPython.new_vectoritkDTITubeSpatialObjectPoint3(*args))
    push_back = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_push_back)
    front = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_front)
    back = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_back)
    assign = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_assign)
    resize = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_resize)
    insert = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_insert)
    reserve = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_reserve)
    capacity = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_capacity)
    __swig_destroy__ = _itkDTITubeSpatialObjectPointPython.delete_vectoritkDTITubeSpatialObjectPoint3

# Register vectoritkDTITubeSpatialObjectPoint3 in _itkDTITubeSpatialObjectPointPython:
_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_swigregister(vectoritkDTITubeSpatialObjectPoint3)

class itkDTITubeSpatialObjectPoint3(itk.itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3):
    r"""


    Point used for a tube definition.

    This class contains all the functions necessary to define a point that
    can be used to build tubes.

    See:   DTITubeSpatialObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkDTITubeSpatialObjectPoint3
        __init__(self, other) -> itkDTITubeSpatialObjectPoint3

        Parameters
        ----------
        other: itkDTITubeSpatialObjectPoint3 const &



        Point used for a tube definition.

        This class contains all the functions necessary to define a point that
        can be used to build tubes.

        See:   DTITubeSpatialObject 
        """
        _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_swiginit(self, _itkDTITubeSpatialObjectPointPython.new_itkDTITubeSpatialObjectPoint3(*args))
    __swig_destroy__ = _itkDTITubeSpatialObjectPointPython.delete_itkDTITubeSpatialObjectPoint3
    SetTensorMatrix = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_SetTensorMatrix)
    GetTensorMatrix = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetTensorMatrix)
    AddField = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_AddField)
    SetField = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_SetField)
    GetFields = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetFields)
    GetField = _swig_new_instance_method(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetField)

# Register itkDTITubeSpatialObjectPoint3 in _itkDTITubeSpatialObjectPointPython:
_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_swigregister(itkDTITubeSpatialObjectPoint3)

class itkDTITubeSpatialObjectPointEnums(object):
    r"""Proxy of C++ itkDTITubeSpatialObjectPointEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DTITubeSpatialObjectPointField_FA = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPointEnums_DTITubeSpatialObjectPointField_FA
    
    DTITubeSpatialObjectPointField_ADC = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPointEnums_DTITubeSpatialObjectPointField_ADC
    
    DTITubeSpatialObjectPointField_GA = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPointEnums_DTITubeSpatialObjectPointField_GA
    

    def __init__(self, *args):
        r"""
        __init__(self) -> itkDTITubeSpatialObjectPointEnums
        __init__(self, arg0) -> itkDTITubeSpatialObjectPointEnums

        Parameters
        ----------
        arg0: itkDTITubeSpatialObjectPointEnums const &

        """
        _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPointEnums_swiginit(self, _itkDTITubeSpatialObjectPointPython.new_itkDTITubeSpatialObjectPointEnums(*args))
    __swig_destroy__ = _itkDTITubeSpatialObjectPointPython.delete_itkDTITubeSpatialObjectPointEnums

# Register itkDTITubeSpatialObjectPointEnums in _itkDTITubeSpatialObjectPointPython:
_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPointEnums_swigregister(itkDTITubeSpatialObjectPointEnums)



