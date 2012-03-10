Feature: index

Just check that the main page loads properly

     Scenario: Load the Index
     When I access the url "/"
     Then the page title is "Faktum"
