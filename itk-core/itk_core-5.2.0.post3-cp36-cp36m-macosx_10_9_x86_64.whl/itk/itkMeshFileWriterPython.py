# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIOMeshBasePython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkMeshFileWriterPython
else:
    import _itkMeshFileWriterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMeshFileWriterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMeshFileWriterPython.SWIG_PyStaticMethod_New

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
import itk.itkMeshBasePython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkVectorContainerPython
import itk.itkPointPython
import itk.itkFixedArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkArrayPython
import itk.itkPointSetPython
import itk.itkMeshIOBasePython

def itkMeshFileWriterMD2_New():
    return itkMeshFileWriterMD2.New()

class itkMeshFileWriterMD2(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Writes mesh data to a single file.

    MeshFileWriter writes its input data to a single output file.
    MeshFileWriter interfaces with an MeshIO class to write out the data.

    A pluggable factory pattern is used that allows different kinds of
    writers to be registered (even at run time) without having to modify
    the code in this class. You can either manually instantiate the MeshIO
    object and associate it with the MeshFileWriter, or let the class
    figure it out from the extension. Normally just setting the filename
    with a suitable suffix (".vtk", etc) and setting the input to the
    writer is enough to get the writer to work properly.

    Wanlin Zhu. Uviversity of New South Wales, Australia.

    See:   MeshIOBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_Clone)
    SetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_GetInput)
    SetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_SetFileName)
    GetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_GetFileName)
    SetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_SetMeshIO)
    GetModifiableMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_GetModifiableMeshIO)
    GetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_GetMeshIO)
    SetFileTypeAsASCII = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_SetFileTypeAsASCII)
    SetFileTypeAsBINARY = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_SetFileTypeAsBINARY)
    Write = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_Write)
    SetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_SetUseCompression)
    GetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_GetUseCompression)
    UseCompressionOn = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_UseCompressionOn)
    UseCompressionOff = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_UseCompressionOff)
    __swig_destroy__ = _itkMeshFileWriterPython.delete_itkMeshFileWriterMD2
    cast = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMD2_cast)

    def New(*args, **kargs):
        """New() -> itkMeshFileWriterMD2

        Create a new object of the class itkMeshFileWriterMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshFileWriterMD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshFileWriterMD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshFileWriterMD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshFileWriterMD2 in _itkMeshFileWriterPython:
_itkMeshFileWriterPython.itkMeshFileWriterMD2_swigregister(itkMeshFileWriterMD2)
itkMeshFileWriterMD2___New_orig__ = _itkMeshFileWriterPython.itkMeshFileWriterMD2___New_orig__
itkMeshFileWriterMD2_cast = _itkMeshFileWriterPython.itkMeshFileWriterMD2_cast


def itkMeshFileWriterMD3_New():
    return itkMeshFileWriterMD3.New()

class itkMeshFileWriterMD3(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Writes mesh data to a single file.

    MeshFileWriter writes its input data to a single output file.
    MeshFileWriter interfaces with an MeshIO class to write out the data.

    A pluggable factory pattern is used that allows different kinds of
    writers to be registered (even at run time) without having to modify
    the code in this class. You can either manually instantiate the MeshIO
    object and associate it with the MeshFileWriter, or let the class
    figure it out from the extension. Normally just setting the filename
    with a suitable suffix (".vtk", etc) and setting the input to the
    writer is enough to get the writer to work properly.

    Wanlin Zhu. Uviversity of New South Wales, Australia.

    See:   MeshIOBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_Clone)
    SetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_GetInput)
    SetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_SetFileName)
    GetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_GetFileName)
    SetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_SetMeshIO)
    GetModifiableMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_GetModifiableMeshIO)
    GetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_GetMeshIO)
    SetFileTypeAsASCII = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_SetFileTypeAsASCII)
    SetFileTypeAsBINARY = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_SetFileTypeAsBINARY)
    Write = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_Write)
    SetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_SetUseCompression)
    GetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_GetUseCompression)
    UseCompressionOn = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_UseCompressionOn)
    UseCompressionOff = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_UseCompressionOff)
    __swig_destroy__ = _itkMeshFileWriterPython.delete_itkMeshFileWriterMD3
    cast = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMD3_cast)

    def New(*args, **kargs):
        """New() -> itkMeshFileWriterMD3

        Create a new object of the class itkMeshFileWriterMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshFileWriterMD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshFileWriterMD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshFileWriterMD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshFileWriterMD3 in _itkMeshFileWriterPython:
_itkMeshFileWriterPython.itkMeshFileWriterMD3_swigregister(itkMeshFileWriterMD3)
itkMeshFileWriterMD3___New_orig__ = _itkMeshFileWriterPython.itkMeshFileWriterMD3___New_orig__
itkMeshFileWriterMD3_cast = _itkMeshFileWriterPython.itkMeshFileWriterMD3_cast


