# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKFastMarchingPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkFastMarchingThresholdStoppingCriterionPython
else:
    import _itkFastMarchingThresholdStoppingCriterionPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkFastMarchingThresholdStoppingCriterionPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkFastMarchingThresholdStoppingCriterionPython.SWIG_PyStaticMethod_New

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
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.pyBasePython
import itk.itkFastMarchingStoppingCriterionBasePython
import itk.itkImagePython
import itk.stdcomplexPython
import itk.ITKCommonBasePython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkRGBAPixelPython
import itk.itkImageRegionPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkNodePairPython

def itkFastMarchingThresholdStoppingCriterionID2ID2_New():
    return itkFastMarchingThresholdStoppingCriterionID2ID2.New()

class itkFastMarchingThresholdStoppingCriterionID2ID2(itk.itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID2ID2):
    r"""


    Stopping Criterion is verified when Current Value is equal to or
    greater than the provided threshold. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_Clone)
    SetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_SetThreshold)
    GetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_GetThreshold)
    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionID2ID2
    cast = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionID2ID2

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingThresholdStoppingCriterionID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingThresholdStoppingCriterionID2ID2 in _itkFastMarchingThresholdStoppingCriterionPython:
_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_swigregister(itkFastMarchingThresholdStoppingCriterionID2ID2)
itkFastMarchingThresholdStoppingCriterionID2ID2___New_orig__ = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2___New_orig__
itkFastMarchingThresholdStoppingCriterionID2ID2_cast = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID2ID2_cast


def itkFastMarchingThresholdStoppingCriterionID3ID3_New():
    return itkFastMarchingThresholdStoppingCriterionID3ID3.New()

class itkFastMarchingThresholdStoppingCriterionID3ID3(itk.itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID3ID3):
    r"""


    Stopping Criterion is verified when Current Value is equal to or
    greater than the provided threshold. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_Clone)
    SetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_SetThreshold)
    GetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_GetThreshold)
    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionID3ID3
    cast = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionID3ID3

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingThresholdStoppingCriterionID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingThresholdStoppingCriterionID3ID3 in _itkFastMarchingThresholdStoppingCriterionPython:
_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_swigregister(itkFastMarchingThresholdStoppingCriterionID3ID3)
itkFastMarchingThresholdStoppingCriterionID3ID3___New_orig__ = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3___New_orig__
itkFastMarchingThresholdStoppingCriterionID3ID3_cast = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID3ID3_cast


def itkFastMarchingThresholdStoppingCriterionID4ID4_New():
    return itkFastMarchingThresholdStoppingCriterionID4ID4.New()

class itkFastMarchingThresholdStoppingCriterionID4ID4(itk.itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseID4ID4):
    r"""


    Stopping Criterion is verified when Current Value is equal to or
    greater than the provided threshold. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID4ID4_Clone)
    SetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID4ID4_SetThreshold)
    GetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID4ID4_GetThreshold)
    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionID4ID4
    cast = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionID4ID4

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingThresholdStoppingCriterionID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingThresholdStoppingCriterionID4ID4 in _itkFastMarchingThresholdStoppingCriterionPython:
_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID4ID4_swigregister(itkFastMarchingThresholdStoppingCriterionID4ID4)
itkFastMarchingThresholdStoppingCriterionID4ID4___New_orig__ = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID4ID4___New_orig__
itkFastMarchingThresholdStoppingCriterionID4ID4_cast = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionID4ID4_cast


def itkFastMarchingThresholdStoppingCriterionIF2IF2_New():
    return itkFastMarchingThresholdStoppingCriterionIF2IF2.New()

class itkFastMarchingThresholdStoppingCriterionIF2IF2(itk.itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF2IF2):
    r"""


    Stopping Criterion is verified when Current Value is equal to or
    greater than the provided threshold. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_Clone)
    SetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_SetThreshold)
    GetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_GetThreshold)
    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionIF2IF2
    cast = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionIF2IF2

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingThresholdStoppingCriterionIF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingThresholdStoppingCriterionIF2IF2 in _itkFastMarchingThresholdStoppingCriterionPython:
_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_swigregister(itkFastMarchingThresholdStoppingCriterionIF2IF2)
itkFastMarchingThresholdStoppingCriterionIF2IF2___New_orig__ = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2___New_orig__
itkFastMarchingThresholdStoppingCriterionIF2IF2_cast = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF2IF2_cast


def itkFastMarchingThresholdStoppingCriterionIF3IF3_New():
    return itkFastMarchingThresholdStoppingCriterionIF3IF3.New()

class itkFastMarchingThresholdStoppingCriterionIF3IF3(itk.itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF3IF3):
    r"""


    Stopping Criterion is verified when Current Value is equal to or
    greater than the provided threshold. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_Clone)
    SetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_SetThreshold)
    GetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_GetThreshold)
    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionIF3IF3
    cast = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionIF3IF3

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingThresholdStoppingCriterionIF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingThresholdStoppingCriterionIF3IF3 in _itkFastMarchingThresholdStoppingCriterionPython:
_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_swigregister(itkFastMarchingThresholdStoppingCriterionIF3IF3)
itkFastMarchingThresholdStoppingCriterionIF3IF3___New_orig__ = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3___New_orig__
itkFastMarchingThresholdStoppingCriterionIF3IF3_cast = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF3IF3_cast


def itkFastMarchingThresholdStoppingCriterionIF4IF4_New():
    return itkFastMarchingThresholdStoppingCriterionIF4IF4.New()

class itkFastMarchingThresholdStoppingCriterionIF4IF4(itk.itkFastMarchingStoppingCriterionBasePython.itkFastMarchingStoppingCriterionBaseIF4IF4):
    r"""


    Stopping Criterion is verified when Current Value is equal to or
    greater than the provided threshold. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF4IF4_Clone)
    SetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF4IF4_SetThreshold)
    GetThreshold = _swig_new_instance_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF4IF4_GetThreshold)
    __swig_destroy__ = _itkFastMarchingThresholdStoppingCriterionPython.delete_itkFastMarchingThresholdStoppingCriterionIF4IF4
    cast = _swig_new_static_method(_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingThresholdStoppingCriterionIF4IF4

        Create a new object of the class itkFastMarchingThresholdStoppingCriterionIF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingThresholdStoppingCriterionIF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingThresholdStoppingCriterionIF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingThresholdStoppingCriterionIF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingThresholdStoppingCriterionIF4IF4 in _itkFastMarchingThresholdStoppingCriterionPython:
_itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF4IF4_swigregister(itkFastMarchingThresholdStoppingCriterionIF4IF4)
itkFastMarchingThresholdStoppingCriterionIF4IF4___New_orig__ = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF4IF4___New_orig__
itkFastMarchingThresholdStoppingCriterionIF4IF4_cast = _itkFastMarchingThresholdStoppingCriterionPython.itkFastMarchingThresholdStoppingCriterionIF4IF4_cast



