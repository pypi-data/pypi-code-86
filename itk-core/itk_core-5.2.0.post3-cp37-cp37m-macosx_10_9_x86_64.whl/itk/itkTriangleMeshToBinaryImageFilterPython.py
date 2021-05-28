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
    from . import _itkTriangleMeshToBinaryImageFilterPython
else:
    import _itkTriangleMeshToBinaryImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTriangleMeshToBinaryImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTriangleMeshToBinaryImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImagePython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkFixedArrayPython
import itk.itkMatrixPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkMeshBasePython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkPointSetPython
import itk.itkArrayPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourceCommonPython
class itkPoint1D(object):
    r"""Proxy of C++ itkPoint1D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkPoint1D
        __init__(self, p, s) -> itkPoint1D

        Parameters
        ----------
        p: double const
        s: int const

        __init__(self, point) -> itkPoint1D

        Parameters
        ----------
        point: itkPoint1D const &

        """
        _itkTriangleMeshToBinaryImageFilterPython.itkPoint1D_swiginit(self, _itkTriangleMeshToBinaryImageFilterPython.new_itkPoint1D(*args))
    getX = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkPoint1D_getX)
    getSign = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkPoint1D_getSign)
    __swig_destroy__ = _itkTriangleMeshToBinaryImageFilterPython.delete_itkPoint1D

# Register itkPoint1D in _itkTriangleMeshToBinaryImageFilterPython:
_itkTriangleMeshToBinaryImageFilterPython.itkPoint1D_swigregister(itkPoint1D)


def itkTriangleMeshToBinaryImageFilterMD3ID3_New():
    return itkTriangleMeshToBinaryImageFilterMD3ID3.New()

class itkTriangleMeshToBinaryImageFilterMD3ID3(itk.itkImageSourcePython.itkImageSourceID3):
    r"""


    3D Rasterization algorithm Courtesy of Dr David Gobbi of Atamai Inc.

    Leila Baghdadi, MICe, Hospital for Sick Childern, Toronto, Canada, 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_Clone)
    SetSpacing = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_GetSpacing)
    SetDirection = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_GetDirection)
    SetInsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_SetInsideValue)
    GetInsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_GetInsideValue)
    SetOutsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_SetOutsideValue)
    GetOutsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_GetOutsideValue)
    SetOrigin = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_GetOrigin)
    SetIndex = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_SetIndex)
    GetIndex = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_GetIndex)
    SetSize = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_SetSize)
    GetSize = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_GetSize)
    SetInput = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_SetInput)
    SetInfoImage = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_SetInfoImage)
    GetInput = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_GetInput)
    SetTolerance = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_SetTolerance)
    GetTolerance = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_GetTolerance)
    __swig_destroy__ = _itkTriangleMeshToBinaryImageFilterPython.delete_itkTriangleMeshToBinaryImageFilterMD3ID3
    cast = _swig_new_static_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleMeshToBinaryImageFilterMD3ID3

        Create a new object of the class itkTriangleMeshToBinaryImageFilterMD3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleMeshToBinaryImageFilterMD3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleMeshToBinaryImageFilterMD3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleMeshToBinaryImageFilterMD3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleMeshToBinaryImageFilterMD3ID3 in _itkTriangleMeshToBinaryImageFilterPython:
_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_swigregister(itkTriangleMeshToBinaryImageFilterMD3ID3)
itkTriangleMeshToBinaryImageFilterMD3ID3___New_orig__ = _itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3___New_orig__
itkTriangleMeshToBinaryImageFilterMD3ID3_cast = _itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMD3ID3_cast


def itkTriangleMeshToBinaryImageFilterMF3IF3_New():
    return itkTriangleMeshToBinaryImageFilterMF3IF3.New()

class itkTriangleMeshToBinaryImageFilterMF3IF3(itk.itkImageSourcePython.itkImageSourceIF3):
    r"""


    3D Rasterization algorithm Courtesy of Dr David Gobbi of Atamai Inc.

    Leila Baghdadi, MICe, Hospital for Sick Childern, Toronto, Canada, 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_Clone)
    SetSpacing = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_GetSpacing)
    SetDirection = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_GetDirection)
    SetInsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_SetInsideValue)
    GetInsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_GetInsideValue)
    SetOutsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_SetOutsideValue)
    GetOutsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_GetOutsideValue)
    SetOrigin = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_GetOrigin)
    SetIndex = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_SetIndex)
    GetIndex = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_GetIndex)
    SetSize = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_SetSize)
    GetSize = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_GetSize)
    SetInput = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_SetInput)
    SetInfoImage = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_SetInfoImage)
    GetInput = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_GetInput)
    SetTolerance = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_SetTolerance)
    GetTolerance = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_GetTolerance)
    __swig_destroy__ = _itkTriangleMeshToBinaryImageFilterPython.delete_itkTriangleMeshToBinaryImageFilterMF3IF3
    cast = _swig_new_static_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleMeshToBinaryImageFilterMF3IF3

        Create a new object of the class itkTriangleMeshToBinaryImageFilterMF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleMeshToBinaryImageFilterMF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleMeshToBinaryImageFilterMF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleMeshToBinaryImageFilterMF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleMeshToBinaryImageFilterMF3IF3 in _itkTriangleMeshToBinaryImageFilterPython:
