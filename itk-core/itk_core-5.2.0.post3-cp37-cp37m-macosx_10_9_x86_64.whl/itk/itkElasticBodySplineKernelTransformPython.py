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
    from . import _itkElasticBodySplineKernelTransformPython
else:
    import _itkElasticBodySplineKernelTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkElasticBodySplineKernelTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkElasticBodySplineKernelTransformPython.SWIG_PyStaticMethod_New

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

def itkElasticBodySplineKernelTransformD2_New():
    return itkElasticBodySplineKernelTransformD2.New()

class itkElasticBodySplineKernelTransformD2(itk.itkKernelTransformPython.itkKernelTransformD2):
    r"""


    This class defines the elastic body spline (EBS) transformation.

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
    __New_orig__ = _swig_new_static_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_Clone)
    SetAlpha = _swig_new_instance_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_GetAlpha)
    __swig_destroy__ = _itkElasticBodySplineKernelTransformPython.delete_itkElasticBodySplineKernelTransformD2
    cast = _swig_new_static_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkElasticBodySplineKernelTransformD2

        Create a new object of the class itkElasticBodySplineKernelTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkElasticBodySplineKernelTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkElasticBodySplineKernelTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkElasticBodySplineKernelTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkElasticBodySplineKernelTransformD2 in _itkElasticBodySplineKernelTransformPython:
_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_swigregister(itkElasticBodySplineKernelTransformD2)
itkElasticBodySplineKernelTransformD2___New_orig__ = _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2___New_orig__
itkElasticBodySplineKernelTransformD2_cast = _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_cast


def itkElasticBodySplineKernelTransformD3_New():
    return itkElasticBodySplineKernelTransformD3.New()

class itkElasticBodySplineKernelTransformD3(itk.itkKernelTransformPython.itkKernelTransformD3):
    r"""


    This class defines the elastic body spline (EBS) transformation.

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
    __New_orig__ = _swig_new_static_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_Clone)
    SetAlpha = _swig_new_instance_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_GetAlpha)
    __swig_destroy__ = _itkElasticBodySplineKernelTransformPython.delete_itkElasticBodySplineKernelTransformD3
    cast = _swig_new_static_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkElasticBodySplineKernelTransformD3

        Create a new object of the class itkElasticBodySplineKernelTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkElasticBodySplineKernelTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkElasticBodySplineKernelTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkElasticBodySplineKernelTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkElasticBodySplineKernelTransformD3 in _itkElasticBodySplineKernelTransformPython:
_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_swigregister(itkElasticBodySplineKernelTransformD3)
itkElasticBodySplineKernelTransformD3___New_orig__ = _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3___New_orig__
itkElasticBodySplineKernelTransformD3_cast = _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_cast


def itkElasticBodySplineKernelTransformD4_New():
    return itkElasticBodySplineKernelTransformD4.New()

class itkElasticBodySplineKernelTransformD4(itk.itkKernelTransformPython.itkKernelTransformD4):
    r"""


    This class defines the elastic body spline (EBS) transformation.

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
    __New_orig__ = _swig_new_static_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD4_Clone)
    SetAlpha = _swig_new_instance_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD4_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD4_GetAlpha)
    __swig_destroy__ = _itkElasticBodySplineKernelTransformPython.delete_itkElasticBodySplineKernelTransformD4
    cast = _swig_new_static_method(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkElasticBodySplineKernelTransformD4

        Create a new object of the class itkElasticBodySplineKernelTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkElasticBodySplineKernelTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkElasticBodySplineKernelTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkElasticBodySplineKernelTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkElasticBodySplineKernelTransformD4 in _itkElasticBodySplineKernelTransformPython:
_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD4_swigregister(itkElasticBodySplineKernelTransformD4)
itkElasticBodySplineKernelTransformD4___New_orig__ = _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD4___New_orig__
itkElasticBodySplineKernelTransformD4_cast = _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD4_cast



