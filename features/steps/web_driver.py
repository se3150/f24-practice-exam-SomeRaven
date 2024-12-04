from behave import given, when, then 
from selenium.webdriver.support.ui import Select
import time

@given('I open the url "{url}"')
def step_open_url(context, url):
    context.behave_driver.get(url)

