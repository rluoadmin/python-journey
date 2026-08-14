from unittest import mock

from source import cal

import pytest

# def test_add():
#     result = add(1, 2)
#     assert result == 3


# @pytest.mark.parametrize("a, b, result", [(1, 1, 2), (2, 3, 5)])
# def test_add2(a, b, result):
#     assert add(a, b) == result


@mock.patch("source.cal.add")
def test_add3(mock_add):
    mock_add.return_value = 4
    result = cal.add(1, 1)
    assert result == 2
