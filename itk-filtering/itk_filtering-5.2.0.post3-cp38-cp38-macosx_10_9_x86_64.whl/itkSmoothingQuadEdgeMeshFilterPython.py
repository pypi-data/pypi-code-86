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
    from . import _itkSmoothingQuadEdgeMeshFilterPython
else:
    import _itkSmoothingQuadEdgeMeshFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSmoothingQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSmoothingQuadEdgeMeshFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython
import itk.itkQuadEdgeMeshBasePython
import itk.itkQuadEdgeCellTraitsInfoPython
import itk.itkQuadEdgeMeshPointPython
import itk.itkGeometricalQuadEdgePython
import itk.itkQuadEdgePython
import itk.itkPointPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkQuadEdgeMeshLineCellPython
import itk.itkArrayPython
import itk.itkImagePython
import itk.itkSizePython
import itk.itkRGBPixelPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkImageRegionPython
import itk.itkCovariantVectorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBAPixelPython
import itk.itkMapContainerPython
import itk.itkMatrixCoefficientsPython

def itkSmoothingQuadEdgeMeshFilterQEMD2_New():
    return itkSmoothingQuadEdgeMeshFilterQEMD2.New()

class itkSmoothingQuadEdgeMeshFilterQEMD2(itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2):
    r"""


    QuadEdgeMesh Smoothing Filter.

    This filter adjusts point coordinates using Laplacian smoothing. The
    effect is to "relax" the mesh, making the cells better shaped and
    the vertices more evenly distributed.

    For one iteration the location of one vertex is computed as follows:
    \\[ \\boldsymbol{ v' }_i = v_i + m_RelaxationFactor \\cdot
    \\frac{ \\sum_j w_{ij} ( \\boldsymbol{ v_j } - \\boldsymbol{
    v_i } ) }{ \\sum_j w_{ij} } \\]

    where $ w_{ij} $ is computed by the means of the set functor
    CoefficientsComputation

    This process is then repeated for m_NumberOfIterations (the more
    iterations, the smoother the output mesh will be).

    At each iteration, one can run DelaunayConformingQuadEdgeMeshFilter
    resulting a more regular (in terms of connectivity) and smoother mesh.
    Depending on the mesh size and configuration it could be an expensive
    process to run it at each iterations, especially if the number of
    iterations is large. Note that one can still run N iterations without
    DelaunayConformingQuadEdgeMeshFilter, then run this filter and apply
    this process M times. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2___New_orig__)
    Clone = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_Clone)
    SetCoefficientsMethod = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetCoefficientsMethod)
    SetNumberOfIterations = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetNumberOfIterations)
    DelaunayConformingOn = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_DelaunayConformingOn)
    DelaunayConformingOff = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_DelaunayConformingOff)
    SetDelaunayConforming = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetDelaunayConforming)
    GetDelaunayConforming = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetDelaunayConforming)
    SetRelaxationFactor = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_SetRelaxationFactor)
    GetRelaxationFactor = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_GetRelaxationFactor)
    __swig_destroy__ = _itkSmoothingQuadEdgeMeshFilterPython.delete_itkSmoothingQuadEdgeMeshFilterQEMD2
    cast = _swig_new_static_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_cast)

    def New(*args, **kargs):
        """New() -> itkSmoothingQuadEdgeMeshFilterQEMD2

        Create a new object of the class itkSmoothingQuadEdgeMeshFilterQEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSmoothingQuadEdgeMeshFilterQEMD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSmoothingQuadEdgeMeshFilterQEMD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSmoothingQuadEdgeMeshFilterQEMD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSmoothingQuadEdgeMeshFilterQEMD2 in _itkSmoothingQuadEdgeMeshFilterPython:
_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_swigregister(itkSmoothingQuadEdgeMeshFilterQEMD2)
itkSmoothingQuadEdgeMeshFilterQEMD2___New_orig__ = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2___New_orig__
itkSmoothingQuadEdgeMeshFilterQEMD2_cast = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD2_cast


def itkSmoothingQuadEdgeMeshFilterQEMD3_New():
    return itkSmoothingQuadEdgeMeshFilterQEMD3.New()

class itkSmoothingQuadEdgeMeshFilterQEMD3(itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3):
    r"""


    QuadEdgeMesh Smoothing Filter.

    This filter adjusts point coordinates using Laplacian smoothing. The
    effect is to "relax" the mesh, making the cells better shaped and
    the vertices more evenly distributed.

    For one iteration the location of one vertex is computed as follows:
    \\[ \\boldsymbol{ v' }_i = v_i + m_RelaxationFactor \\cdot
    \\frac{ \\sum_j w_{ij} ( \\boldsymbol{ v_j } - \\boldsymbol{
    v_i } ) }{ \\sum_j w_{ij} } \\]

    where $ w_{ij} $ is computed by the means of the set functor
    CoefficientsComputation

    This process is then repeated for m_NumberOfIterations (the more
    iterations, the smoother the output mesh will be).

    At each iteration, one can run DelaunayConformingQuadEdgeMeshFilter
    resulting a more regular (in terms of connectivity) and smoother mesh.
    Depending on the mesh size and configuration it could be an expensive
    process to run it at each iterations, especially if the number of
    iterations is large. Note that one can still run N iterations without
    DelaunayConformingQuadEdgeMeshFilter, then run this filter and apply
    this process M times. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3___New_orig__)
    Clone = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_Clone)
    SetCoefficientsMethod = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetCoefficientsMethod)
    SetNumberOfIterations = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetNumberOfIterations)
    DelaunayConformingOn = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_DelaunayConformingOn)
    DelaunayConformingOff = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_DelaunayConformingOff)
    SetDelaunayConforming = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetDelaunayConforming)
    GetDelaunayConforming = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetDelaunayConforming)
    SetRelaxationFactor = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_SetRelaxationFactor)
    GetRelaxationFactor = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_GetRelaxationFactor)
    __swig_destroy__ = _itkSmoothingQuadEdgeMeshFilterPython.delete_itkSmoothingQuadEdgeMeshFilterQEMD3
    cast = _swig_new_static_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_cast)

    def New(*args, **kargs):
        """New() -> itkSmoothingQuadEdgeMeshFilterQEMD3

        Create a new object of the class itkSmoothingQuadEdgeMeshFilterQEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSmoothingQuadEdgeMeshFilterQEMD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSmoothingQuadEdgeMeshFilterQEMD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSmoothingQuadEdgeMeshFilterQEMD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSmoothingQuadEdgeMeshFilterQEMD3 in _itkSmoothingQuadEdgeMeshFilterPython:
