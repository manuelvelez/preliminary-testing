from lettuce import *
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

@step(u'Given ikabo is opened')
def given_ikabo_is_opened(step):
	time.sleep(2)

@step(u'When I configure valo with "([^"]*)"')
def when_i_configure_valo_with_group1(step, group1):
	valoUrl = world.driver.find_element_by_css_selector('[data-type=valoLocation]')
	valoUrl.clear()
	valoUrl.send_keys(group1)

@step(u'And I Configure the tenant with "([^"]*)"')
def and_i_configure_the_tenant_with_group1(step, group1):
	valoTenant = world.driver.find_element_by_css_selector('[data-type=valoTenant]')
	valoTenant.clear()
	valoTenant.send_keys(group1)

@step(u'And click start button')
def and_click_start_button(step):
	world.driver.find_element_by_css_selector('[data-type=save-config]').click()

@step(u'Then I can see the main screen with "([^"]*)" and "([^"]*)"')
def then_i_can_see_the_main_screen_with(step, url, tenant):
	time.sleep(1)

	configElement = world.driver.find_element_by_xpath('//*[@id="mod-user-1"]/div[@data-id="profile"]').text
	assert configElement == url + " " + tenant

	streamLists = world.driver.find_elements_by_css_selector("[class=description]")
	assert len(streamLists) > 0


@step(u'And create a domain in "([^"]*)" called "([^"]*)"')
def and_create_a_domain_in_group1_called_group2(step, group1, group2):
    time.sleep(2)
    world.driver.find_element_by_css_selector('[data-type=new-tab]').click()
    time.sleep(2)
    world.driver.find_element_by_xpath('//*[@id="mod-tabs-1"]/div/div/div[1]').click()

    #time.sleep(10)
    collectionBox = world.driver.find_element_by_css_selector('[data-type=set-domain-collection]')
    collectionBox.clear()
    collectionBox.send_keys(group1)

    nameBox = world.driver.find_element_by_css_selector('[data-type=set-domain-name]')
    nameBox.clear()
    nameBox.send_keys(group2+str(world.scenario_time))

    world.driver.find_element_by_css_selector('[data-type=save-domain]').click()


@step(u'Then the domain "([^"]*)" is saved in "([^"]*)"')
def then_the_domain_group1_is_saved_in_group2(step, group1, group2):
    world.driver.find_element_by_css_selector('[data-id=domains]').click()
    domain_link = world.driver.find_element_by_css_selector('[data-name='+group1+str(world.scenario_time)+']')
    text = " "+group2
    domain_in_collection=world.driver.find_elements_by_xpath('//ul[@class="ui-level2_open"]/li[text()="'+text+'"]/../ul/li[@data-name="'+group1+str(world.scenario_time)+'"]')
    assert len(domain_in_collection) == 1

    domain_in_collection[0].click()
    domain_name = world.driver.find_element_by_css_selector('[data-type=set-page-name]').text
    assert domain_name == group1+str(world.scenario_time)


@step(u'And create an uncontextualized notebook called "([^"]*)" in "([^"]*)"')
def and_create_an_uncontextualized_notebook_called_group1_in_group2(step, group1, group2):
    time.sleep(2)
    world.driver.find_element_by_css_selector('[data-type=new-tab]').click()
    time.sleep(2)
    world.driver.find_element_by_xpath('//*[@id="mod-tabs-1"]/div/div/div[2]').click()

    #time.sleep(10)
    collectionBox = world.driver.find_element_by_css_selector('[data-type=set-notebook-collection]')
    collectionBox.clear()
    collectionBox.send_keys(group2)

    nameBox = world.driver.find_element_by_css_selector('[data-type=set-notebook-name]')
    nameBox.clear()
    nameBox.send_keys(group1+str(world.scenario_time))

    world.driver.find_element_by_css_selector('[data-type=save-notebook]').click()

