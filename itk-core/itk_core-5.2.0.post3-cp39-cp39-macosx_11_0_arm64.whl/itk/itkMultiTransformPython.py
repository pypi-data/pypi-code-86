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
    from . import _itkMultiTransformPython
else:
    import _itkMultiTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMultiTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMultiTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkTransformBasePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkCovariantVectorPython
import itk.itkArray2DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkOptimizerParametersPython
import itk.itkDiffusionTensor3DPython
import itk.itkVariableLengthVectorPython
class itkMultiTransformD22(itk.itkTransformBasePython.itkTransformD22):
    r"""


    This abstract class contains a list of transforms and provides basic
    methods.

    This abstract base class is used by classes that operate on a list of
    sub-transforms. The sub-transforms can have a different dimensionality
    than the container transform.

    Transforms are stored in a container (queue), in the following order:
    $ T_0, T_1, ... , T_N-1 $

    Transforms are added via a single method, AddTransform(). This adds
    the transforms to the back of the queue. A single method for adding
    transforms is meant to simplify the interface and prevent errors.

    Inverse todo

    TODO

    Interface Issues/Comments x The PushFrontTransform and
    PushBackTransform methods are protected to force the user to use the
    AddTransform method, forcing the order of transforms. Are there use
    cases where the user would need to insert transforms at the front of
    the queue? Or at arbitrary positions?

    GetParameters efficiency optimization Can we optimize this to only
    query the sub-transforms when the params in the sub transforms have
    changed since the previous call? Can't use Modified time b/c that will
    get updated in sub-transforms with every call to SetParameters. Is
    this worth worrying about? i.e. how much time will it take in the
    overall registration process? Probably very little. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    AddTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_AddTransform)
    AppendTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_AppendTransform)
    PrependTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_PrependTransform)
    RemoveTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_RemoveTransform)
    GetFrontTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_GetFrontTransform)
    GetBackTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_GetBackTransform)
    GetNthTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_GetNthTransform)
    GetNthTransformModifiablePointer = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_GetNthTransformModifiablePointer)
    GetNthTransformConstPointer = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_GetNthTransformConstPointer)
    GetTransformQueue = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_GetTransformQueue)
    IsTransformQueueEmpty = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_IsTransformQueueEmpty)
    GetNumberOfTransforms = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_GetNumberOfTransforms)
    ClearTransformQueue = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_ClearTransformQueue)
    UpdateTransformParameters = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_UpdateTransformParameters)
    GetInverse = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD22_GetInverse)
    __swig_destroy__ = _itkMultiTransformPython.delete_itkMultiTransformD22
    cast = _swig_new_static_method(_itkMultiTransformPython.itkMultiTransformD22_cast)

# Register itkMultiTransformD22 in _itkMultiTransformPython:
_itkMultiTransformPython.itkMultiTransformD22_swigregister(itkMultiTransformD22)
itkMultiTransformD22_cast = _itkMultiTransformPython.itkMultiTransformD22_cast

class itkMultiTransformD33(itk.itkTransformBasePython.itkTransformD33):
    r"""


    This abstract class contains a list of transforms and provides basic
    methods.

    This abstract base class is used by classes that operate on a list of
    sub-transforms. The sub-transforms can have a different dimensionality
    than the container transform.

    Transforms are stored in a container (queue), in the following order:
    $ T_0, T_1, ... , T_N-1 $

    Transforms are added via a single method, AddTransform(). This adds
    the transforms to the back of the queue. A single method for adding
    transforms is meant to simplify the interface and prevent errors.

    Inverse todo

    TODO

    Interface Issues/Comments x The PushFrontTransform and
    PushBackTransform methods are protected to force the user to use the
    AddTransform method, forcing the order of transforms. Are there use
    cases where the user would need to insert transforms at the front of
    the queue? Or at arbitrary positions?

    GetParameters efficiency optimization Can we optimize this to only
    query the sub-transforms when the params in the sub transforms have
    changed since the previous call? Can't use Modified time b/c that will
    get updated in sub-transforms with every call to SetParameters. Is
    this worth worrying about? i.e. how much time will it take in the
    overall registration process? Probably very little. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    AddTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_AddTransform)
    AppendTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_AppendTransform)
    PrependTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_PrependTransform)
    RemoveTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_RemoveTransform)
    GetFrontTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_GetFrontTransform)
    GetBackTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_GetBackTransform)
    GetNthTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_GetNthTransform)
    GetNthTransformModifiablePointer = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_GetNthTransformModifiablePointer)
    GetNthTransformConstPointer = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_GetNthTransformConstPointer)
    GetTransformQueue = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_GetTransformQueue)
    IsTransformQueueEmpty = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_IsTransformQueueEmpty)
    GetNumberOfTransforms = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_GetNumberOfTransforms)
    ClearTransformQueue = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_ClearTransformQueue)
    UpdateTransformParameters = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_UpdateTransformParameters)
    GetInverse = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD33_GetInverse)
    __swig_destroy__ = _itkMultiTransformPython.delete_itkMultiTransformD33
    cast = _swig_new_static_method(_itkMultiTransformPython.itkMultiTransformD33_cast)

