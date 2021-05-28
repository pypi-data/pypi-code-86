# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKRegistrationCommonPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkBlockMatchingImageFilterPython
else:
    import _itkBlockMatchingImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBlockMatchingImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBlockMatchingImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkVectorContainerPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkPointSetPython
import itk.itkImagePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageRegionPython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython

def itkBlockMatchingImageFilterID3_Superclass_Superclass_New():
    return itkBlockMatchingImageFilterID3_Superclass_Superclass.New()

class itkBlockMatchingImageFilterID3_Superclass_Superclass(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkBlockMatchingImageFilterID3_Superclass_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_Superclass_Clone)
    GetOutput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_Superclass_GetOutput)
    SetOutput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_Superclass_SetOutput)
    GraftOutput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_Superclass_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_Superclass_GraftNthOutput)
    __swig_destroy__ = _itkBlockMatchingImageFilterPython.delete_itkBlockMatchingImageFilterID3_Superclass_Superclass
    cast = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkBlockMatchingImageFilterID3_Superclass_Superclass

        Create a new object of the class itkBlockMatchingImageFilterID3_Superclass_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBlockMatchingImageFilterID3_Superclass_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBlockMatchingImageFilterID3_Superclass_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBlockMatchingImageFilterID3_Superclass_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBlockMatchingImageFilterID3_Superclass_Superclass in _itkBlockMatchingImageFilterPython:
_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_Superclass_swigregister(itkBlockMatchingImageFilterID3_Superclass_Superclass)
itkBlockMatchingImageFilterID3_Superclass_Superclass___New_orig__ = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_Superclass___New_orig__
itkBlockMatchingImageFilterID3_Superclass_Superclass_cast = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_Superclass_cast


def itkBlockMatchingImageFilterIF3_Superclass_Superclass_New():
    return itkBlockMatchingImageFilterIF3_Superclass_Superclass.New()

class itkBlockMatchingImageFilterIF3_Superclass_Superclass(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkBlockMatchingImageFilterIF3_Superclass_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_Superclass_Clone)
    GetOutput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_Superclass_GetOutput)
    SetOutput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_Superclass_SetOutput)
    GraftOutput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_Superclass_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_Superclass_GraftNthOutput)
    __swig_destroy__ = _itkBlockMatchingImageFilterPython.delete_itkBlockMatchingImageFilterIF3_Superclass_Superclass
    cast = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkBlockMatchingImageFilterIF3_Superclass_Superclass

        Create a new object of the class itkBlockMatchingImageFilterIF3_Superclass_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBlockMatchingImageFilterIF3_Superclass_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBlockMatchingImageFilterIF3_Superclass_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBlockMatchingImageFilterIF3_Superclass_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBlockMatchingImageFilterIF3_Superclass_Superclass in _itkBlockMatchingImageFilterPython:
_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_Superclass_swigregister(itkBlockMatchingImageFilterIF3_Superclass_Superclass)
itkBlockMatchingImageFilterIF3_Superclass_Superclass___New_orig__ = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_Superclass___New_orig__
itkBlockMatchingImageFilterIF3_Superclass_Superclass_cast = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_Superclass_cast


def itkPointSetVF33_New():
    return itkPointSetVF33.New()

