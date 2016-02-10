Feature: Fred creates a domain

  Scenario: create an uncontextualized notebook
    Given ikabo is opened
    When I configure valo url
    And I Configure the tenant string
    And click start button
    And create an uncontextualized notebook called "N-smoke" in "smoke-not-coll"
    Then the notebook "N-smoke" is saved in "smoke-not-coll" and contextualized to ""