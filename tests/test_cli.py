
# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import json
import pytest  # type: ignore

import json_schema_tangle_weave.cli as cli


def test_main_ok_weave():
    job = ['name_of_schema.json']
    assert cli.main(job) is 0
