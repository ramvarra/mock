import sys

from pytest_mock import MockerFixture

from .context import *

def test_basic(my_app: App):
    assert my_app



def test_get_my_loc_value(my_app: App, mocker: MockerFixture):
    mocker.patch('app.App.myip', return_value={'loc': '218.0,-13.3'})
    loc = my_app.get_my_loc()
    assert len(loc) == 2
    assert loc == (218.0, -13.3)


def test_get_my_loc_default(my_app: App, mocker: MockerFixture):
    mocker.patch('app.App.myip', return_value={'loc': '20.0'})
    loc = my_app.get_my_loc()
    assert len(loc) == 2
    assert loc == (20.0, 1.0)

def test_get_my_loc_value_error(my_app: App, mocker: MockerFixture):
    mocker.patch('app.App.myip', return_value={})
    with pytest.raises(ValueError):
        _ = my_app.get_my_loc()

def test_get_my_loc(my_app: App):
    loc = my_app.get_my_loc()
    assert isinstance(loc, tuple)
    assert len(loc) == 2
    assert isinstance(loc[0], float)
    assert isinstance(loc[1], float)

