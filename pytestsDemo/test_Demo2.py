import pytest


@pytest.mark.smoke #custome mark
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed, because string are not matching"

def test_secondCCard(): #
    a = 5
    b = 7
    c = a+b
    assert c == 12, "Test failed, because addition is not matching"