def itkMeshFileWriterMD4_New():
    return itkMeshFileWriterMD4.New()

class itkMeshFileWriterMD4(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Writes mesh data to a single file.

    MeshFileWriter writes its input data to a single output file.
    MeshFileWriter interfaces with an MeshIO class to write out the data.

    A pluggable factory pattern is used that allows different kinds of
    writers to be registered (even at run time) without having to modify
    the code in this class. You can either manually instantiate the MeshIO
    object and associate it with the MeshFileWriter, or let the class
    figure it out from the extension. Normally just setting the filename
    with a suitable suffix (".vtk", etc) and setting the input to the
    writer is enough to get the writer to work properly.

    Wanlin Zhu. Uviversity of New South Wales, Australia.

    See:   MeshIOBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_Clone)
    SetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_GetInput)
    SetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_SetFileName)
    GetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_GetFileName)
    SetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_SetMeshIO)
    GetModifiableMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_GetModifiableMeshIO)
    GetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_GetMeshIO)
    SetFileTypeAsASCII = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_SetFileTypeAsASCII)
    SetFileTypeAsBINARY = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_SetFileTypeAsBINARY)
    Write = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_Write)
    SetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_SetUseCompression)
    GetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_GetUseCompression)
    UseCompressionOn = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_UseCompressionOn)
    UseCompressionOff = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_UseCompressionOff)
    __swig_destroy__ = _itkMeshFileWriterPython.delete_itkMeshFileWriterMD4
    cast = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMD4_cast)

    def New(*args, **kargs):
        """New() -> itkMeshFileWriterMD4

        Create a new object of the class itkMeshFileWriterMD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshFileWriterMD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshFileWriterMD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshFileWriterMD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshFileWriterMD4 in _itkMeshFileWriterPython:
_itkMeshFileWriterPython.itkMeshFileWriterMD4_swigregister(itkMeshFileWriterMD4)
itkMeshFileWriterMD4___New_orig__ = _itkMeshFileWriterPython.itkMeshFileWriterMD4___New_orig__
itkMeshFileWriterMD4_cast = _itkMeshFileWriterPython.itkMeshFileWriterMD4_cast


def itkMeshFileWriterMF2_New():
    return itkMeshFileWriterMF2.New()

class itkMeshFileWriterMF2(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Writes mesh data to a single file.

    MeshFileWriter writes its input data to a single output file.
    MeshFileWriter interfaces with an MeshIO class to write out the data.

    A pluggable factory pattern is used that allows different kinds of
    writers to be registered (even at run time) without having to modify
    the code in this class. You can either manually instantiate the MeshIO
    object and associate it with the MeshFileWriter, or let the class
    figure it out from the extension. Normally just setting the filename
    with a suitable suffix (".vtk", etc) and setting the input to the
    writer is enough to get the writer to work properly.

    Wanlin Zhu. Uviversity of New South Wales, Australia.

    See:   MeshIOBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_Clone)
    SetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_GetInput)
    SetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_SetFileName)
    GetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_GetFileName)
    SetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_SetMeshIO)
    GetModifiableMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_GetModifiableMeshIO)
    GetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_GetMeshIO)
    SetFileTypeAsASCII = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_SetFileTypeAsASCII)
    SetFileTypeAsBINARY = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_SetFileTypeAsBINARY)
    Write = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_Write)
    SetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_SetUseCompression)
    GetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_GetUseCompression)
    UseCompressionOn = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_UseCompressionOn)
    UseCompressionOff = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_UseCompressionOff)
    __swig_destroy__ = _itkMeshFileWriterPython.delete_itkMeshFileWriterMF2
    cast = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMF2_cast)

    def New(*args, **kargs):
        """New() -> itkMeshFileWriterMF2

        Create a new object of the class itkMeshFileWriterMF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshFileWriterMF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshFileWriterMF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshFileWriterMF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshFileWriterMF2 in _itkMeshFileWriterPython:
_itkMeshFileWriterPython.itkMeshFileWriterMF2_swigregister(itkMeshFileWriterMF2)
itkMeshFileWriterMF2___New_orig__ = _itkMeshFileWriterPython.itkMeshFileWriterMF2___New_orig__
itkMeshFileWriterMF2_cast = _itkMeshFileWriterPython.itkMeshFileWriterMF2_cast


def itkMeshFileWriterMF3_New():
    return itkMeshFileWriterMF3.New()

