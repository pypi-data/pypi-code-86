# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageFeaturePython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkMaskFeaturePointSelectionFilterPython
else:
    import _itkMaskFeaturePointSelectionFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMaskFeaturePointSelectionFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMaskFeaturePointSelectionFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkSizePython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkPointSetPython
import itk.itkMatrixPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkCovariantVectorPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkVectorContainerPython
import itk.itkOffsetPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkImageRegionPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBAPixelPython

def itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_New():
    return itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass.New()

class itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_Clone)
    GetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_GetOutput)
    SetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_SetOutput)
    GraftOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_GraftNthOutput)
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass

        Create a new object of the class itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_swigregister(itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass)
itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass___New_orig__ = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass___New_orig__
itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_Superclass_cast


def itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_New():
    return itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.New()

class itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_Clone)
    GetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GetOutput)
    SetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_SetOutput)
    GraftOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_GraftNthOutput)
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass

        Create a new object of the class itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_swigregister(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass___New_orig__ = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass___New_orig__
itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass_cast

class itkMaskFeaturePointSelectionFilterID3_Superclass(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass):
    r"""Proxy of C++ itkMaskFeaturePointSelectionFilterID3_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_SetInput)
    GetInput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_GetInput)
    GetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_GetOutput)
    GenerateOutputInformation = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_GenerateOutputInformation)
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterID3_Superclass
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_cast)

# Register itkMaskFeaturePointSelectionFilterID3_Superclass in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_swigregister(itkMaskFeaturePointSelectionFilterID3_Superclass)
itkMaskFeaturePointSelectionFilterID3_Superclass_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Superclass_cast

class itkMaskFeaturePointSelectionFilterIF3_Superclass(itkMaskFeaturePointSelectionFilterIF3_Superclass_Superclass):
    r"""Proxy of C++ itkMaskFeaturePointSelectionFilterIF3_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_SetInput)
    GetInput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GetInput)
    GetOutput = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GetOutput)
    GenerateOutputInformation = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_GenerateOutputInformation)
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterIF3_Superclass
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_cast)

# Register itkMaskFeaturePointSelectionFilterIF3_Superclass in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_swigregister(itkMaskFeaturePointSelectionFilterIF3_Superclass)
itkMaskFeaturePointSelectionFilterIF3_Superclass_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Superclass_cast


def itkMaskFeaturePointSelectionFilterID3_New():
    return itkMaskFeaturePointSelectionFilterID3.New()

