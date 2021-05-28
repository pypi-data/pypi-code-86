from gethash.script import gethashcli, script_main

META = {
    "cmdname": "sha3-512",
    "hashname": "SHA3-512",
    "suffix": ".sha3_512",
    "package": "hashlib",
    "hasher": "sha3_512",
}


@gethashcli(**META)
def main(files, **kwargs):
    """Generate or check SHA3-512."""

    from hashlib import sha3_512 as H

    script_main(H(), files, **kwargs)


if __name__ == "__main__":
    main()
