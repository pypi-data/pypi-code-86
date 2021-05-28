# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKSpatialObjectsPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkCastSpatialObjectFilterPython
else:
    import _itkCastSpatialObjectFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCastSpatialObjectFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCastSpatialObjectFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkBlobSpatialObjectPython
import itk.itkPointBasedSpatialObjectPython
import itk.itkSpatialObjectPointPython
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkSpatialObjectBasePython
import itk.itkBoundingBoxPython
import itk.itkVectorContainerPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkPointPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkMapContainerPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkVariableLengthVectorPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkArray2DPython
import itk.itkTransformBasePython
import itk.itkImageRegionPython
import itk.itkSpatialObjectPropertyPython
import itk.itkGaussianSpatialObjectPython
import itk.itkEllipseSpatialObjectPython
import itk.itkPolygonSpatialObjectPython
import itk.itkLandmarkSpatialObjectPython
import itk.itkArrowSpatialObjectPython
import itk.itkLineSpatialObjectPython
import itk.itkLineSpatialObjectPointPython
import itk.itkImageMaskSpatialObjectPython
import itk.itkImageSpatialObjectPython
import itk.itkInterpolateImageFunctionPython
import itk.itkRGBPixelPython
import itk.itkImageFunctionBasePython
import itk.itkFunctionBasePython
import itk.itkImagePython
import itk.itkSurfaceSpatialObjectPython
import itk.itkSurfaceSpatialObjectPointPython
import itk.itkBoxSpatialObjectPython
import itk.itkGroupSpatialObjectPython
import itk.itkContourSpatialObjectPython
import itk.itkContourSpatialObjectPointPython
import itk.itkTubeSpatialObjectPython
import itk.itkTubeSpatialObjectPointPython

def itkCastSpatialObjectFilter2_New():
    return itkCastSpatialObjectFilter2.New()

class itkCastSpatialObjectFilter2(itk.ITKCommonBasePython.itkObject):
    r"""


    This filter casts one spatialobject to another, when the class
    hierarchy supports it (e.g., Tube to PointBased). Particularly useful
    in Python where casting objects without public contructors (e.g.,
    objects managed by smartpointers) is problematic. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2___New_orig__)
    Clone = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_Clone)
    SetInput = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_SetInput)
    GetInput = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetInput)
    GetArrows = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetArrows)
    GetBlobs = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetBlobs)
    GetBoxes = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetBoxes)
    GetContours = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetContours)
    GetEllipses = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetEllipses)
    GetGaussians = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetGaussians)
    GetGroups = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetGroups)
    GetImageMasks = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetImageMasks)
    GetImages = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetImages)
    GetLandmarks = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetLandmarks)
    GetLines = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetLines)
    GetPointBased = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetPointBased)
    GetPolygons = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetPolygons)
    GetSpatialObjects = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetSpatialObjects)
    GetSurfaces = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetSurfaces)
    GetTubes = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetTubes)
    __swig_destroy__ = _itkCastSpatialObjectFilterPython.delete_itkCastSpatialObjectFilter2
    cast = _swig_new_static_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_cast)

    def New(*args, **kargs):
        """New() -> itkCastSpatialObjectFilter2

        Create a new object of the class itkCastSpatialObjectFilter2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCastSpatialObjectFilter2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCastSpatialObjectFilter2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCastSpatialObjectFilter2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCastSpatialObjectFilter2 in _itkCastSpatialObjectFilterPython:
_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_swigregister(itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2___New_orig__ = _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2___New_orig__
itkCastSpatialObjectFilter2_cast = _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_cast


def itkCastSpatialObjectFilter3_New():
    return itkCastSpatialObjectFilter3.New()

class itkCastSpatialObjectFilter3(itk.ITKCommonBasePython.itkObject):
    r"""


    This filter casts one spatialobject to another, when the class
    hierarchy supports it (e.g., Tube to PointBased). Particularly useful
    in Python where casting objects without public contructors (e.g.,
    objects managed by smartpointers) is problematic. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3___New_orig__)
    Clone = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_Clone)
    SetInput = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_SetInput)
    GetInput = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetInput)
    GetArrows = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetArrows)
    GetBlobs = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetBlobs)
    GetBoxes = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetBoxes)
    GetContours = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetContours)
    GetEllipses = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetEllipses)
    GetGaussians = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetGaussians)
    GetGroups = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetGroups)
    GetImageMasks = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetImageMasks)
    GetImages = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetImages)
    GetLandmarks = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetLandmarks)
    GetLines = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetLines)
    GetPointBased = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetPointBased)
    GetPolygons = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetPolygons)
    GetSpatialObjects = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetSpatialObjects)
    GetSurfaces = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetSurfaces)
    GetTubes = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetTubes)
    __swig_destroy__ = _itkCastSpatialObjectFilterPython.delete_itkCastSpatialObjectFilter3
    cast = _swig_new_static_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_cast)

    def New(*args, **kargs):
        """New() -> itkCastSpatialObjectFilter3

        Create a new object of the class itkCastSpatialObjectFilter3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCastSpatialObjectFilter3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCastSpatialObjectFilter3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCastSpatialObjectFilter3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCastSpatialObjectFilter3 in _itkCastSpatialObjectFilterPython:
_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_swigregister(itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3___New_orig__ = _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3___New_orig__
itkCastSpatialObjectFilter3_cast = _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_cast


def itkCastSpatialObjectFilter4_New():
    return itkCastSpatialObjectFilter4.New()

class itkCastSpatialObjectFilter4(itk.ITKCommonBasePython.itkObject):
    r"""


    This filter casts one spatialobject to another, when the class
    hierarchy supports it (e.g., Tube to PointBased). Particularly useful
    in Python where casting objects without public contructors (e.g.,
    objects managed by smartpointers) is problematic. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4___New_orig__)
    Clone = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_Clone)
    SetInput = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_SetInput)
    GetInput = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetInput)
    GetArrows = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetArrows)
    GetBlobs = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetBlobs)
    GetBoxes = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetBoxes)
    GetContours = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetContours)
    GetEllipses = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetEllipses)
    GetGaussians = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetGaussians)
    GetGroups = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetGroups)
    GetImageMasks = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetImageMasks)
    GetImages = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetImages)
    GetLandmarks = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetLandmarks)
    GetLines = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetLines)
    GetPointBased = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetPointBased)
    GetPolygons = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetPolygons)
    GetSpatialObjects = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetSpatialObjects)
    GetSurfaces = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetSurfaces)
    GetTubes = _swig_new_instance_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_GetTubes)
    __swig_destroy__ = _itkCastSpatialObjectFilterPython.delete_itkCastSpatialObjectFilter4
    cast = _swig_new_static_method(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_cast)

    def New(*args, **kargs):
        """New() -> itkCastSpatialObjectFilter4

        Create a new object of the class itkCastSpatialObjectFilter4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCastSpatialObjectFilter4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCastSpatialObjectFilter4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCastSpatialObjectFilter4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCastSpatialObjectFilter4 in _itkCastSpatialObjectFilterPython:
_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_swigregister(itkCastSpatialObjectFilter4)
itkCastSpatialObjectFilter4___New_orig__ = _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4___New_orig__
itkCastSpatialObjectFilter4_cast = _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter4_cast



