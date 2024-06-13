import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching Firefox Browser")
    else:
        driver = webdriver.Ie()
        print("Launching Explorer Browser")
    return driver


def pytest_addoption(parser): # this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############### PyTest HTML Report #########################

# #It is a hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Pavan'
#
# # It is a hook for delete / Modify Environment info to HTML Report
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("plugins",None)