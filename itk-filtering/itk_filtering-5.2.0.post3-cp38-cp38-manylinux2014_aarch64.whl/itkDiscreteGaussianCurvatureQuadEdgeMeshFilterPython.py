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
    from . import _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython
else:
    import _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkDiscreteCurvatureQuadEdgeMeshFilterPython
import itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython
import itk.itkQuadEdgeMeshBasePython
import itk.itkQuadEdgeCellTraitsInfoPython
import itk.itkQuadEdgeMeshPointPython
import itk.itkPointPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkGeometricalQuadEdgePython
import itk.itkQuadEdgePython
import itk.ITKCommonBasePython
import itk.itkQuadEdgeMeshLineCellPython
import itk.itkArrayPython
import itk.itkMapContainerPython
import itk.itkImagePython
import itk.itkSizePython
import itk.itkRGBPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkRGBAPixelPython

def itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_New():
    return itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2.New()

class itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2(itk.itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2):
    r"""


    see the following paper title: Discrete Differential-Geometry
    Operators for Triangulated 2-Manifolds authors: Mark Meyer, Mathieu
    Desbrun, Peter Schroder, Alan H. Barr conference: VisMath '02
    location: Berlin (Germany)

    : Arnaud Gelas, Alexandre Gouaillard 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2___New_orig__)
    Clone = _swig_new_instance_method(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_Clone)
    OutputIsFloatingPointCheck = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_OutputIsFloatingPointCheck
    
    __swig_destroy__ = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2
    cast = _swig_new_static_method(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_cast)

    def New(*args, **kargs):
        """New() -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2

        Create a new object of the class itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2 in _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython:
_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_swigregister(itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2)
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2___New_orig__ = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2___New_orig__
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_cast = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2_cast


def itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_New():
    return itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3.New()

class itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3(itk.itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3):
    r"""


    see the following paper title: Discrete Differential-Geometry
    Operators for Triangulated 2-Manifolds authors: Mark Meyer, Mathieu
    Desbrun, Peter Schroder, Alan H. Barr conference: VisMath '02
    location: Berlin (Germany)

    : Arnaud Gelas, Alexandre Gouaillard 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3___New_orig__)
    Clone = _swig_new_instance_method(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_Clone)
    OutputIsFloatingPointCheck = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_OutputIsFloatingPointCheck
    
    __swig_destroy__ = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3
    cast = _swig_new_static_method(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_cast)

    def New(*args, **kargs):
        """New() -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3

        Create a new object of the class itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3 in _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython:
_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_swigregister(itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3)
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3___New_orig__ = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3___New_orig__
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_cast = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3_cast


def itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4_New():
    return itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4.New()

class itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4(itk.itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD4):
    r"""


    see the following paper title: Discrete Differential-Geometry
    Operators for Triangulated 2-Manifolds authors: Mark Meyer, Mathieu
    Desbrun, Peter Schroder, Alan H. Barr conference: VisMath '02
    location: Berlin (Germany)

    : Arnaud Gelas, Alexandre Gouaillard 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4___New_orig__)
    Clone = _swig_new_instance_method(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4_Clone)
    OutputIsFloatingPointCheck = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4_OutputIsFloatingPointCheck
    
    __swig_destroy__ = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4
    cast = _swig_new_static_method(_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4_cast)

    def New(*args, **kargs):
        """New() -> itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4

        Create a new object of the class itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4 in _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython:
_itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4_swigregister(itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4)
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4___New_orig__ = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4___New_orig__
itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4_cast = _itkDiscreteGaussianCurvatureQuadEdgeMeshFilterPython.itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def discrete_gaussian_curvature_quad_edge_mesh_filter(*args: itkt.Mesh,  output: itkt.QuadEdgeMesh=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for DiscreteGaussianCurvatureQuadEdgeMeshFilter"""
    import itk

    kwarg_typehints = { 'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.DiscreteGaussianCurvatureQuadEdgeMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def discrete_gaussian_curvature_quad_edge_mesh_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKQuadEdgeMeshFiltering.DiscreteGaussianCurvatureQuadEdgeMeshFilter
    discrete_gaussian_curvature_quad_edge_mesh_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    discrete_gaussian_curvature_quad_edge_mesh_filter.__doc__ = filter_object.__doc__




