import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I am at the end")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return["My", "Name", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "MyChrome", "MyBrowser"), ("Firefox","MyFirefoxbrowser"), "IE"])
def crossBrowser(request):
    return request.param

