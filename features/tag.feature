Feature: Fred creates a tag

  Scenario: clone the domain
    Given ikabo is opened
    When I configure valo with "192.168.34.173:8888"
    And I Configure the tenant with "demo"
    And click start button
    And open the "cpu" stream editor from "infrastructure" collection
    And create a tag "testTag" with body stored in "schemas/cpu.tag"
    And click on save tags button
    Then the new tag "testTag" is created for "cpu" stream