class itkPointSetVF33(itk.ITKCommonBasePython.itkDataObject):
    r"""


    A superclass of the N-dimensional mesh structure; supports point
    (geometric coordinate and attribute) definition.

    PointSet is a superclass of the N-dimensional mesh structure
    (itk::Mesh). It provides the portion of the mesh definition for
    geometric coordinates (and associated attribute or pixel information).
    The defined API provides operations on points but does not tie down
    the underlying implementation and storage. A "MeshTraits" structure
    is used to define the container and identifier to access the points.
    See DefaultStaticMeshTraits for the set of type definitions needed.
    All types that are defined in the "MeshTraits" structure will have
    duplicate type alias in the resulting mesh itself.

    PointSet has two template parameters. The first is the pixel type, or
    the type of data stored (optionally) with the points. The second is
    the "MeshTraits" structure controlling type information
    characterizing the point set. Most users will be happy with the
    defaults, and will not have to worry about this second argument.

    Template parameters for PointSet:

    TPixelType = The type stored as data for the point.

    TMeshTraits = Type information structure for the point set. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33___New_orig__)
    Clone = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_Clone)
    GetMaximumNumberOfRegions = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_GetMaximumNumberOfRegions)
    PassStructure = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_PassStructure)
    GetNumberOfPoints = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_GetNumberOfPoints)
    SetPoints = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_SetPoints)
    GetPoints = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_GetPoints)
    SetPoint = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_SetPoint)
    GetPoint = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_GetPoint)
    SetPointData = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_SetPointData)
    GetPointData = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_GetPointData)
    SetRequestedRegion = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_SetRequestedRegion)
    GetRequestedRegion = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_GetRequestedRegion)
    SetBufferedRegion = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_SetBufferedRegion)
    GetBufferedRegion = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_GetBufferedRegion)
    __swig_destroy__ = _itkBlockMatchingImageFilterPython.delete_itkPointSetVF33
    cast = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkPointSetVF33_cast)

    def New(*args, **kargs):
        """New() -> itkPointSetVF33

        Create a new object of the class itkPointSetVF33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPointSetVF33.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPointSetVF33.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPointSetVF33.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPointSetVF33 in _itkBlockMatchingImageFilterPython:
_itkBlockMatchingImageFilterPython.itkPointSetVF33_swigregister(itkPointSetVF33)
itkPointSetVF33___New_orig__ = _itkBlockMatchingImageFilterPython.itkPointSetVF33___New_orig__
itkPointSetVF33_cast = _itkBlockMatchingImageFilterPython.itkPointSetVF33_cast


def itkBlockMatchingImageFilterID3_Superclass_New():
    return itkBlockMatchingImageFilterID3_Superclass.New()

class itkBlockMatchingImageFilterID3_Superclass(itkBlockMatchingImageFilterIF3_Superclass_Superclass):
    r"""Proxy of C++ itkBlockMatchingImageFilterID3_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_Clone)
    SetInput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_SetInput)
    GetInput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_GetInput)
    __swig_destroy__ = _itkBlockMatchingImageFilterPython.delete_itkBlockMatchingImageFilterID3_Superclass
    cast = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkBlockMatchingImageFilterID3_Superclass

        Create a new object of the class itkBlockMatchingImageFilterID3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBlockMatchingImageFilterID3_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBlockMatchingImageFilterID3_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBlockMatchingImageFilterID3_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBlockMatchingImageFilterID3_Superclass in _itkBlockMatchingImageFilterPython:
_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_swigregister(itkBlockMatchingImageFilterID3_Superclass)
itkBlockMatchingImageFilterID3_Superclass___New_orig__ = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass___New_orig__
itkBlockMatchingImageFilterID3_Superclass_cast = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Superclass_cast


def itkBlockMatchingImageFilterIF3_Superclass_New():
    return itkBlockMatchingImageFilterIF3_Superclass.New()

class itkBlockMatchingImageFilterIF3_Superclass(itkBlockMatchingImageFilterIF3_Superclass_Superclass):
    r"""Proxy of C++ itkBlockMatchingImageFilterIF3_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_Clone)
    SetInput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_SetInput)
    GetInput = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_GetInput)
    __swig_destroy__ = _itkBlockMatchingImageFilterPython.delete_itkBlockMatchingImageFilterIF3_Superclass
    cast = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkBlockMatchingImageFilterIF3_Superclass

        Create a new object of the class itkBlockMatchingImageFilterIF3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBlockMatchingImageFilterIF3_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBlockMatchingImageFilterIF3_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBlockMatchingImageFilterIF3_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBlockMatchingImageFilterIF3_Superclass in _itkBlockMatchingImageFilterPython:
