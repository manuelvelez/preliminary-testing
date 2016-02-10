from lettuce import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

@step(u'Given ikabo is opened')
def given_ikabo_is_opened(step):
	time.sleep(2)

@step(u'When I configure valo url')
def when_i_configure_valo_url(step):
	valoUrl = world.driver.find_element_by_css_selector('[data-type=valoLocation]')
	valoUrl.clear()
	valoUrl.send_keys(world.valo_url)

@step(u'And I Configure the tenant string')
def and_i_configure_the_tenant_string(step):
	valoTenant = world.driver.find_element_by_css_selector('[data-type=valoTenant]')
	valoTenant.clear()
	valoTenant.send_keys(world.ikabo_tenant)

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

    collectionBox = world.driver.find_element_by_css_selector('[data-type=set-domain-collection]')
    collectionBox.clear()
    collectionBox.send_keys(group1)

    nameBox = world.driver.find_element_by_css_selector('[data-type=set-domain-name]')
    nameBox.clear()
    nameBox.send_keys(group2+str(world.scenario_time))

    world.driver.find_element_by_css_selector('[data-type=save-domain]').click()


@step(u'Then the domain "([^"]*)" is saved in "([^"]*)"')
def then_the_domain_group1_is_saved_in_group2(step, group1, group2):
    domain_name_test = group1+str(world.scenario_time)
    world.driver.find_element_by_css_selector('[data-id=domains]').click()
    time.sleep(1)
    domain_link = world.driver.find_element_by_css_selector('[data-name='+group1+str(world.scenario_time)+']')
    text = " "+group2
    domain_in_collection=world.driver.find_elements_by_xpath('//ul[@class="ui-level2_open"]/li[text()="'+text+'"]/../ul/li[@data-name="'+group1+str(world.scenario_time)+'"]')
    assert len(domain_in_collection) == 1
    domain_in_collection[0].click()
    domain_name = world.driver.find_element_by_xpath('//h1[@data-type="set-page-name" and not(ancestor::div[contains(@style,"display: none")])]').text
    assert domain_name == group1+str(world.scenario_time)


@step(u'And create an uncontextualized notebook called "([^"]*)" in "([^"]*)"')
def and_create_an_uncontextualized_notebook_called_group1_in_group2(step, group1, group2):
    time.sleep(2)
    world.driver.find_element_by_css_selector('[data-type=new-tab]').click()
    time.sleep(2)
    world.driver.find_element_by_xpath('//*[@id="mod-tabs-1"]/div/div/div[2]').click()

    time.sleep(2)
    collectionBox = world.driver.find_element_by_xpath('//input[@data-type="set-notebook-collection" and not(ancestor::div[contains(@style,"display: none")])]')
    collectionBox.clear()
    collectionBox.send_keys(group2)
    nameBox = world.driver.find_element_by_xpath('//input[@data-type="set-notebook-name" and not(ancestor::div[contains(@style,"display: none")])]')
    nameBox.clear()
    nameBox.send_keys(group1+str(world.scenario_time))
    world.driver.find_element_by_xpath('//button[@data-type="save-notebook" and not(ancestor::div[contains(@style,"display: none")])]').click()

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
    time.sleep(2)
    collection_name = " "+given_notebook_collection
    notebooks_in_collection=world.driver.find_elements_by_xpath('//ul[@class="ui-level2_open"]/li[text()="'+collection_name+'"]/../ul/li/div[text()="'+notebook_full_name+'"]')
    assert len(notebooks_in_collection) == 1


    notebooks_in_collection[0].click()
    notebook_name_in_app = world.driver.find_element_by_xpath('//h1[@data-type="name" and not(ancestor::div[contains(@style,"display: none")])]').text

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

@step(u'And add a search field')
def and_add_a_search_field(step):
    time.sleep(1)
    world.driver.find_element_by_css_selector('[data-popup=cli0]').click()
    time.sleep(1)
    world.driver.find_element_by_css_selector('[data-panel=search]').click()

@step(u'And perform an "([^"]*)" search')
def and_perform_an_group1_search(step, search_term):
    search_field = world.driver.find_element_by_css_selector('[class=ace_content]')
    time.sleep(1)
    seq = ActionChains(world.driver).move_to_element(search_field).send_keys(search_term)
    seq.perform()

    world.driver.find_element_by_css_selector('[data-type=run-search]').click()

@step(u'And the search is executed')
def and_the_search_is_executed(step):
    time.sleep(1)
    try:
        search_time_element = world.driver.find_element_by_css_selector('[class=ui-panel-controls-btn-time]')
    except NoSuchElementException, e:
        assert False, "Search is not executed"

@step(u'And data is shown')
def and_data_si_shown(step):
    search_result = world.driver.find_element_by_xpath('//*[@data-module="notebook-panel-search"]/div').text.encode('ascii','replace')
    assert search_result.find("No results") == -1

@step(u'And taxonomies are shown')
def and_taxonomies_are_shown(step):
    try:
        world.driver.find_element_by_xpath('//*[@data-module="notebook-panel-search"]/div/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]')
    except NoSuchElementException, e:
        assert False, "No taxonomies are shown in search"

@step(u'And add a query field')
def and_add_a_search_field(step):
    time.sleep(1)
    world.driver.find_element_by_css_selector('[data-popup=cli0]').click()
    time.sleep(1)
    world.driver.find_element_by_css_selector('[data-panel=historical]').click()

