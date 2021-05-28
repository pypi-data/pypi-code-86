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
    from . import _itkForwardDifferenceOperatorPython
else:
    import _itkForwardDifferenceOperatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkForwardDifferenceOperatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkForwardDifferenceOperatorPython.SWIG_PyStaticMethod_New

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
import itk.itkNeighborhoodOperatorPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkNeighborhoodPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vector_refPython
import itk.itkCovariantVectorPython
import itk.itkRGBPixelPython
class itkForwardDifferenceOperatorD2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
    to calculate a "half" derivative useful, among other things, in
    solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    ForwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorD2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkForwardDifferenceOperatorD2
        __init__(self, arg0) -> itkForwardDifferenceOperatorD2

        Parameters
        ----------
        arg0: itkForwardDifferenceOperatorD2 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
        to calculate a "half" derivative useful, among other things, in
        solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        ForwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary. 
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD2_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorD2(*args))

# Register itkForwardDifferenceOperatorD2 in _itkForwardDifferenceOperatorPython:
_itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD2_swigregister(itkForwardDifferenceOperatorD2)

class itkForwardDifferenceOperatorD3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
    to calculate a "half" derivative useful, among other things, in
    solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    ForwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorD3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkForwardDifferenceOperatorD3
        __init__(self, arg0) -> itkForwardDifferenceOperatorD3

        Parameters
        ----------
        arg0: itkForwardDifferenceOperatorD3 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
        to calculate a "half" derivative useful, among other things, in
        solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        ForwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary. 
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD3_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorD3(*args))

# Register itkForwardDifferenceOperatorD3 in _itkForwardDifferenceOperatorPython:
_itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD3_swigregister(itkForwardDifferenceOperatorD3)

class itkForwardDifferenceOperatorD4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
    to calculate a "half" derivative useful, among other things, in
    solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    ForwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorD4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkForwardDifferenceOperatorD4
        __init__(self, arg0) -> itkForwardDifferenceOperatorD4

        Parameters
        ----------
        arg0: itkForwardDifferenceOperatorD4 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
        to calculate a "half" derivative useful, among other things, in
        solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        ForwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary. 
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD4_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorD4(*args))

# Register itkForwardDifferenceOperatorD4 in _itkForwardDifferenceOperatorPython:
_itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD4_swigregister(itkForwardDifferenceOperatorD4)

class itkForwardDifferenceOperatorF2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
    to calculate a "half" derivative useful, among other things, in
    solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    ForwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorF2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkForwardDifferenceOperatorF2
        __init__(self, arg0) -> itkForwardDifferenceOperatorF2

        Parameters
        ----------
        arg0: itkForwardDifferenceOperatorF2 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
        to calculate a "half" derivative useful, among other things, in
        solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        ForwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary. 
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF2_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorF2(*args))

# Register itkForwardDifferenceOperatorF2 in _itkForwardDifferenceOperatorPython:
_itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF2_swigregister(itkForwardDifferenceOperatorF2)

class itkForwardDifferenceOperatorF3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
    to calculate a "half" derivative useful, among other things, in
    solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    ForwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorF3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkForwardDifferenceOperatorF3
        __init__(self, arg0) -> itkForwardDifferenceOperatorF3

        Parameters
        ----------
        arg0: itkForwardDifferenceOperatorF3 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
        to calculate a "half" derivative useful, among other things, in
        solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        ForwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary. 
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF3_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorF3(*args))

# Register itkForwardDifferenceOperatorF3 in _itkForwardDifferenceOperatorPython:
_itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF3_swigregister(itkForwardDifferenceOperatorF3)

class itkForwardDifferenceOperatorF4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
    to calculate a "half" derivative useful, among other things, in
    solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    ForwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorF4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkForwardDifferenceOperatorF4
        __init__(self, arg0) -> itkForwardDifferenceOperatorF4

        Parameters
        ----------
        arg0: itkForwardDifferenceOperatorF4 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
        to calculate a "half" derivative useful, among other things, in
        solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        ForwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary. 
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF4_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorF4(*args))

# Register itkForwardDifferenceOperatorF4 in _itkForwardDifferenceOperatorPython:
_itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF4_swigregister(itkForwardDifferenceOperatorF4)



