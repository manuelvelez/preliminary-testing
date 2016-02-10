Feature: Fred creates a domain

  Scenario: create a domain
    Given ikabo is opened
    When I configure valo url
    And I Configure the tenant string
    And click start button
    And create a domain in "smoke-dom-coll" called "test-domain"
    Then the domain "test-domain" is saved in "smoke-dom-coll"