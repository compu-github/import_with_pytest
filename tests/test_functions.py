# -*- coding: utf-8 -*-

import builtins
import math

import pytest
import scipy

from import_monster import methods_importer


def test_simple1():
    assert methods_importer("__import__", ["builtins"]).__module__ == builtins.__name__


def test_simple2():
    with pytest.raises(TypeError):
        assert methods_importer(sum, [math, builtins, scipy]).__module__ == builtins.__name__


def test_simple3():
    assert methods_importer("nothing", ["builtins"]) is None
