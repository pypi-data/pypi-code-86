# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIOImageBasePython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ITKIOImageBaseBasePython
else:
    import _ITKIOImageBaseBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _ITKIOImageBaseBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _ITKIOImageBaseBasePython.SWIG_PyStaticMethod_New

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
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.ITKCommonBasePython

def itkArchetypeSeriesFileNames_New():
    return itkArchetypeSeriesFileNames.New()

class itkArchetypeSeriesFileNames(itk.ITKCommonBasePython.itkObject):
    r"""


    Generate an ordered sequence of filenames.

    This class generates an ordered sequence of files based on an
    archetypical filename. From the archetypical filename, a set of
    regular expressions is created to group filenames based on numeric
    substrings. There can be multiple numeric substrings in the archetype.
    When this occurs, ArchetypeSeriesFileNames can not determine which
    numeric substring refers to the "image number" and which numeric
    substring refers to the "series" or "study". By default, the
    ArchetypeSeriesFileNames assumes the rightmost numeric substring
    refers to the image number, and this is the group of filenames
    returned by default. However, the other groupings of filenames can
    also be queried by passing in a group number to the GetFileNames()
    method. Groups are numbered by the numeric substrings from right to
    left in the archetype.

    foo_5_1.png     foo_5_2.png     foo_5_3.png     foo_6_1.png
    foo_6_2.png     foo_6_3.png

    and specifying an archetypical file foo_5_1.png, the filename list
    will contain    foo_5_1.png     foo_5_2.png     foo_5_3.png 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_ITKIOImageBaseBasePython.itkArchetypeSeriesFileNames___New_orig__)
    Clone = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkArchetypeSeriesFileNames_Clone)
    SetArchetype = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkArchetypeSeriesFileNames_SetArchetype)
    GetArchetype = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkArchetypeSeriesFileNames_GetArchetype)
    GetNumberOfGroupings = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkArchetypeSeriesFileNames_GetNumberOfGroupings)
    GetFileNames = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkArchetypeSeriesFileNames_GetFileNames)
    __swig_destroy__ = _ITKIOImageBaseBasePython.delete_itkArchetypeSeriesFileNames
    cast = _swig_new_static_method(_ITKIOImageBaseBasePython.itkArchetypeSeriesFileNames_cast)

    def New(*args, **kargs):
        """New() -> itkArchetypeSeriesFileNames

        Create a new object of the class itkArchetypeSeriesFileNames and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkArchetypeSeriesFileNames.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkArchetypeSeriesFileNames.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkArchetypeSeriesFileNames.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkArchetypeSeriesFileNames in _ITKIOImageBaseBasePython:
_ITKIOImageBaseBasePython.itkArchetypeSeriesFileNames_swigregister(itkArchetypeSeriesFileNames)
itkArchetypeSeriesFileNames___New_orig__ = _ITKIOImageBaseBasePython.itkArchetypeSeriesFileNames___New_orig__
itkArchetypeSeriesFileNames_cast = _ITKIOImageBaseBasePython.itkArchetypeSeriesFileNames_cast

