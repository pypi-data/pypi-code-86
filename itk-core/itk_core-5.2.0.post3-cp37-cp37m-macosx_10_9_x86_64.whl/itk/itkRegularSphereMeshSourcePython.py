# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKMeshPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkRegularSphereMeshSourcePython
else:
    import _itkRegularSphereMeshSourcePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRegularSphereMeshSourcePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRegularSphereMeshSourcePython.SWIG_PyStaticMethod_New

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
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkFixedArrayPython
import itk.itkMeshBasePython
import itk.itkBoundingBoxPython
import itk.ITKCommonBasePython
import itk.itkPointPython
import itk.itkMapContainerPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkPointSetPython
import itk.itkArrayPython
import itk.itkMeshSourcePython

def itkRegularSphereMeshSourceMD2_New():
    return itkRegularSphereMeshSourceMD2.New()

class itkRegularSphereMeshSourceMD2(itk.itkMeshSourcePython.itkMeshSourceMD2):
    r"""


    Inputs are the center of the mesh, the scale (radius in each
    dimension) of the mesh and a resolution parameter, which corresponds
    to the recursion depth while creating a spherical triangle mesh.

    Don't use recursion depths larger than 5, because mesh generation gets
    very slow.

    Thomas Boettger. Division Medical and Biological Informatics, German
    Cancer Research Center, Heidelberg. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2___New_orig__)
    Clone = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2_Clone)
    SetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2_SetResolution)
    GetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2_GetResolution)
    SetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2_SetCenter)
    GetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2_GetCenter)
    SetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2_SetScale)
    GetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2_GetScale)
    __swig_destroy__ = _itkRegularSphereMeshSourcePython.delete_itkRegularSphereMeshSourceMD2
    cast = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2_cast)

    def New(*args, **kargs):
        """New() -> itkRegularSphereMeshSourceMD2

        Create a new object of the class itkRegularSphereMeshSourceMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegularSphereMeshSourceMD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRegularSphereMeshSourceMD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRegularSphereMeshSourceMD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRegularSphereMeshSourceMD2 in _itkRegularSphereMeshSourcePython:
_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2_swigregister(itkRegularSphereMeshSourceMD2)
itkRegularSphereMeshSourceMD2___New_orig__ = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2___New_orig__
itkRegularSphereMeshSourceMD2_cast = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD2_cast


def itkRegularSphereMeshSourceMD3_New():
    return itkRegularSphereMeshSourceMD3.New()

class itkRegularSphereMeshSourceMD3(itk.itkMeshSourcePython.itkMeshSourceMD3):
    r"""


    Inputs are the center of the mesh, the scale (radius in each
    dimension) of the mesh and a resolution parameter, which corresponds
    to the recursion depth while creating a spherical triangle mesh.

    Don't use recursion depths larger than 5, because mesh generation gets
    very slow.

    Thomas Boettger. Division Medical and Biological Informatics, German
    Cancer Research Center, Heidelberg. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3___New_orig__)
    Clone = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3_Clone)
    SetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3_SetResolution)
    GetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3_GetResolution)
    SetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3_SetCenter)
    GetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3_GetCenter)
    SetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3_SetScale)
    GetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3_GetScale)
    __swig_destroy__ = _itkRegularSphereMeshSourcePython.delete_itkRegularSphereMeshSourceMD3
    cast = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3_cast)

    def New(*args, **kargs):
        """New() -> itkRegularSphereMeshSourceMD3

        Create a new object of the class itkRegularSphereMeshSourceMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegularSphereMeshSourceMD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRegularSphereMeshSourceMD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRegularSphereMeshSourceMD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRegularSphereMeshSourceMD3 in _itkRegularSphereMeshSourcePython:
_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3_swigregister(itkRegularSphereMeshSourceMD3)
itkRegularSphereMeshSourceMD3___New_orig__ = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3___New_orig__
itkRegularSphereMeshSourceMD3_cast = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD3_cast


def itkRegularSphereMeshSourceMD4_New():
    return itkRegularSphereMeshSourceMD4.New()

class itkRegularSphereMeshSourceMD4(itk.itkMeshSourcePython.itkMeshSourceMD4):
    r"""


    Inputs are the center of the mesh, the scale (radius in each
    dimension) of the mesh and a resolution parameter, which corresponds
    to the recursion depth while creating a spherical triangle mesh.

    Don't use recursion depths larger than 5, because mesh generation gets
    very slow.

    Thomas Boettger. Division Medical and Biological Informatics, German
    Cancer Research Center, Heidelberg. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4___New_orig__)
    Clone = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4_Clone)
    SetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4_SetResolution)
    GetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4_GetResolution)
    SetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4_SetCenter)
    GetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4_GetCenter)
    SetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4_SetScale)
    GetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4_GetScale)
    __swig_destroy__ = _itkRegularSphereMeshSourcePython.delete_itkRegularSphereMeshSourceMD4
    cast = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4_cast)

    def New(*args, **kargs):
        """New() -> itkRegularSphereMeshSourceMD4

        Create a new object of the class itkRegularSphereMeshSourceMD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegularSphereMeshSourceMD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRegularSphereMeshSourceMD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRegularSphereMeshSourceMD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRegularSphereMeshSourceMD4 in _itkRegularSphereMeshSourcePython:
_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4_swigregister(itkRegularSphereMeshSourceMD4)
itkRegularSphereMeshSourceMD4___New_orig__ = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4___New_orig__
itkRegularSphereMeshSourceMD4_cast = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMD4_cast


