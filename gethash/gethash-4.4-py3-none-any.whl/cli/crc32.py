from gethash.script import gethashcli, script_main

META = {
    "cmdname": "crc32",
    "hashname": "CRC32",
    "suffix": ".crc32",
    "package": "gethash.utils.crc32",
    "hasher": "CRC32",
}


@gethashcli(**META)
def main(files, **kwargs):
    """Generate or check CRC32."""

    from gethash.utils.crc32 import CRC32 as H

    script_main(H(), files, **kwargs)


if __name__ == "__main__":
    main()
