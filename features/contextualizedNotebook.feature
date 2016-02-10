Feature: Fred creates a domain

  Scenario: create a contextualized menu
    Given ikabo is opened
    When I configure valo url
    And I Configure the tenant string
    And click start button
    And create a domain in "smoke-dom-coll" called "test-domain"
    And create a contextualized notebook in the domain "test-domain" of collection "smoke-dom-coll" called "NC-smoke" in "smoke-not-coll"
    Then the notebook "NC-smoke" is saved in "smoke-not-coll" and contextualized to "test-domain"