import pytest
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture(self):
        print("I will be executing steps in fixtureDemo method")

    def test_fixture1(self):
        print("I will be executing steps in fixtureDemo 1 method")

    def test_fixture2(self):
        print("I will be executing steps in fixtureDemo 2 method")

    def test_fixture3(self):
        print("I will be executing steps in fixtureDemo 3 method")