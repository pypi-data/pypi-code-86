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
    from . import _itkBSplineTransformPython
else:
    import _itkBSplineTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBSplineTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBSplineTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkArrayPython
import itk.itkArray2DPython
import itk.itkOptimizerParametersPython
import itk.ITKCommonBasePython
import itk.itkSizePython
import itk.itkBSplineBaseTransformPython
import itk.itkTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkVariableLengthVectorPython
import itk.itkBSplineInterpolationWeightFunctionPython
import itk.itkFunctionBasePython
import itk.itkRGBPixelPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkImagePython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython

def itkBSplineTransformD23_New():
    return itkBSplineTransformD23.New()

class itkBSplineTransformD23(itk.itkBSplineBaseTransformPython.itkBSplineBaseTransformD23):
    r"""


    Deformable transform using a BSpline representation.

    This class encapsulates a deformable transform of points from one
    N-dimensional space to another N-dimensional space. The deformation
    field is modelled using B-splines. A deformation is defined on a
    sparse regular grid of control points $ \\vec{\\lambda}_j $ and is
    varied by defining a deformation $ \\vec{g}(\\vec{\\lambda}_j) $
    of each control point. The deformation $ D(\\vec{x}) $ at any point
    $ \\vec{x} $ is obtained by using a B-spline interpolation kernel.

    The deformation field grid is defined by a user specified transform
    domain (origin, physical dimensions, direction) and B-spline mesh size
    where the mesh size is the number of polynomial patches comprising the
    finite domain of support. The relationship between the mesh size (
    number of polynomial pieces) and the number of control points in any
    given dimension is

    mesh size = number of control points - spline order

    Each grid/control point has associated with it N deformation
    coefficients $ \\vec{\\delta}_j $, representing the N directional
    components of the deformation. Deformation outside the grid plus
    support region for the BSpline interpolation is assumed to be zero.

    The parameters for this transform is N x N-D grid of spline
    coefficients. The user specifies the parameters as one flat array:
    each N-D grid is represented by an array in the same way an N-D image
    is represented in the buffer; the N arrays are then concatenated
    together to form a single array.

    The following illustrates the typical usage of this class:

    An alternative way to set the B-spline coefficients is via array of
    images. The fixed parameters of the transform are taken directly from
    the first image. It is assumed that the subsequent images are the same
    buffered region. The following illustrates the API:

    WARNING:  Use either the SetParameters() or SetCoefficientImages()
    API. Mixing the two modes may results in unexpected results.  The
    class is templated coordinate representation type (float or double),
    the space dimension and the spline order. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformPython.itkBSplineTransformD23___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_Clone)
    SetTransformDomainOrigin = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainOrigin)
    GetTransformDomainOrigin = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainOrigin)
    SetTransformDomainPhysicalDimensions = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainPhysicalDimensions)
    GetTransformDomainPhysicalDimensions = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainPhysicalDimensions)
    SetTransformDomainDirection = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainDirection)
    GetTransformDomainDirection = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainDirection)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainMeshSize)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainMeshSize)
    __swig_destroy__ = _itkBSplineTransformPython.delete_itkBSplineTransformD23
    cast = _swig_new_static_method(_itkBSplineTransformPython.itkBSplineTransformD23_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformD23

        Create a new object of the class itkBSplineTransformD23 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformD23.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineTransformD23.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineTransformD23.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformD23 in _itkBSplineTransformPython:
_itkBSplineTransformPython.itkBSplineTransformD23_swigregister(itkBSplineTransformD23)
itkBSplineTransformD23___New_orig__ = _itkBSplineTransformPython.itkBSplineTransformD23___New_orig__
itkBSplineTransformD23_cast = _itkBSplineTransformPython.itkBSplineTransformD23_cast


def itkBSplineTransformD33_New():
    return itkBSplineTransformD33.New()

class itkBSplineTransformD33(itk.itkBSplineBaseTransformPython.itkBSplineBaseTransformD33):
    r"""


    Deformable transform using a BSpline representation.

    This class encapsulates a deformable transform of points from one
    N-dimensional space to another N-dimensional space. The deformation
    field is modelled using B-splines. A deformation is defined on a
    sparse regular grid of control points $ \\vec{\\lambda}_j $ and is
    varied by defining a deformation $ \\vec{g}(\\vec{\\lambda}_j) $
    of each control point. The deformation $ D(\\vec{x}) $ at any point
    $ \\vec{x} $ is obtained by using a B-spline interpolation kernel.

    The deformation field grid is defined by a user specified transform
    domain (origin, physical dimensions, direction) and B-spline mesh size
    where the mesh size is the number of polynomial patches comprising the
    finite domain of support. The relationship between the mesh size (
    number of polynomial pieces) and the number of control points in any
    given dimension is

    mesh size = number of control points - spline order

    Each grid/control point has associated with it N deformation
    coefficients $ \\vec{\\delta}_j $, representing the N directional
    components of the deformation. Deformation outside the grid plus
    support region for the BSpline interpolation is assumed to be zero.

    The parameters for this transform is N x N-D grid of spline
    coefficients. The user specifies the parameters as one flat array:
    each N-D grid is represented by an array in the same way an N-D image
    is represented in the buffer; the N arrays are then concatenated
    together to form a single array.

    The following illustrates the typical usage of this class:

    An alternative way to set the B-spline coefficients is via array of
    images. The fixed parameters of the transform are taken directly from
    the first image. It is assumed that the subsequent images are the same
    buffered region. The following illustrates the API:

    WARNING:  Use either the SetParameters() or SetCoefficientImages()
    API. Mixing the two modes may results in unexpected results.  The
    class is templated coordinate representation type (float or double),
    the space dimension and the spline order. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformPython.itkBSplineTransformD33___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_Clone)
    SetTransformDomainOrigin = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainOrigin)
    GetTransformDomainOrigin = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainOrigin)
    SetTransformDomainPhysicalDimensions = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainPhysicalDimensions)
    GetTransformDomainPhysicalDimensions = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainPhysicalDimensions)
    SetTransformDomainDirection = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainDirection)
    GetTransformDomainDirection = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainDirection)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainMeshSize)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainMeshSize)
    __swig_destroy__ = _itkBSplineTransformPython.delete_itkBSplineTransformD33
    cast = _swig_new_static_method(_itkBSplineTransformPython.itkBSplineTransformD33_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformD33

        Create a new object of the class itkBSplineTransformD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformD33.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineTransformD33.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineTransformD33.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformD33 in _itkBSplineTransformPython:
_itkBSplineTransformPython.itkBSplineTransformD33_swigregister(itkBSplineTransformD33)
itkBSplineTransformD33___New_orig__ = _itkBSplineTransformPython.itkBSplineTransformD33___New_orig__
itkBSplineTransformD33_cast = _itkBSplineTransformPython.itkBSplineTransformD33_cast


def itkBSplineTransformD43_New():
    return itkBSplineTransformD43.New()

class itkBSplineTransformD43(itk.itkBSplineBaseTransformPython.itkBSplineBaseTransformD43):
    r"""


    Deformable transform using a BSpline representation.

    This class encapsulates a deformable transform of points from one
    N-dimensional space to another N-dimensional space. The deformation
    field is modelled using B-splines. A deformation is defined on a
    sparse regular grid of control points $ \\vec{\\lambda}_j $ and is
    varied by defining a deformation $ \\vec{g}(\\vec{\\lambda}_j) $
    of each control point. The deformation $ D(\\vec{x}) $ at any point
    $ \\vec{x} $ is obtained by using a B-spline interpolation kernel.

    The deformation field grid is defined by a user specified transform
    domain (origin, physical dimensions, direction) and B-spline mesh size
    where the mesh size is the number of polynomial patches comprising the
    finite domain of support. The relationship between the mesh size (
    number of polynomial pieces) and the number of control points in any
    given dimension is

    mesh size = number of control points - spline order

    Each grid/control point has associated with it N deformation
    coefficients $ \\vec{\\delta}_j $, representing the N directional
    components of the deformation. Deformation outside the grid plus
    support region for the BSpline interpolation is assumed to be zero.

    The parameters for this transform is N x N-D grid of spline
    coefficients. The user specifies the parameters as one flat array:
    each N-D grid is represented by an array in the same way an N-D image
    is represented in the buffer; the N arrays are then concatenated
    together to form a single array.

    The following illustrates the typical usage of this class:

    An alternative way to set the B-spline coefficients is via array of
    images. The fixed parameters of the transform are taken directly from
    the first image. It is assumed that the subsequent images are the same
    buffered region. The following illustrates the API:

    WARNING:  Use either the SetParameters() or SetCoefficientImages()
    API. Mixing the two modes may results in unexpected results.  The
    class is templated coordinate representation type (float or double),
    the space dimension and the spline order. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformPython.itkBSplineTransformD43___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD43_Clone)
    SetTransformDomainOrigin = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD43_SetTransformDomainOrigin)
    GetTransformDomainOrigin = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD43_GetTransformDomainOrigin)
    SetTransformDomainPhysicalDimensions = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD43_SetTransformDomainPhysicalDimensions)
    GetTransformDomainPhysicalDimensions = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD43_GetTransformDomainPhysicalDimensions)
    SetTransformDomainDirection = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD43_SetTransformDomainDirection)
    GetTransformDomainDirection = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD43_GetTransformDomainDirection)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD43_SetTransformDomainMeshSize)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD43_GetTransformDomainMeshSize)
    __swig_destroy__ = _itkBSplineTransformPython.delete_itkBSplineTransformD43
    cast = _swig_new_static_method(_itkBSplineTransformPython.itkBSplineTransformD43_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformD43

        Create a new object of the class itkBSplineTransformD43 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformD43.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineTransformD43.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineTransformD43.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformD43 in _itkBSplineTransformPython:
_itkBSplineTransformPython.itkBSplineTransformD43_swigregister(itkBSplineTransformD43)
itkBSplineTransformD43___New_orig__ = _itkBSplineTransformPython.itkBSplineTransformD43___New_orig__
itkBSplineTransformD43_cast = _itkBSplineTransformPython.itkBSplineTransformD43_cast



