import pytest

@pytest.mark.xfail
def test_firstProgram():
    print("hello")


@pytest.mark.smoke #custome mark
def test_secondDCard(setup):
    print("day")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])