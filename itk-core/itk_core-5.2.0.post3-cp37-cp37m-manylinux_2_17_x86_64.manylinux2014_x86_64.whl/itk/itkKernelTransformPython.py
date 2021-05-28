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
    from . import _itkKernelTransformPython
else:
    import _itkKernelTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkKernelTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkKernelTransformPython.SWIG_PyStaticMethod_New

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
import itk.vnl_matrix_fixedPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.itkOptimizerParametersPython
import itk.ITKCommonBasePython
import itk.itkArrayPython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkTransformBasePython
import itk.itkArray2DPython
import itk.itkVariableLengthVectorPython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.itkPointSetPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython

def itkKernelTransformD2_New():
    return itkKernelTransformD2.New()

class itkKernelTransformD2(itk.itkTransformBasePython.itkTransformD22):
    r"""


    Intended to be a base class for elastic body spline and thin plate
    spline. This is implemented in as straightforward a manner as possible
    from the IEEE TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol.
    16, No. 3 June 1997. Notation closely follows their paper, so if you
    have it in front of you, this code will make a lot more sense.

    KernelTransform: Provides support for defining source and target
    landmarks Defines a number of data types used in the computations
    Defines the mathematical framework used to compute all splines, so
    that subclasses need only provide a kernel specific to that spline

    This formulation allows the stiffness of the spline to be adjusted,
    allowing the spline to vary from interpolating the landmarks to
    approximating the landmarks. This part of the formulation is based on
    the short paper by R. Sprengel, K. Rohr, H. Stiehl. "Thin-Plate
    Spline Approximation for Image  Registration". In 18th International
    Conference of the IEEE Engineering in Medicine and Biology Society.
    1996. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKernelTransformPython.itkKernelTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_Clone)
    GetModifiableSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetModifiableSourceLandmarks)
    GetSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetSourceLandmarks)
    SetSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_SetSourceLandmarks)
    GetModifiableTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetModifiableTargetLandmarks)
    GetTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetTargetLandmarks)
    SetTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_SetTargetLandmarks)
    GetModifiableDisplacements = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetModifiableDisplacements)
    GetDisplacements = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetDisplacements)
    ComputeWMatrix = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_ComputeWMatrix)
    TransformVector = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_TransformVector)
    UpdateParameters = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_UpdateParameters)
    SetStiffness = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_SetStiffness)
    GetStiffness = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetStiffness)
    __swig_destroy__ = _itkKernelTransformPython.delete_itkKernelTransformD2
    cast = _swig_new_static_method(_itkKernelTransformPython.itkKernelTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkKernelTransformD2

        Create a new object of the class itkKernelTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKernelTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKernelTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKernelTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKernelTransformD2 in _itkKernelTransformPython:
_itkKernelTransformPython.itkKernelTransformD2_swigregister(itkKernelTransformD2)
itkKernelTransformD2___New_orig__ = _itkKernelTransformPython.itkKernelTransformD2___New_orig__
itkKernelTransformD2_cast = _itkKernelTransformPython.itkKernelTransformD2_cast


def itkKernelTransformD3_New():
    return itkKernelTransformD3.New()

class itkKernelTransformD3(itk.itkTransformBasePython.itkTransformD33):
    r"""


    Intended to be a base class for elastic body spline and thin plate
    spline. This is implemented in as straightforward a manner as possible
    from the IEEE TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol.
    16, No. 3 June 1997. Notation closely follows their paper, so if you
    have it in front of you, this code will make a lot more sense.

    KernelTransform: Provides support for defining source and target
    landmarks Defines a number of data types used in the computations
    Defines the mathematical framework used to compute all splines, so
    that subclasses need only provide a kernel specific to that spline

    This formulation allows the stiffness of the spline to be adjusted,
    allowing the spline to vary from interpolating the landmarks to
    approximating the landmarks. This part of the formulation is based on
    the short paper by R. Sprengel, K. Rohr, H. Stiehl. "Thin-Plate
    Spline Approximation for Image  Registration". In 18th International
    Conference of the IEEE Engineering in Medicine and Biology Society.
    1996. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKernelTransformPython.itkKernelTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_Clone)
    GetModifiableSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetModifiableSourceLandmarks)
    GetSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetSourceLandmarks)
    SetSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_SetSourceLandmarks)
    GetModifiableTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetModifiableTargetLandmarks)
    GetTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetTargetLandmarks)
    SetTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_SetTargetLandmarks)
    GetModifiableDisplacements = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetModifiableDisplacements)
    GetDisplacements = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetDisplacements)
    ComputeWMatrix = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_ComputeWMatrix)
    TransformVector = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_TransformVector)
    UpdateParameters = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_UpdateParameters)
    SetStiffness = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_SetStiffness)
    GetStiffness = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetStiffness)
    __swig_destroy__ = _itkKernelTransformPython.delete_itkKernelTransformD3
    cast = _swig_new_static_method(_itkKernelTransformPython.itkKernelTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkKernelTransformD3

        Create a new object of the class itkKernelTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKernelTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKernelTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKernelTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKernelTransformD3 in _itkKernelTransformPython:
_itkKernelTransformPython.itkKernelTransformD3_swigregister(itkKernelTransformD3)
itkKernelTransformD3___New_orig__ = _itkKernelTransformPython.itkKernelTransformD3___New_orig__
itkKernelTransformD3_cast = _itkKernelTransformPython.itkKernelTransformD3_cast


def itkKernelTransformD4_New():
    return itkKernelTransformD4.New()

class itkKernelTransformD4(itk.itkTransformBasePython.itkTransformD44):
    r"""


    Intended to be a base class for elastic body spline and thin plate
    spline. This is implemented in as straightforward a manner as possible
    from the IEEE TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol.
    16, No. 3 June 1997. Notation closely follows their paper, so if you
    have it in front of you, this code will make a lot more sense.

    KernelTransform: Provides support for defining source and target
    landmarks Defines a number of data types used in the computations
    Defines the mathematical framework used to compute all splines, so
    that subclasses need only provide a kernel specific to that spline

    This formulation allows the stiffness of the spline to be adjusted,
    allowing the spline to vary from interpolating the landmarks to
    approximating the landmarks. This part of the formulation is based on
    the short paper by R. Sprengel, K. Rohr, H. Stiehl. "Thin-Plate
    Spline Approximation for Image  Registration". In 18th International
    Conference of the IEEE Engineering in Medicine and Biology Society.
    1996. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKernelTransformPython.itkKernelTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_Clone)
    GetModifiableSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_GetModifiableSourceLandmarks)
    GetSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_GetSourceLandmarks)
    SetSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_SetSourceLandmarks)
    GetModifiableTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_GetModifiableTargetLandmarks)
    GetTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_GetTargetLandmarks)
    SetTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_SetTargetLandmarks)
    GetModifiableDisplacements = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_GetModifiableDisplacements)
    GetDisplacements = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_GetDisplacements)
    ComputeWMatrix = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_ComputeWMatrix)
    TransformVector = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_TransformVector)
    UpdateParameters = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_UpdateParameters)
    SetStiffness = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_SetStiffness)
    GetStiffness = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD4_GetStiffness)
    __swig_destroy__ = _itkKernelTransformPython.delete_itkKernelTransformD4
    cast = _swig_new_static_method(_itkKernelTransformPython.itkKernelTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkKernelTransformD4

        Create a new object of the class itkKernelTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKernelTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKernelTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKernelTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKernelTransformD4 in _itkKernelTransformPython:
_itkKernelTransformPython.itkKernelTransformD4_swigregister(itkKernelTransformD4)
itkKernelTransformD4___New_orig__ = _itkKernelTransformPython.itkKernelTransformD4___New_orig__
itkKernelTransformD4_cast = _itkKernelTransformPython.itkKernelTransformD4_cast



