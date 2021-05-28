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
    from . import _itkFixedCenterOfRotationAffineTransformPython
else:
    import _itkFixedCenterOfRotationAffineTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkFixedCenterOfRotationAffineTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkFixedCenterOfRotationAffineTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkScalableAffineTransformPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.itkTransformBasePython
import itk.itkVariableLengthVectorPython
import itk.itkArray2DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.itkDiffusionTensor3DPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython

def itkFixedCenterOfRotationAffineTransformD2_New():
    return itkFixedCenterOfRotationAffineTransformD2.New()

class itkFixedCenterOfRotationAffineTransformD2(itk.itkScalableAffineTransformPython.itkScalableAffineTransformD2):
    r"""


    Affine transformation with a specified center of rotation.

    This class implements an Affine transform in which the rotation center
    can be explicitly selected. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_Clone)
    SetCenterOfRotationComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_SetCenterOfRotationComponent)
    GetCenterOfRotationComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_GetCenterOfRotationComponent)
    SetMatrixComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_SetMatrixComponent)
    GetMatrixComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_GetMatrixComponent)
    SetOffsetComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_SetOffsetComponent)
    GetOffsetComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_GetOffsetComponent)
    __swig_destroy__ = _itkFixedCenterOfRotationAffineTransformPython.delete_itkFixedCenterOfRotationAffineTransformD2
    cast = _swig_new_static_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkFixedCenterOfRotationAffineTransformD2

        Create a new object of the class itkFixedCenterOfRotationAffineTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFixedCenterOfRotationAffineTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFixedCenterOfRotationAffineTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFixedCenterOfRotationAffineTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFixedCenterOfRotationAffineTransformD2 in _itkFixedCenterOfRotationAffineTransformPython:
_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_swigregister(itkFixedCenterOfRotationAffineTransformD2)
itkFixedCenterOfRotationAffineTransformD2___New_orig__ = _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2___New_orig__
itkFixedCenterOfRotationAffineTransformD2_cast = _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_cast


def itkFixedCenterOfRotationAffineTransformD3_New():
    return itkFixedCenterOfRotationAffineTransformD3.New()

class itkFixedCenterOfRotationAffineTransformD3(itk.itkScalableAffineTransformPython.itkScalableAffineTransformD3):
    r"""


    Affine transformation with a specified center of rotation.

    This class implements an Affine transform in which the rotation center
    can be explicitly selected. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_Clone)
    SetCenterOfRotationComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_SetCenterOfRotationComponent)
    GetCenterOfRotationComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_GetCenterOfRotationComponent)
    SetMatrixComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_SetMatrixComponent)
    GetMatrixComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_GetMatrixComponent)
    SetOffsetComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_SetOffsetComponent)
    GetOffsetComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_GetOffsetComponent)
    __swig_destroy__ = _itkFixedCenterOfRotationAffineTransformPython.delete_itkFixedCenterOfRotationAffineTransformD3
    cast = _swig_new_static_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkFixedCenterOfRotationAffineTransformD3

        Create a new object of the class itkFixedCenterOfRotationAffineTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFixedCenterOfRotationAffineTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFixedCenterOfRotationAffineTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFixedCenterOfRotationAffineTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFixedCenterOfRotationAffineTransformD3 in _itkFixedCenterOfRotationAffineTransformPython:
_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_swigregister(itkFixedCenterOfRotationAffineTransformD3)
itkFixedCenterOfRotationAffineTransformD3___New_orig__ = _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3___New_orig__
itkFixedCenterOfRotationAffineTransformD3_cast = _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_cast


def itkFixedCenterOfRotationAffineTransformD4_New():
    return itkFixedCenterOfRotationAffineTransformD4.New()

class itkFixedCenterOfRotationAffineTransformD4(itk.itkScalableAffineTransformPython.itkScalableAffineTransformD4):
    r"""


    Affine transformation with a specified center of rotation.

    This class implements an Affine transform in which the rotation center
    can be explicitly selected. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4_Clone)
    SetCenterOfRotationComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4_SetCenterOfRotationComponent)
    GetCenterOfRotationComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4_GetCenterOfRotationComponent)
    SetMatrixComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4_SetMatrixComponent)
    GetMatrixComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4_GetMatrixComponent)
    SetOffsetComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4_SetOffsetComponent)
    GetOffsetComponent = _swig_new_instance_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4_GetOffsetComponent)
    __swig_destroy__ = _itkFixedCenterOfRotationAffineTransformPython.delete_itkFixedCenterOfRotationAffineTransformD4
    cast = _swig_new_static_method(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkFixedCenterOfRotationAffineTransformD4

        Create a new object of the class itkFixedCenterOfRotationAffineTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFixedCenterOfRotationAffineTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFixedCenterOfRotationAffineTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFixedCenterOfRotationAffineTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFixedCenterOfRotationAffineTransformD4 in _itkFixedCenterOfRotationAffineTransformPython:
_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4_swigregister(itkFixedCenterOfRotationAffineTransformD4)
itkFixedCenterOfRotationAffineTransformD4___New_orig__ = _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4___New_orig__
itkFixedCenterOfRotationAffineTransformD4_cast = _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD4_cast