_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_swigregister(itkTriangleMeshToBinaryImageFilterMF3IF3)
itkTriangleMeshToBinaryImageFilterMF3IF3___New_orig__ = _itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3___New_orig__
itkTriangleMeshToBinaryImageFilterMF3IF3_cast = _itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMF3IF3_cast


def itkTriangleMeshToBinaryImageFilterMSS3ISS3_New():
    return itkTriangleMeshToBinaryImageFilterMSS3ISS3.New()

class itkTriangleMeshToBinaryImageFilterMSS3ISS3(itk.itkImageSourcePython.itkImageSourceISS3):
    r"""


    3D Rasterization algorithm Courtesy of Dr David Gobbi of Atamai Inc.

    Leila Baghdadi, MICe, Hospital for Sick Childern, Toronto, Canada, 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_Clone)
    SetSpacing = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_GetSpacing)
    SetDirection = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_GetDirection)
    SetInsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_SetInsideValue)
    GetInsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_GetInsideValue)
    SetOutsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_SetOutsideValue)
    GetOutsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_GetOutsideValue)
    SetOrigin = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_GetOrigin)
    SetIndex = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_SetIndex)
    GetIndex = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_GetIndex)
    SetSize = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_SetSize)
    GetSize = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_GetSize)
    SetInput = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_SetInput)
    SetInfoImage = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_SetInfoImage)
    GetInput = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_GetInput)
    SetTolerance = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_SetTolerance)
    GetTolerance = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_GetTolerance)
    __swig_destroy__ = _itkTriangleMeshToBinaryImageFilterPython.delete_itkTriangleMeshToBinaryImageFilterMSS3ISS3
    cast = _swig_new_static_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleMeshToBinaryImageFilterMSS3ISS3

        Create a new object of the class itkTriangleMeshToBinaryImageFilterMSS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleMeshToBinaryImageFilterMSS3ISS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleMeshToBinaryImageFilterMSS3ISS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleMeshToBinaryImageFilterMSS3ISS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleMeshToBinaryImageFilterMSS3ISS3 in _itkTriangleMeshToBinaryImageFilterPython:
_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_swigregister(itkTriangleMeshToBinaryImageFilterMSS3ISS3)
itkTriangleMeshToBinaryImageFilterMSS3ISS3___New_orig__ = _itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3___New_orig__
itkTriangleMeshToBinaryImageFilterMSS3ISS3_cast = _itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMSS3ISS3_cast


def itkTriangleMeshToBinaryImageFilterMUC3IUC3_New():
    return itkTriangleMeshToBinaryImageFilterMUC3IUC3.New()

class itkTriangleMeshToBinaryImageFilterMUC3IUC3(itk.itkImageSourcePython.itkImageSourceIUC3):
    r"""


    3D Rasterization algorithm Courtesy of Dr David Gobbi of Atamai Inc.

    Leila Baghdadi, MICe, Hospital for Sick Childern, Toronto, Canada, 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_Clone)
    SetSpacing = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_GetSpacing)
    SetDirection = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_GetDirection)
    SetInsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_SetInsideValue)
    GetInsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_GetInsideValue)
    SetOutsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_SetOutsideValue)
    GetOutsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_GetOutsideValue)
    SetOrigin = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_GetOrigin)
    SetIndex = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_SetIndex)
    GetIndex = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_GetIndex)
    SetSize = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_SetSize)
    GetSize = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_GetSize)
    SetInput = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_SetInput)
    SetInfoImage = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_SetInfoImage)
    GetInput = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_GetInput)
    SetTolerance = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_SetTolerance)
    GetTolerance = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_GetTolerance)
    __swig_destroy__ = _itkTriangleMeshToBinaryImageFilterPython.delete_itkTriangleMeshToBinaryImageFilterMUC3IUC3
    cast = _swig_new_static_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleMeshToBinaryImageFilterMUC3IUC3

        Create a new object of the class itkTriangleMeshToBinaryImageFilterMUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleMeshToBinaryImageFilterMUC3IUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleMeshToBinaryImageFilterMUC3IUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleMeshToBinaryImageFilterMUC3IUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleMeshToBinaryImageFilterMUC3IUC3 in _itkTriangleMeshToBinaryImageFilterPython:
