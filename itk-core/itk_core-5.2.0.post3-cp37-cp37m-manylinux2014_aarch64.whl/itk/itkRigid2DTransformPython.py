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
    from . import _itkRigid2DTransformPython
else:
    import _itkRigid2DTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRigid2DTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRigid2DTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkPointPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkVariableLengthVectorPython
import itk.ITKCommonBasePython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkArray2DPython
import itk.itkTransformBasePython

def itkRigid2DTransformD_New():
    return itkRigid2DTransformD.New()

class itkRigid2DTransformD(itk.itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD22):
    r"""


    Rigid2DTransform of a vector space (e.g. space coordinates)

    This transform applies a rigid transformation in 2D space. The
    transform is specified as a rotation around a arbitrary center and is
    followed by a translation.

    The parameters for this transform can be set either using individual
    Set methods or in serialized form using SetParameters() and
    SetFixedParameters().

    The serialization of the optimizable parameters is an array of 3
    elements ordered as follows: p[0] = angle p[1] = x component of the
    translation p[2] = y component of the translation

    The serialization of the fixed parameters is an array of 2 elements
    ordered as follows: p[0] = x coordinate of the center p[1] = y
    coordinate of the center

    Access methods for the center, translation and underlying matrix
    offset vectors are documented in the superclass
    MatrixOffsetTransformBase.

    See:  Transfrom

    See:   MatrixOffsetTransformBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRigid2DTransformPython.itkRigid2DTransformD___New_orig__)
    Clone = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_Clone)
    SetMatrix = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_SetMatrix)
    Translate = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_Translate)
    BackTransform = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_BackTransform)
    SetAngle = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_SetAngle)
    GetAngle = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_GetAngle)
    SetAngleInDegrees = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_SetAngleInDegrees)
    SetRotation = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_SetRotation)
    GetRotation = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_GetRotation)
    CloneInverseTo = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_CloneInverseTo)
    GetInverse = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_GetInverse)
    CloneTo = _swig_new_instance_method(_itkRigid2DTransformPython.itkRigid2DTransformD_CloneTo)
    __swig_destroy__ = _itkRigid2DTransformPython.delete_itkRigid2DTransformD
    cast = _swig_new_static_method(_itkRigid2DTransformPython.itkRigid2DTransformD_cast)

    def New(*args, **kargs):
        """New() -> itkRigid2DTransformD

        Create a new object of the class itkRigid2DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRigid2DTransformD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRigid2DTransformD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRigid2DTransformD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRigid2DTransformD in _itkRigid2DTransformPython:
_itkRigid2DTransformPython.itkRigid2DTransformD_swigregister(itkRigid2DTransformD)
itkRigid2DTransformD___New_orig__ = _itkRigid2DTransformPython.itkRigid2DTransformD___New_orig__
itkRigid2DTransformD_cast = _itkRigid2DTransformPython.itkRigid2DTransformD_cast



