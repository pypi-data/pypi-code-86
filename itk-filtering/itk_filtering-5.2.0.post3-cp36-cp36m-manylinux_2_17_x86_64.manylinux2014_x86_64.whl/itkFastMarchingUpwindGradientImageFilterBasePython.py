# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKFastMarchingPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkFastMarchingUpwindGradientImageFilterBasePython
else:
    import _itkFastMarchingUpwindGradientImageFilterBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkFastMarchingUpwindGradientImageFilterBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkFastMarchingUpwindGradientImageFilterBasePython.SWIG_PyStaticMethod_New

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
import itk.itkFastMarchingImageFilterBasePython
import itk.itkVectorPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.ITKFastMarchingBasePython
import itk.itkNodePairPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkImageToImageFilterAPython
import itk.itkImageRegionPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkCovariantVectorPython
import itk.itkPointPython
import itk.itkRGBPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkImageToImageFilterCommonPython
import itk.itkLevelSetNodePython
import itk.itkFastMarchingStoppingCriterionBasePython

def itkFastMarchingUpwindGradientImageFilterBaseID2ID2_New():
    return itkFastMarchingUpwindGradientImageFilterBaseID2ID2.New()

class itkFastMarchingUpwindGradientImageFilterBaseID2ID2(itk.itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID2ID2):
    r"""


    Generates the upwind gradient field of fast marching arrival times.

    This filter adds some extra functionality to its base class. While the
    solution T(x) of the Eikonal equation is being generated by the base
    class with the fast marching method, the filter generates the upwind
    gradient vectors of T(x), storing them in an image.

    Since the Eikonal equation generates the arrival times of a wave
    traveling at a given speed, the generated gradient vectors can be
    interpreted as the slowness (1/velocity) vectors of the front (the
    quantity inside the modulus operator in the Eikonal equation).

    Gradient vectors are computed using upwind finite differences, that
    is, information only propagates from points where the wavefront has
    already passed. This is consistent with how the fast marching method
    works.

    For an alternative implementation, see
    itk::FastMarchingUpwindGradientImageFilter.

    Luca Antiga Ph.D. Biomedical Technologies Laboratory, Bioengineering
    Department, Mario Negri Institute, Italy.

    See:   FastMarchingUpwindGradientImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_Clone)
    GetGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_GetGradientImage)
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterBasePython.delete_itkFastMarchingUpwindGradientImageFilterBaseID2ID2
    cast = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterBaseID2ID2

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterBaseID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterBaseID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterBaseID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingUpwindGradientImageFilterBaseID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingUpwindGradientImageFilterBaseID2ID2 in _itkFastMarchingUpwindGradientImageFilterBasePython:
_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_swigregister(itkFastMarchingUpwindGradientImageFilterBaseID2ID2)
itkFastMarchingUpwindGradientImageFilterBaseID2ID2___New_orig__ = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2___New_orig__
itkFastMarchingUpwindGradientImageFilterBaseID2ID2_cast = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID2ID2_cast


def itkFastMarchingUpwindGradientImageFilterBaseID3ID3_New():
    return itkFastMarchingUpwindGradientImageFilterBaseID3ID3.New()

class itkFastMarchingUpwindGradientImageFilterBaseID3ID3(itk.itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID3ID3):
    r"""


    Generates the upwind gradient field of fast marching arrival times.

    This filter adds some extra functionality to its base class. While the
    solution T(x) of the Eikonal equation is being generated by the base
    class with the fast marching method, the filter generates the upwind
    gradient vectors of T(x), storing them in an image.

    Since the Eikonal equation generates the arrival times of a wave
    traveling at a given speed, the generated gradient vectors can be
    interpreted as the slowness (1/velocity) vectors of the front (the
    quantity inside the modulus operator in the Eikonal equation).

    Gradient vectors are computed using upwind finite differences, that
    is, information only propagates from points where the wavefront has
    already passed. This is consistent with how the fast marching method
    works.

    For an alternative implementation, see
    itk::FastMarchingUpwindGradientImageFilter.

    Luca Antiga Ph.D. Biomedical Technologies Laboratory, Bioengineering
    Department, Mario Negri Institute, Italy.

    See:   FastMarchingUpwindGradientImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_Clone)
    GetGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_GetGradientImage)
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterBasePython.delete_itkFastMarchingUpwindGradientImageFilterBaseID3ID3
    cast = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterBaseID3ID3

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterBaseID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterBaseID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterBaseID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingUpwindGradientImageFilterBaseID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingUpwindGradientImageFilterBaseID3ID3 in _itkFastMarchingUpwindGradientImageFilterBasePython:
_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_swigregister(itkFastMarchingUpwindGradientImageFilterBaseID3ID3)
itkFastMarchingUpwindGradientImageFilterBaseID3ID3___New_orig__ = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3___New_orig__
itkFastMarchingUpwindGradientImageFilterBaseID3ID3_cast = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID3ID3_cast


