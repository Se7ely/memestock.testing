import datetime
import pytest
from GeneralUtilities import BrowserFunctions

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):

    timestamp = datetime.datetime.now().strftime('%H-%M-%S')

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':

        feature_request = item.funcargs['request']

        #driver = feature_request.getfuncargvalue('browser')
        #driver.save_screenshot(BrowserFunctions.screenshots+timestamp+'.png')

        #extra.append(pytest_html.extras.image(BrowserFunctions.screenshots+timestamp+'.png'))

        # always add url to report
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            driver = feature_request.getfixturevalue('Setup')
            driver.save_screenshot(BrowserFunctions.screenshots + timestamp + '.png')

            extra.append(pytest_html.extras.image(BrowserFunctions.screenshots + timestamp + '.png'))

        report.extra = extra