class itkImageIOBase(itk.ITKCommonBasePython.itkLightProcessObject):
    r"""


    Abstract superclass defines image IO interface.

    ImageIOBase is a class that reads and/or writes image data of a
    particular format (such as PNG or raw binary). The ImageIOBase
    encapsulates both the reading and writing of data. The ImageIOBase is
    used by the ImageFileReader class (to read data) and the
    ImageFileWriter (to write data) into a single file. The
    ImageSeriesReader and ImageSeriesWriter classes are used to read and
    write data (in conjunction with ImageIOBase) when the data is
    represented by a series of files. Normally the user does not directly
    manipulate this class other than to instantiate it, set the FileName,
    and assign it to a ImageFileReader/ImageFileWriter or
    ImageSeriesReader/ImageSeriesWriter.

    A Pluggable factory pattern is used this allows different kinds of
    readers to be registered (even at run time) without having to modify
    the code in this class.

    See:   ImageFileWriter

    See:   ImageFileReader

    See:   ImageSeriesWriter

    See:   ImageSeriesReader 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetFileName = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetFileName)
    GetFileName = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetFileName)
    SetNumberOfDimensions = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetNumberOfDimensions)
    GetNumberOfDimensions = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetNumberOfDimensions)
    SetDimensions = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetDimensions)
    GetDimensions = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetDimensions)
    SetOrigin = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetOrigin)
    GetOrigin = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetOrigin)
    SetSpacing = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetSpacing)
    GetSpacing = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetSpacing)
    SetDirection = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetDirection)
    GetDirection = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetDirection)
    GetDefaultDirection = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetDefaultDirection)
    SetIORegion = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetIORegion)
    GetIORegion = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetIORegion)
    SetPixelType = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetPixelType)
    GetPixelType = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetPixelType)
    SetComponentType = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetComponentType)
    GetComponentType = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetComponentType)
    GetComponentTypeInfo = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetComponentTypeInfo)
    SetNumberOfComponents = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetNumberOfComponents)
    GetNumberOfComponents = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetNumberOfComponents)
    SetUseCompression = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetUseCompression)
    GetUseCompression = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetUseCompression)
    UseCompressionOn = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_UseCompressionOn)
    UseCompressionOff = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_UseCompressionOff)
    SetCompressionLevel = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetCompressionLevel)
    GetCompressionLevel = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetCompressionLevel)
    SetCompressor = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetCompressor)
    GetCompressor = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetCompressor)
    SetUseStreamedReading = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetUseStreamedReading)
    GetUseStreamedReading = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetUseStreamedReading)
    UseStreamedReadingOn = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_UseStreamedReadingOn)
    UseStreamedReadingOff = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_UseStreamedReadingOff)
    SetUseStreamedWriting = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetUseStreamedWriting)
    GetUseStreamedWriting = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetUseStreamedWriting)
    UseStreamedWritingOn = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_UseStreamedWritingOn)
    UseStreamedWritingOff = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_UseStreamedWritingOff)
    SetExpandRGBPalette = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetExpandRGBPalette)
    GetExpandRGBPalette = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetExpandRGBPalette)
    ExpandRGBPaletteOn = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_ExpandRGBPaletteOn)
    ExpandRGBPaletteOff = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_ExpandRGBPaletteOff)
    SetWritePalette = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetWritePalette)
    GetWritePalette = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetWritePalette)
    WritePaletteOn = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_WritePaletteOn)
    WritePaletteOff = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_WritePaletteOff)
    GetIsReadAsScalarPlusPalette = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetIsReadAsScalarPlusPalette)
    GetComponentTypeAsString = _swig_new_static_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetComponentTypeAsString)
    GetComponentTypeFromString = _swig_new_static_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetComponentTypeFromString)
    GetPixelTypeAsString = _swig_new_static_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetPixelTypeAsString)
    GetPixelTypeFromString = _swig_new_static_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetPixelTypeFromString)
    SetFileType = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetFileType)
    GetFileType = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetFileType)
    SetFileTypeToASCII = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetFileTypeToASCII)
    SetFileTypeToBinary = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetFileTypeToBinary)
    SetByteOrder = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetByteOrder)
    GetByteOrder = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetByteOrder)
    SetByteOrderToBigEndian = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetByteOrderToBigEndian)
    SetByteOrderToLittleEndian = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SetByteOrderToLittleEndian)
    GetFileTypeAsString = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetFileTypeAsString)
    GetByteOrderAsString = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetByteOrderAsString)
    GetPixelStride = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetPixelStride)
    GetImageSizeInPixels = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetImageSizeInPixels)
    GetImageSizeInBytes = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetImageSizeInBytes)
    GetImageSizeInComponents = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetImageSizeInComponents)
    GetComponentSize = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetComponentSize)
    CanReadFile = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_CanReadFile)
    CanStreamRead = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_CanStreamRead)
    ReadImageInformation = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_ReadImageInformation)
    Read = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_Read)
    CanWriteFile = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_CanWriteFile)
    CanStreamWrite = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_CanStreamWrite)
    WriteImageInformation = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_WriteImageInformation)
    Write = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_Write)
    SupportsDimension = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_SupportsDimension)
    GenerateStreamableReadRegionFromRequestedRegion = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GenerateStreamableReadRegionFromRequestedRegion)
    GetActualNumberOfSplitsForWriting = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetActualNumberOfSplitsForWriting)
    GetSplitRegionForWriting = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetSplitRegionForWriting)
    GetSupportedReadExtensions = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetSupportedReadExtensions)
    GetSupportedWriteExtensions = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkImageIOBase_GetSupportedWriteExtensions)
    __swig_destroy__ = _ITKIOImageBaseBasePython.delete_itkImageIOBase
    cast = _swig_new_static_method(_ITKIOImageBaseBasePython.itkImageIOBase_cast)

# Register itkImageIOBase in _ITKIOImageBaseBasePython:
_ITKIOImageBaseBasePython.itkImageIOBase_swigregister(itkImageIOBase)
itkImageIOBase_GetComponentTypeAsString = _ITKIOImageBaseBasePython.itkImageIOBase_GetComponentTypeAsString
itkImageIOBase_GetComponentTypeFromString = _ITKIOImageBaseBasePython.itkImageIOBase_GetComponentTypeFromString
itkImageIOBase_GetPixelTypeAsString = _ITKIOImageBaseBasePython.itkImageIOBase_GetPixelTypeAsString
itkImageIOBase_GetPixelTypeFromString = _ITKIOImageBaseBasePython.itkImageIOBase_GetPixelTypeFromString
itkImageIOBase_cast = _ITKIOImageBaseBasePython.itkImageIOBase_cast

class itkImageIOFactory(itk.ITKCommonBasePython.itkObject):
    r"""


    Create instances of ImageIO objects using an object factory. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    CreateImageIO = _swig_new_static_method(_ITKIOImageBaseBasePython.itkImageIOFactory_CreateImageIO)