@step(u'And perform the following "([^"]*)" query')
def and_perform_the_following_group1_query(step, query_string):
    search_field = world.driver.find_element_by_css_selector('[class=ace_content]')
    time.sleep(1)
    seq = ActionChains(world.driver).move_to_element(search_field).send_keys(query_string)
    seq.perform()

    world.driver.find_element_by_css_selector('[data-type=run-query]').click()

@step(u'And the query is run')
def and_the_query_is_run(step):
    time.sleep(1)
    try:
        query_time_element = world.driver.find_element_by_css_selector('[class=ui-panel-controls-btn-time]')
    except NoSuchElementException, e:
        assert False, "Query is not executed"

@step(u'And table is shown')
def and_table_is_shown(step):
    try:
        query_header_element = world.driver.find_element_by_css_selector('[class=dataTables_scrollHead]')
    except NoSuchElementException, e:
        assert False, "Query header is not shown"

    try:
        query_body_element = world.driver.find_element_by_css_selector('[class=dataTables_scrollHead]')
    except NoSuchElementException, e:
        assert False, "Query body is not shown"

@step(u'And chart "([^"]*)" buttons are shown')
def and_chart_group1_buttons_are_shown(step, buttons_string):
    for button in buttons_string.split():
        try:
            query_time_element = world.driver.find_element_by_css_selector('[id=selector-' + button + ']')
        except NoSuchElementException, e:
            assert False, button + " button is not shown"

@step(u'When I create an uncontextualized notebook called "([^"]*)" in "([^"]*)"')
def when_i_create_an_uncontextualized_notebook_called_group1_in_group2(step, notebook_name, notebook_collection):
    and_create_an_uncontextualized_notebook_called_group1_in_group2(step, notebook_name, notebook_collection)

@step(u'And clone the domain "([^"]*)" to "([^"]*)"')
def and_clone_the_domain_group1_to_group2(step, group1, group2):
    domain_name_test = group1+str(world.scenario_time)
    cloned_domain_name_test = group2+str(world.scenario_time)

    time.sleep(1)
    #world.driver.find_element_by_css_selector(css_selector).click()
    xpath_selector='//a[@title="' + domain_name_test + '"]'

    world.driver.find_element_by_xpath(xpath_selector).click()
    world.driver.find_element_by_css_selector('[data-type=save-domain-as-modal]').click()
    cloning_name_element = world.driver.find_element_by_css_selector('[data-type=cloning-name]')
    cloning_name_element.clear()
    cloning_name_element.send_keys(cloned_domain_name_test)

    world.driver.find_element_by_css_selector('[data-type=include-all-notebooks]').click()
    time.sleep(1)
    world.driver.find_element_by_css_selector('[data-type=save-domain-as]').click()
    time.sleep(1)
    world.driver.find_element_by_css_selector('[data-type=save-domain-as]').click()
    time.sleep(2)

@step(u'And the notebook "([^"]*)" is saved in "([^"]*)" and contextualized to "([^"]*)"')
def and_the_notebook_group1_is_saved_in_group2_and_contextualized_to_group3(step, give_notebook_name, given_notebook_collection, given_domain_name):
    then_the_notebook_group1_is_saved_in_group2_and_contextualized_to_group3(step, give_notebook_name, given_notebook_collection, given_domain_name)

@step(u'And open the "([^"]*)" stream editor from "([^"]*)" collection')
def and_open_the_group1_stream_editor_from_group2_collection(step, stream_name, collection_name):
    time.sleep(1)
    world.driver.find_element_by_css_selector('[data-id=' + collection_name + '-' + stream_name + ']').click()

@step(u'And create a tag "([^"]*)" with body stored in "([^"]*)"')
def and_create_a_tag_group1_with_body_stored_in_group2(step, tag_name, tag_file_name):
    tag_name_test = tag_name+str(world.scenario_time)
    time.sleep(1)
    world.driver.find_element_by_xpath('//a[text()="TAGGING" and not(ancestor::div[contains(@style,"display: none")])]').click()

    try:
        tag_field = world.driver.find_element_by_xpath('//input[@data-type="set-tag-field" and @disabled!=true() and not(ancestor::div[contains(@style,"display: none")])]')
    except NoSuchElementException, e:
        world.driver.find_element_by_xpath('//div[@data-type="set-tag" and not(ancestor::div[contains(@style,"display: none")])]/img').click()
        tag_field = world.driver.find_element_by_xpath('//input[@data-type="set-tag-field" and @disabled!=true() and not(ancestor::div[contains(@style,"display: none")])]')


    tag_field.clear()
    tag_field.send_keys(tag_name_test)

    tag_definition=open(tag_file_name).read()
    body_field = world.driver.find_element_by_xpath('//input[@data-type="set-tag-field" and @disabled!=true() and not(ancestor::div[contains(@style,"display: none")])]//ancestor::div[@class="ui-tagging-panel"]//div[@class="ace_content"]')
    seq = ActionChains(world.driver).move_to_element(body_field).click().send_keys(Keys.ENTER).send_keys("function tag(payload) {}").move_to_element(body_field)
    seq.perform()

    time.sleep(1)

@step(u'And click on save tags button')
def and_click_on_save_tags_button(step):
    world.driver.find_element_by_xpath('//button[@data-type="save-tags"]').click()
    time.sleep(1)

@step(u'Then the new tag "([^"]*)" is created for "([^"]*)" stream')
def then_the_new_tag_group1_is_created_for_group2_stream(step, group1, group2):
    success_text = world.driver.find_element_by_xpath('//div[@class="header" and text()="The stream tags were successfully updated"]')
    assert True, success_text





