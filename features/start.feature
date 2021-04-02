@start
Feature: Start

@tutorial
Scenario: Tutorial screen contains three screen and can be closed successfully
    Given I am on the first Tutorial screen
    Then  I verify first Tutorial screen
    When  I tap Next button
    Then  I verify second Tutorial screen
    When  I swipe to the next Tutorial screen
    Then  I verify third Tutorial screen
    When  I tap Next button
    Then  I verify Start screen

@main
Scenario: User can open wallet screen and copy wallet address
    Given I am on the first Tutorial screen
    And   I tap close button
    Then  I verify Start screen
    When  I tap "Create account" button
    Then  I verify Pin Code screen
    When  I enter random code on Pin Code screen
    And   I tap "Log in" button on Pin Code screen
    Then  I wait when loader disappeared
    And   I verify Wallet Info screen
    When  I tap "Next" button
    Then  I wait when loader disappeared
    And   I am on Main screen
    When  I tap on Wallet tab
    Then  I am on Wallet screen
    When  I tap "Top up" button
    Then  I am on Top Up Info screen
    When  I tap "Copy" button
    Then  I verify "Wallet address" toast