@step(u'Then the notebook "([^"]*)" is saved in "([^"]*)" and contextualized to "([^"]*)"')
def then_the_notebook_group1_is_saved_in_group2_and_contextualized_to_group3(step, give_notebook_name, given_notebook_collection, given_domain_name):

    scenario_time_str = str(world.scenario_time)
    notebook_name = give_notebook_name + scenario_time_str
    domain_name = given_domain_name + scenario_time_str

    if (given_domain_name == ""):
        notebook_full_name = notebook_name + ' '
    else:
        notebook_full_name = notebook_name + ' (' + domain_name + ')'

    world.driver.find_element_by_css_selector('[data-id=notebooks]').click()
    collection_name = " "+given_notebook_collection
    notebooks_in_collection=world.driver.find_elements_by_xpath('//ul[@class="ui-level2_open"]/li[text()="'+collection_name+'"]/../ul/li/div[text()="'+notebook_full_name+'"]')
    assert len(notebooks_in_collection) == 1


    notebooks_in_collection[0].click()
    notebook_name_in_app = world.driver.find_element_by_xpath('//*[@id="mod-page-notebook-1"]/div/div[1]/div[1]/div[3]/h1').text
    assert notebook_name_in_app == notebook_name

    try:
        button = world.driver.find_element_by_css_selector('[data-popup=cli0]')
    except NoSuchElementException, e:
        print "Element button is not present in notebook page"
        assert False, "Element button is not present in notebook page"


@step(u'And create a contextualized notebook in the domain "([^"]*)" of collection "([^"]*)" called "([^"]*)" in "([^"]*)"')
def and_create_a_contextualized_notebook_in_the_domain_group1_of_collection_group2_called_group3_in_group4(step, domain_name, domain_collection, notebook_name, notebook_collection):
    then_the_domain_group1_is_saved_in_group2(step, domain_name, domain_collection)
    world.driver.find_element_by_xpath('//*[@id="mod-domain-detail-notebooks-1"]//div[@data-controller="notebook"]').click()

    collectionBox = world.driver.find_element_by_css_selector('[data-type=set-notebook-collection]')
    collectionBox.clear()
    collectionBox.send_keys(notebook_collection)

    nameBox = world.driver.find_element_by_css_selector('[data-type=set-notebook-name]')
    nameBox.clear()
    nameBox.send_keys(notebook_name+str(world.scenario_time))

    world.driver.find_element_by_css_selector('[data-type=save-notebook]').click()

@step(u'And I click on add new contributor type')
def and_i_click_on_add_new_contributor_type(step):
    time.sleep(1)
    contributor_type_link = world.driver.find_element_by_css_selector('[data-controller=contributor-editor]')
    contributor_box_header = world.driver.find_element_by_xpath('//*[@id="mod-dashboard-detail-streams-contributors-1"]/div/div[3]/div[1]/div/h2')
    hov = ActionChains(world.driver).move_to_element(contributor_box_header)
    hov.perform()
    contributor_type_link.click()

@step(u'And create a contributor type with name "([^"]*)" and schema stored in "([^"]*)"')
def and_create_a_contributor_type_with_name_group1_and_schema_stored_in_group2(step, contributor_type_name, contributor_type_schema_file):
    contributor_type_schema=open(contributor_type_schema_file).read()

    contributor_type_name_test = contributor_type_name + str(world.scenario_time)

    contributor_field = world.driver.find_element_by_css_selector('[data-type=set-collection]')
    contributor_field.clear()
    contributor_field.send_keys(contributor_type_name_test)

    contributor_schema_field = world.driver.find_element_by_css_selector('[class=ace_content]')
    seq = ActionChains(world.driver).move_to_element(contributor_schema_field).click().send_keys(contributor_type_schema)
    seq.perform()

    world.driver.find_element_by_css_selector('[data-type=save]').click()

@step(u'Then the new contributor type with name "([^"]*)" is created')
def then_the_new_contributor_type_is_created(step, contributor_type_name):
    contributor_type_name_test = contributor_type_name + str(world.scenario_time)
    time.sleep(1)
    try:
        contributor_element = world.driver.find_element_by_xpath('//div[text()="' + contributor_type_name_test + '"]')
    except NoSuchElementException, e:
        print "New Contributor type is not created properly"
        assert False, "New Contributor type is not created properly"

