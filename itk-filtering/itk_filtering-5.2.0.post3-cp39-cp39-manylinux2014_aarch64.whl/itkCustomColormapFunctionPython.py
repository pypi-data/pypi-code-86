# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKColormapPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkCustomColormapFunctionPython
else:
    import _itkCustomColormapFunctionPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCustomColormapFunctionPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCustomColormapFunctionPython.SWIG_PyStaticMethod_New

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
import itk.itkColormapFunctionPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkRGBAPixelPython

def itkCustomColormapFunctionDRGBAPD_New():
    return itkCustomColormapFunctionDRGBAPD.New()

class itkCustomColormapFunctionDRGBAPD(itk.itkColormapFunctionPython.itkColormapFunctionDRGBAPD):
    r"""


    Function object which maps a scalar value into an RGB colormap value.

    Nicholas Tustison, Hui Zhang, Gaetan Lehmann, Paul Yushkevich and
    James C. Gee  This code was contributed in the Insight Journal paper:

    "Meeting Andy Warhol Somewhere Over the Rainbow: RGB Colormapping and
    ITK"https://www.insight-journal.org/browse/publication/285 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD___New_orig__)
    Clone = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD_Clone)
    SetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD_SetRedChannel)
    GetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD_GetRedChannel)
    SetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD_SetGreenChannel)
    GetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD_GetGreenChannel)
    SetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD_SetBlueChannel)
    GetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD_GetBlueChannel)
    __swig_destroy__ = _itkCustomColormapFunctionPython.delete_itkCustomColormapFunctionDRGBAPD
    cast = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD_cast)

    def New(*args, **kargs):
        """New() -> itkCustomColormapFunctionDRGBAPD

        Create a new object of the class itkCustomColormapFunctionDRGBAPD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCustomColormapFunctionDRGBAPD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCustomColormapFunctionDRGBAPD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCustomColormapFunctionDRGBAPD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCustomColormapFunctionDRGBAPD in _itkCustomColormapFunctionPython:
_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD_swigregister(itkCustomColormapFunctionDRGBAPD)
itkCustomColormapFunctionDRGBAPD___New_orig__ = _itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD___New_orig__
itkCustomColormapFunctionDRGBAPD_cast = _itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBAPD_cast


def itkCustomColormapFunctionDRGBPD_New():
    return itkCustomColormapFunctionDRGBPD.New()

class itkCustomColormapFunctionDRGBPD(itk.itkColormapFunctionPython.itkColormapFunctionDRGBPD):
    r"""


    Function object which maps a scalar value into an RGB colormap value.

    Nicholas Tustison, Hui Zhang, Gaetan Lehmann, Paul Yushkevich and
    James C. Gee  This code was contributed in the Insight Journal paper:

    "Meeting Andy Warhol Somewhere Over the Rainbow: RGB Colormapping and
    ITK"https://www.insight-journal.org/browse/publication/285 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD___New_orig__)
    Clone = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD_Clone)
    SetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD_SetRedChannel)
    GetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD_GetRedChannel)
    SetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD_SetGreenChannel)
    GetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD_GetGreenChannel)
    SetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD_SetBlueChannel)
    GetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD_GetBlueChannel)
    __swig_destroy__ = _itkCustomColormapFunctionPython.delete_itkCustomColormapFunctionDRGBPD
    cast = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD_cast)

    def New(*args, **kargs):
        """New() -> itkCustomColormapFunctionDRGBPD

        Create a new object of the class itkCustomColormapFunctionDRGBPD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCustomColormapFunctionDRGBPD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCustomColormapFunctionDRGBPD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCustomColormapFunctionDRGBPD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCustomColormapFunctionDRGBPD in _itkCustomColormapFunctionPython:
_itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD_swigregister(itkCustomColormapFunctionDRGBPD)
itkCustomColormapFunctionDRGBPD___New_orig__ = _itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD___New_orig__
itkCustomColormapFunctionDRGBPD_cast = _itkCustomColormapFunctionPython.itkCustomColormapFunctionDRGBPD_cast


def itkCustomColormapFunctionFRGBAPF_New():
    return itkCustomColormapFunctionFRGBAPF.New()

class itkCustomColormapFunctionFRGBAPF(itk.itkColormapFunctionPython.itkColormapFunctionFRGBAPF):
    r"""


    Function object which maps a scalar value into an RGB colormap value.

    Nicholas Tustison, Hui Zhang, Gaetan Lehmann, Paul Yushkevich and
    James C. Gee  This code was contributed in the Insight Journal paper:

    "Meeting Andy Warhol Somewhere Over the Rainbow: RGB Colormapping and
    ITK"https://www.insight-journal.org/browse/publication/285 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF___New_orig__)
    Clone = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF_Clone)
    SetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF_SetRedChannel)
    GetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF_GetRedChannel)
    SetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF_SetGreenChannel)
    GetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF_GetGreenChannel)
    SetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF_SetBlueChannel)
    GetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF_GetBlueChannel)
    __swig_destroy__ = _itkCustomColormapFunctionPython.delete_itkCustomColormapFunctionFRGBAPF
    cast = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF_cast)

    def New(*args, **kargs):
        """New() -> itkCustomColormapFunctionFRGBAPF

        Create a new object of the class itkCustomColormapFunctionFRGBAPF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCustomColormapFunctionFRGBAPF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCustomColormapFunctionFRGBAPF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCustomColormapFunctionFRGBAPF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCustomColormapFunctionFRGBAPF in _itkCustomColormapFunctionPython:
_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF_swigregister(itkCustomColormapFunctionFRGBAPF)
itkCustomColormapFunctionFRGBAPF___New_orig__ = _itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF___New_orig__
itkCustomColormapFunctionFRGBAPF_cast = _itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBAPF_cast


