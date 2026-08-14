from source.calClass import Cal

import pytest

# `conftest.py` file can be used to store and make fixtures globally accessible across different test files.
# Pytest fixtures allow creating reusable objects for tests, reducing redundancy and improving maintainability.


@pytest.fixture
def create():
    return Cal()