# Register itkImageIOFactory in _ITKIOImageBaseBasePython:
_ITKIOImageBaseBasePython.itkImageIOFactory_swigregister(itkImageIOFactory)
itkImageIOFactory_CreateImageIO = _ITKIOImageBaseBasePython.itkImageIOFactory_CreateImageIO


def itkNumericSeriesFileNames_New():
    return itkNumericSeriesFileNames.New()

class itkNumericSeriesFileNames(itk.ITKCommonBasePython.itkObject):
    r"""


    Generate an ordered sequence of filenames.

    This class generate an ordered sequence of files whose filenames
    contain a single unique, non-negative, integral value (e.g.
    test.1.png, test2.png, foo.3, etc.).

    The file name is created from a sprintf-style series format which
    should contain an integer format string like "%d". Bad formats will
    cause the series reader to throw an exception.

    Warning: returned filenames (which may be full or relative paths) are
    not checked against any system-imposed path-length limit, because of
    difficulties finding a portable method to do so. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames___New_orig__)
    Clone = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_Clone)
    SetStartIndex = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_SetStartIndex)
    GetStartIndex = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_GetStartIndex)
    SetEndIndex = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_SetEndIndex)
    GetEndIndex = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_GetEndIndex)
    SetIncrementIndex = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_SetIncrementIndex)
    GetIncrementIndex = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_GetIncrementIndex)
    SetSeriesFormat = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_SetSeriesFormat)
    GetSeriesFormat = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_GetSeriesFormat)
    GetFileNames = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_GetFileNames)
    __swig_destroy__ = _ITKIOImageBaseBasePython.delete_itkNumericSeriesFileNames
    cast = _swig_new_static_method(_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_cast)

    def New(*args, **kargs):
        """New() -> itkNumericSeriesFileNames

        Create a new object of the class itkNumericSeriesFileNames and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNumericSeriesFileNames.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkNumericSeriesFileNames.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkNumericSeriesFileNames.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkNumericSeriesFileNames in _ITKIOImageBaseBasePython:
_ITKIOImageBaseBasePython.itkNumericSeriesFileNames_swigregister(itkNumericSeriesFileNames)
itkNumericSeriesFileNames___New_orig__ = _ITKIOImageBaseBasePython.itkNumericSeriesFileNames___New_orig__
itkNumericSeriesFileNames_cast = _ITKIOImageBaseBasePython.itkNumericSeriesFileNames_cast


