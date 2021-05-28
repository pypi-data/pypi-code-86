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
    from . import _itkScaleTransformPython
else:
    import _itkScaleTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkScaleTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkScaleTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.vnl_matrix_fixedPython
import itk.itkTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.itkOptimizerParametersPython
import itk.ITKCommonBasePython
import itk.itkArrayPython
import itk.itkVariableLengthVectorPython
import itk.itkArray2DPython
import itk.itkMatrixOffsetTransformBasePython

def itkScaleTransformD2_New():
    return itkScaleTransformD2.New()

class itkScaleTransformD2(itk.itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD22):
    r"""


    Scale transformation of a vector space (e.g. space coordinates)

    The same functionality could be obtained by using the Affine
    transform, but with a large difference in performance since the affine
    transform will use a matrix multiplication using a diagonal matrix.

    example{Core/Transform/ScaleAnImage,Scale An Image} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkScaleTransformPython.itkScaleTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD2_Clone)
    SetScale = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD2_SetScale)
    ComputeMatrix = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD2_ComputeMatrix)
    Compose = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD2_Compose)
    Scale = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD2_Scale)
    TransformVector = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD2_TransformVector)
    BackTransform = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD2_BackTransform)
    GetInverse = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD2_GetInverse)
    GetScale = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD2_GetScale)
    __swig_destroy__ = _itkScaleTransformPython.delete_itkScaleTransformD2
    cast = _swig_new_static_method(_itkScaleTransformPython.itkScaleTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkScaleTransformD2

        Create a new object of the class itkScaleTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScaleTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkScaleTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkScaleTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkScaleTransformD2 in _itkScaleTransformPython:
_itkScaleTransformPython.itkScaleTransformD2_swigregister(itkScaleTransformD2)
itkScaleTransformD2___New_orig__ = _itkScaleTransformPython.itkScaleTransformD2___New_orig__
itkScaleTransformD2_cast = _itkScaleTransformPython.itkScaleTransformD2_cast


def itkScaleTransformD3_New():
    return itkScaleTransformD3.New()

class itkScaleTransformD3(itk.itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD33):
    r"""


    Scale transformation of a vector space (e.g. space coordinates)

    The same functionality could be obtained by using the Affine
    transform, but with a large difference in performance since the affine
    transform will use a matrix multiplication using a diagonal matrix.

    example{Core/Transform/ScaleAnImage,Scale An Image} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkScaleTransformPython.itkScaleTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD3_Clone)
    SetScale = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD3_SetScale)
    ComputeMatrix = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD3_ComputeMatrix)
    Compose = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD3_Compose)
    Scale = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD3_Scale)
    TransformVector = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD3_TransformVector)
    BackTransform = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD3_BackTransform)
    GetInverse = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD3_GetInverse)
    GetScale = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD3_GetScale)
    __swig_destroy__ = _itkScaleTransformPython.delete_itkScaleTransformD3
    cast = _swig_new_static_method(_itkScaleTransformPython.itkScaleTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkScaleTransformD3

        Create a new object of the class itkScaleTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScaleTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkScaleTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkScaleTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkScaleTransformD3 in _itkScaleTransformPython:
_itkScaleTransformPython.itkScaleTransformD3_swigregister(itkScaleTransformD3)
itkScaleTransformD3___New_orig__ = _itkScaleTransformPython.itkScaleTransformD3___New_orig__
itkScaleTransformD3_cast = _itkScaleTransformPython.itkScaleTransformD3_cast


def itkScaleTransformD4_New():
    return itkScaleTransformD4.New()

class itkScaleTransformD4(itk.itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD44):
    r"""


    Scale transformation of a vector space (e.g. space coordinates)

    The same functionality could be obtained by using the Affine
    transform, but with a large difference in performance since the affine
    transform will use a matrix multiplication using a diagonal matrix.

    example{Core/Transform/ScaleAnImage,Scale An Image} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkScaleTransformPython.itkScaleTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD4_Clone)
    SetScale = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD4_SetScale)
    ComputeMatrix = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD4_ComputeMatrix)
    Compose = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD4_Compose)
    Scale = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD4_Scale)
    TransformVector = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD4_TransformVector)
    BackTransform = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD4_BackTransform)
    GetInverse = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD4_GetInverse)
    GetScale = _swig_new_instance_method(_itkScaleTransformPython.itkScaleTransformD4_GetScale)
    __swig_destroy__ = _itkScaleTransformPython.delete_itkScaleTransformD4
    cast = _swig_new_static_method(_itkScaleTransformPython.itkScaleTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkScaleTransformD4

        Create a new object of the class itkScaleTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScaleTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkScaleTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkScaleTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkScaleTransformD4 in _itkScaleTransformPython:
_itkScaleTransformPython.itkScaleTransformD4_swigregister(itkScaleTransformD4)
itkScaleTransformD4___New_orig__ = _itkScaleTransformPython.itkScaleTransformD4___New_orig__
itkScaleTransformD4_cast = _itkScaleTransformPython.itkScaleTransformD4_cast



