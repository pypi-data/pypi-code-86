# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKCommonPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkVersorPython
else:
    import _itkVersorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVersorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVersorPython.SWIG_PyStaticMethod_New

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
class itkVersorD(object):
    r"""


    A templated class holding a unit quaternion.

    Versor is a templated class that holds a unit quaternion. The
    difference between versors and quaternions is that quaternions can
    represent rotations and scale changes while versors are limited to
    rotations.

    This class only implements the operations that maintain versors as a
    group, that is, any operations between versors result in another
    versor. For this reason, addition is not defined in this class, even
    though it is a valid operation between quaternions.

    See:   Vector

    See:   Point

    See:   CovariantVector

    See:   Matrix 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GetVnlQuaternion = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetVnlQuaternion)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkVersorD
        __init__(self, v) -> itkVersorD

        Parameters
        ----------
        v: itkVersorD const &



        A templated class holding a unit quaternion.

        Versor is a templated class that holds a unit quaternion. The
        difference between versors and quaternions is that quaternions can
        represent rotations and scale changes while versors are limited to
        rotations.

        This class only implements the operations that maintain versors as a
        group, that is, any operations between versors result in another
        versor. For this reason, addition is not defined in this class, even
        though it is a valid operation between quaternions.

        See:   Vector

        See:   Point

        See:   CovariantVector

        See:   Matrix 
        """
        _itkVersorPython.itkVersorD_swiginit(self, _itkVersorPython.new_itkVersorD(*args))
    __imul__ = _swig_new_instance_method(_itkVersorPython.itkVersorD___imul__)

    def __itruediv__(self, *args):
        return _itkVersorPython.itkVersorD___itruediv__(self, *args)
    __idiv__ = __itruediv__


    GetTensor = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetTensor)
    Normalize = _swig_new_instance_method(_itkVersorPython.itkVersorD_Normalize)
    GetConjugate = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetConjugate)
    GetReciprocal = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetReciprocal)
    __mul__ = _swig_new_instance_method(_itkVersorPython.itkVersorD___mul__)

    def __truediv__(self, *args):
        return _itkVersorPython.itkVersorD___truediv__(self, *args)
    __div__ = __truediv__


    __eq__ = _swig_new_instance_method(_itkVersorPython.itkVersorD___eq__)
    __ne__ = _swig_new_instance_method(_itkVersorPython.itkVersorD___ne__)
    GetScalar = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetScalar)
    GetX = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetX)
    GetY = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetY)
    GetZ = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetZ)
    GetW = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetW)
    GetAngle = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetAngle)
    GetAxis = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetAxis)
    GetRight = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetRight)
    Set = _swig_new_instance_method(_itkVersorPython.itkVersorD_Set)
    SetRotationAroundX = _swig_new_instance_method(_itkVersorPython.itkVersorD_SetRotationAroundX)
    SetRotationAroundY = _swig_new_instance_method(_itkVersorPython.itkVersorD_SetRotationAroundY)
    SetRotationAroundZ = _swig_new_instance_method(_itkVersorPython.itkVersorD_SetRotationAroundZ)
    SetIdentity = _swig_new_instance_method(_itkVersorPython.itkVersorD_SetIdentity)
    Transform = _swig_new_instance_method(_itkVersorPython.itkVersorD_Transform)
    GetMatrix = _swig_new_instance_method(_itkVersorPython.itkVersorD_GetMatrix)
    SquareRoot = _swig_new_instance_method(_itkVersorPython.itkVersorD_SquareRoot)
    Exponential = _swig_new_instance_method(_itkVersorPython.itkVersorD_Exponential)
    __swig_destroy__ = _itkVersorPython.delete_itkVersorD

# Register itkVersorD in _itkVersorPython:
_itkVersorPython.itkVersorD_swigregister(itkVersorD)



