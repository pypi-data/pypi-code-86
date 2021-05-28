# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIOMRCPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkMRCImageIOPython
else:
    import _itkMRCImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMRCImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMRCImageIOPython.SWIG_PyStaticMethod_New

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
import itk.ITKIOImageBaseBasePython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.ITKCommonBasePython

def itkMRCImageIO_New():
    return itkMRCImageIO.New()

class itkMRCImageIO(itk.ITKIOImageBaseBasePython.itkStreamingImageIOBase):
    r"""


    An ImageIO class to read the MRC file format. The MRC file format
    frequently has the extension ".mrc" or ".rec". It is used
    frequently for electron microscopy and is an emerging standard for
    cryo-electron tomography and molecular imaging. The format is used to
    represent 2D, 3D images along with 2D tilt series for tomography.

    The header of the file can contain important information which can not
    be represented in an Image. Therefor the header is placed into the
    MetaDataDictionary of "this". The key to access this is
    MetaDataHeaderName ( fix me when renamed ). See:  MRCHeaderObject
    MetaDataDictionary  This implementation is designed to support IO
    Streaming of arbitrary regions.

    As with all ImageIOs this class is designed to work with
    ImageFileReader and ImageFileWriter, so its direct use is discouraged.

    This code was contributed in the Insight Journal paper: "A Streaming
    IO Base Class and Support for Streaming the MRC and VTK File Format"
    by Lowekamp B., Chen D.https://www.insight-
    journal.org/browse/publication/729

    See:  ImageFileWriter ImageFileReader ImageIOBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMRCImageIOPython.itkMRCImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkMRCImageIOPython.itkMRCImageIO_Clone)
    __swig_destroy__ = _itkMRCImageIOPython.delete_itkMRCImageIO
    cast = _swig_new_static_method(_itkMRCImageIOPython.itkMRCImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkMRCImageIO

        Create a new object of the class itkMRCImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMRCImageIO.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMRCImageIO.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMRCImageIO.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMRCImageIO in _itkMRCImageIOPython:
_itkMRCImageIOPython.itkMRCImageIO_swigregister(itkMRCImageIO)
itkMRCImageIO___New_orig__ = _itkMRCImageIOPython.itkMRCImageIO___New_orig__
itkMRCImageIO_cast = _itkMRCImageIOPython.itkMRCImageIO_cast


def itkMRCImageIOFactory_New():
    return itkMRCImageIOFactory.New()

class itkMRCImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    r"""


    Create instances of MRCImageIO objects using an object factory.

    This code was contributed in the Insight Journal paper: "A Streaming
    IO Base Class and Support for Streaming the MRC and VTK File Format"
    by Lowekamp B., Chen D.https://www.insight-
    journal.org/browse/publication/729 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMRCImageIOPython.itkMRCImageIOFactory___New_orig__)
    RegisterOneFactory = _swig_new_static_method(_itkMRCImageIOPython.itkMRCImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkMRCImageIOPython.delete_itkMRCImageIOFactory
    cast = _swig_new_static_method(_itkMRCImageIOPython.itkMRCImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkMRCImageIOFactory

        Create a new object of the class itkMRCImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMRCImageIOFactory.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMRCImageIOFactory.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMRCImageIOFactory.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMRCImageIOFactory in _itkMRCImageIOPython:
_itkMRCImageIOPython.itkMRCImageIOFactory_swigregister(itkMRCImageIOFactory)
itkMRCImageIOFactory___New_orig__ = _itkMRCImageIOPython.itkMRCImageIOFactory___New_orig__
itkMRCImageIOFactory_RegisterOneFactory = _itkMRCImageIOPython.itkMRCImageIOFactory_RegisterOneFactory
itkMRCImageIOFactory_cast = _itkMRCImageIOPython.itkMRCImageIOFactory_cast



