from source.calClass import Cal

import pytest


def test_add(create):
    assert create.add(1, 1) == 2
