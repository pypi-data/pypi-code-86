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
    from . import _itkPolyLineParametricPathPython
else:
    import _itkPolyLineParametricPathPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkPolyLineParametricPathPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkPolyLineParametricPathPython.SWIG_PyStaticMethod_New

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
import itk.itkContinuousIndexPython
import itk.itkPointPython
import itk.itkFixedArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkParametricPathPython
import itk.itkPathBasePython
import itk.itkVectorContainerPython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.vnl_matrix_fixedPython

def itkPolyLineParametricPath2_New():
    return itkPolyLineParametricPath2.New()

class itkPolyLineParametricPath2(itk.itkParametricPathPython.itkParametricPath2):
    r"""


    Represent a path of line segments through ND Space.

    This class is intended to represent parametric paths through an image,
    where the paths are composed of line segments. Each line segment
    traverses one unit of input. A classic application of this class is
    the representation of contours in 2D images, especially when the
    contours only need to be approximately correct. Another use of a path
    is to guide the movement of an iterator through an image.

    See:  EllipseParametricPath

    See:  FourierSeriesPath

    See:  OrthogonallyCorrectedParametricPath

    See:   ParametricPath

    See:  ChainCodePath

    See:   Path

    See:  ContinuousIndex

    See:  Index

    See:  Offset

    See:  Vector 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    AddVertex = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath2_AddVertex)
    __New_orig__ = _swig_new_static_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath2___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath2_Clone)
    GetModifiableVertexList = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath2_GetModifiableVertexList)
    GetVertexList = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath2_GetVertexList)
    __swig_destroy__ = _itkPolyLineParametricPathPython.delete_itkPolyLineParametricPath2
    cast = _swig_new_static_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath2_cast)

    def New(*args, **kargs):
        """New() -> itkPolyLineParametricPath2

        Create a new object of the class itkPolyLineParametricPath2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyLineParametricPath2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyLineParametricPath2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyLineParametricPath2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyLineParametricPath2 in _itkPolyLineParametricPathPython:
_itkPolyLineParametricPathPython.itkPolyLineParametricPath2_swigregister(itkPolyLineParametricPath2)
itkPolyLineParametricPath2___New_orig__ = _itkPolyLineParametricPathPython.itkPolyLineParametricPath2___New_orig__
itkPolyLineParametricPath2_cast = _itkPolyLineParametricPathPython.itkPolyLineParametricPath2_cast


def itkPolyLineParametricPath3_New():
    return itkPolyLineParametricPath3.New()

class itkPolyLineParametricPath3(itk.itkParametricPathPython.itkParametricPath3):
    r"""


    Represent a path of line segments through ND Space.

    This class is intended to represent parametric paths through an image,
    where the paths are composed of line segments. Each line segment
    traverses one unit of input. A classic application of this class is
    the representation of contours in 2D images, especially when the
    contours only need to be approximately correct. Another use of a path
    is to guide the movement of an iterator through an image.

    See:  EllipseParametricPath

    See:  FourierSeriesPath

    See:  OrthogonallyCorrectedParametricPath

    See:   ParametricPath

    See:  ChainCodePath

    See:   Path

    See:  ContinuousIndex

    See:  Index

    See:  Offset

    See:  Vector 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    AddVertex = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath3_AddVertex)
    __New_orig__ = _swig_new_static_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath3___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath3_Clone)
    GetModifiableVertexList = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath3_GetModifiableVertexList)
    GetVertexList = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath3_GetVertexList)
    __swig_destroy__ = _itkPolyLineParametricPathPython.delete_itkPolyLineParametricPath3
    cast = _swig_new_static_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath3_cast)

    def New(*args, **kargs):
        """New() -> itkPolyLineParametricPath3

        Create a new object of the class itkPolyLineParametricPath3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyLineParametricPath3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyLineParametricPath3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyLineParametricPath3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyLineParametricPath3 in _itkPolyLineParametricPathPython:
_itkPolyLineParametricPathPython.itkPolyLineParametricPath3_swigregister(itkPolyLineParametricPath3)
itkPolyLineParametricPath3___New_orig__ = _itkPolyLineParametricPathPython.itkPolyLineParametricPath3___New_orig__
itkPolyLineParametricPath3_cast = _itkPolyLineParametricPathPython.itkPolyLineParametricPath3_cast


def itkPolyLineParametricPath4_New():
    return itkPolyLineParametricPath4.New()

class itkPolyLineParametricPath4(itk.itkParametricPathPython.itkParametricPath4):
    r"""


    Represent a path of line segments through ND Space.

    This class is intended to represent parametric paths through an image,
    where the paths are composed of line segments. Each line segment
    traverses one unit of input. A classic application of this class is
    the representation of contours in 2D images, especially when the
    contours only need to be approximately correct. Another use of a path
    is to guide the movement of an iterator through an image.

    See:  EllipseParametricPath

    See:  FourierSeriesPath

    See:  OrthogonallyCorrectedParametricPath

    See:   ParametricPath

    See:  ChainCodePath

    See:   Path

    See:  ContinuousIndex

    See:  Index

    See:  Offset

    See:  Vector 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    AddVertex = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath4_AddVertex)
    __New_orig__ = _swig_new_static_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath4___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath4_Clone)
    GetModifiableVertexList = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath4_GetModifiableVertexList)
    GetVertexList = _swig_new_instance_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath4_GetVertexList)
    __swig_destroy__ = _itkPolyLineParametricPathPython.delete_itkPolyLineParametricPath4
    cast = _swig_new_static_method(_itkPolyLineParametricPathPython.itkPolyLineParametricPath4_cast)

    def New(*args, **kargs):
        """New() -> itkPolyLineParametricPath4

        Create a new object of the class itkPolyLineParametricPath4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyLineParametricPath4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyLineParametricPath4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyLineParametricPath4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyLineParametricPath4 in _itkPolyLineParametricPathPython:
_itkPolyLineParametricPathPython.itkPolyLineParametricPath4_swigregister(itkPolyLineParametricPath4)
itkPolyLineParametricPath4___New_orig__ = _itkPolyLineParametricPathPython.itkPolyLineParametricPath4___New_orig__
itkPolyLineParametricPath4_cast = _itkPolyLineParametricPathPython.itkPolyLineParametricPath4_cast