def itkFastMarchingUpwindGradientImageFilterBaseID4ID4_New():
    return itkFastMarchingUpwindGradientImageFilterBaseID4ID4.New()

class itkFastMarchingUpwindGradientImageFilterBaseID4ID4(itk.itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseID4ID4):
    r"""


    Generates the upwind gradient field of fast marching arrival times.

    This filter adds some extra functionality to its base class. While the
    solution T(x) of the Eikonal equation is being generated by the base
    class with the fast marching method, the filter generates the upwind
    gradient vectors of T(x), storing them in an image.

    Since the Eikonal equation generates the arrival times of a wave
    traveling at a given speed, the generated gradient vectors can be
    interpreted as the slowness (1/velocity) vectors of the front (the
    quantity inside the modulus operator in the Eikonal equation).

    Gradient vectors are computed using upwind finite differences, that
    is, information only propagates from points where the wavefront has
    already passed. This is consistent with how the fast marching method
    works.

    For an alternative implementation, see
    itk::FastMarchingUpwindGradientImageFilter.

    Luca Antiga Ph.D. Biomedical Technologies Laboratory, Bioengineering
    Department, Mario Negri Institute, Italy.

    See:   FastMarchingUpwindGradientImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID4ID4_Clone)
    GetGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID4ID4_GetGradientImage)
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterBasePython.delete_itkFastMarchingUpwindGradientImageFilterBaseID4ID4
    cast = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterBaseID4ID4

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterBaseID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterBaseID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterBaseID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingUpwindGradientImageFilterBaseID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingUpwindGradientImageFilterBaseID4ID4 in _itkFastMarchingUpwindGradientImageFilterBasePython:
_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID4ID4_swigregister(itkFastMarchingUpwindGradientImageFilterBaseID4ID4)
itkFastMarchingUpwindGradientImageFilterBaseID4ID4___New_orig__ = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID4ID4___New_orig__
itkFastMarchingUpwindGradientImageFilterBaseID4ID4_cast = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseID4ID4_cast


def itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_New():
    return itkFastMarchingUpwindGradientImageFilterBaseIF2IF2.New()

class itkFastMarchingUpwindGradientImageFilterBaseIF2IF2(itk.itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF2IF2):
    r"""


    Generates the upwind gradient field of fast marching arrival times.

    This filter adds some extra functionality to its base class. While the
    solution T(x) of the Eikonal equation is being generated by the base
    class with the fast marching method, the filter generates the upwind
    gradient vectors of T(x), storing them in an image.

    Since the Eikonal equation generates the arrival times of a wave
    traveling at a given speed, the generated gradient vectors can be
    interpreted as the slowness (1/velocity) vectors of the front (the
    quantity inside the modulus operator in the Eikonal equation).

    Gradient vectors are computed using upwind finite differences, that
    is, information only propagates from points where the wavefront has
    already passed. This is consistent with how the fast marching method
    works.

    For an alternative implementation, see
    itk::FastMarchingUpwindGradientImageFilter.

    Luca Antiga Ph.D. Biomedical Technologies Laboratory, Bioengineering
    Department, Mario Negri Institute, Italy.

    See:   FastMarchingUpwindGradientImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_Clone)
    GetGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_GetGradientImage)
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterBasePython.delete_itkFastMarchingUpwindGradientImageFilterBaseIF2IF2
    cast = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterBaseIF2IF2

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterBaseIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterBaseIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterBaseIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingUpwindGradientImageFilterBaseIF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingUpwindGradientImageFilterBaseIF2IF2 in _itkFastMarchingUpwindGradientImageFilterBasePython:
_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_swigregister(itkFastMarchingUpwindGradientImageFilterBaseIF2IF2)
itkFastMarchingUpwindGradientImageFilterBaseIF2IF2___New_orig__ = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2___New_orig__
itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_cast = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF2IF2_cast


def itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_New():
    return itkFastMarchingUpwindGradientImageFilterBaseIF3IF3.New()