_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_swigregister(itkBlockMatchingImageFilterIF3_Superclass)
itkBlockMatchingImageFilterIF3_Superclass___New_orig__ = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass___New_orig__
itkBlockMatchingImageFilterIF3_Superclass_cast = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Superclass_cast


def itkBlockMatchingImageFilterID3_New():
    return itkBlockMatchingImageFilterID3.New()

class itkBlockMatchingImageFilterID3(itkBlockMatchingImageFilterIF3_Superclass):
    r"""


    Computes displacements of given points from a fixed image in a
    floating image.

    BlockMatchingImageFilter takes fixed and moving Images as well as
    PointSet of feature points as inputs. Physical coordinates of feature
    points are stored as point coordinates. Points of the input point set
    must have unique identifiers within range 0..N-1, where N is the
    number of points. Pixels (pointData) of input point set are not used.
    Additionally, by default, feature points are expected to lie at least
    (SearchRadius + BlockRadius) voxels from a boundary. This is usually
    achieved by using an appropriate mask during selection of feature
    points. If you are unsure whether feature points satisfy the above
    condition set CheckBoundary flag to true which turns on boundary
    checks. The default output(0) is a PointSet with displacements stored
    as vectors. Additional output(1) is a PointSet containing
    similarities. Similarities are needed to compute displacements and are
    always computed. The number of points in the output PointSet is equal
    to the number of points in the input PointSet.

    The filter is templated over fixed Image, moving Image, input
    PointSet, output displacements PointSet and output similarities
    PointSet.

    This filter is intended to be used in the process of Physics-Based
    Non-Rigid Registration. It computes displacement for selected points
    based on similarity [M. Bierling, Displacement estimation by
    hierarchical block matching, Proc. SPIE Vis. Comm. and Image Proc.,
    vol. 1001, pp. 942-951, 1988.].

    Andriy Kot, Center for Real-Time Computing, Old Dominion University,
    Norfolk, VA

    See:  MaskFeaturePointSelectionFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3___New_orig__)
    Clone = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_Clone)
    SetBlockRadius = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_SetBlockRadius)
    GetBlockRadius = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_GetBlockRadius)
    SetSearchRadius = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_SetSearchRadius)
    GetSearchRadius = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_GetSearchRadius)
    SetFixedImage = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_SetFixedImage)
    GetFixedImage = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_GetFixedImage)
    SetMovingImage = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_SetMovingImage)
    GetMovingImage = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_GetMovingImage)
    SetFeaturePoints = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_SetFeaturePoints)
    GetFeaturePoints = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_GetFeaturePoints)
    GetDisplacements = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_GetDisplacements)
    GetSimilarities = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_GetSimilarities)
    __swig_destroy__ = _itkBlockMatchingImageFilterPython.delete_itkBlockMatchingImageFilterID3
    cast = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_cast)

    def New(*args, **kargs):
        """New() -> itkBlockMatchingImageFilterID3

        Create a new object of the class itkBlockMatchingImageFilterID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBlockMatchingImageFilterID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBlockMatchingImageFilterID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBlockMatchingImageFilterID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBlockMatchingImageFilterID3 in _itkBlockMatchingImageFilterPython:
_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_swigregister(itkBlockMatchingImageFilterID3)
itkBlockMatchingImageFilterID3___New_orig__ = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3___New_orig__
itkBlockMatchingImageFilterID3_cast = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterID3_cast


def itkBlockMatchingImageFilterIF3_New():
    return itkBlockMatchingImageFilterIF3.New()

