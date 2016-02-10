Feature: Sarah opens ikabo

  Scenario: open ikabo
    Given ikabo is opened
    When I configure valo url
    And I Configure the tenant string
    And click start button
    Then I can see the main screen with "192.168.34.185:8888" and "demo"