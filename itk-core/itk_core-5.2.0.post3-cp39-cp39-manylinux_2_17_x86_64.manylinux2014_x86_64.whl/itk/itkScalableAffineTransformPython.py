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
    from . import _itkScalableAffineTransformPython
else:
    import _itkScalableAffineTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkScalableAffineTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkScalableAffineTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkFixedArrayPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkVariableLengthVectorPython
import itk.itkArray2DPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.itkDiffusionTensor3DPython
import itk.itkMatrixOffsetTransformBasePython

def itkScalableAffineTransformD2_New():
    return itkScalableAffineTransformD2.New()

class itkScalableAffineTransformD2(itk.itkAffineTransformPython.itkAffineTransformD2):
    r"""


    Affine transformation with a specified center of rotation.

    This class implements an Affine transform in which the rotation center
    can be explicitly selected. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD2_Clone)
    SetScale = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD2_SetScale)
    SetScaleComponent = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD2_SetScaleComponent)
    GetScale = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD2_GetScale)
    GetScaleComponent = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD2_GetScaleComponent)
    GetInverse = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD2_GetInverse)
    __swig_destroy__ = _itkScalableAffineTransformPython.delete_itkScalableAffineTransformD2
    cast = _swig_new_static_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkScalableAffineTransformD2

        Create a new object of the class itkScalableAffineTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScalableAffineTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkScalableAffineTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkScalableAffineTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkScalableAffineTransformD2 in _itkScalableAffineTransformPython:
_itkScalableAffineTransformPython.itkScalableAffineTransformD2_swigregister(itkScalableAffineTransformD2)
itkScalableAffineTransformD2___New_orig__ = _itkScalableAffineTransformPython.itkScalableAffineTransformD2___New_orig__
itkScalableAffineTransformD2_cast = _itkScalableAffineTransformPython.itkScalableAffineTransformD2_cast


def itkScalableAffineTransformD3_New():
    return itkScalableAffineTransformD3.New()

class itkScalableAffineTransformD3(itk.itkAffineTransformPython.itkAffineTransformD3):
    r"""


    Affine transformation with a specified center of rotation.

    This class implements an Affine transform in which the rotation center
    can be explicitly selected. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD3_Clone)
    SetScale = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD3_SetScale)
    SetScaleComponent = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD3_SetScaleComponent)
    GetScale = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD3_GetScale)
    GetScaleComponent = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD3_GetScaleComponent)
    GetInverse = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD3_GetInverse)
    __swig_destroy__ = _itkScalableAffineTransformPython.delete_itkScalableAffineTransformD3
    cast = _swig_new_static_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkScalableAffineTransformD3

        Create a new object of the class itkScalableAffineTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScalableAffineTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkScalableAffineTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkScalableAffineTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkScalableAffineTransformD3 in _itkScalableAffineTransformPython:
_itkScalableAffineTransformPython.itkScalableAffineTransformD3_swigregister(itkScalableAffineTransformD3)
itkScalableAffineTransformD3___New_orig__ = _itkScalableAffineTransformPython.itkScalableAffineTransformD3___New_orig__
itkScalableAffineTransformD3_cast = _itkScalableAffineTransformPython.itkScalableAffineTransformD3_cast


def itkScalableAffineTransformD4_New():
    return itkScalableAffineTransformD4.New()

class itkScalableAffineTransformD4(itk.itkAffineTransformPython.itkAffineTransformD4):
    r"""


    Affine transformation with a specified center of rotation.

    This class implements an Affine transform in which the rotation center
    can be explicitly selected. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD4_Clone)
    SetScale = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD4_SetScale)
    SetScaleComponent = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD4_SetScaleComponent)
    GetScale = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD4_GetScale)
    GetScaleComponent = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD4_GetScaleComponent)
    GetInverse = _swig_new_instance_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD4_GetInverse)
    __swig_destroy__ = _itkScalableAffineTransformPython.delete_itkScalableAffineTransformD4
    cast = _swig_new_static_method(_itkScalableAffineTransformPython.itkScalableAffineTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkScalableAffineTransformD4

        Create a new object of the class itkScalableAffineTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScalableAffineTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkScalableAffineTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkScalableAffineTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkScalableAffineTransformD4 in _itkScalableAffineTransformPython:
_itkScalableAffineTransformPython.itkScalableAffineTransformD4_swigregister(itkScalableAffineTransformD4)
itkScalableAffineTransformD4___New_orig__ = _itkScalableAffineTransformPython.itkScalableAffineTransformD4___New_orig__
itkScalableAffineTransformD4_cast = _itkScalableAffineTransformPython.itkScalableAffineTransformD4_cast



