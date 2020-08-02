#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Add logical documentation here later TODO."""
import os
import sys

from json_schema_tangle_weave.json_schema_tangle_weave import tangle, weave

DEBUG = os.getenv("JSON_SCHEMA_TANGLE_WEAVE_DEBUG")


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Process ... TODO."""
    argv = sys.argv[1:] if argv is None else argv
    verbose = True if "-v" in argv or "--verbose" in argv else False
    verbose and print(f"No verbose mode implemented")
    if argv[0].endswith(".json"):
        weave(argv)
    elif argv[0].endswith(".json.md"):
        tangle(argv)
    else:
        return 1
    return 0
