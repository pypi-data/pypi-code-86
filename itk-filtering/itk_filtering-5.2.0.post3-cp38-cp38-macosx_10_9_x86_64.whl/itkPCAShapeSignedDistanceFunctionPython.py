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


from . import _ITKSignedDistanceFunctionPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkPCAShapeSignedDistanceFunctionPython
else:
    import _itkPCAShapeSignedDistanceFunctionPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkPCAShapeSignedDistanceFunctionPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkPCAShapeSignedDistanceFunctionPython.SWIG_PyStaticMethod_New

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
import itk.itkShapeSignedDistanceFunctionPython
import itk.itkPointPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkSpatialFunctionPython
import itk.itkFunctionBasePython
import itk.itkArrayPython
import itk.itkRGBPixelPython
import itk.itkCovariantVectorPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkRGBAPixelPython
import itk.itkImagePython
import itk.itkImageRegionPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkOptimizerParametersPython
import itk.itkTransformBasePython
import itk.itkArray2DPython
import itk.itkVariableLengthVectorPython
import itk.itkDiffusionTensor3DPython

def itkPCAShapeSignedDistanceFunctionD2ID2_New():
    return itkPCAShapeSignedDistanceFunctionD2ID2.New()

class itkPCAShapeSignedDistanceFunctionD2ID2(itk.itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD2):
    r"""


    Compute the signed distance from a N-dimensional PCA Shape.

    This class computes the signed distance from a N-dimensional shape
    defined by: (1) a mean signed distance image $ M(x) $, (2) the first $
    q $ principal components images $ P_i(x) $ and (3) a transform $ T(x)
    $ to define the pose (i.e. position or orientation of the shape).

    A particular instance of the shape is defined by a set of parameters $
    p $. The first $ q $ parameters defines the weights applied to each
    principal components and the remaining parameters is used to define
    the transform. The user should refer to the documentation of the
    particular Transform class being used. The first set of parameters are
    called the ShapeParameters and the remaining parameters the
    PoseParameters.

    The method Evaluate( point x ) returns the approximate signed to the
    shape at point x such that:

    \\[ s = M(T(x)) + \\sum_i^{q} p[i] * \\sigma[i] * P_i(T(x))
    \\]

    Where $\\sigma[i]$ are the square root of the eigenvalues. These are
    defined using method SetPrincipalComponentStandardDeviations().

    This class is templated over the coordinate representation type (e.g.
    float or double) and the space dimension.

    See:   ShapeSignedDistanceFunction

    See:  Transform 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_Clone)
    SetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_SetNumberOfPrincipalComponents)
    GetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_GetNumberOfPrincipalComponents)
    SetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_SetMeanImage)
    GetModifiableMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_GetModifiableMeanImage)
    GetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_GetMeanImage)
    SetPrincipalComponentImages = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_SetPrincipalComponentImages)
    SetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_SetPrincipalComponentStandardDeviations)
    GetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_GetPrincipalComponentStandardDeviations)
    SetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_GetTransform)
    __swig_destroy__ = _itkPCAShapeSignedDistanceFunctionPython.delete_itkPCAShapeSignedDistanceFunctionD2ID2
    cast = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkPCAShapeSignedDistanceFunctionD2ID2

        Create a new object of the class itkPCAShapeSignedDistanceFunctionD2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPCAShapeSignedDistanceFunctionD2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPCAShapeSignedDistanceFunctionD2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPCAShapeSignedDistanceFunctionD2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPCAShapeSignedDistanceFunctionD2ID2 in _itkPCAShapeSignedDistanceFunctionPython:
_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_swigregister(itkPCAShapeSignedDistanceFunctionD2ID2)
itkPCAShapeSignedDistanceFunctionD2ID2___New_orig__ = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2___New_orig__
itkPCAShapeSignedDistanceFunctionD2ID2_cast = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2ID2_cast


def itkPCAShapeSignedDistanceFunctionD2IF2_New():
    return itkPCAShapeSignedDistanceFunctionD2IF2.New()

class itkPCAShapeSignedDistanceFunctionD2IF2(itk.itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD2):
    r"""


    Compute the signed distance from a N-dimensional PCA Shape.

    This class computes the signed distance from a N-dimensional shape
    defined by: (1) a mean signed distance image $ M(x) $, (2) the first $
    q $ principal components images $ P_i(x) $ and (3) a transform $ T(x)
    $ to define the pose (i.e. position or orientation of the shape).

    A particular instance of the shape is defined by a set of parameters $
    p $. The first $ q $ parameters defines the weights applied to each
    principal components and the remaining parameters is used to define
    the transform. The user should refer to the documentation of the
    particular Transform class being used. The first set of parameters are
    called the ShapeParameters and the remaining parameters the
    PoseParameters.

    The method Evaluate( point x ) returns the approximate signed to the
    shape at point x such that:

    \\[ s = M(T(x)) + \\sum_i^{q} p[i] * \\sigma[i] * P_i(T(x))
    \\]

    Where $\\sigma[i]$ are the square root of the eigenvalues. These are
    defined using method SetPrincipalComponentStandardDeviations().

    This class is templated over the coordinate representation type (e.g.
    float or double) and the space dimension.

    See:   ShapeSignedDistanceFunction

    See:  Transform 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_Clone)
    SetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_SetNumberOfPrincipalComponents)
    GetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_GetNumberOfPrincipalComponents)
    SetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_SetMeanImage)
    GetModifiableMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_GetModifiableMeanImage)
    GetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_GetMeanImage)
    SetPrincipalComponentImages = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_SetPrincipalComponentImages)
    SetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_SetPrincipalComponentStandardDeviations)
    GetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_GetPrincipalComponentStandardDeviations)
    SetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_GetTransform)
    __swig_destroy__ = _itkPCAShapeSignedDistanceFunctionPython.delete_itkPCAShapeSignedDistanceFunctionD2IF2
    cast = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkPCAShapeSignedDistanceFunctionD2IF2

        Create a new object of the class itkPCAShapeSignedDistanceFunctionD2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPCAShapeSignedDistanceFunctionD2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPCAShapeSignedDistanceFunctionD2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPCAShapeSignedDistanceFunctionD2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPCAShapeSignedDistanceFunctionD2IF2 in _itkPCAShapeSignedDistanceFunctionPython:
