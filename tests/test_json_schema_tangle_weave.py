# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import json
import pytest  # type: ignore

import json_schema_tangle_weave.json_schema_tangle_weave as lp


def test_weave_ok_json():
    job = ['name_of_schema.json']
    assert lp.weave(job) is None


def test_tangle_ok_json_md():
    job = ['name_of_prose.json.md']
    assert lp.tangle(job) is None
