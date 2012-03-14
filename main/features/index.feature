Feature: index

Just check that the main page loads properly

     Scenario: Load the Index
     When I access the url "/"
     Then the page title is "Faktum: Welcome"

     Scenario: Login Link
     Given I am not logged in
     When I access the url "/"
     Then there is a login link
     And there is no logout link
     And I click on the login link
     Then there is a login form

     Scenario: Logged in
     Given I am logged in
     When I access the url "/"
     Then the text "testuser" is present
     And there is no login link
     And there is a logout link


     