# Register itkMultiTransformD33 in _itkMultiTransformPython:
_itkMultiTransformPython.itkMultiTransformD33_swigregister(itkMultiTransformD33)
itkMultiTransformD33_cast = _itkMultiTransformPython.itkMultiTransformD33_cast

class itkMultiTransformD44(itk.itkTransformBasePython.itkTransformD44):
    r"""


    This abstract class contains a list of transforms and provides basic
    methods.

    This abstract base class is used by classes that operate on a list of
    sub-transforms. The sub-transforms can have a different dimensionality
    than the container transform.

    Transforms are stored in a container (queue), in the following order:
    $ T_0, T_1, ... , T_N-1 $

    Transforms are added via a single method, AddTransform(). This adds
    the transforms to the back of the queue. A single method for adding
    transforms is meant to simplify the interface and prevent errors.

    Inverse todo

    TODO

    Interface Issues/Comments x The PushFrontTransform and
    PushBackTransform methods are protected to force the user to use the
    AddTransform method, forcing the order of transforms. Are there use
    cases where the user would need to insert transforms at the front of
    the queue? Or at arbitrary positions?

    GetParameters efficiency optimization Can we optimize this to only
    query the sub-transforms when the params in the sub transforms have
    changed since the previous call? Can't use Modified time b/c that will
    get updated in sub-transforms with every call to SetParameters. Is
    this worth worrying about? i.e. how much time will it take in the
    overall registration process? Probably very little. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    AddTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_AddTransform)
    AppendTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_AppendTransform)
    PrependTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_PrependTransform)
    RemoveTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_RemoveTransform)
    GetFrontTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_GetFrontTransform)
    GetBackTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_GetBackTransform)
    GetNthTransform = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_GetNthTransform)
    GetNthTransformModifiablePointer = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_GetNthTransformModifiablePointer)
    GetNthTransformConstPointer = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_GetNthTransformConstPointer)
    GetTransformQueue = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_GetTransformQueue)
    IsTransformQueueEmpty = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_IsTransformQueueEmpty)
    GetNumberOfTransforms = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_GetNumberOfTransforms)
    ClearTransformQueue = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_ClearTransformQueue)
    UpdateTransformParameters = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_UpdateTransformParameters)
    GetInverse = _swig_new_instance_method(_itkMultiTransformPython.itkMultiTransformD44_GetInverse)
    __swig_destroy__ = _itkMultiTransformPython.delete_itkMultiTransformD44
    cast = _swig_new_static_method(_itkMultiTransformPython.itkMultiTransformD44_cast)

# Register itkMultiTransformD44 in _itkMultiTransformPython:
_itkMultiTransformPython.itkMultiTransformD44_swigregister(itkMultiTransformD44)
itkMultiTransformD44_cast = _itkMultiTransformPython.itkMultiTransformD44_cast



