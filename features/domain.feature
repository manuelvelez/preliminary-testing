Feature: Fred creates a domain
Scenario: open ikabo
  Given ikabo is opened
  When I configure valo with "192.168.34.185:8888"
  And I Configure the tenant with "demo"
  And click start button
  And create a domain in "smoke-dom-coll" called "test-domain"
  Then the domain "test-domain" is saved in "smoke-dom-coll"