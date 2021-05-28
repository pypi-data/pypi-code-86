# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageIntensityPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkSymmetricEigenAnalysisImageFilterPython
else:
    import _itkSymmetricEigenAnalysisImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSymmetricEigenAnalysisImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSymmetricEigenAnalysisImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkImageToImageFilterBPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.stdcomplexPython
import itk.itkImagePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkFixedArrayPython
import itk.itkMatrixPython
import itk.vnl_matrixPython
import itk.vnl_vectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
class itkSymmetricEigenAnalysisEnums(object):
    r"""Proxy of C++ itkSymmetricEigenAnalysisEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    EigenValueOrder_OrderByValue = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisEnums_EigenValueOrder_OrderByValue
    
    EigenValueOrder_OrderByMagnitude = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisEnums_EigenValueOrder_OrderByMagnitude
    
    EigenValueOrder_DoNotOrder = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisEnums_EigenValueOrder_DoNotOrder
    

    def __init__(self, *args):
        r"""
        __init__(self) -> itkSymmetricEigenAnalysisEnums
        __init__(self, arg0) -> itkSymmetricEigenAnalysisEnums

        Parameters
        ----------
        arg0: itkSymmetricEigenAnalysisEnums const &

        """
        _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisEnums_swiginit(self, _itkSymmetricEigenAnalysisImageFilterPython.new_itkSymmetricEigenAnalysisEnums(*args))
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisEnums

# Register itkSymmetricEigenAnalysisEnums in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisEnums_swigregister(itkSymmetricEigenAnalysisEnums)

class itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass(itk.itkImageToImageFilterBPython.itkImageToImageFilterISSRTD22ISSRTD22):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_SetInPlace)
    GetInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_GetInPlace)
    InPlaceOn = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_InPlaceOn)
    InPlaceOff = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_InPlaceOff)
    CanRunInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_CanRunInPlace)
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_cast)

# Register itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass)
itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_cast

class itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass(itk.itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33ISSRTD33):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_SetInPlace)
    GetInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_GetInPlace)
    InPlaceOn = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_InPlaceOn)
    InPlaceOff = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_InPlaceOff)
    CanRunInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_CanRunInPlace)
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_cast)

# Register itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass)
itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_cast

class itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass(itk.itkImageToImageFilterBPython.itkImageToImageFilterISSRTD44ISSRTD44):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass_SetInPlace)
    GetInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass_GetInPlace)
    InPlaceOn = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass_InPlaceOn)
    InPlaceOff = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass_InPlaceOff)
    CanRunInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass_CanRunInPlace)
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass_cast)

# Register itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass)
itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass_cast


def itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_New():
    return itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass.New()

class itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass(itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Clone)
    GetFunctor = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_GetFunctor)
    SetFunctor = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_SetFunctor)
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass)
itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass___New_orig__ = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass___New_orig__
itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_cast


def itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_New():
    return itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass.New()

class itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass(itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Clone)
    GetFunctor = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_GetFunctor)
    SetFunctor = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_SetFunctor)
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass)
itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass___New_orig__ = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass___New_orig__
itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_cast


def itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_New():
    return itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass.New()

class itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass(itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Superclass):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_Clone)
    GetFunctor = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_GetFunctor)
    SetFunctor = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_SetFunctor)
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass)
itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass___New_orig__ = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass___New_orig__
itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass_cast


def itkSymmetricEigenAnalysisImageFilterISSRTD22_New():
    return itkSymmetricEigenAnalysisImageFilterISSRTD22.New()

class itkSymmetricEigenAnalysisImageFilterISSRTD22(itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass):
    r"""


    Computes the eigen-values of every input symmetric matrix pixel.

    SymmetricEigenAnalysisImageFilter applies pixel-wise the invocation
    for computing the eigen-values and eigen-vectors of the symmetric
    matrix corresponding to every input pixel.

    The OrderEigenValuesBy( .. ) method can be used to order eigen values
    in ascending order by value or magnitude or no ordering. OrderByValue:
    lambda_1 < lambda_2 < .... OrderByMagnitude: |lambda_1| < |lambda_2| <
    ..... DoNotOrder: Default order of eigen values obtained after QL
    method 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    OrderEigenValuesBy = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_OrderEigenValuesBy)
    SetOrderEigenValuesBy = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_SetOrderEigenValuesBy)
    GetOrderEigenValuesBy = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_GetOrderEigenValuesBy)
    __New_orig__ = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22___New_orig__)
    Clone = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Clone)
    PrintSelf = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_PrintSelf)
    SetDimension = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_GetDimension)
    InputHasNumericTraitsCheck = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD22
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD22

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD22.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD22.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD22.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD22 in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD22)
itkSymmetricEigenAnalysisImageFilterISSRTD22___New_orig__ = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22___New_orig__
itkSymmetricEigenAnalysisImageFilterISSRTD22_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_cast


