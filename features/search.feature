Feature: Fred executes a search

  Scenario: create a search in a contextualized notebook
    Given ikabo is opened
    When I configure valo with "192.168.34.185:8888"
    And I Configure the tenant with "demo"
    And click start button
    And create a domain in "smoke-dom-coll" called "test-domain"
    And create a contextualized notebook in the domain "test-domain" of collection "smoke-dom-coll" called "NC-smoke" in "smoke-not-coll"
    And add a search field
    And perform an "404" search
    Then the notebook "NC-smoke" is saved in "smoke-not-coll" and contextualized to "test-domain"
    And the search is executed
    And data is shown
    And taxonomies are shown