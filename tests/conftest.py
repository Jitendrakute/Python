import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from TestData.HomePageData import HomePageData

driver = None


#Command Line options to set browser name to test website
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



@pytest.fixture(scope="class")
def setup(request):                 #request is an instance for our fixture, thats come by default

    browser_name=request.config.getoption("browser_name")

    if browser_name == "chrome":
       driver_path = r"D:\SOFT\WEBDRIVERS\chromedriver-win64\chromedriver.exe"
       service = Service(driver_path)
       driver = webdriver.Chrome(service=service)

    elif browser_name == "IE":
        driver_path = r"D:\SOFT\WEBDRIVERS\Edge Webdriver\msedgedriver.exe"
        service=Service(driver_path)
        driver = webdriver.Edge(service=service)

    elif browser_name == "firefox":
        driver_path = r"D:\SOFT\WEBDRIVERS\Firefox Webdriver\geckodriver.exe"
        service = Service(driver_path)
        driver = webdriver.Firefox(service=service)

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver

    yield
    driver.close()

# ============== to data which is send by pycharm itself which is used in HomePageata.py

# @pytest.fixture(params=HomePageData.test_HomePage_data)
# def getData(request):
#     return request.param

# ============== to data which fecth from excel sheet and send it to form

@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
def getData(request):
    return request.param

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

@pytest.mark.skip
def abc():
    pass