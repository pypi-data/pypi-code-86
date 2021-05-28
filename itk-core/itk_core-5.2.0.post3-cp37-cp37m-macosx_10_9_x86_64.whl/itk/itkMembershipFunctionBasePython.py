# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKStatisticsPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkMembershipFunctionBasePython
else:
    import _itkMembershipFunctionBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMembershipFunctionBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMembershipFunctionBasePython.SWIG_PyStaticMethod_New

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
import itk.itkFunctionBasePython
import itk.itkContinuousIndexPython
import itk.itkPointPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkImagePython
import itk.itkImageRegionPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkArrayPython
class itkMembershipFunctionBaseVF2(itk.itkFunctionBasePython.itkFunctionBaseVF2D):
    r"""


    MembershipFunctionBase defines common interfaces for membership
    functions.

    MembershipFunctionBase is a subclass of FunctionBase which restricts
    the function type to be a membership function. Membership functions
    provide a mapping from an arbitrary domain to a set of real numbers.
    Membership functions are typically used to model or approximate
    likelihood functions, $p( x | i )$, i.e. the probability of the
    measurement $x$ belonging to a class $i$.

    The Statistics framework models random variables $x$ as vectors.
    Typical uses of MembershipFunctions include templating over a
    FixedArray, Array, Vector, or VariableLengthVector.

    The Evaluate() method returns the membership rank or likelihood that
    the measurement belongs to the class represented by this membership
    function.

    Evaluations of a single measurement across of set MembershipFunctions
    can then be passed to a DecisionRule in order to establish class (or
    group) assignment. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetMeasurementVectorSize = _swig_new_instance_method(_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF2_SetMeasurementVectorSize)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF2_GetMeasurementVectorSize)
    __swig_destroy__ = _itkMembershipFunctionBasePython.delete_itkMembershipFunctionBaseVF2
    cast = _swig_new_static_method(_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF2_cast)

# Register itkMembershipFunctionBaseVF2 in _itkMembershipFunctionBasePython:
_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF2_swigregister(itkMembershipFunctionBaseVF2)
itkMembershipFunctionBaseVF2_cast = _itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF2_cast

class itkMembershipFunctionBaseVF3(itk.itkFunctionBasePython.itkFunctionBaseVF3D):
    r"""


    MembershipFunctionBase defines common interfaces for membership
    functions.

    MembershipFunctionBase is a subclass of FunctionBase which restricts
    the function type to be a membership function. Membership functions
    provide a mapping from an arbitrary domain to a set of real numbers.
    Membership functions are typically used to model or approximate
    likelihood functions, $p( x | i )$, i.e. the probability of the
    measurement $x$ belonging to a class $i$.

    The Statistics framework models random variables $x$ as vectors.
    Typical uses of MembershipFunctions include templating over a
    FixedArray, Array, Vector, or VariableLengthVector.

    The Evaluate() method returns the membership rank or likelihood that
    the measurement belongs to the class represented by this membership
    function.

    Evaluations of a single measurement across of set MembershipFunctions
    can then be passed to a DecisionRule in order to establish class (or
    group) assignment. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetMeasurementVectorSize = _swig_new_instance_method(_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF3_SetMeasurementVectorSize)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF3_GetMeasurementVectorSize)
    __swig_destroy__ = _itkMembershipFunctionBasePython.delete_itkMembershipFunctionBaseVF3
    cast = _swig_new_static_method(_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF3_cast)

# Register itkMembershipFunctionBaseVF3 in _itkMembershipFunctionBasePython:
_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF3_swigregister(itkMembershipFunctionBaseVF3)
itkMembershipFunctionBaseVF3_cast = _itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF3_cast

class itkMembershipFunctionBaseVF4(itk.itkFunctionBasePython.itkFunctionBaseVF4D):
    r"""


    MembershipFunctionBase defines common interfaces for membership
    functions.

    MembershipFunctionBase is a subclass of FunctionBase which restricts
    the function type to be a membership function. Membership functions
    provide a mapping from an arbitrary domain to a set of real numbers.
    Membership functions are typically used to model or approximate
    likelihood functions, $p( x | i )$, i.e. the probability of the
    measurement $x$ belonging to a class $i$.

    The Statistics framework models random variables $x$ as vectors.
    Typical uses of MembershipFunctions include templating over a
    FixedArray, Array, Vector, or VariableLengthVector.

    The Evaluate() method returns the membership rank or likelihood that
    the measurement belongs to the class represented by this membership
    function.

    Evaluations of a single measurement across of set MembershipFunctions
    can then be passed to a DecisionRule in order to establish class (or
    group) assignment. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetMeasurementVectorSize = _swig_new_instance_method(_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF4_SetMeasurementVectorSize)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF4_GetMeasurementVectorSize)
    __swig_destroy__ = _itkMembershipFunctionBasePython.delete_itkMembershipFunctionBaseVF4
    cast = _swig_new_static_method(_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF4_cast)

# Register itkMembershipFunctionBaseVF4 in _itkMembershipFunctionBasePython:
_itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF4_swigregister(itkMembershipFunctionBaseVF4)
itkMembershipFunctionBaseVF4_cast = _itkMembershipFunctionBasePython.itkMembershipFunctionBaseVF4_cast



