Feature: Insert a new store into the model
    In order to have stores
    As a store administrator
    I need to insert new stores into the database

    Scenario: Insert new store row
        Given I have the following data to be inserted:
        | name      |   address     |
        | David     |   Cll 35-12   |
        When I access the url '/crudstorecreate/'
        And I fill in "name" with "David"
        And I fill in "address" with "Cll 35-12"
        And I press "send" button'
        Then I should see all stores

