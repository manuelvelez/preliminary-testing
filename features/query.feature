Feature: Fred creates a domain

  Scenario: create a query in a contextualized notebook
    Given ikabo is opened
    When I configure valo with "192.168.34.185:8888"
    And I Configure the tenant with "demo"
    And click start button
    And create a domain in "smoke-dom-coll" called "test-domain"
    And create a contextualized notebook in the domain "test-domain" of collection "smoke-dom-coll" called "NC-smoke" in "smoke-not-coll"
    And add a query field
    And perform the following "from /streams/demo/infrastructure/cpu" query
    Then the notebook "NC-smoke" is saved in "smoke-not-coll" and contextualized to "test-domain"
    And the query is run
    And table is shown
    And chart "table line sparklines scatterplot column" buttons are shown

  Scenario: create a query in an uncontextualized notebook
    Given ikabo is opened
    When I create an uncontextualized notebook called "N-smoke" in "smoke-not-coll"
    And add a query field
    And perform the following "from /streams/demo/infrastructure/cpu" query
    Then the notebook "NC-smoke" is saved in "smoke-not-coll" and contextualized to ""
    And the query is run
    And table is shown
    And chart "table line sparklines scatterplot column" buttons are shown