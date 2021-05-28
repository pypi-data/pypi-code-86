# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIOBrukerPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkBruker2dseqImageIOPython
else:
    import _itkBruker2dseqImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBruker2dseqImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBruker2dseqImageIOPython.SWIG_PyStaticMethod_New

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
import itk.stdcomplexPython
import itk.vnl_matrixPython

def itkBruker2dseqImageIO_New():
    return itkBruker2dseqImageIO.New()

class itkBruker2dseqImageIO(itk.ITKIOImageBaseBasePython.itkImageIOBase):
    r"""


    Class that defines how to read Bruker file format.

    The following is a brief description of the Bruker file format.

    Within the directory representing a 'session' on the scanner, data is
    laid out thus:

    session/ 1/ <- Series/Acquisition number method <- An important header
    file acqp <- Another important header fid <- Raw data other
    unimportant files pdata/ 1/ <- Reconstruction number (may be multiple)
    2dseq <- Reconstructed data visu_pars <- Most important header reco <-
    Mostly duplicated in visu_pars procs <- Unimportant header id <-
    Unimportant header 2/ ...

    The minimum required data to read the image is the '2dseq' and
    'visu_pars' file. To use this reader, specify the 2dseq file as the
    filename. It will check for the existence of the visu_pars file. If
    both these exist, the file is opened. If the other header files exist
    (method, acqp, etc.) in the correct locations then they will be read
    and added to the meta-data dictionary, but they are not used to read
    the image data itself.

    This class supports reading only.

    This file reader has been updated for ParaVision 6 2dseq files. The
    original code was written by Don C. Bigler at Penn State in 2004. It
    has been significantly changed, as Bruker also changed the format for
    ParaVision 6. In particular a new header file, 'visu_pars' was
    introduced that means that multiple headers no longer need to be read
    in order to read the '2dseq' file. However, if the other Bruker
    headers are still present they are read and added to the meta-data in
    case users wish to extract data from them.

    The original implementation was contributed as a paper to the Insight
    Journalhttps://www.insight-journal.org/browse/publication/237

    Tobias C Wood, King's College London 2017 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIO_Clone)
    __swig_destroy__ = _itkBruker2dseqImageIOPython.delete_itkBruker2dseqImageIO
    cast = _swig_new_static_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkBruker2dseqImageIO

        Create a new object of the class itkBruker2dseqImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBruker2dseqImageIO.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBruker2dseqImageIO.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBruker2dseqImageIO.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBruker2dseqImageIO in _itkBruker2dseqImageIOPython:
_itkBruker2dseqImageIOPython.itkBruker2dseqImageIO_swigregister(itkBruker2dseqImageIO)
itkBruker2dseqImageIO___New_orig__ = _itkBruker2dseqImageIOPython.itkBruker2dseqImageIO___New_orig__
itkBruker2dseqImageIO_cast = _itkBruker2dseqImageIOPython.itkBruker2dseqImageIO_cast


def itkBruker2dseqImageIOFactory_New():
    return itkBruker2dseqImageIOFactory.New()

class itkBruker2dseqImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    r"""


    Create instances of Bruker2dseqImageIO objects using an object
    factory.

    Don C. Bigler The Pennsylvania State University 2005  This
    implementation was contributed as a paper to the Insight
    Journalhttps://www.insight-journal.org/browse/publication/237 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory___New_orig__)
    RegisterOneFactory = _swig_new_static_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkBruker2dseqImageIOPython.delete_itkBruker2dseqImageIOFactory
    cast = _swig_new_static_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkBruker2dseqImageIOFactory

        Create a new object of the class itkBruker2dseqImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBruker2dseqImageIOFactory.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBruker2dseqImageIOFactory.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBruker2dseqImageIOFactory.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBruker2dseqImageIOFactory in _itkBruker2dseqImageIOPython:
_itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory_swigregister(itkBruker2dseqImageIOFactory)
itkBruker2dseqImageIOFactory___New_orig__ = _itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory___New_orig__
itkBruker2dseqImageIOFactory_RegisterOneFactory = _itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory_RegisterOneFactory
itkBruker2dseqImageIOFactory_cast = _itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory_cast



