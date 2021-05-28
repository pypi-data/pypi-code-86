# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKPathPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkParametricPathPython
else:
    import _itkParametricPathPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkParametricPathPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkParametricPathPython.SWIG_PyStaticMethod_New

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
import itk.itkPathBasePython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkContinuousIndexPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkIndexPython
class itkParametricPath2(itk.itkPathBasePython.itkPathDCID22):
    r"""


    Represent a parametric path through ND Space.

    This virtual class is intended to represent a parametric path through
    an image. A parametric path maps a single floating-point 1D parameter
    (usually designated as either time or arc-length) to a floating-point
    ND point in continuous image index space. This mapping is done via the
    abstract Evaluate() method, which must be overridden in all
    instantiable subclasses. Parametric paths are required to be
    continuous. They may be open or form a closed loop. A parametric path
    may cross itself several times, although the end point is constrained
    to have a unique spatial location unless it is shared with and only
    with the starting point (a path tracing the number "9," starting at
    the bottom and ending in the middle of the right side, would therefore
    be illegal). Classic applications of this class include the
    representation of contours in 2D images and path smoothing. Another
    use of a path is to guide the movement of an iterator through an
    image.

    See:  EllipseParametricPath

    See:   PolyLineParametricPath

    See:  FourierSeriesPath

    See:  OrthogonallyCorrectedParametricPath

    See:  ChainCodePath

    See:   Path

    See:  ContinuousIndex

    See:  Index

    See:  Offset

    See:  Vector 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    EvaluateDerivative = _swig_new_instance_method(_itkParametricPathPython.itkParametricPath2_EvaluateDerivative)
    SetDefaultInputStepSize = _swig_new_instance_method(_itkParametricPathPython.itkParametricPath2_SetDefaultInputStepSize)
    GetDefaultInputStepSize = _swig_new_instance_method(_itkParametricPathPython.itkParametricPath2_GetDefaultInputStepSize)
    __swig_destroy__ = _itkParametricPathPython.delete_itkParametricPath2
    cast = _swig_new_static_method(_itkParametricPathPython.itkParametricPath2_cast)

# Register itkParametricPath2 in _itkParametricPathPython:
_itkParametricPathPython.itkParametricPath2_swigregister(itkParametricPath2)
itkParametricPath2_cast = _itkParametricPathPython.itkParametricPath2_cast

class itkParametricPath3(itk.itkPathBasePython.itkPathDCID33):
    r"""


    Represent a parametric path through ND Space.

    This virtual class is intended to represent a parametric path through
    an image. A parametric path maps a single floating-point 1D parameter
    (usually designated as either time or arc-length) to a floating-point
    ND point in continuous image index space. This mapping is done via the
    abstract Evaluate() method, which must be overridden in all
    instantiable subclasses. Parametric paths are required to be
    continuous. They may be open or form a closed loop. A parametric path
    may cross itself several times, although the end point is constrained
    to have a unique spatial location unless it is shared with and only
    with the starting point (a path tracing the number "9," starting at
    the bottom and ending in the middle of the right side, would therefore
    be illegal). Classic applications of this class include the
    representation of contours in 2D images and path smoothing. Another
    use of a path is to guide the movement of an iterator through an
    image.

    See:  EllipseParametricPath

    See:   PolyLineParametricPath

    See:  FourierSeriesPath

    See:  OrthogonallyCorrectedParametricPath

    See:  ChainCodePath

    See:   Path

    See:  ContinuousIndex

    See:  Index

    See:  Offset

    See:  Vector 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    EvaluateDerivative = _swig_new_instance_method(_itkParametricPathPython.itkParametricPath3_EvaluateDerivative)
    SetDefaultInputStepSize = _swig_new_instance_method(_itkParametricPathPython.itkParametricPath3_SetDefaultInputStepSize)
    GetDefaultInputStepSize = _swig_new_instance_method(_itkParametricPathPython.itkParametricPath3_GetDefaultInputStepSize)
    __swig_destroy__ = _itkParametricPathPython.delete_itkParametricPath3
    cast = _swig_new_static_method(_itkParametricPathPython.itkParametricPath3_cast)

# Register itkParametricPath3 in _itkParametricPathPython:
_itkParametricPathPython.itkParametricPath3_swigregister(itkParametricPath3)
itkParametricPath3_cast = _itkParametricPathPython.itkParametricPath3_cast

class itkParametricPath4(itk.itkPathBasePython.itkPathDCID44):
    r"""


    Represent a parametric path through ND Space.

    This virtual class is intended to represent a parametric path through
    an image. A parametric path maps a single floating-point 1D parameter
    (usually designated as either time or arc-length) to a floating-point
    ND point in continuous image index space. This mapping is done via the
    abstract Evaluate() method, which must be overridden in all
    instantiable subclasses. Parametric paths are required to be
    continuous. They may be open or form a closed loop. A parametric path
    may cross itself several times, although the end point is constrained
    to have a unique spatial location unless it is shared with and only
    with the starting point (a path tracing the number "9," starting at
    the bottom and ending in the middle of the right side, would therefore
    be illegal). Classic applications of this class include the
    representation of contours in 2D images and path smoothing. Another
    use of a path is to guide the movement of an iterator through an
    image.

    See:  EllipseParametricPath

    See:   PolyLineParametricPath

    See:  FourierSeriesPath

    See:  OrthogonallyCorrectedParametricPath

    See:  ChainCodePath

    See:   Path

    See:  ContinuousIndex

    See:  Index

    See:  Offset

    See:  Vector 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    EvaluateDerivative = _swig_new_instance_method(_itkParametricPathPython.itkParametricPath4_EvaluateDerivative)
    SetDefaultInputStepSize = _swig_new_instance_method(_itkParametricPathPython.itkParametricPath4_SetDefaultInputStepSize)
    GetDefaultInputStepSize = _swig_new_instance_method(_itkParametricPathPython.itkParametricPath4_GetDefaultInputStepSize)
    __swig_destroy__ = _itkParametricPathPython.delete_itkParametricPath4
    cast = _swig_new_static_method(_itkParametricPathPython.itkParametricPath4_cast)

# Register itkParametricPath4 in _itkParametricPathPython:
_itkParametricPathPython.itkParametricPath4_swigregister(itkParametricPath4)
itkParametricPath4_cast = _itkParametricPathPython.itkParametricPath4_cast



