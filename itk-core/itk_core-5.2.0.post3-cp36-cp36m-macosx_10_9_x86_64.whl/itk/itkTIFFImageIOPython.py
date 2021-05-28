# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIOTIFFPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkTIFFImageIOPython
else:
    import _itkTIFFImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTIFFImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTIFFImageIOPython.SWIG_PyStaticMethod_New

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
import itk.ITKIOImageBaseBasePython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython

def itkTIFFImageIO_New():
    return itkTIFFImageIO.New()

class itkTIFFImageIO(itk.ITKIOImageBaseBasePython.itkImageIOBase):
    r"""


    ImageIO object for reading and writing TIFF images.

    The compressors supported include "PackBits" (default), "JPEG",
    "DEFLATE" and may also include "LZW". Only the "JPEG" compressor
    supports the compression level for JPEG quality parameter in the range
    0-100.

    example{IO/TIFF/WriteATIFFImage,Write A TIFF Image} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTIFFImageIOPython.itkTIFFImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkTIFFImageIOPython.itkTIFFImageIO_Clone)
    ReadVolume = _swig_new_instance_method(_itkTIFFImageIOPython.itkTIFFImageIO_ReadVolume)
    NOFORMAT = _itkTIFFImageIOPython.itkTIFFImageIO_NOFORMAT
    
    RGB_ = _itkTIFFImageIOPython.itkTIFFImageIO_RGB_
    
    GRAYSCALE = _itkTIFFImageIOPython.itkTIFFImageIO_GRAYSCALE
    
    PALETTE_RGB = _itkTIFFImageIOPython.itkTIFFImageIO_PALETTE_RGB
    
    PALETTE_GRAYSCALE = _itkTIFFImageIOPython.itkTIFFImageIO_PALETTE_GRAYSCALE
    
    OTHER = _itkTIFFImageIOPython.itkTIFFImageIO_OTHER
    
    NoCompression = _itkTIFFImageIOPython.itkTIFFImageIO_NoCompression
    
    PackBits = _itkTIFFImageIOPython.itkTIFFImageIO_PackBits
    
    JPEG = _itkTIFFImageIOPython.itkTIFFImageIO_JPEG
    
    Deflate = _itkTIFFImageIOPython.itkTIFFImageIO_Deflate
    
    LZW = _itkTIFFImageIOPython.itkTIFFImageIO_LZW
    
    SetCompressionToNoCompression = _swig_new_instance_method(_itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToNoCompression)
    SetCompressionToPackBits = _swig_new_instance_method(_itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToPackBits)
    SetCompressionToJPEG = _swig_new_instance_method(_itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToJPEG)
    SetCompressionToDeflate = _swig_new_instance_method(_itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToDeflate)
    SetCompressionToLZW = _swig_new_instance_method(_itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToLZW)
    SetJPEGQuality = _swig_new_instance_method(_itkTIFFImageIOPython.itkTIFFImageIO_SetJPEGQuality)
    GetJPEGQuality = _swig_new_instance_method(_itkTIFFImageIOPython.itkTIFFImageIO_GetJPEGQuality)
    GetColorPalette = _swig_new_instance_method(_itkTIFFImageIOPython.itkTIFFImageIO_GetColorPalette)
    SetColorPalette = _swig_new_instance_method(_itkTIFFImageIOPython.itkTIFFImageIO_SetColorPalette)
    __swig_destroy__ = _itkTIFFImageIOPython.delete_itkTIFFImageIO
    cast = _swig_new_static_method(_itkTIFFImageIOPython.itkTIFFImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkTIFFImageIO

        Create a new object of the class itkTIFFImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTIFFImageIO.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTIFFImageIO.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTIFFImageIO.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTIFFImageIO in _itkTIFFImageIOPython:
_itkTIFFImageIOPython.itkTIFFImageIO_swigregister(itkTIFFImageIO)
itkTIFFImageIO___New_orig__ = _itkTIFFImageIOPython.itkTIFFImageIO___New_orig__
itkTIFFImageIO_cast = _itkTIFFImageIOPython.itkTIFFImageIO_cast


def itkTIFFImageIOFactory_New():
    return itkTIFFImageIOFactory.New()

class itkTIFFImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    r"""


    Create instances of TIFFImageIO objects using an object factory. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTIFFImageIOPython.itkTIFFImageIOFactory___New_orig__)
    FactoryNew = _swig_new_static_method(_itkTIFFImageIOPython.itkTIFFImageIOFactory_FactoryNew)
    RegisterOneFactory = _swig_new_static_method(_itkTIFFImageIOPython.itkTIFFImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkTIFFImageIOPython.delete_itkTIFFImageIOFactory
    cast = _swig_new_static_method(_itkTIFFImageIOPython.itkTIFFImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkTIFFImageIOFactory

        Create a new object of the class itkTIFFImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTIFFImageIOFactory.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTIFFImageIOFactory.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTIFFImageIOFactory.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTIFFImageIOFactory in _itkTIFFImageIOPython:
_itkTIFFImageIOPython.itkTIFFImageIOFactory_swigregister(itkTIFFImageIOFactory)
itkTIFFImageIOFactory___New_orig__ = _itkTIFFImageIOPython.itkTIFFImageIOFactory___New_orig__
itkTIFFImageIOFactory_FactoryNew = _itkTIFFImageIOPython.itkTIFFImageIOFactory_FactoryNew
itkTIFFImageIOFactory_RegisterOneFactory = _itkTIFFImageIOPython.itkTIFFImageIOFactory_RegisterOneFactory
itkTIFFImageIOFactory_cast = _itkTIFFImageIOPython.itkTIFFImageIOFactory_cast



