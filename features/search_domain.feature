Feature: Search on domain and templates screen

@search
  Scenario: Search on domain screen work correctly
    Given I am on Tutorial screen
    And   I tap close button
    Then  I am on Start screen
    When  I tap "Create account" button
    Then  I am on Pin Code screen
    When  I enter random code on Pin Code screen
    And   I tap "Log in" button on Pin Code screen
    Then  I wait when loader disappeared
    And   I am on Wallet Info screen
    When  I tap "Next" button
    Then  I wait when loader disappeared
    And   I am on Main screen
    When  I tap on Docs tab
    And   I tap on "Add doc" button
    Then  I verify Choose Domen screen
    When  I tap search button
    And   I enter "РОССИЙСКАЯ ФЕДЕРАЦИЯ" in search field
    And   Scroll to a particular domain
    Then  I verify "РОССИЙСКАЯ ФЕДЕРАЦИЯ" on screen
    When  I tap clear button
    Then   I enter "12345" in search field
#    Then  I verify screen has message "Ничего не найдено" https://midhub.atlassian.net/browse/MHNEW-922
    When  I tap clear button
    And   I enter "SP" in search field
    And   Scroll to a particular domain
    And   I choose "Spain" option on Choose Domen screen
    Then  I verify following elements in list on Add Doc screen
        | name                               | value |
        | Documento nacional de identidad    | Free  |
        | PASAPORTE (ESP)                    | Free  |
        | Driving Licence                    | Free  |
    When  I tap system back button
    Then  I verify "Spain" on screen
    When  I tap clear button
    Then  I verify text in search field
