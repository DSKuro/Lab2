import pytest
from classes.wallpaper import Wallpaper
from classes.laminate import Laminate
from classes.bar import Bar

def test_wallpaper():
    wp = Wallpaper(10.0, 10.0, 5, (255, 0, 255))
    wp.calculate_cost(500)
    assert isinstance(wp, Wallpaper) == True
    assert wp.get_count == 5
    assert wp.get_cost == 25

def test_laminate():
    lm = Laminate(5.0, 5.0, 3.0)
    lm.calculate_cost(400)
    assert isinstance(lm, Laminate)
    assert lm.get_count == 16
    assert lm.get_cost == 48.0

def test_bar():
    bar = Bar(1, 1, 2)
    bar.calculate_cost(50)
    assert isinstance(bar, Bar)
    assert bar.get_count == 50
    assert bar.get_cost == 100.0