class itkBlockMatchingImageFilterIF3(itkBlockMatchingImageFilterIF3_Superclass):
    r"""


    Computes displacements of given points from a fixed image in a
    floating image.

    BlockMatchingImageFilter takes fixed and moving Images as well as
    PointSet of feature points as inputs. Physical coordinates of feature
    points are stored as point coordinates. Points of the input point set
    must have unique identifiers within range 0..N-1, where N is the
    number of points. Pixels (pointData) of input point set are not used.
    Additionally, by default, feature points are expected to lie at least
    (SearchRadius + BlockRadius) voxels from a boundary. This is usually
    achieved by using an appropriate mask during selection of feature
    points. If you are unsure whether feature points satisfy the above
    condition set CheckBoundary flag to true which turns on boundary
    checks. The default output(0) is a PointSet with displacements stored
    as vectors. Additional output(1) is a PointSet containing
    similarities. Similarities are needed to compute displacements and are
    always computed. The number of points in the output PointSet is equal
    to the number of points in the input PointSet.

    The filter is templated over fixed Image, moving Image, input
    PointSet, output displacements PointSet and output similarities
    PointSet.

    This filter is intended to be used in the process of Physics-Based
    Non-Rigid Registration. It computes displacement for selected points
    based on similarity [M. Bierling, Displacement estimation by
    hierarchical block matching, Proc. SPIE Vis. Comm. and Image Proc.,
    vol. 1001, pp. 942-951, 1988.].

    Andriy Kot, Center for Real-Time Computing, Old Dominion University,
    Norfolk, VA

    See:  MaskFeaturePointSelectionFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3___New_orig__)
    Clone = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_Clone)
    SetBlockRadius = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_SetBlockRadius)
    GetBlockRadius = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_GetBlockRadius)
    SetSearchRadius = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_SetSearchRadius)
    GetSearchRadius = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_GetSearchRadius)
    SetFixedImage = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_SetFixedImage)
    GetFixedImage = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_GetFixedImage)
    SetMovingImage = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_SetMovingImage)
    GetMovingImage = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_GetMovingImage)
    SetFeaturePoints = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_SetFeaturePoints)
    GetFeaturePoints = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_GetFeaturePoints)
    GetDisplacements = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_GetDisplacements)
    GetSimilarities = _swig_new_instance_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_GetSimilarities)
    __swig_destroy__ = _itkBlockMatchingImageFilterPython.delete_itkBlockMatchingImageFilterIF3
    cast = _swig_new_static_method(_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_cast)

    def New(*args, **kargs):
        """New() -> itkBlockMatchingImageFilterIF3

        Create a new object of the class itkBlockMatchingImageFilterIF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBlockMatchingImageFilterIF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBlockMatchingImageFilterIF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBlockMatchingImageFilterIF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBlockMatchingImageFilterIF3 in _itkBlockMatchingImageFilterPython:
_itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_swigregister(itkBlockMatchingImageFilterIF3)
itkBlockMatchingImageFilterIF3___New_orig__ = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3___New_orig__
itkBlockMatchingImageFilterIF3_cast = _itkBlockMatchingImageFilterPython.itkBlockMatchingImageFilterIF3_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def mesh_to_mesh_filter(*args,  output: itkt.PointSet=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for MeshToMeshFilter"""
    import itk

    kwarg_typehints = { 'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.MeshToMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def mesh_to_mesh_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKRegistrationCommon.MeshToMeshFilter
    mesh_to_mesh_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    mesh_to_mesh_filter.__doc__ = filter_object.__doc__

from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def block_matching_image_filter(*args: itkt.Mesh,  block_radius: Sequence[int]=..., search_radius: Sequence[int]=..., fixed_image: itkt.Image=..., moving_image: itkt.Image=..., feature_points: itkt.PointSet=..., output: itkt.PointSet=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for BlockMatchingImageFilter"""
    import itk

    kwarg_typehints = { 'block_radius':block_radius,'search_radius':search_radius,'fixed_image':fixed_image,'moving_image':moving_image,'feature_points':feature_points,'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.BlockMatchingImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def block_matching_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKRegistrationCommon.BlockMatchingImageFilter
    block_matching_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    block_matching_image_filter.__doc__ = filter_object.__doc__

from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def mesh_source(*args,  output: itkt.PointSet=...,**kwargs):
    """Functional interface for MeshSource"""
    import itk

    kwarg_typehints = { 'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.MeshSource.New(*args, **kwargs)
    return instance.__internal_call__()

def mesh_source_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKRegistrationCommon.MeshSource
    mesh_source.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    mesh_source.__doc__ = filter_object.__doc__




