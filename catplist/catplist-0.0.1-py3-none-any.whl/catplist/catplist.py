#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

"""
handle Metadata information from ios.
Reads and unwraps all kind of plist in use for albums e.g.
 *.facemetadata, *.albummetadata, *.foldermetadata

For documentation visit: https://github.com/yoshtec/catplist
"""

from pathlib import Path
import uuid
import pprint
import click
from click_default_group import DefaultGroup
import plistlib
from plistlib import InvalidFileException
import datetime
import shutil
import re
import sys

UUID_REGEX = re.compile(
    "[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\Z", re.I
)

# important keys
NS_TOP = "$top"
NS_OBJ = "$objects"
NS_ARC = "$archiver"
NS_CLASS = "$class"

NS_KEYS = "NS.keys"
NS_OBJECTS = "NS.objects"
NS_TIME = "NS.time"
NS_DATA = "NS.data"
NS_STRING = "NS.string"
NS_STRING2 = "NSString"
NS_ATTRIBUTE = "NSAttributes"

KEY_TITLE = "title"
KEY_ASSETS = "assetUUIDs"
KEY_UUID = "uuid"
KEY_TRASH = "isInTrash"
KEY_ASSETUUIDS = "assetUUIDs"
KEY_ROOT = "root"

TYPE_PHMFEATUREENCODER = "PHMemoryFeatureEncoder"
TYPE_NSKEYEDARCHIVER = "NSKeyedArchiver"

HEAD_PLIST = b"bplist00"
HEAD_XZ = b"\xfd7zXZ"


def _is_plist(b: bytes):
    return len(b) > len(HEAD_PLIST) and b[0 : len(HEAD_PLIST)] == HEAD_PLIST


def _is_xz(b: bytes):
    return len(b) > len(HEAD_XZ) and b[0 : len(HEAD_XZ)] == HEAD_XZ


def _unwrap_bytes(b, uuids=False):
    if _is_xz(b):
        import lzma

        return unwrap(lzma.decompress(b))

    if _is_plist(b):
        return unwrap(plistlib.loads(b))

    HEAD_FFF = b"\n\xd3\x04bplist00"
    if len(b) > len(HEAD_FFF) and b[0 : len(HEAD_FFF)] == HEAD_FFF:
        return unwrap(plistlib.loads(b[3:]))

    if uuids:
        return _unwrap_uuids(b)

    # import hashlib
    # m = hashlib.sha1()
    # m.update(b)
    # with open(f"./tmp/bin/bin_{m.hexdigest()}.bin", "wb") as f:
    #     f.write(b)

    return b


def _unwrap_uuids(b):
    data = []
    i = 0
    while i < len(b):
        ux = uuid.UUID(bytes=b[i : i + 16])
        data.append(ux)
        i = i + 16
    return data


def _unwrap_dict(d: dict, orig: list = None):
    if d is None:
        return {}

    if NS_STRING in d:
        return d[NS_STRING]

    if NS_STRING2 in d:
        return d[NS_STRING2]

    if NS_TIME in d:
        return datetime.datetime(2001, 1, 1) + datetime.timedelta(seconds=d[NS_TIME])

    if NS_ARC in d and NS_TOP in d and NS_OBJ in d:
        if d[NS_ARC] in [TYPE_NSKEYEDARCHIVER, TYPE_PHMFEATUREENCODER]:
            result_dict: dict = {}
            for t in d[NS_TOP]:
                index = d[NS_TOP][t]

                if isinstance(index, plistlib.UID):
                    index = index.data
                    data = d[NS_OBJ][index]
                    if type(data) is bytes:
                        result_dict[t] = _unwrap_bytes(data, str(t).endswith("UUIDs"))
                    else:
                        result_dict[t] = unwrap(data, d[NS_OBJ])
                else:
                    result_dict[t] = index

            # unpack single "root" dictionaries
            if KEY_ROOT in result_dict and len(result_dict) == 1:
                return result_dict[KEY_ROOT]

            return result_dict

    if NS_DATA in d:
        return unwrap(d[NS_DATA])

    if NS_KEYS in d and NS_OBJECTS in d:
        data2 = {}
        for k, v in zip(d[NS_KEYS], d[NS_OBJECTS]):
            # print(f"k,v:{k},{v}")
            k = unwrap(k, orig)
            v = unwrap(v, orig)
            # print(f"k,v:{k},{v}")
            data2[k] = v
        return data2

    if NS_OBJECTS in d:
        data2 = []
        for v in d[NS_OBJECTS]:
            data2.append(unwrap(v, orig))
        return data2

    for t in d:
        d[t] = unwrap(d[t], orig)

    return d