class itkMaskFeaturePointSelectionFilterID3(itkMaskFeaturePointSelectionFilterID3_Superclass):
    r"""


    Generate a PointSet containing the feature points selected from a
    masked 3D input image.

    MaskFeaturePointSelectionFilter takes 3D image and 3D mask as inputs
    and generates a PointSet of feature points as output.

    This filter is intended to be used for initializing the process of
    Physics-Based Non-Rigid Registration. It selects a fraction of non-
    masked points with highest variance. Optionally, tensors are computed
    for each point and stored as pixel values. [ M. Bierling, Displacement
    estimation by hierarchical block matching, Proc. SPIE Vis. Comm. and
    Image Proc., vol. 1001, pp. 942-951, 1988. ].

    The filter is templated over input image and mask and output pointset.
    Andriy Kot, Center for Real-Time Computing, Old Dominion University,
    Norfolk, VA

    See:  BlockMatchingImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3___New_orig__)
    Clone = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_Clone)
    VERTEX_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_VERTEX_CONNECTIVITY
    
    EDGE_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_EDGE_CONNECTIVITY
    
    FACE_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_FACE_CONNECTIVITY
    
    SetNonConnectivity = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_SetNonConnectivity)
    GetNonConnectivity = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_GetNonConnectivity)
    SetMaskImage = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_SetMaskImage)
    GetMaskImage = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_GetMaskImage)
    SetBlockRadius = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_SetBlockRadius)
    GetBlockRadius = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_GetBlockRadius)
    SetComputeStructureTensors = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_SetComputeStructureTensors)
    GetComputeStructureTensors = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_GetComputeStructureTensors)
    ComputeStructureTensorsOn = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_ComputeStructureTensorsOn)
    ComputeStructureTensorsOff = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_ComputeStructureTensorsOff)
    SetSelectFraction = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_SetSelectFraction)
    GetSelectFraction = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_GetSelectFraction)
    ImageDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_ImageDimensionShouldBe3
    
    MaskDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_MaskDimensionShouldBe3
    
    PointDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_PointDimensionShouldBe3
    
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterID3
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_cast)

    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterID3

        Create a new object of the class itkMaskFeaturePointSelectionFilterID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMaskFeaturePointSelectionFilterID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaskFeaturePointSelectionFilterID3 in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_swigregister(itkMaskFeaturePointSelectionFilterID3)
itkMaskFeaturePointSelectionFilterID3___New_orig__ = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3___New_orig__
itkMaskFeaturePointSelectionFilterID3_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterID3_cast


def itkMaskFeaturePointSelectionFilterIF3_New():
    return itkMaskFeaturePointSelectionFilterIF3.New()

class itkMaskFeaturePointSelectionFilterIF3(itkMaskFeaturePointSelectionFilterIF3_Superclass):
    r"""


    Generate a PointSet containing the feature points selected from a
    masked 3D input image.

    MaskFeaturePointSelectionFilter takes 3D image and 3D mask as inputs
    and generates a PointSet of feature points as output.

    This filter is intended to be used for initializing the process of
    Physics-Based Non-Rigid Registration. It selects a fraction of non-
    masked points with highest variance. Optionally, tensors are computed
    for each point and stored as pixel values. [ M. Bierling, Displacement
    estimation by hierarchical block matching, Proc. SPIE Vis. Comm. and
    Image Proc., vol. 1001, pp. 942-951, 1988. ].

    The filter is templated over input image and mask and output pointset.
    Andriy Kot, Center for Real-Time Computing, Old Dominion University,
    Norfolk, VA

    See:  BlockMatchingImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3___New_orig__)
    Clone = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_Clone)
    VERTEX_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_VERTEX_CONNECTIVITY
    
    EDGE_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_EDGE_CONNECTIVITY
    
    FACE_CONNECTIVITY = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_FACE_CONNECTIVITY
    
    SetNonConnectivity = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetNonConnectivity)
    GetNonConnectivity = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetNonConnectivity)
    SetMaskImage = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetMaskImage)
    GetMaskImage = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetMaskImage)
    SetBlockRadius = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetBlockRadius)
    GetBlockRadius = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetBlockRadius)
    SetComputeStructureTensors = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetComputeStructureTensors)
    GetComputeStructureTensors = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetComputeStructureTensors)
    ComputeStructureTensorsOn = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_ComputeStructureTensorsOn)
    ComputeStructureTensorsOff = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_ComputeStructureTensorsOff)
    SetSelectFraction = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_SetSelectFraction)
    GetSelectFraction = _swig_new_instance_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_GetSelectFraction)
    ImageDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_ImageDimensionShouldBe3
    
    MaskDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_MaskDimensionShouldBe3
    
    PointDimensionShouldBe3 = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_PointDimensionShouldBe3
    
    __swig_destroy__ = _itkMaskFeaturePointSelectionFilterPython.delete_itkMaskFeaturePointSelectionFilterIF3
    cast = _swig_new_static_method(_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_cast)

    def New(*args, **kargs):
        """New() -> itkMaskFeaturePointSelectionFilterIF3

        Create a new object of the class itkMaskFeaturePointSelectionFilterIF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaskFeaturePointSelectionFilterIF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMaskFeaturePointSelectionFilterIF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMaskFeaturePointSelectionFilterIF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaskFeaturePointSelectionFilterIF3 in _itkMaskFeaturePointSelectionFilterPython:
_itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_swigregister(itkMaskFeaturePointSelectionFilterIF3)
itkMaskFeaturePointSelectionFilterIF3___New_orig__ = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3___New_orig__
itkMaskFeaturePointSelectionFilterIF3_cast = _itkMaskFeaturePointSelectionFilterPython.itkMaskFeaturePointSelectionFilterIF3_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def mask_feature_point_selection_filter(*args: itkt.ImageLike,  non_connectivity: int=..., mask_image: itkt.Image=..., block_radius: Sequence[int]=..., compute_structure_tensors: bool=..., select_fraction: float=..., output: itkt.PointSet=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for MaskFeaturePointSelectionFilter"""
    import itk

    kwarg_typehints = { 'non_connectivity':non_connectivity,'mask_image':mask_image,'block_radius':block_radius,'compute_structure_tensors':compute_structure_tensors,'select_fraction':select_fraction,'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.MaskFeaturePointSelectionFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def mask_feature_point_selection_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageFeature.MaskFeaturePointSelectionFilter
    mask_feature_point_selection_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    mask_feature_point_selection_filter.__doc__ = filter_object.__doc__

from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def image_to_mesh_filter(*args,  output: itkt.PointSet=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for ImageToMeshFilter"""
    import itk

    kwarg_typehints = { 'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ImageToMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def image_to_mesh_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageFeature.ImageToMeshFilter
    image_to_mesh_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    image_to_mesh_filter.__doc__ = filter_object.__doc__

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

    filter_class = itk.ITKImageFeature.MeshSource
    mesh_source.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    mesh_source.__doc__ = filter_object.__doc__




