import pytest

from app import App

@pytest.fixture
def my_app():
    return App()

