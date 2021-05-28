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
    from . import _itkEuler2DTransformPython
else:
    import _itkEuler2DTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkEuler2DTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkEuler2DTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkTransformBasePython
import itk.itkArray2DPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
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
import itk.itkRigid2DTransformPython
import itk.itkMatrixOffsetTransformBasePython

def itkEuler2DTransformD_New():
    return itkEuler2DTransformD.New()

class itkEuler2DTransformD(itk.itkRigid2DTransformPython.itkRigid2DTransformD):
    r"""


    Euler2DTransform of a vector space (e.g. space coordinates)

    This transform applies a rigid transformation is 2D space. The
    transform is specified as a rotation around arbitrary center and is
    followed by a translation.

    This transform is basically is a synonym for Rigid2DTransform.

    See:   Rigid2DTransform 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEuler2DTransformPython.itkEuler2DTransformD___New_orig__)
    Clone = _swig_new_instance_method(_itkEuler2DTransformPython.itkEuler2DTransformD_Clone)
    CloneInverseTo = _swig_new_instance_method(_itkEuler2DTransformPython.itkEuler2DTransformD_CloneInverseTo)
    GetInverse = _swig_new_instance_method(_itkEuler2DTransformPython.itkEuler2DTransformD_GetInverse)
    CloneTo = _swig_new_instance_method(_itkEuler2DTransformPython.itkEuler2DTransformD_CloneTo)
    ComputeAngleFromMatrix = _swig_new_instance_method(_itkEuler2DTransformPython.itkEuler2DTransformD_ComputeAngleFromMatrix)
    __swig_destroy__ = _itkEuler2DTransformPython.delete_itkEuler2DTransformD
    cast = _swig_new_static_method(_itkEuler2DTransformPython.itkEuler2DTransformD_cast)

    def New(*args, **kargs):
        """New() -> itkEuler2DTransformD

        Create a new object of the class itkEuler2DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEuler2DTransformD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkEuler2DTransformD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkEuler2DTransformD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEuler2DTransformD in _itkEuler2DTransformPython:
_itkEuler2DTransformPython.itkEuler2DTransformD_swigregister(itkEuler2DTransformD)
itkEuler2DTransformD___New_orig__ = _itkEuler2DTransformPython.itkEuler2DTransformD___New_orig__
itkEuler2DTransformD_cast = _itkEuler2DTransformPython.itkEuler2DTransformD_cast