class itkMeshFileWriterMF3(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Writes mesh data to a single file.

    MeshFileWriter writes its input data to a single output file.
    MeshFileWriter interfaces with an MeshIO class to write out the data.

    A pluggable factory pattern is used that allows different kinds of
    writers to be registered (even at run time) without having to modify
    the code in this class. You can either manually instantiate the MeshIO
    object and associate it with the MeshFileWriter, or let the class
    figure it out from the extension. Normally just setting the filename
    with a suitable suffix (".vtk", etc) and setting the input to the
    writer is enough to get the writer to work properly.

    Wanlin Zhu. Uviversity of New South Wales, Australia.

    See:   MeshIOBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_Clone)
    SetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_GetInput)
    SetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_SetFileName)
    GetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_GetFileName)
    SetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_SetMeshIO)
    GetModifiableMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_GetModifiableMeshIO)
    GetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_GetMeshIO)
    SetFileTypeAsASCII = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_SetFileTypeAsASCII)
    SetFileTypeAsBINARY = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_SetFileTypeAsBINARY)
    Write = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_Write)
    SetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_SetUseCompression)
    GetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_GetUseCompression)
    UseCompressionOn = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_UseCompressionOn)
    UseCompressionOff = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_UseCompressionOff)
    __swig_destroy__ = _itkMeshFileWriterPython.delete_itkMeshFileWriterMF3
    cast = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMF3_cast)

    def New(*args, **kargs):
        """New() -> itkMeshFileWriterMF3

        Create a new object of the class itkMeshFileWriterMF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshFileWriterMF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshFileWriterMF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshFileWriterMF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshFileWriterMF3 in _itkMeshFileWriterPython:
_itkMeshFileWriterPython.itkMeshFileWriterMF3_swigregister(itkMeshFileWriterMF3)
itkMeshFileWriterMF3___New_orig__ = _itkMeshFileWriterPython.itkMeshFileWriterMF3___New_orig__
itkMeshFileWriterMF3_cast = _itkMeshFileWriterPython.itkMeshFileWriterMF3_cast


def itkMeshFileWriterMF4_New():
    return itkMeshFileWriterMF4.New()

class itkMeshFileWriterMF4(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Writes mesh data to a single file.

    MeshFileWriter writes its input data to a single output file.
    MeshFileWriter interfaces with an MeshIO class to write out the data.

    A pluggable factory pattern is used that allows different kinds of
    writers to be registered (even at run time) without having to modify
    the code in this class. You can either manually instantiate the MeshIO
    object and associate it with the MeshFileWriter, or let the class
    figure it out from the extension. Normally just setting the filename
    with a suitable suffix (".vtk", etc) and setting the input to the
    writer is enough to get the writer to work properly.

    Wanlin Zhu. Uviversity of New South Wales, Australia.

    See:   MeshIOBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_Clone)
    SetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_GetInput)
    SetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_SetFileName)
    GetFileName = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_GetFileName)
    SetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_SetMeshIO)
    GetModifiableMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_GetModifiableMeshIO)
    GetMeshIO = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_GetMeshIO)
    SetFileTypeAsASCII = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_SetFileTypeAsASCII)
    SetFileTypeAsBINARY = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_SetFileTypeAsBINARY)
    Write = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_Write)
    SetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_SetUseCompression)
    GetUseCompression = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_GetUseCompression)
    UseCompressionOn = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_UseCompressionOn)
    UseCompressionOff = _swig_new_instance_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_UseCompressionOff)
    __swig_destroy__ = _itkMeshFileWriterPython.delete_itkMeshFileWriterMF4
    cast = _swig_new_static_method(_itkMeshFileWriterPython.itkMeshFileWriterMF4_cast)

    def New(*args, **kargs):
        """New() -> itkMeshFileWriterMF4

        Create a new object of the class itkMeshFileWriterMF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshFileWriterMF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshFileWriterMF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshFileWriterMF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshFileWriterMF4 in _itkMeshFileWriterPython:
_itkMeshFileWriterPython.itkMeshFileWriterMF4_swigregister(itkMeshFileWriterMF4)
itkMeshFileWriterMF4___New_orig__ = _itkMeshFileWriterPython.itkMeshFileWriterMF4___New_orig__
itkMeshFileWriterMF4_cast = _itkMeshFileWriterPython.itkMeshFileWriterMF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def mesh_file_writer(*args,  file_name: str=..., mesh_io=..., use_compression: bool=...,**kwargs):
    """Functional interface for MeshFileWriter"""
    import itk

    kwarg_typehints = { 'file_name':file_name,'mesh_io':mesh_io,'use_compression':use_compression }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.MeshFileWriter.New(*args, **kwargs)
    return instance.__internal_call__()

def mesh_file_writer_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKIOMeshBase.MeshFileWriter
    mesh_file_writer.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    mesh_file_writer.__doc__ = filter_object.__doc__




