Feature: Happy Path

The path through the application when everything
is entered correctly and nothing goes wrong.

   Scenario: Form Present
     Given I am logged in
     When I access the url "/"
     Then there is an add fact form
     And there is a "title" form field
     And there is a "details" textarea
     And there is a "source name" form field
     And there is a "source URL" form field
     And there is a "add fact" submit button
     
   Scenario: Add Fact
     Given I am logged in
     When I access the url "/"
     And enter "test fact" in the "title" form field
     And enter "some random details" in the "details" textarea
     And enter "some random source" in the "source name" form field
     And enter "http://somerandomurl.com/" in the "source URL" form field
     And press the "add fact" submit button
     Then I access the url "/"
     And there is a Fact with the title "test fact" displayed

