Feature: Fred creates a contributor type

  Scenario: create contributor type using YAML
    Given ikabo is opened
    When I configure valo url
    And I Configure the tenant string
    And click start button
    And I click on add new contributor type
    And create a contributor type with name "ContribTypeJSON" and schema stored in "schemas/contribType.json"
    Then the new contributor type with name "ContribTypeJSON" is created