_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_swigregister(itkPCAShapeSignedDistanceFunctionD2IF2)
itkPCAShapeSignedDistanceFunctionD2IF2___New_orig__ = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2___New_orig__
itkPCAShapeSignedDistanceFunctionD2IF2_cast = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD2IF2_cast


def itkPCAShapeSignedDistanceFunctionD3ID3_New():
    return itkPCAShapeSignedDistanceFunctionD3ID3.New()

class itkPCAShapeSignedDistanceFunctionD3ID3(itk.itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD3):
    r"""


    Compute the signed distance from a N-dimensional PCA Shape.

    This class computes the signed distance from a N-dimensional shape
    defined by: (1) a mean signed distance image $ M(x) $, (2) the first $
    q $ principal components images $ P_i(x) $ and (3) a transform $ T(x)
    $ to define the pose (i.e. position or orientation of the shape).

    A particular instance of the shape is defined by a set of parameters $
    p $. The first $ q $ parameters defines the weights applied to each
    principal components and the remaining parameters is used to define
    the transform. The user should refer to the documentation of the
    particular Transform class being used. The first set of parameters are
    called the ShapeParameters and the remaining parameters the
    PoseParameters.

    The method Evaluate( point x ) returns the approximate signed to the
    shape at point x such that:

    \\[ s = M(T(x)) + \\sum_i^{q} p[i] * \\sigma[i] * P_i(T(x))
    \\]

    Where $\\sigma[i]$ are the square root of the eigenvalues. These are
    defined using method SetPrincipalComponentStandardDeviations().

    This class is templated over the coordinate representation type (e.g.
    float or double) and the space dimension.

    See:   ShapeSignedDistanceFunction

    See:  Transform 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_Clone)
    SetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_SetNumberOfPrincipalComponents)
    GetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_GetNumberOfPrincipalComponents)
    SetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_SetMeanImage)
    GetModifiableMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_GetModifiableMeanImage)
    GetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_GetMeanImage)
    SetPrincipalComponentImages = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_SetPrincipalComponentImages)
    SetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_SetPrincipalComponentStandardDeviations)
    GetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_GetPrincipalComponentStandardDeviations)
    SetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_GetTransform)
    __swig_destroy__ = _itkPCAShapeSignedDistanceFunctionPython.delete_itkPCAShapeSignedDistanceFunctionD3ID3
    cast = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkPCAShapeSignedDistanceFunctionD3ID3

        Create a new object of the class itkPCAShapeSignedDistanceFunctionD3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPCAShapeSignedDistanceFunctionD3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPCAShapeSignedDistanceFunctionD3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPCAShapeSignedDistanceFunctionD3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPCAShapeSignedDistanceFunctionD3ID3 in _itkPCAShapeSignedDistanceFunctionPython:
_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_swigregister(itkPCAShapeSignedDistanceFunctionD3ID3)
itkPCAShapeSignedDistanceFunctionD3ID3___New_orig__ = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3___New_orig__
itkPCAShapeSignedDistanceFunctionD3ID3_cast = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3ID3_cast


def itkPCAShapeSignedDistanceFunctionD3IF3_New():
    return itkPCAShapeSignedDistanceFunctionD3IF3.New()

class itkPCAShapeSignedDistanceFunctionD3IF3(itk.itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD3):
    r"""


    Compute the signed distance from a N-dimensional PCA Shape.

    This class computes the signed distance from a N-dimensional shape
    defined by: (1) a mean signed distance image $ M(x) $, (2) the first $
    q $ principal components images $ P_i(x) $ and (3) a transform $ T(x)
    $ to define the pose (i.e. position or orientation of the shape).

    A particular instance of the shape is defined by a set of parameters $
    p $. The first $ q $ parameters defines the weights applied to each
    principal components and the remaining parameters is used to define
    the transform. The user should refer to the documentation of the
    particular Transform class being used. The first set of parameters are
    called the ShapeParameters and the remaining parameters the
    PoseParameters.

    The method Evaluate( point x ) returns the approximate signed to the
    shape at point x such that:

    \\[ s = M(T(x)) + \\sum_i^{q} p[i] * \\sigma[i] * P_i(T(x))
    \\]

    Where $\\sigma[i]$ are the square root of the eigenvalues. These are
    defined using method SetPrincipalComponentStandardDeviations().

    This class is templated over the coordinate representation type (e.g.
    float or double) and the space dimension.

    See:   ShapeSignedDistanceFunction

    See:  Transform 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_Clone)
    SetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_SetNumberOfPrincipalComponents)
    GetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_GetNumberOfPrincipalComponents)
    SetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_SetMeanImage)
    GetModifiableMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_GetModifiableMeanImage)
    GetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_GetMeanImage)
    SetPrincipalComponentImages = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_SetPrincipalComponentImages)
    SetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_SetPrincipalComponentStandardDeviations)
    GetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_GetPrincipalComponentStandardDeviations)
    SetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_GetTransform)
    __swig_destroy__ = _itkPCAShapeSignedDistanceFunctionPython.delete_itkPCAShapeSignedDistanceFunctionD3IF3
    cast = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkPCAShapeSignedDistanceFunctionD3IF3

        Create a new object of the class itkPCAShapeSignedDistanceFunctionD3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPCAShapeSignedDistanceFunctionD3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPCAShapeSignedDistanceFunctionD3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPCAShapeSignedDistanceFunctionD3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPCAShapeSignedDistanceFunctionD3IF3 in _itkPCAShapeSignedDistanceFunctionPython:
