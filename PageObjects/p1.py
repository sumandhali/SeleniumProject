import pytest


@pytest.fixture
def setup():
    print("this statement will execute before the testfunction")
    yield
    print("this statement will execute after testfunction")

@pytest.mark.usefixtures("setup")
def test_add(setup):
    print(5+5)