def _unwrap_list(l: list, orig: list = None):
    if not l:
        return []

    result_list = []
    for e in l:
        result_list.append(unwrap(e, orig))
    return result_list


def unwrap(x, orig: list = None):
    if x is None:
        return ""

    if isinstance(x, int) or isinstance(x, float) or isinstance(x, bool):
        return x

    try:

        if isinstance(x, plistlib.UID):
            x = x.data
            if orig is not None and len(orig) > x:
                x = unwrap(orig[x], orig)
            return x

        if isinstance(x, str):
            if UUID_REGEX.match(x):
                return uuid.UUID(x)
            return x

        if isinstance(x, dict):
            return _unwrap_dict(x, orig)

        if isinstance(x, list):
            return _unwrap_list(x, orig)

        if type(x) is bytes:
            return _unwrap_bytes(x)

        # Fallback just return the original
        return x

    except (RuntimeError, InvalidFileException) as r:
        return f"$ERROR: {r}"


def read_ns_archiver(plist=None):
    return unwrap(plist)


def read_plist(plist=None):

    if not plist:
        return {}

    return unwrap(plist)


class BaseMetadataFile:
    def __init__(self, file: Path = None, bytez: bytes = None):
        self.file = file
        self.raw_metadata = {}
        self.metadata = {}

        if file:
            if not self.file.is_file():
                raise RuntimeError(f"Path '{self.file}' is not a regular file)")

            with open(self.file, "rb") as f:
                self.raw_metadata = plistlib.load(f)

        elif bytes and _is_plist(bytez):
            self.raw_metadata = plistlib.loads(bytez)
        else:
            raise RuntimeError(
                f"Supplied file '{file}' is invalid and supplied bytes is not a plist"
            )

        self.metadata = unwrap(self.raw_metadata)

    def dump_raw(self):
        width, lines = shutil.get_terminal_size()
        pprint.pp(self.raw_metadata, width=width)

    def dump(self):
        width, lines = shutil.get_terminal_size()
        pprint.pp(self.metadata, width=width)


class PhotosMetadataFile(BaseMetadataFile):
    def __init__(self, file: Path):
        BaseMetadataFile.__init__(self, file=file)

        self.asset_uuids = []
        self.title = ""
        self.uuid = None
        self.isInTrash = False

        if KEY_UUID in self.metadata:
            self.uuid = self.metadata[KEY_UUID]

        if KEY_TITLE in self.metadata:
            self.title = self.metadata[KEY_TITLE]

        if KEY_ASSETUUIDS in self.metadata:
            self.asset_uuids = self.metadata[KEY_ASSETUUIDS]

        if KEY_TRASH in self.metadata:
            self.isInTrash = bool(self.metadata[KEY_TRASH])

    def get_picture_uuids(self):
        return self.asset_uuids


@click.command()
@click.argument(
    "file", nargs=-1, type=click.Path(exists=True, file_okay=True, readable=True)
)
@click.option(
    "--raw", "-R", default=False, is_flag=True, help="print raw plist contents, will not unpack nested plists"
)
@click.option(
    "--recurse",
    "-r",
    default=False,
    is_flag=True,
    help="recurse into subdirs, reads all files ignores non plist files",
)
def catplist(file=None, raw=False, recurse=False):
    """
    This is catplist: display your plist for human reading and easy grepping.

    display contents of plist metadata files. helps to understand where and how data
    is stored on your ios device. Reads and displays:

    \b
        *.albummetadata
        *.memorymetadata
        *.facemetadata
        *.foldermetadata

    and general .plist like files.
    """

    stack: list = []
    if not file:
        click.echo(" - No file given! Usage: ")
        click.echo(" catplist file")
        return 0

    stack.extend(file)

    while len(stack) > 0:
        p = Path(stack.pop())
        if p.is_dir() and recurse:
            stack.extend(p.iterdir())
        elif p.is_file():
            click.secho(f"Analyzing file {p}:", bold=True)
            try:
                pm = BaseMetadataFile(p)
                if raw:
                    pm.dump_raw()
                    click.echo("")
                else:
                    pm.dump()
            except InvalidFileException as i:
                click.echo(f" - is not a valid plist. Skipping over Error '{i}'.")
            click.echo("")
    sys.exit(0)


if "__main__" == __name__:
    sys.exit(catplist())
