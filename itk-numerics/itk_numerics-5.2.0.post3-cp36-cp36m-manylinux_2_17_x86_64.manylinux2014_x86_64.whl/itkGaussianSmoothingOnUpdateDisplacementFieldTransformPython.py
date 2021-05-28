# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKDisplacementFieldPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython
else:
    import _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkDisplacementFieldTransformPython
import itk.itkVariableLengthVectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkImagePython
import itk.itkVectorPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkRGBAPixelPython
import itk.itkCovariantVectorPython
import itk.itkSizePython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.ITKCommonBasePython
import itk.itkPointPython
import itk.itkRGBPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkTransformBasePython
import itk.itkArrayPython
import itk.itkDiffusionTensor3DPython
import itk.itkOptimizerParametersPython
import itk.itkArray2DPython

def itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_New():
    return itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.New()

class itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2(itk.itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2):
    r"""


    Modifies the UpdateTransformParameters method to peform a Gaussian
    smoothing of the displacement field after adding the update array.

    This class is the same as  DisplacementFieldTransform, except for the
    changes to UpdateTransformParameters. The method smooths the result of
    the addition of the update array and the displacement field, using a
    GaussianOperator filter.

    To free the memory allocated and cached in
    GaussianSmoothDisplacementField on demand, see
    FreeGaussianSmoothingTempField. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_Clone)
    SetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_SetGaussianSmoothingVarianceForTheUpdateField)
    GetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_GetGaussianSmoothingVarianceForTheUpdateField)
    SetGaussianSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_SetGaussianSmoothingVarianceForTheTotalField)
    GetGaussianSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_GetGaussianSmoothingVarianceForTheTotalField)
    UpdateTransformParameters = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_UpdateTransformParameters)
    GaussianSmoothDisplacementField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_GaussianSmoothDisplacementField)
    __swig_destroy__ = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.delete_itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2
    cast = _swig_new_static_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2

        Create a new object of the class itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2 in _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython:
_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_swigregister(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__ = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_cast = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD2_cast


def itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_New():
    return itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.New()

class itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3(itk.itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3):
    r"""


    Modifies the UpdateTransformParameters method to peform a Gaussian
    smoothing of the displacement field after adding the update array.

    This class is the same as  DisplacementFieldTransform, except for the
    changes to UpdateTransformParameters. The method smooths the result of
    the addition of the update array and the displacement field, using a
    GaussianOperator filter.

    To free the memory allocated and cached in
    GaussianSmoothDisplacementField on demand, see
    FreeGaussianSmoothingTempField. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_Clone)
    SetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_SetGaussianSmoothingVarianceForTheUpdateField)
    GetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_GetGaussianSmoothingVarianceForTheUpdateField)
    SetGaussianSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_SetGaussianSmoothingVarianceForTheTotalField)
    GetGaussianSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_GetGaussianSmoothingVarianceForTheTotalField)
    UpdateTransformParameters = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_UpdateTransformParameters)
    GaussianSmoothDisplacementField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_GaussianSmoothDisplacementField)
    __swig_destroy__ = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.delete_itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3
    cast = _swig_new_static_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3

        Create a new object of the class itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3 in _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython:
_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_swigregister(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__ = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_cast = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD3_cast


def itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_New():
    return itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4.New()

class itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4(itk.itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD4):
    r"""


    Modifies the UpdateTransformParameters method to peform a Gaussian
    smoothing of the displacement field after adding the update array.

    This class is the same as  DisplacementFieldTransform, except for the
    changes to UpdateTransformParameters. The method smooths the result of
    the addition of the update array and the displacement field, using a
    GaussianOperator filter.

    To free the memory allocated and cached in
    GaussianSmoothDisplacementField on demand, see
    FreeGaussianSmoothingTempField. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_Clone)
    SetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_SetGaussianSmoothingVarianceForTheUpdateField)
    GetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_GetGaussianSmoothingVarianceForTheUpdateField)
    SetGaussianSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_SetGaussianSmoothingVarianceForTheTotalField)
    GetGaussianSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_GetGaussianSmoothingVarianceForTheTotalField)
    UpdateTransformParameters = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_UpdateTransformParameters)
    GaussianSmoothDisplacementField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_GaussianSmoothDisplacementField)
    __swig_destroy__ = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.delete_itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4
    cast = _swig_new_static_method(_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4

        Create a new object of the class itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4 in _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython:
_itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_swigregister(itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4)
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4___New_orig__ = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4___New_orig__
itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_cast = _itkGaussianSmoothingOnUpdateDisplacementFieldTransformPython.itkGaussianSmoothingOnUpdateDisplacementFieldTransformD4_cast



