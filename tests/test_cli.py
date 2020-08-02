
# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import json
import pytest  # type: ignore

import json_schema_tangle_weave.cli as cli


def test_main_ok_json():
    job = ['name_of_schema.json']
    assert cli.main(job) is 0


def test_main_ok_json_md():
    job = ['name_of_prose.json.md']
    assert cli.main(job) is 0
