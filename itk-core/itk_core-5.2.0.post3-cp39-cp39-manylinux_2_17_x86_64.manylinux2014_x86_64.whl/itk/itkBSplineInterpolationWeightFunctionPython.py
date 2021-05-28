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
    from . import _itkBSplineInterpolationWeightFunctionPython
else:
    import _itkBSplineInterpolationWeightFunctionPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBSplineInterpolationWeightFunctionPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBSplineInterpolationWeightFunctionPython.SWIG_PyStaticMethod_New

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
import itk.itkFunctionBasePython
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkImagePython
import itk.itkImageRegionPython
import itk.ITKCommonBasePython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkPointPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBPixelPython
import itk.itkArrayPython
import itk.itkContinuousIndexPython

def itkBSplineInterpolationWeightFunctionD22_New():
    return itkBSplineInterpolationWeightFunctionD22.New()

class itkBSplineInterpolationWeightFunctionD22(itk.itkFunctionBasePython.itkFunctionBaseCID2AD):
    r"""


    Returns the weights over the support region used for B-spline
    interpolation/reconstruction.

    Computes/evaluate the B-spline interpolation weights over the support
    region of the B-spline.

    This class is templated over the coordinate representation type, the
    space dimension and the spline order.

    See:   Point

    See:   Index

    See:   ContinuousIndex 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD22___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD22_Clone)
    Evaluate = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD22_Evaluate)
    GetSupportSize = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD22_GetSupportSize)
    GetNumberOfWeights = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD22_GetNumberOfWeights)
    __swig_destroy__ = _itkBSplineInterpolationWeightFunctionPython.delete_itkBSplineInterpolationWeightFunctionD22
    cast = _swig_new_static_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD22_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineInterpolationWeightFunctionD22

        Create a new object of the class itkBSplineInterpolationWeightFunctionD22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineInterpolationWeightFunctionD22.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineInterpolationWeightFunctionD22.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineInterpolationWeightFunctionD22.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineInterpolationWeightFunctionD22 in _itkBSplineInterpolationWeightFunctionPython:
_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD22_swigregister(itkBSplineInterpolationWeightFunctionD22)
itkBSplineInterpolationWeightFunctionD22___New_orig__ = _itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD22___New_orig__
itkBSplineInterpolationWeightFunctionD22_cast = _itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD22_cast


def itkBSplineInterpolationWeightFunctionD33_New():
    return itkBSplineInterpolationWeightFunctionD33.New()

class itkBSplineInterpolationWeightFunctionD33(itk.itkFunctionBasePython.itkFunctionBaseCID3AD):
    r"""


    Returns the weights over the support region used for B-spline
    interpolation/reconstruction.

    Computes/evaluate the B-spline interpolation weights over the support
    region of the B-spline.

    This class is templated over the coordinate representation type, the
    space dimension and the spline order.

    See:   Point

    See:   Index

    See:   ContinuousIndex 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD33___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD33_Clone)
    Evaluate = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD33_Evaluate)
    GetSupportSize = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD33_GetSupportSize)
    GetNumberOfWeights = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD33_GetNumberOfWeights)
    __swig_destroy__ = _itkBSplineInterpolationWeightFunctionPython.delete_itkBSplineInterpolationWeightFunctionD33
    cast = _swig_new_static_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD33_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineInterpolationWeightFunctionD33

        Create a new object of the class itkBSplineInterpolationWeightFunctionD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineInterpolationWeightFunctionD33.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineInterpolationWeightFunctionD33.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineInterpolationWeightFunctionD33.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineInterpolationWeightFunctionD33 in _itkBSplineInterpolationWeightFunctionPython:
_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD33_swigregister(itkBSplineInterpolationWeightFunctionD33)
itkBSplineInterpolationWeightFunctionD33___New_orig__ = _itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD33___New_orig__
itkBSplineInterpolationWeightFunctionD33_cast = _itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD33_cast


def itkBSplineInterpolationWeightFunctionD44_New():
    return itkBSplineInterpolationWeightFunctionD44.New()

class itkBSplineInterpolationWeightFunctionD44(itk.itkFunctionBasePython.itkFunctionBaseCID4AD):
    r"""


    Returns the weights over the support region used for B-spline
    interpolation/reconstruction.

    Computes/evaluate the B-spline interpolation weights over the support
    region of the B-spline.

    This class is templated over the coordinate representation type, the
    space dimension and the spline order.

    See:   Point

    See:   Index

    See:   ContinuousIndex 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD44___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD44_Clone)
    Evaluate = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD44_Evaluate)
    GetSupportSize = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD44_GetSupportSize)
    GetNumberOfWeights = _swig_new_instance_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD44_GetNumberOfWeights)
    __swig_destroy__ = _itkBSplineInterpolationWeightFunctionPython.delete_itkBSplineInterpolationWeightFunctionD44
    cast = _swig_new_static_method(_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD44_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineInterpolationWeightFunctionD44

        Create a new object of the class itkBSplineInterpolationWeightFunctionD44 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineInterpolationWeightFunctionD44.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineInterpolationWeightFunctionD44.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineInterpolationWeightFunctionD44.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineInterpolationWeightFunctionD44 in _itkBSplineInterpolationWeightFunctionPython:
_itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD44_swigregister(itkBSplineInterpolationWeightFunctionD44)
itkBSplineInterpolationWeightFunctionD44___New_orig__ = _itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD44___New_orig__
itkBSplineInterpolationWeightFunctionD44_cast = _itkBSplineInterpolationWeightFunctionPython.itkBSplineInterpolationWeightFunctionD44_cast



