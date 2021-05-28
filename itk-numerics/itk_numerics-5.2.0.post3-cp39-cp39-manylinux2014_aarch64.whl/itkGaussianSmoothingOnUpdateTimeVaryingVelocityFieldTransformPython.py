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
    from . import _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython
else:
    import _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkRGBPixelPython
import itk.ITKCommonBasePython
import itk.itkImageRegionPython
import itk.itkTimeVaryingVelocityFieldTransformPython
import itk.itkVelocityFieldTransformPython
import itk.itkDisplacementFieldTransformPython
import itk.itkArray2DPython
import itk.itkTransformBasePython
import itk.itkVariableLengthVectorPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.itkDiffusionTensor3DPython

def itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_New():
    return itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.New()

class itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2(itk.itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2):
    r"""


    Modifies the UpdateTransformParameters method to peform a Gaussian
    smoothing of the velocity field after adding the update array.

    This class is the same as  TimeVaryingVelocityFieldTransform, except
    for the changes to UpdateTransformParameters. The method smooths the
    result of the addition of the update array and the displacement field,
    using a GaussianOperator filter. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_Clone)
    SetGaussianSpatialSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianSpatialSmoothingVarianceForTheUpdateField)
    GetGaussianSpatialSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianSpatialSmoothingVarianceForTheUpdateField)
    SetGaussianTemporalSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianTemporalSmoothingVarianceForTheUpdateField)
    GetGaussianTemporalSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianTemporalSmoothingVarianceForTheUpdateField)
    SetGaussianSpatialSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianSpatialSmoothingVarianceForTheTotalField)
    GetGaussianSpatialSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianSpatialSmoothingVarianceForTheTotalField)
    SetGaussianTemporalSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_SetGaussianTemporalSmoothingVarianceForTheTotalField)
    GetGaussianTemporalSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GetGaussianTemporalSmoothingVarianceForTheTotalField)
    UpdateTransformParameters = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_UpdateTransformParameters)
    GaussianSmoothTimeVaryingVelocityField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_GaussianSmoothTimeVaryingVelocityField)
    __swig_destroy__ = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.delete_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2
    cast = _swig_new_static_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2

        Create a new object of the class itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2 in _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython:
_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_swigregister(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2___New_orig__ = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2___New_orig__
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_cast = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD2_cast


def itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_New():
    return itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.New()

class itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3(itk.itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3):
    r"""


    Modifies the UpdateTransformParameters method to peform a Gaussian
    smoothing of the velocity field after adding the update array.

    This class is the same as  TimeVaryingVelocityFieldTransform, except
    for the changes to UpdateTransformParameters. The method smooths the
    result of the addition of the update array and the displacement field,
    using a GaussianOperator filter. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_Clone)
    SetGaussianSpatialSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianSpatialSmoothingVarianceForTheUpdateField)
    GetGaussianSpatialSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianSpatialSmoothingVarianceForTheUpdateField)
    SetGaussianTemporalSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianTemporalSmoothingVarianceForTheUpdateField)
    GetGaussianTemporalSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianTemporalSmoothingVarianceForTheUpdateField)
    SetGaussianSpatialSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianSpatialSmoothingVarianceForTheTotalField)
    GetGaussianSpatialSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianSpatialSmoothingVarianceForTheTotalField)
    SetGaussianTemporalSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_SetGaussianTemporalSmoothingVarianceForTheTotalField)
    GetGaussianTemporalSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GetGaussianTemporalSmoothingVarianceForTheTotalField)
    UpdateTransformParameters = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_UpdateTransformParameters)
    GaussianSmoothTimeVaryingVelocityField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_GaussianSmoothTimeVaryingVelocityField)
    __swig_destroy__ = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.delete_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3
    cast = _swig_new_static_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3

        Create a new object of the class itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3 in _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython:
_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_swigregister(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3___New_orig__ = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3___New_orig__
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_cast = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD3_cast


def itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_New():
    return itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4.New()

class itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4(itk.itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD4):
    r"""


    Modifies the UpdateTransformParameters method to peform a Gaussian
    smoothing of the velocity field after adding the update array.

    This class is the same as  TimeVaryingVelocityFieldTransform, except
    for the changes to UpdateTransformParameters. The method smooths the
    result of the addition of the update array and the displacement field,
    using a GaussianOperator filter. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_Clone)
    SetGaussianSpatialSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_SetGaussianSpatialSmoothingVarianceForTheUpdateField)
    GetGaussianSpatialSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_GetGaussianSpatialSmoothingVarianceForTheUpdateField)
    SetGaussianTemporalSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_SetGaussianTemporalSmoothingVarianceForTheUpdateField)
    GetGaussianTemporalSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_GetGaussianTemporalSmoothingVarianceForTheUpdateField)
    SetGaussianSpatialSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_SetGaussianSpatialSmoothingVarianceForTheTotalField)
    GetGaussianSpatialSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_GetGaussianSpatialSmoothingVarianceForTheTotalField)
    SetGaussianTemporalSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_SetGaussianTemporalSmoothingVarianceForTheTotalField)
    GetGaussianTemporalSmoothingVarianceForTheTotalField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_GetGaussianTemporalSmoothingVarianceForTheTotalField)
    UpdateTransformParameters = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_UpdateTransformParameters)
    GaussianSmoothTimeVaryingVelocityField = _swig_new_instance_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_GaussianSmoothTimeVaryingVelocityField)
    __swig_destroy__ = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.delete_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4
    cast = _swig_new_static_method(_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4

        Create a new object of the class itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4 in _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython:
_itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_swigregister(itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4)
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4___New_orig__ = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4___New_orig__
itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_cast = _itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformPython.itkGaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransformD4_cast



