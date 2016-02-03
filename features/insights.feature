Feature: Sarah opens ikabo

Scenario: open ikabo
  Given ikabo is opened
  When I configure valo with "192.168.34.185:8888"
  And I Configure the tenant with "demo"
  And click start button
  Then I can see the main screen with "192.168.34.185:8888" and "demo"