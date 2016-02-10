Feature: Fred clones a domain

  Scenario: clone the domain
    Given ikabo is opened
    When I configure valo url
    And I Configure the tenant string
    And click start button
    And create a domain in "smoke-dom-coll" called "test-domain"
    And create a contextualized notebook in the domain "test-domain" of collection "smoke-dom-coll" called "NC-smoke" in "smoke-not-coll"
    And clone the domain "test-domain" to "cloned-domain"
    Then the domain "cloned-domain" is saved in "smoke-dom-coll"
    And the notebook "NC-smoke" is saved in "smoke-not-coll" and contextualized to "cloned-domain"