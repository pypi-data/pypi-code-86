# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKQuadEdgeMeshFilteringPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkBorderQuadEdgeMeshFilterPython
else:
    import _itkBorderQuadEdgeMeshFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBorderQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBorderQuadEdgeMeshFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkGeometricalQuadEdgePython
import itk.itkQuadEdgePython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkQuadEdgeMeshPointPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython
import itk.itkQuadEdgeMeshBasePython
import itk.itkQuadEdgeMeshLineCellPython
import itk.itkQuadEdgeCellTraitsInfoPython
import itk.itkArrayPython
import itk.itkMapContainerPython
import itk.itkImagePython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkRGBPixelPython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
class itkBorderQuadEdgeMeshFilterEnums(object):
    r"""Proxy of C++ itkBorderQuadEdgeMeshFilterEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    BorderTransform_SQUARE_BORDER_TRANSFORM = _itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterEnums_BorderTransform_SQUARE_BORDER_TRANSFORM
    
    BorderTransform_DISK_BORDER_TRANSFORM = _itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterEnums_BorderTransform_DISK_BORDER_TRANSFORM
    
    BorderPick_LONGEST = _itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterEnums_BorderPick_LONGEST
    
    BorderPick_LARGEST = _itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterEnums_BorderPick_LARGEST
    

    def __init__(self, *args):
        r"""
        __init__(self) -> itkBorderQuadEdgeMeshFilterEnums
        __init__(self, arg0) -> itkBorderQuadEdgeMeshFilterEnums

        Parameters
        ----------
        arg0: itkBorderQuadEdgeMeshFilterEnums const &

        """
        _itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterEnums_swiginit(self, _itkBorderQuadEdgeMeshFilterPython.new_itkBorderQuadEdgeMeshFilterEnums(*args))
    __swig_destroy__ = _itkBorderQuadEdgeMeshFilterPython.delete_itkBorderQuadEdgeMeshFilterEnums

# Register itkBorderQuadEdgeMeshFilterEnums in _itkBorderQuadEdgeMeshFilterPython:
_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterEnums_swigregister(itkBorderQuadEdgeMeshFilterEnums)


def itkBorderQuadEdgeMeshFilterQEMD2_New():
    return itkBorderQuadEdgeMeshFilterQEMD2.New()

class itkBorderQuadEdgeMeshFilterQEMD2(itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2):
    r"""


    Transform one border of a QuadEdgeMesh into either a circle
    (conformal) or a square (arclength-wise).

    This class is one important step when computing a planar
    parameterization of one mesh.

    If the input mesh has several boundaries, one can choose the one which
    would be transformed via the variable m_BorderPick.

    m_BorderPick == Self::LONGEST refers to the boundary $ b $ which
    satisfies: \\[ b = \\arg \\max_{b^k} \\sum_{i=1}^{N^k}
    \\left\\| x_{i}^k - x_{i+1}^k \\right\\| \\]

    m_BorderPick == Self::LARGEST refers to the boundary $ b $ which
    satisfies: \\[ b = \\arg \\max_{b^k} N^k \\]

    See:  ParameterizationQuadEdgeMeshFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2___New_orig__)
    Clone = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_Clone)
    SetTransformType = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_SetTransformType)
    GetTransformType = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_GetTransformType)
    SetBorderPick = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_SetBorderPick)
    GetBorderPick = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_GetBorderPick)
    SetRadius = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_SetRadius)
    GetRadius = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_GetRadius)
    ComputeTransform = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_ComputeTransform)
    GetBoundaryPtMap = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_GetBoundaryPtMap)
    GetBorder = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_GetBorder)
    __swig_destroy__ = _itkBorderQuadEdgeMeshFilterPython.delete_itkBorderQuadEdgeMeshFilterQEMD2
    cast = _swig_new_static_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_cast)

    def New(*args, **kargs):
        """New() -> itkBorderQuadEdgeMeshFilterQEMD2

        Create a new object of the class itkBorderQuadEdgeMeshFilterQEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBorderQuadEdgeMeshFilterQEMD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBorderQuadEdgeMeshFilterQEMD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBorderQuadEdgeMeshFilterQEMD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBorderQuadEdgeMeshFilterQEMD2 in _itkBorderQuadEdgeMeshFilterPython:
_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_swigregister(itkBorderQuadEdgeMeshFilterQEMD2)
itkBorderQuadEdgeMeshFilterQEMD2___New_orig__ = _itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2___New_orig__
itkBorderQuadEdgeMeshFilterQEMD2_cast = _itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD2_cast


def itkBorderQuadEdgeMeshFilterQEMD3_New():
    return itkBorderQuadEdgeMeshFilterQEMD3.New()

class itkBorderQuadEdgeMeshFilterQEMD3(itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3):
    r"""


    Transform one border of a QuadEdgeMesh into either a circle
    (conformal) or a square (arclength-wise).

    This class is one important step when computing a planar
    parameterization of one mesh.

    If the input mesh has several boundaries, one can choose the one which
    would be transformed via the variable m_BorderPick.

    m_BorderPick == Self::LONGEST refers to the boundary $ b $ which
    satisfies: \\[ b = \\arg \\max_{b^k} \\sum_{i=1}^{N^k}
    \\left\\| x_{i}^k - x_{i+1}^k \\right\\| \\]

    m_BorderPick == Self::LARGEST refers to the boundary $ b $ which
    satisfies: \\[ b = \\arg \\max_{b^k} N^k \\]

    See:  ParameterizationQuadEdgeMeshFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3___New_orig__)
    Clone = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_Clone)
    SetTransformType = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_SetTransformType)
    GetTransformType = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_GetTransformType)
    SetBorderPick = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_SetBorderPick)
    GetBorderPick = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_GetBorderPick)
    SetRadius = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_SetRadius)
    GetRadius = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_GetRadius)
    ComputeTransform = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_ComputeTransform)
    GetBoundaryPtMap = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_GetBoundaryPtMap)
    GetBorder = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_GetBorder)
    __swig_destroy__ = _itkBorderQuadEdgeMeshFilterPython.delete_itkBorderQuadEdgeMeshFilterQEMD3
    cast = _swig_new_static_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_cast)

    def New(*args, **kargs):
        """New() -> itkBorderQuadEdgeMeshFilterQEMD3

        Create a new object of the class itkBorderQuadEdgeMeshFilterQEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBorderQuadEdgeMeshFilterQEMD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBorderQuadEdgeMeshFilterQEMD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBorderQuadEdgeMeshFilterQEMD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBorderQuadEdgeMeshFilterQEMD3 in _itkBorderQuadEdgeMeshFilterPython:
_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_swigregister(itkBorderQuadEdgeMeshFilterQEMD3)
itkBorderQuadEdgeMeshFilterQEMD3___New_orig__ = _itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3___New_orig__
itkBorderQuadEdgeMeshFilterQEMD3_cast = _itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD3_cast


def itkBorderQuadEdgeMeshFilterQEMD4_New():
    return itkBorderQuadEdgeMeshFilterQEMD4.New()

class itkBorderQuadEdgeMeshFilterQEMD4(itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD4QEMD4):
    r"""


    Transform one border of a QuadEdgeMesh into either a circle
    (conformal) or a square (arclength-wise).

    This class is one important step when computing a planar
    parameterization of one mesh.

    If the input mesh has several boundaries, one can choose the one which
    would be transformed via the variable m_BorderPick.

    m_BorderPick == Self::LONGEST refers to the boundary $ b $ which
    satisfies: \\[ b = \\arg \\max_{b^k} \\sum_{i=1}^{N^k}
    \\left\\| x_{i}^k - x_{i+1}^k \\right\\| \\]

    m_BorderPick == Self::LARGEST refers to the boundary $ b $ which
    satisfies: \\[ b = \\arg \\max_{b^k} N^k \\]

    See:  ParameterizationQuadEdgeMeshFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4___New_orig__)
    Clone = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_Clone)
    SetTransformType = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_SetTransformType)
    GetTransformType = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_GetTransformType)
    SetBorderPick = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_SetBorderPick)
    GetBorderPick = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_GetBorderPick)
    SetRadius = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_SetRadius)
    GetRadius = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_GetRadius)
    ComputeTransform = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_ComputeTransform)
    GetBoundaryPtMap = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_GetBoundaryPtMap)
    GetBorder = _swig_new_instance_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_GetBorder)
    __swig_destroy__ = _itkBorderQuadEdgeMeshFilterPython.delete_itkBorderQuadEdgeMeshFilterQEMD4
    cast = _swig_new_static_method(_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_cast)

    def New(*args, **kargs):
        """New() -> itkBorderQuadEdgeMeshFilterQEMD4

        Create a new object of the class itkBorderQuadEdgeMeshFilterQEMD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBorderQuadEdgeMeshFilterQEMD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBorderQuadEdgeMeshFilterQEMD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBorderQuadEdgeMeshFilterQEMD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBorderQuadEdgeMeshFilterQEMD4 in _itkBorderQuadEdgeMeshFilterPython:
_itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_swigregister(itkBorderQuadEdgeMeshFilterQEMD4)
itkBorderQuadEdgeMeshFilterQEMD4___New_orig__ = _itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4___New_orig__
itkBorderQuadEdgeMeshFilterQEMD4_cast = _itkBorderQuadEdgeMeshFilterPython.itkBorderQuadEdgeMeshFilterQEMD4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def border_quad_edge_mesh_filter(*args: itkt.Mesh,  transform_type=..., border_pick=..., radius: float=..., output: itkt.QuadEdgeMesh=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for BorderQuadEdgeMeshFilter"""
    import itk

    kwarg_typehints = { 'transform_type':transform_type,'border_pick':border_pick,'radius':radius,'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.BorderQuadEdgeMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def border_quad_edge_mesh_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKQuadEdgeMeshFiltering.BorderQuadEdgeMeshFilter
    border_quad_edge_mesh_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    border_quad_edge_mesh_filter.__doc__ = filter_object.__doc__




