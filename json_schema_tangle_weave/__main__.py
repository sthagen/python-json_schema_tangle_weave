# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring
import sys

from json_schema_tangle_weave.cli import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))  # pragma: no cover
