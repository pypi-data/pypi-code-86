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
    from . import _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython
else:
    import _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkDiscreteCurvatureQuadEdgeMeshFilterPython
import itk.itkQuadEdgeMeshPointPython
import itk.itkGeometricalQuadEdgePython
import itk.itkQuadEdgePython
import itk.itkPointPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython
import itk.itkQuadEdgeMeshBasePython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkRGBPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
import itk.itkMapContainerPython
import itk.itkQuadEdgeCellTraitsInfoPython
import itk.itkQuadEdgeMeshLineCellPython
import itk.itkArrayPython

def itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2_New():
    return itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2.New()

class itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2(itk.itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2):
    r"""


    see the following paper title: Discrete Differential-Geometry
    Operators for Triangulated 2-Manifolds authors: Mark Meyer, Mathieu
    Desbrun, Peter Schroder, Alan H. Barr conference: VisMath '02
    location: Berlin (Germany) 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2___New_orig__)
    Clone = _swig_new_instance_method(_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2_Clone)
    OutputIsFloatingPointCheck = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2_OutputIsFloatingPointCheck
    
    __swig_destroy__ = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2
    cast = _swig_new_static_method(_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2_cast)

    def New(*args, **kargs):
        """New() -> itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2

        Create a new object of the class itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2 in _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython:
_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2_swigregister(itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2)
itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2___New_orig__ = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2___New_orig__
itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2_cast = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2_cast


def itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3_New():
    return itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3.New()

class itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3(itk.itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3):
    r"""


    see the following paper title: Discrete Differential-Geometry
    Operators for Triangulated 2-Manifolds authors: Mark Meyer, Mathieu
    Desbrun, Peter Schroder, Alan H. Barr conference: VisMath '02
    location: Berlin (Germany) 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3___New_orig__)
    Clone = _swig_new_instance_method(_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3_Clone)
    OutputIsFloatingPointCheck = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3_OutputIsFloatingPointCheck
    
    __swig_destroy__ = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3
    cast = _swig_new_static_method(_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3_cast)

    def New(*args, **kargs):
        """New() -> itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3

        Create a new object of the class itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3 in _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython:
_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3_swigregister(itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3)
itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3___New_orig__ = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3___New_orig__
itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3_cast = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3_cast


def itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4_New():
    return itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4.New()

class itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4(itk.itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD4):
    r"""


    see the following paper title: Discrete Differential-Geometry
    Operators for Triangulated 2-Manifolds authors: Mark Meyer, Mathieu
    Desbrun, Peter Schroder, Alan H. Barr conference: VisMath '02
    location: Berlin (Germany) 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4___New_orig__)
    Clone = _swig_new_instance_method(_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4_Clone)
    OutputIsFloatingPointCheck = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4_OutputIsFloatingPointCheck
    
    __swig_destroy__ = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4
    cast = _swig_new_static_method(_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4_cast)

    def New(*args, **kargs):
        """New() -> itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4

        Create a new object of the class itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4 in _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython:
_itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4_swigregister(itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4)
itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4___New_orig__ = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4___New_orig__
itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4_cast = _itkDiscreteMeanCurvatureQuadEdgeMeshFilterPython.itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def discrete_mean_curvature_quad_edge_mesh_filter(*args: itkt.Mesh,  output: itkt.QuadEdgeMesh=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for DiscreteMeanCurvatureQuadEdgeMeshFilter"""
    import itk

    kwarg_typehints = { 'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.DiscreteMeanCurvatureQuadEdgeMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def discrete_mean_curvature_quad_edge_mesh_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKQuadEdgeMeshFiltering.DiscreteMeanCurvatureQuadEdgeMeshFilter
    discrete_mean_curvature_quad_edge_mesh_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    discrete_mean_curvature_quad_edge_mesh_filter.__doc__ = filter_object.__doc__




