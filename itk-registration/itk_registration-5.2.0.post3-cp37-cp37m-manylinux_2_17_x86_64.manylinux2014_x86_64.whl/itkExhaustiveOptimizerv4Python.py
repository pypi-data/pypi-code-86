# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKOptimizersv4Python



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkExhaustiveOptimizerv4Python
else:
    import _itkExhaustiveOptimizerv4Python

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkExhaustiveOptimizerv4Python.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkExhaustiveOptimizerv4Python.SWIG_PyStaticMethod_New

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
import itk.itkObjectToObjectOptimizerBasePython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkObjectToObjectMetricBasePython
import itk.itkSingleValuedCostFunctionv4Python
import itk.itkCostFunctionPython
import itk.itkOptimizerParameterScalesEstimatorPython

def itkExhaustiveOptimizerv4D_New():
    return itkExhaustiveOptimizerv4D.New()

class itkExhaustiveOptimizerv4D(itk.itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD):
    r"""


    Optimizer that fully samples a grid on the parametric space.

    This optimizer is equivalent to an exhaustive search in a discrete
    grid defined over the parametric space. The grid is centered on the
    initial position. The subdivisions of the grid along each one of the
    dimensions of the parametric space is defined by an array of number of
    steps.

    A typical use is to plot the metric space to get an idea of how noisy
    it space with respect to translations along x, y and z in a 3D
    registration application: Here it is assumed that the transform is
    Euler3DTransform.

    The optimizer throws IterationEvents after every iteration. We use
    this to plot the metric space in an image as follows:

    The image size is expected to be 11 x 11 x 11.

    If you wish to use different step lengths along each parametric axis,
    you can use the SetScales() method. This accepts an array, each
    element represents the number of subdivisions per step length. For
    instance scales of [0.5 1 4] along with a step length of 2 will cause
    the optimizer to search the metric space on a grid with x,y,z spacing
    of [1 2 8].

    Physical dimensions of the grid are influenced by both the scales and
    the number of steps along each dimension, a side of the region is
    stepLength*(2*numberOfSteps[d]+1)*scaling[d]. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D___New_orig__)
    Clone = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_Clone)
    StartOptimization = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_StartOptimization)
    StartWalking = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_StartWalking)
    ResumeWalking = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_ResumeWalking)
    StopWalking = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_StopWalking)
    SetStepLength = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_SetStepLength)
    SetNumberOfSteps = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_SetNumberOfSteps)
    GetStepLength = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetStepLength)
    GetNumberOfSteps = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetNumberOfSteps)
    GetCurrentValue = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetCurrentValue)
    GetMaximumMetricValue = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMaximumMetricValue)
    GetMinimumMetricValue = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMinimumMetricValue)
    GetMinimumMetricValuePosition = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMinimumMetricValuePosition)
    GetMaximumMetricValuePosition = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetMaximumMetricValuePosition)
    GetCurrentIndex = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetCurrentIndex)
    SetInitialPosition = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_SetInitialPosition)
    GetInitialPosition = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_GetInitialPosition)
    __swig_destroy__ = _itkExhaustiveOptimizerv4Python.delete_itkExhaustiveOptimizerv4D
    cast = _swig_new_static_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_cast)

    def New(*args, **kargs):
        """New() -> itkExhaustiveOptimizerv4D

        Create a new object of the class itkExhaustiveOptimizerv4D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExhaustiveOptimizerv4D.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkExhaustiveOptimizerv4D.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkExhaustiveOptimizerv4D.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExhaustiveOptimizerv4D in _itkExhaustiveOptimizerv4Python:
_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_swigregister(itkExhaustiveOptimizerv4D)
itkExhaustiveOptimizerv4D___New_orig__ = _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D___New_orig__
itkExhaustiveOptimizerv4D_cast = _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4D_cast


def itkExhaustiveOptimizerv4F_New():
    return itkExhaustiveOptimizerv4F.New()

class itkExhaustiveOptimizerv4F(itk.itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF):
    r"""


    Optimizer that fully samples a grid on the parametric space.

    This optimizer is equivalent to an exhaustive search in a discrete
    grid defined over the parametric space. The grid is centered on the
    initial position. The subdivisions of the grid along each one of the
    dimensions of the parametric space is defined by an array of number of
    steps.

    A typical use is to plot the metric space to get an idea of how noisy
    it space with respect to translations along x, y and z in a 3D
    registration application: Here it is assumed that the transform is
    Euler3DTransform.

    The optimizer throws IterationEvents after every iteration. We use
    this to plot the metric space in an image as follows:

    The image size is expected to be 11 x 11 x 11.

    If you wish to use different step lengths along each parametric axis,
    you can use the SetScales() method. This accepts an array, each
    element represents the number of subdivisions per step length. For
    instance scales of [0.5 1 4] along with a step length of 2 will cause
    the optimizer to search the metric space on a grid with x,y,z spacing
    of [1 2 8].

    Physical dimensions of the grid are influenced by both the scales and
    the number of steps along each dimension, a side of the region is
    stepLength*(2*numberOfSteps[d]+1)*scaling[d]. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F___New_orig__)
    Clone = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_Clone)
    StartOptimization = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_StartOptimization)
    StartWalking = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_StartWalking)
    ResumeWalking = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_ResumeWalking)
    StopWalking = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_StopWalking)
    SetStepLength = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_SetStepLength)
    SetNumberOfSteps = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_SetNumberOfSteps)
    GetStepLength = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetStepLength)
    GetNumberOfSteps = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetNumberOfSteps)
    GetCurrentValue = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetCurrentValue)
    GetMaximumMetricValue = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMaximumMetricValue)
    GetMinimumMetricValue = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMinimumMetricValue)
    GetMinimumMetricValuePosition = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMinimumMetricValuePosition)
    GetMaximumMetricValuePosition = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetMaximumMetricValuePosition)
    GetCurrentIndex = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetCurrentIndex)
    SetInitialPosition = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_SetInitialPosition)
    GetInitialPosition = _swig_new_instance_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_GetInitialPosition)
    __swig_destroy__ = _itkExhaustiveOptimizerv4Python.delete_itkExhaustiveOptimizerv4F
    cast = _swig_new_static_method(_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_cast)

    def New(*args, **kargs):
        """New() -> itkExhaustiveOptimizerv4F

        Create a new object of the class itkExhaustiveOptimizerv4F and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExhaustiveOptimizerv4F.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkExhaustiveOptimizerv4F.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkExhaustiveOptimizerv4F.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExhaustiveOptimizerv4F in _itkExhaustiveOptimizerv4Python:
_itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_swigregister(itkExhaustiveOptimizerv4F)
itkExhaustiveOptimizerv4F___New_orig__ = _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F___New_orig__
itkExhaustiveOptimizerv4F_cast = _itkExhaustiveOptimizerv4Python.itkExhaustiveOptimizerv4F_cast