def itkRegularSphereMeshSourceMF2_New():
    return itkRegularSphereMeshSourceMF2.New()

class itkRegularSphereMeshSourceMF2(itk.itkMeshSourcePython.itkMeshSourceMF2):
    r"""


    Inputs are the center of the mesh, the scale (radius in each
    dimension) of the mesh and a resolution parameter, which corresponds
    to the recursion depth while creating a spherical triangle mesh.

    Don't use recursion depths larger than 5, because mesh generation gets
    very slow.

    Thomas Boettger. Division Medical and Biological Informatics, German
    Cancer Research Center, Heidelberg. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2___New_orig__)
    Clone = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2_Clone)
    SetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2_SetResolution)
    GetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2_GetResolution)
    SetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2_SetCenter)
    GetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2_GetCenter)
    SetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2_SetScale)
    GetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2_GetScale)
    __swig_destroy__ = _itkRegularSphereMeshSourcePython.delete_itkRegularSphereMeshSourceMF2
    cast = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2_cast)

    def New(*args, **kargs):
        """New() -> itkRegularSphereMeshSourceMF2

        Create a new object of the class itkRegularSphereMeshSourceMF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegularSphereMeshSourceMF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRegularSphereMeshSourceMF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRegularSphereMeshSourceMF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRegularSphereMeshSourceMF2 in _itkRegularSphereMeshSourcePython:
_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2_swigregister(itkRegularSphereMeshSourceMF2)
itkRegularSphereMeshSourceMF2___New_orig__ = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2___New_orig__
itkRegularSphereMeshSourceMF2_cast = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF2_cast


def itkRegularSphereMeshSourceMF3_New():
    return itkRegularSphereMeshSourceMF3.New()

class itkRegularSphereMeshSourceMF3(itk.itkMeshSourcePython.itkMeshSourceMF3):
    r"""


    Inputs are the center of the mesh, the scale (radius in each
    dimension) of the mesh and a resolution parameter, which corresponds
    to the recursion depth while creating a spherical triangle mesh.

    Don't use recursion depths larger than 5, because mesh generation gets
    very slow.

    Thomas Boettger. Division Medical and Biological Informatics, German
    Cancer Research Center, Heidelberg. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3___New_orig__)
    Clone = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3_Clone)
    SetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3_SetResolution)
    GetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3_GetResolution)
    SetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3_SetCenter)
    GetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3_GetCenter)
    SetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3_SetScale)
    GetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3_GetScale)
    __swig_destroy__ = _itkRegularSphereMeshSourcePython.delete_itkRegularSphereMeshSourceMF3
    cast = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3_cast)

    def New(*args, **kargs):
        """New() -> itkRegularSphereMeshSourceMF3

        Create a new object of the class itkRegularSphereMeshSourceMF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegularSphereMeshSourceMF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRegularSphereMeshSourceMF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRegularSphereMeshSourceMF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRegularSphereMeshSourceMF3 in _itkRegularSphereMeshSourcePython:
_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3_swigregister(itkRegularSphereMeshSourceMF3)
itkRegularSphereMeshSourceMF3___New_orig__ = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3___New_orig__
itkRegularSphereMeshSourceMF3_cast = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF3_cast


def itkRegularSphereMeshSourceMF4_New():
    return itkRegularSphereMeshSourceMF4.New()

class itkRegularSphereMeshSourceMF4(itk.itkMeshSourcePython.itkMeshSourceMF4):
    r"""


    Inputs are the center of the mesh, the scale (radius in each
    dimension) of the mesh and a resolution parameter, which corresponds
    to the recursion depth while creating a spherical triangle mesh.

    Don't use recursion depths larger than 5, because mesh generation gets
    very slow.

    Thomas Boettger. Division Medical and Biological Informatics, German
    Cancer Research Center, Heidelberg. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4___New_orig__)
    Clone = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4_Clone)
    SetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4_SetResolution)
    GetResolution = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4_GetResolution)
    SetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4_SetCenter)
    GetCenter = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4_GetCenter)
    SetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4_SetScale)
    GetScale = _swig_new_instance_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4_GetScale)
    __swig_destroy__ = _itkRegularSphereMeshSourcePython.delete_itkRegularSphereMeshSourceMF4
    cast = _swig_new_static_method(_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4_cast)

    def New(*args, **kargs):
        """New() -> itkRegularSphereMeshSourceMF4

        Create a new object of the class itkRegularSphereMeshSourceMF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegularSphereMeshSourceMF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRegularSphereMeshSourceMF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRegularSphereMeshSourceMF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRegularSphereMeshSourceMF4 in _itkRegularSphereMeshSourcePython:
_itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4_swigregister(itkRegularSphereMeshSourceMF4)
itkRegularSphereMeshSourceMF4___New_orig__ = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4___New_orig__
itkRegularSphereMeshSourceMF4_cast = _itkRegularSphereMeshSourcePython.itkRegularSphereMeshSourceMF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def regular_sphere_mesh_source(*args,  resolution: int=..., center: Sequence[float]=..., scale: Sequence[float]=..., output: itkt.Mesh=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for RegularSphereMeshSource"""
    import itk

    kwarg_typehints = { 'resolution':resolution,'center':center,'scale':scale,'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.RegularSphereMeshSource.New(*args, **kwargs)
    return instance.__internal_call__()

def regular_sphere_mesh_source_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKMesh.RegularSphereMeshSource
    regular_sphere_mesh_source.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    regular_sphere_mesh_source.__doc__ = filter_object.__doc__




