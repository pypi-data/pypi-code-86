
import pcbnew
import types

# KiCAD 6 renames some of the types, ensure compatibility by introducing aliases
# when KiCAD 5 is used

def getVersion():
    try:
        v = [int(x) for x in pcbnew.GetMajorMinorVersion().split(".")]
        return tuple(v)
    except AttributeError:
        # KiCAD 5 does not have such function, assume it version 5.something
        return 5, 0

def boardGetProperties(self):
    raise NotImplementedError("The API is gone in v6, should be back in a few months")

def boardSetProperties(self, p):
    raise NotImplementedError("The API is gone in v6, should be back in a few months")

def GetBoundingBox(self, includeText=True, includeInvisibleText=True):
    if not includeText and not includeInvisibleText:
        return self.GetFootprintRect()
    if includeText and includeInvisibleText:
        return self._GetBoundingBox()
    raise NotImplementedError("Incompatible v5 and v6 API")

pcbnewVersion = getVersion()

def isV6(version=pcbnewVersion):
    if version[0] == 5 and version[1] == 99:
        return True
    return version[0] == 6

if not isV6(pcbnewVersion):
    # Introduce type aliases
    pcbnew.PCB_SHAPE = pcbnew.DRAWSEGMENT
    pcbnew.FP_SHAPE = pcbnew.EDGE_MODULE
    pcbnew.PCB_TEXT = pcbnew.TEXTE_PCB
    pcbnew.FP_TEXT = pcbnew.TEXTE_MODULE
    pcbnew.PCB_PLOT_PARAMS.SetSketchPadLineWidth = pcbnew.PCB_PLOT_PARAMS.SetLineWidth
    pcbnew.PCB_TEXT.SetTextThickness = pcbnew.PCB_TEXT.SetThickness
    pcbnew.ZONE = pcbnew.ZONE_CONTAINER
    pcbnew.ZONES = pcbnew.ZONE_CONTAINERS
    pcbnew.DXF_UNITS_MILLIMETERS = pcbnew.DXF_PLOTTER.DXF_UNIT_MILLIMETERS

    # Introduce renamed functions
    pcbnew.BOARD.GetFootprints = pcbnew.BOARD.GetModules
    pcbnew.BOARD.FindFootprintByReference = pcbnew.BOARD.FindModuleByReference

    pcbnew.MODULE._GetBoundingBox = pcbnew.MODULE.GetBoundingBox
    pcbnew.MODULE.GetBoundingBox = GetBoundingBox

    # Add board properties
    pcbnew.BOARD.GetProperties = boardGetProperties
    pcbnew.BOARD.SetProperties = boardSetProperties

    # PLOTTING ENUMS
    pcbnew.PLOT_TEXT_MODE_STROKE = pcbnew.PLOTTEXTMODE_STROKE
    pcbnew.PLOT_TEXT_MODE_DEFAULT = pcbnew.PLOTTEXTMODE_DEFAULT
    pcbnew.PLOT_TEXT_MODE_NATIVE = pcbnew.PLOTTEXTMODE_NATIVE
    pcbnew.PLOT_TEXT_MODE_PHANTOM = pcbnew.PLOTTEXTMODE_PHANTOM

