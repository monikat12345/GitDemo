import pytest

@pytest.mark.xfail
def test_firstProgram():
    print("hello lovely world")


@pytest.mark.smoke #custome mark
def test_secondDCard(setup):
    print("day night")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])