# -*- coding: utf-8 -*-
import py
import pytest

def test_import():
    import _maix
    print(_maix.help())
    tmp = _maix.Camera()
    print(tmp.rgb2jpg(b"\xff"*640*480*3))