def itkSymmetricEigenAnalysisImageFilterISSRTD33_New():
    return itkSymmetricEigenAnalysisImageFilterISSRTD33.New()

class itkSymmetricEigenAnalysisImageFilterISSRTD33(itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass):
    r"""


    Computes the eigen-values of every input symmetric matrix pixel.

    SymmetricEigenAnalysisImageFilter applies pixel-wise the invocation
    for computing the eigen-values and eigen-vectors of the symmetric
    matrix corresponding to every input pixel.

    The OrderEigenValuesBy( .. ) method can be used to order eigen values
    in ascending order by value or magnitude or no ordering. OrderByValue:
    lambda_1 < lambda_2 < .... OrderByMagnitude: |lambda_1| < |lambda_2| <
    ..... DoNotOrder: Default order of eigen values obtained after QL
    method 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    OrderEigenValuesBy = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_OrderEigenValuesBy)
    SetOrderEigenValuesBy = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_SetOrderEigenValuesBy)
    GetOrderEigenValuesBy = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_GetOrderEigenValuesBy)
    __New_orig__ = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33___New_orig__)
    Clone = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Clone)
    PrintSelf = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_PrintSelf)
    SetDimension = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_GetDimension)
    InputHasNumericTraitsCheck = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD33
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD33

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD33.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD33.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD33.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD33 in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD33)
itkSymmetricEigenAnalysisImageFilterISSRTD33___New_orig__ = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33___New_orig__
itkSymmetricEigenAnalysisImageFilterISSRTD33_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_cast


def itkSymmetricEigenAnalysisImageFilterISSRTD44_New():
    return itkSymmetricEigenAnalysisImageFilterISSRTD44.New()

class itkSymmetricEigenAnalysisImageFilterISSRTD44(itkSymmetricEigenAnalysisImageFilterISSRTD44_Superclass):
    r"""


    Computes the eigen-values of every input symmetric matrix pixel.

    SymmetricEigenAnalysisImageFilter applies pixel-wise the invocation
    for computing the eigen-values and eigen-vectors of the symmetric
    matrix corresponding to every input pixel.

    The OrderEigenValuesBy( .. ) method can be used to order eigen values
    in ascending order by value or magnitude or no ordering. OrderByValue:
    lambda_1 < lambda_2 < .... OrderByMagnitude: |lambda_1| < |lambda_2| <
    ..... DoNotOrder: Default order of eigen values obtained after QL
    method 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    OrderEigenValuesBy = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_OrderEigenValuesBy)
    SetOrderEigenValuesBy = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_SetOrderEigenValuesBy)
    GetOrderEigenValuesBy = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_GetOrderEigenValuesBy)
    __New_orig__ = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44___New_orig__)
    Clone = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_Clone)
    PrintSelf = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_PrintSelf)
    SetDimension = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_GetDimension)
    InputHasNumericTraitsCheck = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD44
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD44

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD44 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD44.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD44.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD44.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD44 in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD44)
itkSymmetricEigenAnalysisImageFilterISSRTD44___New_orig__ = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44___New_orig__
itkSymmetricEigenAnalysisImageFilterISSRTD44_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD44_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def unary_functor_image_filter(*args: itkt.ImageLike,  functor=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for UnaryFunctorImageFilter"""
    import itk

    kwarg_typehints = { 'functor':functor }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.UnaryFunctorImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def unary_functor_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.UnaryFunctorImageFilter
    unary_functor_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    unary_functor_image_filter.__doc__ = filter_object.__doc__

from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def symmetric_eigen_analysis_image_filter(*args: itkt.ImageLike,  order_eigen_values_by=..., dimension: int=..., functor=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for SymmetricEigenAnalysisImageFilter"""
    import itk

    kwarg_typehints = { 'order_eigen_values_by':order_eigen_values_by,'dimension':dimension,'functor':functor }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.SymmetricEigenAnalysisImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def symmetric_eigen_analysis_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.SymmetricEigenAnalysisImageFilter
    symmetric_eigen_analysis_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    symmetric_eigen_analysis_image_filter.__doc__ = filter_object.__doc__

from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def in_place_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for InPlaceImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.InPlaceImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def in_place_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.InPlaceImageFilter
    in_place_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    in_place_image_filter.__doc__ = filter_object.__doc__




