from lettuce import before, world, after
from selenium import webdriver
import time
import selenium.webdriver.chrome.service as service
import lettuce_webdriver.webdriver

@before.each_feature
def setup_browser(feature):
    # chrome_path="/opt/ikabo_releases/IKABO-1.0.0-linux-x64-caa40496/IKABO-1.0.0"
    # chrome_path="/opt/ikabo_latest/IKABO-0.1.0"
    chrome_path = "/opt/ikabo_latest/ITRS-Insights"
    opts = webdriver.ChromeOptions()
    opts.binary_location = chrome_path
    world.driver = webdriver.Chrome(chrome_options=opts)

@before.each_scenario
def get_timestamp(feature):
    world.scenario_time=int(time.time())

@after.each_feature
def close_browser(feature):
    world.driver.close()

@after.all
def report(total):
    print "Congratulations, %d of %d scenarios passed!" % (
        total.scenarios_ran,
        total.scenarios_passed
    )
