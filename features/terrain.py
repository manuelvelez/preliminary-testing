from lettuce import before, world, after
from selenium import webdriver
import time
import os

@before.each_feature
def setup_browser(feature):
    try:
        world.valo_url = os.environ['VALO_SMOKE_URL']
    except KeyError:
        print "Please set the environment variable VALO_SMOKE_URL"
        assert False, "Please set the environment variable VALO_SMOKE_URL"

    try:
        world.ikabo_binary_path = os.environ['IKABO_PATH']
    except KeyError:
        print "Please set the environment variable IKABO_PATH"
        assert False, "Please set the environment variable IKABO_PATH"

    try:
        world.ikabo_tenant = os.environ['IKABO_TENANT']
    except KeyError:
        print "Please set the environment variable IKABO_TENANT"
        assert False, "Please set the environment IKABO_TENANT"

    opts = webdriver.ChromeOptions()
    opts.binary_location = world.ikabo_binary_path
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