def itkCustomColormapFunctionFRGBPF_New():
    return itkCustomColormapFunctionFRGBPF.New()

class itkCustomColormapFunctionFRGBPF(itk.itkColormapFunctionPython.itkColormapFunctionFRGBPF):
    r"""


    Function object which maps a scalar value into an RGB colormap value.

    Nicholas Tustison, Hui Zhang, Gaetan Lehmann, Paul Yushkevich and
    James C. Gee  This code was contributed in the Insight Journal paper:

    "Meeting Andy Warhol Somewhere Over the Rainbow: RGB Colormapping and
    ITK"https://www.insight-journal.org/browse/publication/285 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF___New_orig__)
    Clone = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF_Clone)
    SetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF_SetRedChannel)
    GetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF_GetRedChannel)
    SetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF_SetGreenChannel)
    GetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF_GetGreenChannel)
    SetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF_SetBlueChannel)
    GetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF_GetBlueChannel)
    __swig_destroy__ = _itkCustomColormapFunctionPython.delete_itkCustomColormapFunctionFRGBPF
    cast = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF_cast)

    def New(*args, **kargs):
        """New() -> itkCustomColormapFunctionFRGBPF

        Create a new object of the class itkCustomColormapFunctionFRGBPF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCustomColormapFunctionFRGBPF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCustomColormapFunctionFRGBPF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCustomColormapFunctionFRGBPF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCustomColormapFunctionFRGBPF in _itkCustomColormapFunctionPython:
_itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF_swigregister(itkCustomColormapFunctionFRGBPF)
itkCustomColormapFunctionFRGBPF___New_orig__ = _itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF___New_orig__
itkCustomColormapFunctionFRGBPF_cast = _itkCustomColormapFunctionPython.itkCustomColormapFunctionFRGBPF_cast


def itkCustomColormapFunctionUCRGBAPUC_New():
    return itkCustomColormapFunctionUCRGBAPUC.New()

class itkCustomColormapFunctionUCRGBAPUC(itk.itkColormapFunctionPython.itkColormapFunctionUCRGBAPUC):
    r"""


    Function object which maps a scalar value into an RGB colormap value.

    Nicholas Tustison, Hui Zhang, Gaetan Lehmann, Paul Yushkevich and
    James C. Gee  This code was contributed in the Insight Journal paper:

    "Meeting Andy Warhol Somewhere Over the Rainbow: RGB Colormapping and
    ITK"https://www.insight-journal.org/browse/publication/285 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC___New_orig__)
    Clone = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC_Clone)
    SetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC_SetRedChannel)
    GetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC_GetRedChannel)
    SetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC_SetGreenChannel)
    GetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC_GetGreenChannel)
    SetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC_SetBlueChannel)
    GetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC_GetBlueChannel)
    __swig_destroy__ = _itkCustomColormapFunctionPython.delete_itkCustomColormapFunctionUCRGBAPUC
    cast = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC_cast)

    def New(*args, **kargs):
        """New() -> itkCustomColormapFunctionUCRGBAPUC

        Create a new object of the class itkCustomColormapFunctionUCRGBAPUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCustomColormapFunctionUCRGBAPUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCustomColormapFunctionUCRGBAPUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCustomColormapFunctionUCRGBAPUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCustomColormapFunctionUCRGBAPUC in _itkCustomColormapFunctionPython:
_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC_swigregister(itkCustomColormapFunctionUCRGBAPUC)
itkCustomColormapFunctionUCRGBAPUC___New_orig__ = _itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC___New_orig__
itkCustomColormapFunctionUCRGBAPUC_cast = _itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBAPUC_cast


def itkCustomColormapFunctionUCRGBPUC_New():
    return itkCustomColormapFunctionUCRGBPUC.New()

class itkCustomColormapFunctionUCRGBPUC(itk.itkColormapFunctionPython.itkColormapFunctionUCRGBPUC):
    r"""


    Function object which maps a scalar value into an RGB colormap value.

    Nicholas Tustison, Hui Zhang, Gaetan Lehmann, Paul Yushkevich and
    James C. Gee  This code was contributed in the Insight Journal paper:

    "Meeting Andy Warhol Somewhere Over the Rainbow: RGB Colormapping and
    ITK"https://www.insight-journal.org/browse/publication/285 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC___New_orig__)
    Clone = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC_Clone)
    SetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC_SetRedChannel)
    GetRedChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC_GetRedChannel)
    SetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC_SetGreenChannel)
    GetGreenChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC_GetGreenChannel)
    SetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC_SetBlueChannel)
    GetBlueChannel = _swig_new_instance_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC_GetBlueChannel)
    __swig_destroy__ = _itkCustomColormapFunctionPython.delete_itkCustomColormapFunctionUCRGBPUC
    cast = _swig_new_static_method(_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC_cast)

    def New(*args, **kargs):
        """New() -> itkCustomColormapFunctionUCRGBPUC

        Create a new object of the class itkCustomColormapFunctionUCRGBPUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCustomColormapFunctionUCRGBPUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCustomColormapFunctionUCRGBPUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCustomColormapFunctionUCRGBPUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCustomColormapFunctionUCRGBPUC in _itkCustomColormapFunctionPython:
_itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC_swigregister(itkCustomColormapFunctionUCRGBPUC)
itkCustomColormapFunctionUCRGBPUC___New_orig__ = _itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC___New_orig__
itkCustomColormapFunctionUCRGBPUC_cast = _itkCustomColormapFunctionPython.itkCustomColormapFunctionUCRGBPUC_cast