class itkFastMarchingUpwindGradientImageFilterBaseIF3IF3(itk.itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF3IF3):
    r"""


    Generates the upwind gradient field of fast marching arrival times.

    This filter adds some extra functionality to its base class. While the
    solution T(x) of the Eikonal equation is being generated by the base
    class with the fast marching method, the filter generates the upwind
    gradient vectors of T(x), storing them in an image.

    Since the Eikonal equation generates the arrival times of a wave
    traveling at a given speed, the generated gradient vectors can be
    interpreted as the slowness (1/velocity) vectors of the front (the
    quantity inside the modulus operator in the Eikonal equation).

    Gradient vectors are computed using upwind finite differences, that
    is, information only propagates from points where the wavefront has
    already passed. This is consistent with how the fast marching method
    works.

    For an alternative implementation, see
    itk::FastMarchingUpwindGradientImageFilter.

    Luca Antiga Ph.D. Biomedical Technologies Laboratory, Bioengineering
    Department, Mario Negri Institute, Italy.

    See:   FastMarchingUpwindGradientImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_Clone)
    GetGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_GetGradientImage)
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterBasePython.delete_itkFastMarchingUpwindGradientImageFilterBaseIF3IF3
    cast = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterBaseIF3IF3

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterBaseIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterBaseIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterBaseIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingUpwindGradientImageFilterBaseIF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingUpwindGradientImageFilterBaseIF3IF3 in _itkFastMarchingUpwindGradientImageFilterBasePython:
_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_swigregister(itkFastMarchingUpwindGradientImageFilterBaseIF3IF3)
itkFastMarchingUpwindGradientImageFilterBaseIF3IF3___New_orig__ = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3___New_orig__
itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_cast = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF3IF3_cast


def itkFastMarchingUpwindGradientImageFilterBaseIF4IF4_New():
    return itkFastMarchingUpwindGradientImageFilterBaseIF4IF4.New()

class itkFastMarchingUpwindGradientImageFilterBaseIF4IF4(itk.itkFastMarchingImageFilterBasePython.itkFastMarchingImageFilterBaseIF4IF4):
    r"""


    Generates the upwind gradient field of fast marching arrival times.

    This filter adds some extra functionality to its base class. While the
    solution T(x) of the Eikonal equation is being generated by the base
    class with the fast marching method, the filter generates the upwind
    gradient vectors of T(x), storing them in an image.

    Since the Eikonal equation generates the arrival times of a wave
    traveling at a given speed, the generated gradient vectors can be
    interpreted as the slowness (1/velocity) vectors of the front (the
    quantity inside the modulus operator in the Eikonal equation).

    Gradient vectors are computed using upwind finite differences, that
    is, information only propagates from points where the wavefront has
    already passed. This is consistent with how the fast marching method
    works.

    For an alternative implementation, see
    itk::FastMarchingUpwindGradientImageFilter.

    Luca Antiga Ph.D. Biomedical Technologies Laboratory, Bioengineering
    Department, Mario Negri Institute, Italy.

    See:   FastMarchingUpwindGradientImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF4IF4_Clone)
    GetGradientImage = _swig_new_instance_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF4IF4_GetGradientImage)
    __swig_destroy__ = _itkFastMarchingUpwindGradientImageFilterBasePython.delete_itkFastMarchingUpwindGradientImageFilterBaseIF4IF4
    cast = _swig_new_static_method(_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingUpwindGradientImageFilterBaseIF4IF4

        Create a new object of the class itkFastMarchingUpwindGradientImageFilterBaseIF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingUpwindGradientImageFilterBaseIF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingUpwindGradientImageFilterBaseIF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingUpwindGradientImageFilterBaseIF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingUpwindGradientImageFilterBaseIF4IF4 in _itkFastMarchingUpwindGradientImageFilterBasePython:
_itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF4IF4_swigregister(itkFastMarchingUpwindGradientImageFilterBaseIF4IF4)
itkFastMarchingUpwindGradientImageFilterBaseIF4IF4___New_orig__ = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF4IF4___New_orig__
itkFastMarchingUpwindGradientImageFilterBaseIF4IF4_cast = _itkFastMarchingUpwindGradientImageFilterBasePython.itkFastMarchingUpwindGradientImageFilterBaseIF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def fast_marching_upwind_gradient_image_filter_base(*args: itkt.ImageLike,  output_size: Sequence[int]=..., output_region: itkt.ImageRegion=..., output_spacing: Sequence[float]=..., output_direction=..., output_origin: Sequence[float]=..., override_output_information: bool=..., topology_check=..., trial_points=..., alive_points=..., processed_points=..., forbidden_points=..., stopping_criterion=..., speed_constant: float=..., normalization_factor: float=..., collect_points: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for FastMarchingUpwindGradientImageFilterBase"""
    import itk

    kwarg_typehints = { 'output_size':output_size,'output_region':output_region,'output_spacing':output_spacing,'output_direction':output_direction,'output_origin':output_origin,'override_output_information':override_output_information,'topology_check':topology_check,'trial_points':trial_points,'alive_points':alive_points,'processed_points':processed_points,'forbidden_points':forbidden_points,'stopping_criterion':stopping_criterion,'speed_constant':speed_constant,'normalization_factor':normalization_factor,'collect_points':collect_points }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.FastMarchingUpwindGradientImageFilterBase.New(*args, **kwargs)
    return instance.__internal_call__()

def fast_marching_upwind_gradient_image_filter_base_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKFastMarching.FastMarchingUpwindGradientImageFilterBase
    fast_marching_upwind_gradient_image_filter_base.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    fast_marching_upwind_gradient_image_filter_base.__doc__ = filter_object.__doc__




