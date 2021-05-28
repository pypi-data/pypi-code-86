# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageIntensityPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkXorImageFilterPython
else:
    import _itkXorImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkXorImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkXorImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkBinaryGeneratorImageFilterPython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkImageRegionPython
import itk.itkInPlaceImageFilterBPython
import itk.itkImageToImageFilterBPython
import itk.itkImageToImageFilterCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkArrayPython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterAPython

def itkXorImageFilterISS2ISS2ISS2_New():
    return itkXorImageFilterISS2ISS2ISS2.New()

class itkXorImageFilterISS2ISS2ISS2(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    r"""


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterISS2ISS2ISS2
    cast = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterISS2ISS2ISS2

        Create a new object of the class itkXorImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterISS2ISS2ISS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkXorImageFilterISS2ISS2ISS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkXorImageFilterISS2ISS2ISS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkXorImageFilterISS2ISS2ISS2 in _itkXorImageFilterPython:
_itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2_swigregister(itkXorImageFilterISS2ISS2ISS2)
itkXorImageFilterISS2ISS2ISS2___New_orig__ = _itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2___New_orig__
itkXorImageFilterISS2ISS2ISS2_cast = _itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2_cast


def itkXorImageFilterISS3ISS3ISS3_New():
    return itkXorImageFilterISS3ISS3ISS3.New()

class itkXorImageFilterISS3ISS3ISS3(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    r"""


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterISS3ISS3ISS3
    cast = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterISS3ISS3ISS3

        Create a new object of the class itkXorImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterISS3ISS3ISS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkXorImageFilterISS3ISS3ISS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkXorImageFilterISS3ISS3ISS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkXorImageFilterISS3ISS3ISS3 in _itkXorImageFilterPython:
_itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3_swigregister(itkXorImageFilterISS3ISS3ISS3)
itkXorImageFilterISS3ISS3ISS3___New_orig__ = _itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3___New_orig__
itkXorImageFilterISS3ISS3ISS3_cast = _itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3_cast


def itkXorImageFilterISS4ISS4ISS4_New():
    return itkXorImageFilterISS4ISS4ISS4.New()

class itkXorImageFilterISS4ISS4ISS4(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS4ISS4ISS4):
    r"""


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterISS4ISS4ISS4___New_orig__)
    Clone = _swig_new_instance_method(_itkXorImageFilterPython.itkXorImageFilterISS4ISS4ISS4_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterISS4ISS4ISS4_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterISS4ISS4ISS4
    cast = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterISS4ISS4ISS4_cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterISS4ISS4ISS4

        Create a new object of the class itkXorImageFilterISS4ISS4ISS4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterISS4ISS4ISS4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkXorImageFilterISS4ISS4ISS4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkXorImageFilterISS4ISS4ISS4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkXorImageFilterISS4ISS4ISS4 in _itkXorImageFilterPython:
_itkXorImageFilterPython.itkXorImageFilterISS4ISS4ISS4_swigregister(itkXorImageFilterISS4ISS4ISS4)
itkXorImageFilterISS4ISS4ISS4___New_orig__ = _itkXorImageFilterPython.itkXorImageFilterISS4ISS4ISS4___New_orig__
itkXorImageFilterISS4ISS4ISS4_cast = _itkXorImageFilterPython.itkXorImageFilterISS4ISS4ISS4_cast


def itkXorImageFilterIUC2IUC2IUC2_New():
    return itkXorImageFilterIUC2IUC2IUC2.New()

class itkXorImageFilterIUC2IUC2IUC2(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    r"""


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterIUC2IUC2IUC2
    cast = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterIUC2IUC2IUC2

        Create a new object of the class itkXorImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterIUC2IUC2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkXorImageFilterIUC2IUC2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkXorImageFilterIUC2IUC2IUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkXorImageFilterIUC2IUC2IUC2 in _itkXorImageFilterPython:
_itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2_swigregister(itkXorImageFilterIUC2IUC2IUC2)
itkXorImageFilterIUC2IUC2IUC2___New_orig__ = _itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2___New_orig__
itkXorImageFilterIUC2IUC2IUC2_cast = _itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2_cast


def itkXorImageFilterIUC3IUC3IUC3_New():
    return itkXorImageFilterIUC3IUC3IUC3.New()

class itkXorImageFilterIUC3IUC3IUC3(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    r"""


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterIUC3IUC3IUC3
    cast = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterIUC3IUC3IUC3

        Create a new object of the class itkXorImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterIUC3IUC3IUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkXorImageFilterIUC3IUC3IUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkXorImageFilterIUC3IUC3IUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkXorImageFilterIUC3IUC3IUC3 in _itkXorImageFilterPython:
_itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3_swigregister(itkXorImageFilterIUC3IUC3IUC3)
itkXorImageFilterIUC3IUC3IUC3___New_orig__ = _itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3___New_orig__
itkXorImageFilterIUC3IUC3IUC3_cast = _itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3_cast


def itkXorImageFilterIUC4IUC4IUC4_New():
    return itkXorImageFilterIUC4IUC4IUC4.New()

class itkXorImageFilterIUC4IUC4IUC4(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC4IUC4IUC4):
    r"""


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUC4IUC4IUC4___New_orig__)
    Clone = _swig_new_instance_method(_itkXorImageFilterPython.itkXorImageFilterIUC4IUC4IUC4_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterIUC4IUC4IUC4_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterIUC4IUC4IUC4
    cast = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUC4IUC4IUC4_cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterIUC4IUC4IUC4

        Create a new object of the class itkXorImageFilterIUC4IUC4IUC4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterIUC4IUC4IUC4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkXorImageFilterIUC4IUC4IUC4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkXorImageFilterIUC4IUC4IUC4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkXorImageFilterIUC4IUC4IUC4 in _itkXorImageFilterPython:
_itkXorImageFilterPython.itkXorImageFilterIUC4IUC4IUC4_swigregister(itkXorImageFilterIUC4IUC4IUC4)
itkXorImageFilterIUC4IUC4IUC4___New_orig__ = _itkXorImageFilterPython.itkXorImageFilterIUC4IUC4IUC4___New_orig__
itkXorImageFilterIUC4IUC4IUC4_cast = _itkXorImageFilterPython.itkXorImageFilterIUC4IUC4IUC4_cast


def itkXorImageFilterIUS2IUS2IUS2_New():
    return itkXorImageFilterIUS2IUS2IUS2.New()

class itkXorImageFilterIUS2IUS2IUS2(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    r"""


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterIUS2IUS2IUS2
    cast = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterIUS2IUS2IUS2

        Create a new object of the class itkXorImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterIUS2IUS2IUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkXorImageFilterIUS2IUS2IUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkXorImageFilterIUS2IUS2IUS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkXorImageFilterIUS2IUS2IUS2 in _itkXorImageFilterPython:
_itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2_swigregister(itkXorImageFilterIUS2IUS2IUS2)
itkXorImageFilterIUS2IUS2IUS2___New_orig__ = _itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2___New_orig__
itkXorImageFilterIUS2IUS2IUS2_cast = _itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2_cast


def itkXorImageFilterIUS3IUS3IUS3_New():
    return itkXorImageFilterIUS3IUS3IUS3.New()

class itkXorImageFilterIUS3IUS3IUS3(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    r"""


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterIUS3IUS3IUS3
    cast = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterIUS3IUS3IUS3

        Create a new object of the class itkXorImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterIUS3IUS3IUS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkXorImageFilterIUS3IUS3IUS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkXorImageFilterIUS3IUS3IUS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkXorImageFilterIUS3IUS3IUS3 in _itkXorImageFilterPython:
_itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3_swigregister(itkXorImageFilterIUS3IUS3IUS3)
itkXorImageFilterIUS3IUS3IUS3___New_orig__ = _itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3___New_orig__
itkXorImageFilterIUS3IUS3IUS3_cast = _itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3_cast


def itkXorImageFilterIUS4IUS4IUS4_New():
    return itkXorImageFilterIUS4IUS4IUS4.New()

class itkXorImageFilterIUS4IUS4IUS4(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS4IUS4IUS4):
    r"""


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUS4IUS4IUS4___New_orig__)
    Clone = _swig_new_instance_method(_itkXorImageFilterPython.itkXorImageFilterIUS4IUS4IUS4_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterIUS4IUS4IUS4_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterIUS4IUS4IUS4
    cast = _swig_new_static_method(_itkXorImageFilterPython.itkXorImageFilterIUS4IUS4IUS4_cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterIUS4IUS4IUS4

        Create a new object of the class itkXorImageFilterIUS4IUS4IUS4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterIUS4IUS4IUS4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkXorImageFilterIUS4IUS4IUS4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkXorImageFilterIUS4IUS4IUS4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkXorImageFilterIUS4IUS4IUS4 in _itkXorImageFilterPython:
_itkXorImageFilterPython.itkXorImageFilterIUS4IUS4IUS4_swigregister(itkXorImageFilterIUS4IUS4IUS4)
itkXorImageFilterIUS4IUS4IUS4___New_orig__ = _itkXorImageFilterPython.itkXorImageFilterIUS4IUS4IUS4___New_orig__
itkXorImageFilterIUS4IUS4IUS4_cast = _itkXorImageFilterPython.itkXorImageFilterIUS4IUS4IUS4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def xor_image_filter(*args: itkt.ImageLike,  constant1: int=..., constant2: int=..., constant: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for XorImageFilter"""
    import itk

    kwarg_typehints = { 'constant1':constant1,'constant2':constant2,'constant':constant }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.XorImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def xor_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.XorImageFilter
    xor_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    xor_image_filter.__doc__ = filter_object.__doc__




