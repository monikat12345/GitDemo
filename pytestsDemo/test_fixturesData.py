import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        #print(dataLoad)
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])

        print(dataLoad[1])
        print(dataLoad[2])
