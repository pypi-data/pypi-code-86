# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKQuadEdgeMeshFilteringPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkDiscreteCurvatureQuadEdgeMeshFilterPython
else:
    import _itkDiscreteCurvatureQuadEdgeMeshFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkQuadEdgeMeshPointPython
import itk.itkGeometricalQuadEdgePython
import itk.itkQuadEdgePython
import itk.pyBasePython
import itk.itkPointPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython
import itk.itkQuadEdgeMeshBasePython
import itk.itkQuadEdgeMeshLineCellPython
import itk.itkArrayPython
import itk.ITKCommonBasePython
import itk.itkQuadEdgeCellTraitsInfoPython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkCovariantVectorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
import itk.itkMapContainerPython
class itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2(itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2):
    r"""


    FIXME. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    OutputIsFloatingPointCheck = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_OutputIsFloatingPointCheck
    
    __swig_destroy__ = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2
    cast = _swig_new_static_method(_itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_cast)

# Register itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2 in _itkDiscreteCurvatureQuadEdgeMeshFilterPython:
_itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_swigregister(itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2)
itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_cast = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2_cast

class itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3(itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3):
    r"""


    FIXME. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    OutputIsFloatingPointCheck = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_OutputIsFloatingPointCheck
    
    __swig_destroy__ = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3
    cast = _swig_new_static_method(_itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_cast)

# Register itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3 in _itkDiscreteCurvatureQuadEdgeMeshFilterPython:
_itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_swigregister(itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3)
itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_cast = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3_cast

class itkDiscreteCurvatureQuadEdgeMeshFilterQEMD4(itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD4QEMD4):
    r"""


    FIXME. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    OutputIsFloatingPointCheck = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD4_OutputIsFloatingPointCheck
    
    __swig_destroy__ = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.delete_itkDiscreteCurvatureQuadEdgeMeshFilterQEMD4
    cast = _swig_new_static_method(_itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD4_cast)

# Register itkDiscreteCurvatureQuadEdgeMeshFilterQEMD4 in _itkDiscreteCurvatureQuadEdgeMeshFilterPython:
_itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD4_swigregister(itkDiscreteCurvatureQuadEdgeMeshFilterQEMD4)
itkDiscreteCurvatureQuadEdgeMeshFilterQEMD4_cast = _itkDiscreteCurvatureQuadEdgeMeshFilterPython.itkDiscreteCurvatureQuadEdgeMeshFilterQEMD4_cast



