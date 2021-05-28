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
    from . import _itkMetaConverterBasePython
else:
    import _itkMetaConverterBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMetaConverterBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMetaConverterBasePython.SWIG_PyStaticMethod_New

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
import itk.itkSpatialObjectBasePython
import itk.itkCovariantVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.vnl_matrix_fixedPython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkTransformBasePython
import itk.itkArray2DPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.itkVariableLengthVectorPython
import itk.itkDiffusionTensor3DPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkSpatialObjectPropertyPython
import itk.itkRGBAPixelPython
class itkMetaConverterBase2(itk.ITKCommonBasePython.itkObject):
    r"""


    Base class for MetaObject<-> SpatialObject converters.

    SpatialObject scenes are written and read using the MetaIO Library.
    This is managed by the MetaSceneConverter class, which converts
    MetaObject scenes to SpatialObject scenes and vice versa.

    MetaScene walks the scene and uses the converter on each object in the
    scene. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    ReadMeta = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase2_ReadMeta)
    WriteMeta = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase2_WriteMeta)
    MetaObjectToSpatialObject = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase2_MetaObjectToSpatialObject)
    SpatialObjectToMetaObject = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase2_SpatialObjectToMetaObject)
    SetWriteImagesInSeparateFile = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase2_SetWriteImagesInSeparateFile)
    GetWriteImagesInSeparateFile = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase2_GetWriteImagesInSeparateFile)
    WriteImagesInSeparateFileOn = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase2_WriteImagesInSeparateFileOn)
    WriteImagesInSeparateFileOff = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase2_WriteImagesInSeparateFileOff)

# Register itkMetaConverterBase2 in _itkMetaConverterBasePython:
_itkMetaConverterBasePython.itkMetaConverterBase2_swigregister(itkMetaConverterBase2)

class itkMetaConverterBase3(itk.ITKCommonBasePython.itkObject):
    r"""


    Base class for MetaObject<-> SpatialObject converters.

    SpatialObject scenes are written and read using the MetaIO Library.
    This is managed by the MetaSceneConverter class, which converts
    MetaObject scenes to SpatialObject scenes and vice versa.

    MetaScene walks the scene and uses the converter on each object in the
    scene. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    ReadMeta = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase3_ReadMeta)
    WriteMeta = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase3_WriteMeta)
    MetaObjectToSpatialObject = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase3_MetaObjectToSpatialObject)
    SpatialObjectToMetaObject = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase3_SpatialObjectToMetaObject)
    SetWriteImagesInSeparateFile = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase3_SetWriteImagesInSeparateFile)
    GetWriteImagesInSeparateFile = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase3_GetWriteImagesInSeparateFile)
    WriteImagesInSeparateFileOn = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase3_WriteImagesInSeparateFileOn)
    WriteImagesInSeparateFileOff = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase3_WriteImagesInSeparateFileOff)

# Register itkMetaConverterBase3 in _itkMetaConverterBasePython:
_itkMetaConverterBasePython.itkMetaConverterBase3_swigregister(itkMetaConverterBase3)

class itkMetaConverterBase4(itk.ITKCommonBasePython.itkObject):
    r"""


    Base class for MetaObject<-> SpatialObject converters.

    SpatialObject scenes are written and read using the MetaIO Library.
    This is managed by the MetaSceneConverter class, which converts
    MetaObject scenes to SpatialObject scenes and vice versa.

    MetaScene walks the scene and uses the converter on each object in the
    scene. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    ReadMeta = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase4_ReadMeta)
    WriteMeta = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase4_WriteMeta)
    MetaObjectToSpatialObject = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase4_MetaObjectToSpatialObject)
    SpatialObjectToMetaObject = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase4_SpatialObjectToMetaObject)
    SetWriteImagesInSeparateFile = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase4_SetWriteImagesInSeparateFile)
    GetWriteImagesInSeparateFile = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase4_GetWriteImagesInSeparateFile)
    WriteImagesInSeparateFileOn = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase4_WriteImagesInSeparateFileOn)
    WriteImagesInSeparateFileOff = _swig_new_instance_method(_itkMetaConverterBasePython.itkMetaConverterBase4_WriteImagesInSeparateFileOff)

# Register itkMetaConverterBase4 in _itkMetaConverterBasePython:
_itkMetaConverterBasePython.itkMetaConverterBase4_swigregister(itkMetaConverterBase4)



