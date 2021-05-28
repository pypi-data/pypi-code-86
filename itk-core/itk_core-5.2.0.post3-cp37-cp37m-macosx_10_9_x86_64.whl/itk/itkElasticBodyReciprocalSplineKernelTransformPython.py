# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKTransformPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkElasticBodyReciprocalSplineKernelTransformPython
else:
    import _itkElasticBodyReciprocalSplineKernelTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkElasticBodyReciprocalSplineKernelTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkElasticBodyReciprocalSplineKernelTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkKernelTransformPython
import itk.itkTransformBasePython
import itk.itkArray2DPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.ITKCommonBasePython
import itk.itkCovariantVectorPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkArrayPython
import itk.itkPointPython
import itk.itkVariableLengthVectorPython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkOptimizerParametersPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkPointSetPython

def itkElasticBodyReciprocalSplineKernelTransformD2_New():
    return itkElasticBodyReciprocalSplineKernelTransformD2.New()

class itkElasticBodyReciprocalSplineKernelTransformD2(itk.itkKernelTransformPython.itkKernelTransformD2):
    r"""


    This class defines the elastic body spline (EBS) transformation. It is
    implemented in as straightforward a manner as possible from the IEEE
    TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol. 16 No. 3 June
    1997 Taken from the paper: The EBS "is based on a physical model of a
    homogeneous, isotropic, three-dimensional elastic body. The model can
    approximate the way that some physical objects deform". 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD2_Clone)
    SetAlpha = _swig_new_instance_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD2_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD2_GetAlpha)
    __swig_destroy__ = _itkElasticBodyReciprocalSplineKernelTransformPython.delete_itkElasticBodyReciprocalSplineKernelTransformD2
    cast = _swig_new_static_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkElasticBodyReciprocalSplineKernelTransformD2

        Create a new object of the class itkElasticBodyReciprocalSplineKernelTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkElasticBodyReciprocalSplineKernelTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkElasticBodyReciprocalSplineKernelTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkElasticBodyReciprocalSplineKernelTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkElasticBodyReciprocalSplineKernelTransformD2 in _itkElasticBodyReciprocalSplineKernelTransformPython:
_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD2_swigregister(itkElasticBodyReciprocalSplineKernelTransformD2)
itkElasticBodyReciprocalSplineKernelTransformD2___New_orig__ = _itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD2___New_orig__
itkElasticBodyReciprocalSplineKernelTransformD2_cast = _itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD2_cast


def itkElasticBodyReciprocalSplineKernelTransformD3_New():
    return itkElasticBodyReciprocalSplineKernelTransformD3.New()

class itkElasticBodyReciprocalSplineKernelTransformD3(itk.itkKernelTransformPython.itkKernelTransformD3):
    r"""


    This class defines the elastic body spline (EBS) transformation. It is
    implemented in as straightforward a manner as possible from the IEEE
    TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol. 16 No. 3 June
    1997 Taken from the paper: The EBS "is based on a physical model of a
    homogeneous, isotropic, three-dimensional elastic body. The model can
    approximate the way that some physical objects deform". 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD3_Clone)
    SetAlpha = _swig_new_instance_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD3_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD3_GetAlpha)
    __swig_destroy__ = _itkElasticBodyReciprocalSplineKernelTransformPython.delete_itkElasticBodyReciprocalSplineKernelTransformD3
    cast = _swig_new_static_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkElasticBodyReciprocalSplineKernelTransformD3

        Create a new object of the class itkElasticBodyReciprocalSplineKernelTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkElasticBodyReciprocalSplineKernelTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkElasticBodyReciprocalSplineKernelTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkElasticBodyReciprocalSplineKernelTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkElasticBodyReciprocalSplineKernelTransformD3 in _itkElasticBodyReciprocalSplineKernelTransformPython:
_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD3_swigregister(itkElasticBodyReciprocalSplineKernelTransformD3)
itkElasticBodyReciprocalSplineKernelTransformD3___New_orig__ = _itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD3___New_orig__
itkElasticBodyReciprocalSplineKernelTransformD3_cast = _itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD3_cast


def itkElasticBodyReciprocalSplineKernelTransformD4_New():
    return itkElasticBodyReciprocalSplineKernelTransformD4.New()

class itkElasticBodyReciprocalSplineKernelTransformD4(itk.itkKernelTransformPython.itkKernelTransformD4):
    r"""


    This class defines the elastic body spline (EBS) transformation. It is
    implemented in as straightforward a manner as possible from the IEEE
    TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol. 16 No. 3 June
    1997 Taken from the paper: The EBS "is based on a physical model of a
    homogeneous, isotropic, three-dimensional elastic body. The model can
    approximate the way that some physical objects deform". 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD4_Clone)
    SetAlpha = _swig_new_instance_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD4_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD4_GetAlpha)
    __swig_destroy__ = _itkElasticBodyReciprocalSplineKernelTransformPython.delete_itkElasticBodyReciprocalSplineKernelTransformD4
    cast = _swig_new_static_method(_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkElasticBodyReciprocalSplineKernelTransformD4

        Create a new object of the class itkElasticBodyReciprocalSplineKernelTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkElasticBodyReciprocalSplineKernelTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkElasticBodyReciprocalSplineKernelTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkElasticBodyReciprocalSplineKernelTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkElasticBodyReciprocalSplineKernelTransformD4 in _itkElasticBodyReciprocalSplineKernelTransformPython:
_itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD4_swigregister(itkElasticBodyReciprocalSplineKernelTransformD4)
itkElasticBodyReciprocalSplineKernelTransformD4___New_orig__ = _itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD4___New_orig__
itkElasticBodyReciprocalSplineKernelTransformD4_cast = _itkElasticBodyReciprocalSplineKernelTransformPython.itkElasticBodyReciprocalSplineKernelTransformD4_cast