def itkRegularExpressionSeriesFileNames_New():
    return itkRegularExpressionSeriesFileNames.New()

class itkRegularExpressionSeriesFileNames(itk.ITKCommonBasePython.itkObject):
    r"""


    Generate an ordered sequence of filenames that match a regular
    expression.

    This class generates an ordered sequence of files whose filenames
    match a regular expression. The file names are sorted using a sub
    expression match selected by SubMatch. Regular expressions are a
    powerful, compact mechanism for parsing strings. Expressions consist
    of the following metacharacters:

    ^ Matches at beginning of a line

    $ Matches at end of a line

    . Matches any single character

    [ ] Matches any character(s) inside the brackets

    [^ ] Matches any character(s) not inside the brackets

    Matches any character in range on either side of a dash

    Matches preceding pattern zero or more times

    Matches preceding pattern one or more times

    ? Matches preceding pattern zero or once only

    () Saves a matched expression and uses it in a later match

    Note that more than one of these metacharacters can be used in a
    single regular expression in order to create complex match any
    character sequence that does not begin with the characters "ab"
    followed by numbers in the series one through nine. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames___New_orig__)
    Clone = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_Clone)
    SetDirectory = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_SetDirectory)
    GetDirectory = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_GetDirectory)
    SetRegularExpression = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_SetRegularExpression)
    GetRegularExpression = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_GetRegularExpression)
    SetSubMatch = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_SetSubMatch)
    GetSubMatch = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_GetSubMatch)
    SetNumericSort = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_SetNumericSort)
    GetNumericSort = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_GetNumericSort)
    NumericSortOn = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_NumericSortOn)
    NumericSortOff = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_NumericSortOff)
    GetFileNames = _swig_new_instance_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_GetFileNames)
    __swig_destroy__ = _ITKIOImageBaseBasePython.delete_itkRegularExpressionSeriesFileNames
    cast = _swig_new_static_method(_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_cast)

    def New(*args, **kargs):
        """New() -> itkRegularExpressionSeriesFileNames

        Create a new object of the class itkRegularExpressionSeriesFileNames and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRegularExpressionSeriesFileNames.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRegularExpressionSeriesFileNames.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRegularExpressionSeriesFileNames.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRegularExpressionSeriesFileNames in _ITKIOImageBaseBasePython:
_ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_swigregister(itkRegularExpressionSeriesFileNames)
itkRegularExpressionSeriesFileNames___New_orig__ = _ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames___New_orig__
itkRegularExpressionSeriesFileNames_cast = _ITKIOImageBaseBasePython.itkRegularExpressionSeriesFileNames_cast

class itkStreamingImageIOBase(itkImageIOBase):
    r"""


    A base class for specific ImageIO file formats which support
    streaming.

    This class overloads the methods needed to enable streaming. These
    methods are utilized by the ImageFileReader and ImageFileWriter. The
    implementation supports streaming of an arbitrary sized region as well
    as pasting to new or existing file ( of the same name, size, and pixel
    type ). See:  CanStreamWrite CanStreamRead
    GenerateStreamableReadRegionFromRequestedRegion
    GetActualNumberOfSplitsForWriting  Additionally low level IO methods
    are provided to read and write an IORegion from a file. See:
    StreamReadBufferAsBinary StreamWriteBufferAsBinary  This
    implementation was taken fron the Insight Joural:https://www.insight-
    journal.org/browse/publication/729

    See:   itk::ImageFileReader itk::ImageFileWriter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ITKIOImageBaseBasePython.delete_itkStreamingImageIOBase
    cast = _swig_new_static_method(_ITKIOImageBaseBasePython.itkStreamingImageIOBase_cast)

# Register itkStreamingImageIOBase in _ITKIOImageBaseBasePython:
_ITKIOImageBaseBasePython.itkStreamingImageIOBase_swigregister(itkStreamingImageIOBase)
itkStreamingImageIOBase_cast = _ITKIOImageBaseBasePython.itkStreamingImageIOBase_cast