_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_swigregister(itkPCAShapeSignedDistanceFunctionD3IF3)
itkPCAShapeSignedDistanceFunctionD3IF3___New_orig__ = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3___New_orig__
itkPCAShapeSignedDistanceFunctionD3IF3_cast = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD3IF3_cast


def itkPCAShapeSignedDistanceFunctionD4ID4_New():
    return itkPCAShapeSignedDistanceFunctionD4ID4.New()

class itkPCAShapeSignedDistanceFunctionD4ID4(itk.itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD4):
    r"""


    Compute the signed distance from a N-dimensional PCA Shape.

    This class computes the signed distance from a N-dimensional shape
    defined by: (1) a mean signed distance image $ M(x) $, (2) the first $
    q $ principal components images $ P_i(x) $ and (3) a transform $ T(x)
    $ to define the pose (i.e. position or orientation of the shape).

    A particular instance of the shape is defined by a set of parameters $
    p $. The first $ q $ parameters defines the weights applied to each
    principal components and the remaining parameters is used to define
    the transform. The user should refer to the documentation of the
    particular Transform class being used. The first set of parameters are
    called the ShapeParameters and the remaining parameters the
    PoseParameters.

    The method Evaluate( point x ) returns the approximate signed to the
    shape at point x such that:

    \\[ s = M(T(x)) + \\sum_i^{q} p[i] * \\sigma[i] * P_i(T(x))
    \\]

    Where $\\sigma[i]$ are the square root of the eigenvalues. These are
    defined using method SetPrincipalComponentStandardDeviations().

    This class is templated over the coordinate representation type (e.g.
    float or double) and the space dimension.

    See:   ShapeSignedDistanceFunction

    See:  Transform 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_Clone)
    SetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_SetNumberOfPrincipalComponents)
    GetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_GetNumberOfPrincipalComponents)
    SetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_SetMeanImage)
    GetModifiableMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_GetModifiableMeanImage)
    GetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_GetMeanImage)
    SetPrincipalComponentImages = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_SetPrincipalComponentImages)
    SetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_SetPrincipalComponentStandardDeviations)
    GetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_GetPrincipalComponentStandardDeviations)
    SetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_GetTransform)
    __swig_destroy__ = _itkPCAShapeSignedDistanceFunctionPython.delete_itkPCAShapeSignedDistanceFunctionD4ID4
    cast = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkPCAShapeSignedDistanceFunctionD4ID4

        Create a new object of the class itkPCAShapeSignedDistanceFunctionD4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPCAShapeSignedDistanceFunctionD4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPCAShapeSignedDistanceFunctionD4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPCAShapeSignedDistanceFunctionD4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPCAShapeSignedDistanceFunctionD4ID4 in _itkPCAShapeSignedDistanceFunctionPython:
_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_swigregister(itkPCAShapeSignedDistanceFunctionD4ID4)
itkPCAShapeSignedDistanceFunctionD4ID4___New_orig__ = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4___New_orig__
itkPCAShapeSignedDistanceFunctionD4ID4_cast = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4ID4_cast


def itkPCAShapeSignedDistanceFunctionD4IF4_New():
    return itkPCAShapeSignedDistanceFunctionD4IF4.New()

class itkPCAShapeSignedDistanceFunctionD4IF4(itk.itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD4):
    r"""


    Compute the signed distance from a N-dimensional PCA Shape.

    This class computes the signed distance from a N-dimensional shape
    defined by: (1) a mean signed distance image $ M(x) $, (2) the first $
    q $ principal components images $ P_i(x) $ and (3) a transform $ T(x)
    $ to define the pose (i.e. position or orientation of the shape).

    A particular instance of the shape is defined by a set of parameters $
    p $. The first $ q $ parameters defines the weights applied to each
    principal components and the remaining parameters is used to define
    the transform. The user should refer to the documentation of the
    particular Transform class being used. The first set of parameters are
    called the ShapeParameters and the remaining parameters the
    PoseParameters.

    The method Evaluate( point x ) returns the approximate signed to the
    shape at point x such that:

    \\[ s = M(T(x)) + \\sum_i^{q} p[i] * \\sigma[i] * P_i(T(x))
    \\]

    Where $\\sigma[i]$ are the square root of the eigenvalues. These are
    defined using method SetPrincipalComponentStandardDeviations().

    This class is templated over the coordinate representation type (e.g.
    float or double) and the space dimension.

    See:   ShapeSignedDistanceFunction

    See:  Transform 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_Clone)
    SetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_SetNumberOfPrincipalComponents)
    GetNumberOfPrincipalComponents = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_GetNumberOfPrincipalComponents)
    SetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_SetMeanImage)
    GetModifiableMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_GetModifiableMeanImage)
    GetMeanImage = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_GetMeanImage)
    SetPrincipalComponentImages = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_SetPrincipalComponentImages)
    SetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_SetPrincipalComponentStandardDeviations)
    GetPrincipalComponentStandardDeviations = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_GetPrincipalComponentStandardDeviations)
    SetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_GetTransform)
    __swig_destroy__ = _itkPCAShapeSignedDistanceFunctionPython.delete_itkPCAShapeSignedDistanceFunctionD4IF4
    cast = _swig_new_static_method(_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkPCAShapeSignedDistanceFunctionD4IF4

        Create a new object of the class itkPCAShapeSignedDistanceFunctionD4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPCAShapeSignedDistanceFunctionD4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPCAShapeSignedDistanceFunctionD4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPCAShapeSignedDistanceFunctionD4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPCAShapeSignedDistanceFunctionD4IF4 in _itkPCAShapeSignedDistanceFunctionPython:
_itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_swigregister(itkPCAShapeSignedDistanceFunctionD4IF4)
itkPCAShapeSignedDistanceFunctionD4IF4___New_orig__ = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4___New_orig__
itkPCAShapeSignedDistanceFunctionD4IF4_cast = _itkPCAShapeSignedDistanceFunctionPython.itkPCAShapeSignedDistanceFunctionD4IF4_cast