_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_swigregister(itkSmoothingQuadEdgeMeshFilterQEMD3)
itkSmoothingQuadEdgeMeshFilterQEMD3___New_orig__ = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3___New_orig__
itkSmoothingQuadEdgeMeshFilterQEMD3_cast = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD3_cast


def itkSmoothingQuadEdgeMeshFilterQEMD4_New():
    return itkSmoothingQuadEdgeMeshFilterQEMD4.New()

class itkSmoothingQuadEdgeMeshFilterQEMD4(itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD4QEMD4):
    r"""


    QuadEdgeMesh Smoothing Filter.

    This filter adjusts point coordinates using Laplacian smoothing. The
    effect is to "relax" the mesh, making the cells better shaped and
    the vertices more evenly distributed.

    For one iteration the location of one vertex is computed as follows:
    \\[ \\boldsymbol{ v' }_i = v_i + m_RelaxationFactor \\cdot
    \\frac{ \\sum_j w_{ij} ( \\boldsymbol{ v_j } - \\boldsymbol{
    v_i } ) }{ \\sum_j w_{ij} } \\]

    where $ w_{ij} $ is computed by the means of the set functor
    CoefficientsComputation

    This process is then repeated for m_NumberOfIterations (the more
    iterations, the smoother the output mesh will be).

    At each iteration, one can run DelaunayConformingQuadEdgeMeshFilter
    resulting a more regular (in terms of connectivity) and smoother mesh.
    Depending on the mesh size and configuration it could be an expensive
    process to run it at each iterations, especially if the number of
    iterations is large. Note that one can still run N iterations without
    DelaunayConformingQuadEdgeMeshFilter, then run this filter and apply
    this process M times. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4___New_orig__)
    Clone = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_Clone)
    SetCoefficientsMethod = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_SetCoefficientsMethod)
    SetNumberOfIterations = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_GetNumberOfIterations)
    DelaunayConformingOn = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_DelaunayConformingOn)
    DelaunayConformingOff = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_DelaunayConformingOff)
    SetDelaunayConforming = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_SetDelaunayConforming)
    GetDelaunayConforming = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_GetDelaunayConforming)
    SetRelaxationFactor = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_SetRelaxationFactor)
    GetRelaxationFactor = _swig_new_instance_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_GetRelaxationFactor)
    __swig_destroy__ = _itkSmoothingQuadEdgeMeshFilterPython.delete_itkSmoothingQuadEdgeMeshFilterQEMD4
    cast = _swig_new_static_method(_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_cast)

    def New(*args, **kargs):
        """New() -> itkSmoothingQuadEdgeMeshFilterQEMD4

        Create a new object of the class itkSmoothingQuadEdgeMeshFilterQEMD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSmoothingQuadEdgeMeshFilterQEMD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSmoothingQuadEdgeMeshFilterQEMD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSmoothingQuadEdgeMeshFilterQEMD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSmoothingQuadEdgeMeshFilterQEMD4 in _itkSmoothingQuadEdgeMeshFilterPython:
_itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_swigregister(itkSmoothingQuadEdgeMeshFilterQEMD4)
itkSmoothingQuadEdgeMeshFilterQEMD4___New_orig__ = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4___New_orig__
itkSmoothingQuadEdgeMeshFilterQEMD4_cast = _itkSmoothingQuadEdgeMeshFilterPython.itkSmoothingQuadEdgeMeshFilterQEMD4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def smoothing_quad_edge_mesh_filter(*args: itkt.Mesh,  coefficients_method=..., number_of_iterations: int=..., delaunay_conforming: bool=..., relaxation_factor: float=..., output: itkt.QuadEdgeMesh=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for SmoothingQuadEdgeMeshFilter"""
    import itk

    kwarg_typehints = { 'coefficients_method':coefficients_method,'number_of_iterations':number_of_iterations,'delaunay_conforming':delaunay_conforming,'relaxation_factor':relaxation_factor,'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.SmoothingQuadEdgeMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def smoothing_quad_edge_mesh_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKQuadEdgeMeshFiltering.SmoothingQuadEdgeMeshFilter
    smoothing_quad_edge_mesh_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    smoothing_quad_edge_mesh_filter.__doc__ = filter_object.__doc__