_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_swigregister(itkTriangleMeshToBinaryImageFilterMUC3IUC3)
itkTriangleMeshToBinaryImageFilterMUC3IUC3___New_orig__ = _itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3___New_orig__
itkTriangleMeshToBinaryImageFilterMUC3IUC3_cast = _itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUC3IUC3_cast


def itkTriangleMeshToBinaryImageFilterMUS3IUS3_New():
    return itkTriangleMeshToBinaryImageFilterMUS3IUS3.New()

class itkTriangleMeshToBinaryImageFilterMUS3IUS3(itk.itkImageSourcePython.itkImageSourceIUS3):
    r"""


    3D Rasterization algorithm Courtesy of Dr David Gobbi of Atamai Inc.

    Leila Baghdadi, MICe, Hospital for Sick Childern, Toronto, Canada, 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_Clone)
    SetSpacing = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_GetSpacing)
    SetDirection = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_GetDirection)
    SetInsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_SetInsideValue)
    GetInsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_GetInsideValue)
    SetOutsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_SetOutsideValue)
    GetOutsideValue = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_GetOutsideValue)
    SetOrigin = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_GetOrigin)
    SetIndex = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_SetIndex)
    GetIndex = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_GetIndex)
    SetSize = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_SetSize)
    GetSize = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_GetSize)
    SetInput = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_SetInput)
    SetInfoImage = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_SetInfoImage)
    GetInput = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_GetInput)
    SetTolerance = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_SetTolerance)
    GetTolerance = _swig_new_instance_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_GetTolerance)
    __swig_destroy__ = _itkTriangleMeshToBinaryImageFilterPython.delete_itkTriangleMeshToBinaryImageFilterMUS3IUS3
    cast = _swig_new_static_method(_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleMeshToBinaryImageFilterMUS3IUS3

        Create a new object of the class itkTriangleMeshToBinaryImageFilterMUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleMeshToBinaryImageFilterMUS3IUS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleMeshToBinaryImageFilterMUS3IUS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleMeshToBinaryImageFilterMUS3IUS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleMeshToBinaryImageFilterMUS3IUS3 in _itkTriangleMeshToBinaryImageFilterPython:
_itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_swigregister(itkTriangleMeshToBinaryImageFilterMUS3IUS3)
itkTriangleMeshToBinaryImageFilterMUS3IUS3___New_orig__ = _itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3___New_orig__
itkTriangleMeshToBinaryImageFilterMUS3IUS3_cast = _itkTriangleMeshToBinaryImageFilterPython.itkTriangleMeshToBinaryImageFilterMUS3IUS3_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def triangle_mesh_to_binary_image_filter(*args,  spacing: Sequence[float]=..., direction=..., inside_value: float=..., outside_value: float=..., origin: Sequence[float]=..., index: Sequence[int]=..., size: Sequence[int]=..., info_image: itkt.Image=..., tolerance: float=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for TriangleMeshToBinaryImageFilter"""
    import itk

    kwarg_typehints = { 'spacing':spacing,'direction':direction,'inside_value':inside_value,'outside_value':outside_value,'origin':origin,'index':index,'size':size,'info_image':info_image,'tolerance':tolerance }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.TriangleMeshToBinaryImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def triangle_mesh_to_binary_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKMesh.TriangleMeshToBinaryImageFilter
    triangle_mesh_to_binary_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    triangle_mesh_to_binary_image_filter.__doc__ = filter_object.__doc__




