# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKFastMarchingPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkFastMarchingStoppingCriterionBasePython
else:
    import _itkFastMarchingStoppingCriterionBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkFastMarchingStoppingCriterionBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkFastMarchingStoppingCriterionBasePython.SWIG_PyStaticMethod_New

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
import itk.itkIndexPython
import itk.itkSizePython
import itk.pyBasePython
import itk.itkOffsetPython
import itk.itkImagePython
import itk.itkImageRegionPython
import itk.ITKCommonBasePython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkNodePairPython
class itkFastMarchingStoppingCriterionBaseID2ID2(itk.ITKCommonBasePython.itkStoppingCriterionBase):
    r"""


    Abstract Stopping Criterion dedicated for Fast Marching Methods. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    Reinitialize = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_Reinitialize)
    SetCurrentNodePair = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_SetCurrentNodePair)
    SetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_SetDomain)
    GetModifiableDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_GetModifiableDomain)
    GetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_GetDomain)
    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseID2ID2
    cast = _swig_new_static_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_cast)

# Register itkFastMarchingStoppingCriterionBaseID2ID2 in _itkFastMarchingStoppingCriterionBasePython:
_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_swigregister(itkFastMarchingStoppingCriterionBaseID2ID2)
itkFastMarchingStoppingCriterionBaseID2ID2_cast = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2_cast

class itkFastMarchingStoppingCriterionBaseID3ID3(itk.ITKCommonBasePython.itkStoppingCriterionBase):
    r"""


    Abstract Stopping Criterion dedicated for Fast Marching Methods. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    Reinitialize = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_Reinitialize)
    SetCurrentNodePair = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_SetCurrentNodePair)
    SetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_SetDomain)
    GetModifiableDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_GetModifiableDomain)
    GetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_GetDomain)
    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseID3ID3
    cast = _swig_new_static_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_cast)

# Register itkFastMarchingStoppingCriterionBaseID3ID3 in _itkFastMarchingStoppingCriterionBasePython:
_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_swigregister(itkFastMarchingStoppingCriterionBaseID3ID3)
itkFastMarchingStoppingCriterionBaseID3ID3_cast = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3_cast

class itkFastMarchingStoppingCriterionBaseID4ID4(itk.ITKCommonBasePython.itkStoppingCriterionBase):
    r"""


    Abstract Stopping Criterion dedicated for Fast Marching Methods. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    Reinitialize = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID4ID4_Reinitialize)
    SetCurrentNodePair = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID4ID4_SetCurrentNodePair)
    SetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID4ID4_SetDomain)
    GetModifiableDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID4ID4_GetModifiableDomain)
    GetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID4ID4_GetDomain)
    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseID4ID4
    cast = _swig_new_static_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID4ID4_cast)

# Register itkFastMarchingStoppingCriterionBaseID4ID4 in _itkFastMarchingStoppingCriterionBasePython:
_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID4ID4_swigregister(itkFastMarchingStoppingCriterionBaseID4ID4)
itkFastMarchingStoppingCriterionBaseID4ID4_cast = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID4ID4_cast

class itkFastMarchingStoppingCriterionBaseIF2IF2(itk.ITKCommonBasePython.itkStoppingCriterionBase):
    r"""


    Abstract Stopping Criterion dedicated for Fast Marching Methods. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    Reinitialize = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_Reinitialize)
    SetCurrentNodePair = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_SetCurrentNodePair)
    SetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_SetDomain)
    GetModifiableDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetModifiableDomain)
    GetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_GetDomain)
    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseIF2IF2
    cast = _swig_new_static_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_cast)

# Register itkFastMarchingStoppingCriterionBaseIF2IF2 in _itkFastMarchingStoppingCriterionBasePython:
_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_swigregister(itkFastMarchingStoppingCriterionBaseIF2IF2)
itkFastMarchingStoppingCriterionBaseIF2IF2_cast = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2_cast

class itkFastMarchingStoppingCriterionBaseIF3IF3(itk.ITKCommonBasePython.itkStoppingCriterionBase):
    r"""


    Abstract Stopping Criterion dedicated for Fast Marching Methods. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    Reinitialize = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_Reinitialize)
    SetCurrentNodePair = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_SetCurrentNodePair)
    SetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_SetDomain)
    GetModifiableDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetModifiableDomain)
    GetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_GetDomain)
    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseIF3IF3
    cast = _swig_new_static_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_cast)

# Register itkFastMarchingStoppingCriterionBaseIF3IF3 in _itkFastMarchingStoppingCriterionBasePython:
_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_swigregister(itkFastMarchingStoppingCriterionBaseIF3IF3)
itkFastMarchingStoppingCriterionBaseIF3IF3_cast = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3_cast

class itkFastMarchingStoppingCriterionBaseIF4IF4(itk.ITKCommonBasePython.itkStoppingCriterionBase):
    r"""


    Abstract Stopping Criterion dedicated for Fast Marching Methods. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    Reinitialize = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF4IF4_Reinitialize)
    SetCurrentNodePair = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF4IF4_SetCurrentNodePair)
    SetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF4IF4_SetDomain)
    GetModifiableDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF4IF4_GetModifiableDomain)
    GetDomain = _swig_new_instance_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF4IF4_GetDomain)
    __swig_destroy__ = _itkFastMarchingStoppingCriterionBasePython.delete_itkFastMarchingStoppingCriterionBaseIF4IF4
    cast = _swig_new_static_method(_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF4IF4_cast)

# Register itkFastMarchingStoppingCriterionBaseIF4IF4 in _itkFastMarchingStoppingCriterionBasePython:
_itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF4IF4_swigregister(itkFastMarchingStoppingCriterionBaseIF4IF4)
itkFastMarchingStoppingCriterionBaseIF4IF4_cast = _itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF4IF4_cast



