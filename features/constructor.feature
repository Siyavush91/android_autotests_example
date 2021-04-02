# INFO: Template with one text field (СНИЛС)
# INFO: Template with one photo field (Водительские права)
# INFO: Template with a lot of pages and one-two field (Свидетельство о браке)
# INFO: Template with a lot of fields on one page (Заявление на пенсию)
# INFO: Complex templete (Паспорт гражданина РФ)

@constructor
Feature: Constructor

@russian_passport @smoke
Scenario: [Паспорт гражданина РФ] Send filled form to verification
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
    Then  I verify My Docs screen
    And   I verify empty Ready Docs Section
    When  I tap on Checking Docs Tab
    And   I tap on "Add doc" button
    Then  I verify Choose Domen screen
    When  I choose "РОССИЙСКАЯ ФЕДЕРАЦИЯ" option on Choose Domen screen
    Then  I verify Add Doc screen
    And   I verify following elements in list on Add Doc screen
        | name                               | value |
        | Паспорт гражданина РФ              | Free  |
        | Приказ о назначении ген. директора | Free  |
    When  I choose "Паспорт гражданина РФ" option on Add Doc screen
    Then  I verify Verification Type screen
        | attribute    | value                      |
        | header       | Паспорт гражданина РФ      |
    When  I choose global green verification on Verification Type screen
    Then  I verify not supported verification alert
    When  I tap on OK button on not supported verification alert
    And   I choose global yellow verification on Verification Type screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | type         | Text                       |
    And   I verify following fields on Add Doc Form Screen
        | name                    |
        | Фамилия                 |
        | Имя                     |
        | Отчество                |
        | Пол                     |
        | Дата рождения           |
        | Место рождения          |
        | Серия и номер паспорта  |
        | Кем выдан               |
        | Дата выдачи             |
    When  I tap on "Фамилия" field on Add Doc Form Screen
    And   I fill out following fields on Field Screen
        | name                    | value           | type     | after_mask |
        | Фамилия                 | Иванов          | Text     |            |
        | Имя                     | Иван            | Text     |            |
        | Отчество                | Иванович        | Text     |            |
        | Пол                     | М               | Checkbox |            |
        | Дата рождения           | 03.12.1980      | Date     |            |
        | Место рождения          | Россия, Иваново | Text     |            |
        | Серия и номер паспорта  | 4444 44444444   | Text     |            |
        | Кем выдан               | ОВД Иваново     | Text     |            |
        | Дата выдачи             | 01.01.2000      | Date     |            |
    Then I verify following fields on Add Doc Form Screen
        | name                    |
        | Иванов                  |
        | Иван                    |
        | Иванович                |
        | М                       |
        | 03.12.1980              |
        | Россия, Иваново         |
        | 4444 44444444           |
        | ОВД Иваново             |
        | 01.01.2000              |
    When I tap next button on Add Doc Form Screen
    Then I verify Add Doc Form page with following attributes
        | attribute    | value                                                                                |
        | name         | Паспорт гражданина РФ                                                                |
        | type         | Photo                                                                                |
        | photo_header | Фото паспорта                                                                        |
        | photo_hint   | Две фотографии – первая и третья страницы. Края паспорта не должны быть обрезаны.    |
    When I tap Add Photo button
    And  I give all requested permissions
    And  I take a photo
    Then I verify 1 attached photo
    When I attach 1 photos on Attach Doc screen
    Then I verify 2 attached photo
    When I tap on agreement switch
    And  I tap Next button on Attach Doc screen
    Then I verify Request In Progress screen
    When I close Request In Progress screen
    Then I verify My Docs screen
    And  I verify "Паспорт гражданина РФ" doc is in status "Pending"
    When I open "Паспорт гражданина РФ"
    Then I verify Request In Progress screen

@snils
Scenario: [СНИЛС] Mask field matches its mask
    Given I am on Tutorial screen
    And   I tap close button
    Then  I am on Start screen
    When  I tap "Create account" button
    Then  I am on Pin Code screen
    When  I enter "9833" on Pin Code screen
    And   I tap "Log in" button on Pin Code screen
    Then  I wait when loader disappeared
    And   I am on Wallet Info screen
    When  I tap "Next" button
    Then  I wait when loader disappeared
    And   I am on Main screen
    When  I tap on Docs tab
    And   I tap on "Add doc" button
    When  I choose "РОССИЙСКАЯ ФЕДЕРАЦИЯ" option on Choose Domen screen
    When  I choose "СНИЛС" option on Add Doc screen
    And   I choose global yellow verification on Verification Type screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | type         | Text                       |
    And   I verify following fields on Add Doc Form Screen
        | name                    |
        | Номер                   |
    When  I tap on "Номер" field on Add Doc Form Screen
    Then  I verify mask hint "###-###-###-##"
    When  I fill out following fields on Field Screen
        | name                    | value           | type       | after_mask     |
        | Номер                   | 12312312312     | Text       | 123-123-123-12 |
    Then I verify following fields on Add Doc Form Screen
        | name                    |
        | 123-123-123-12          |
    When I tap on agreement switch
    And  I tap Next button on Attach Doc screen
    Then I verify Request In Progress screen

@russian_passport @navigation
Scenario: [Паспорт гражданина РФ] Navigation buttons work correctly
    Given I am on the first Tutorial screen
    And   I tap close button
    Then  I am on Start screen
    When  I tap "Create account" button
    Then  I am on Pin Code screen
    When  I enter "9833" on Pin Code screen
    And   I tap "Log in" button on Pin Code screen
    Then  I wait when loader disappeared
    And   I am on Wallet Info screen
    When  I tap "Next" button
    Then  I wait when loader disappeared
    And   I am on Main screen
    When  I tap on Docs tab
    And   I tap on "Add doc" button
    When  I choose "РОССИЙСКАЯ ФЕДЕРАЦИЯ" option on Choose Domen screen
    And   I choose "Паспорт гражданина РФ" option on Add Doc screen
    And   I tap Details button for yellow verification
    Then  I verify Verification Details screen
    When  I tap back button on Verification Details screen
    When  I tap Details button for yellow verification
    When  I choose verification on Verification Details screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | type         | Text                       |
    When  I tap system back button
    When  I choose global yellow verification on Verification Type screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | type         | Text                       |
    When  I tap on "Фамилия" field on Add Doc Form Screen
    Then  I verify "Фамилия" text field is 1 step out of 9
    When  I tap on previous step button on Field Screen
    Then  I verify "Фамилия" text field is 1 step out of 9
    When  I tap on confirm button on Field Screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Фамилия                 |
    When  I tap on "Пол" field on Add Doc Form Screen
    Then  I verify "Пол" option field is 4 step out of 9
    When  I tap on previous step button on Field Screen
    Then  I verify "Отчество" text field is 3 step out of 9
    When  I fill out following field on Field Screen without confirmation
        | name                    | value           | type     |
        | Отчество                | Иванович        | Text     |
    When  I tap back button on Field Screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Отчество                |
    When  I tap on "Пол" field on Add Doc Form Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     |
        | Пол                     | М               | Checkbox |
    Then  I verify "Дата рождения" date field is 5 step out of 9
    When  I fill out following field on Field Screen without confirmation
        | name                    | value           | type     |
        | Дата рождения           | 21.10.1999      | Date     |
    And   I tap on previous step button on Field Screen
    # TODO: check tick on correct option
    Then  I verify "Пол" option field is 4 step out of 9
    When  I tap on previous step button on Field Screen
    Then  I verify "Отчество" text field is 3 step out of 9
    When  I fill out following field on Field Screen without confirmation
        | name                    | value           | type     |
        | Отчество                | Петрович        | Text     |
    And   I tap on confirm button on Field Screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Фамилия                 |
        | Имя                     |
        | Петрович                |
        | М                       |
        | 21.10.1999              |

@marriage_doc @field_clean
Scenario: [Свидетельство о браке] Field cleans successfully
    Given I am on the first Tutorial screen
    And   I tap close button
    Then  I am on Start screen
    When  I tap "Create account" button
    Then  I am on Pin Code screen
    When  I enter "9833" on Pin Code screen
    And   I tap "Log in" button on Pin Code screen
    Then  I wait when loader disappeared
    And   I am on Wallet Info screen
    When  I tap "Next" button
    Then  I wait when loader disappeared
    And   I am on Main screen
    When  I tap on Docs tab
    And   I tap on Checking Docs Tab
    And   I tap on "Add doc" button
    And   I choose "РОССИЙСКАЯ ФЕДЕРАЦИЯ" option on Choose Domen screen
    And   I choose "Свидетельство о браке" option on Add Doc screen
    And   I choose global yellow verification on Verification Type screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | name         | Свидетельство о браке      |
        | type         | Text                       |
    And   I verify following fields on Add Doc Form Screen
        | name                    |
        | Фамилия мужа            |
        | Имя мужа                |
        | Дата рождения мужа      |
        | Дети мужа               |
        | Номер паспорта          |
    When  I tap on "Фамилия мужа" field on Add Doc Form Screen
    And   I fill out following fields on Field Screen
        | name                    | value           | type     | after_mask |
        | Фамилия мужа            | Иванов          | Text     |            |
        | Имя мужа                | Михаил          | Text     |            |
        | Дата рождения мужа      | 03.12.1980      | Date     |            |
        | Дети мужа               | 5               | Number   |            |
        | Номер паспорта          |                 | Text     |            |
    Then I verify following fields on Add Doc Form Screen
        | name                    |
        | Иванов                  |
        | Михаил                  |
        | 03.12.1980              |
        | 5                       |
        | Номер паспорта          |
    When  I tap on "03.12.1980" field on Add Doc Form Screen
    And   I clean field on Field Screen
    And   I tap on confirm button on Field Screen
    And   I tap on "Михаил" field on Add Doc Form Screen
    And   I clean field on Field Screen
    And   I tap on confirm button on Field Screen
    And   I tap on "5" field on Add Doc Form Screen
    And   I clean field on Field Screen
    And   I tap on confirm button on Field Screen
    # TODO: small bug if uncommented
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Иванов                  |
        | Имя мужа                |
        # | Дата рождения мужа      |
        | Дети мужа               |
        | Номер паспорта          |
    When  I tap on "Имя мужа" field on Add Doc Form Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     | after_mask |
        | Имя мужа                | Игорь           | Text     |            |
    And   I tap on confirm button on Field Screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Иванов                  |
        | Игорь                   |
        # | Дата рождения мужа      |
        | Дети мужа               |
        | Номер паспорта          |
    # When  I tap on "Дата рождения мужа" field on Add Doc Form Screen
    When  I tap on "03.12.1980" field on Add Doc Form Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     | after_mask |
        | Дата рождения мужа      | 09.05.1977      | Date     |            |
    And   I tap on confirm button on Field Screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Иванов                  |
        | Игорь                   |
        | 09.05.1977              |
        | Дети мужа               |
        | Номер паспорта          |
    When  I tap on "Дети мужа" field on Add Doc Form Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     | after_mask |
        | Дети мужа               | 6               | Number   |            |
    And   I tap on confirm button on Field Screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Иванов                  |
        | Игорь                   |
        | 09.05.1977              |
        | 6                       |
        | Номер паспорта          |

@marriage_doc @symbols_number
Scenario: [Свидетельство о браке] Warning about number of symbols displays for proper field
    Given I am on the first Tutorial screen
    And   I tap close button
    Then  I am on Start screen
    When  I tap "Create account" button
    Then  I am on Pin Code screen
    When  I enter "9833" on Pin Code screen
    And   I tap "Log in" button on Pin Code screen
    Then  I wait when loader disappeared
    And   I am on Wallet Info screen
    When  I tap "Next" button
    Then  I wait when loader disappeared
    And   I am on Main screen
    When  I tap on Docs tab
    And   I tap on Checking Docs Tab
    And   I tap on "Add doc" button
    And   I choose "РОССИЙСКАЯ ФЕДЕРАЦИЯ" option on Choose Domen screen
    And   I choose "Свидетельство о браке" option on Add Doc screen
    And   I choose global yellow verification on Verification Type screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Фамилия мужа            |
        | Имя мужа                |
        | Дата рождения мужа      |
        | Дети мужа               |
        | Номер паспорта          |
    When  I tap on "Номер паспорта" field on Add Doc Form Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     | after_mask |
        | Номер паспорта          | 4444 666666     | Text     |            |
    And   I tap on confirm button on Field Screen
    Then  I verify field "4444 666666" has no warning
    When  I tap on "4444 666666" field on Add Doc Form Screen
    And   I clean field on Field Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     | after_mask |
        | Номер паспорта          | 4444 777        | Text     |            |
    And   I tap on confirm button on Field Screen
    Then  I verify field "4444 777" has warning "Недопустимая длина. Требуемое количество символов: 11"
    When  I tap on "4444 777" field on Add Doc Form Screen
    And   I clean field on Field Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     | after_mask |
        | Номер паспорта          | 4444 777777     | Text     |            |
    And   I tap on confirm button on Field Screen
    Then  I verify field "4444 777777" has no warning

@marriage_doc @empty_fields
Scenario: [Свидетельство о браке] Warning for empty fields
    Given I am on the first Tutorial screen
    And   I tap close button
    Then  I am on Start screen
    When  I tap "Create account" button
    Then  I am on Pin Code screen
    When  I enter "9833" on Pin Code screen
    And   I tap "Log in" button on Pin Code screen
    Then  I wait when loader disappeared
    And   I am on Wallet Info screen
    When  I tap "Next" button
    Then  I wait when loader disappeared
    And   I am on Main screen
    When  I tap on Docs tab
    And   I tap on Checking Docs Tab
    And   I tap on "Add doc" button
    And   I choose "РОССИЙСКАЯ ФЕДЕРАЦИЯ" option on Choose Domen screen
    And   I choose "Свидетельство о браке" option on Add Doc screen
    And   I choose global yellow verification on Verification Type screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Фамилия мужа            |
        | Имя мужа                |
        | Дата рождения мужа      |
        | Дети мужа               |
        | Номер паспорта          |
    When  I tap next button on Add Doc Form Screen
    Then  I verify 5 fields have warning "Заполните поле"
    When  I tap on the first field on Add Doc Form Screen
    And   I fill out following fields on Field Screen
        | name                    | value           | type     | after_mask |
        | Фамилия мужа            | Иванов          | Text     |            |
        | Имя мужа                | Михаил          | Text     |            |
        | Дата рождения мужа      | 03.12.1980      | Date     |            |
        | Дети мужа               | 5               | Number   |            |
        | Номер паспорта          | 4444 333333     | Text     |            |
    And   I tap next button on Add Doc Form Screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | name         | Свидетельство о браке      |
        | type         | Photo                      |
        | photo_header | Паспорт мужа               |
    When  I tap back button on Add Doc Form Screen
    Then  I verify all fields have no warning

@marriage_doc @saved_fields
Scenario: [Свидетельство о браке] Fields save their values after different actions
    Given I am on the first Tutorial screen
    And   I tap close button
    Then  I am on Start screen
    When  I tap "Create account" button
    Then  I am on Pin Code screen
    When  I enter "9833" on Pin Code screen
    And   I tap "Log in" button on Pin Code screen
    Then  I wait when loader disappeared
    And   I am on Wallet Info screen
    When  I tap "Next" button
    Then  I wait when loader disappeared
    And   I am on Main screen
    When  I tap on Docs tab
    And   I tap on Checking Docs Tab
    And   I tap on "Add doc" button
    And   I choose "РОССИЙСКАЯ ФЕДЕРАЦИЯ" option on Choose Domen screen
    And   I choose "Свидетельство о браке" option on Add Doc screen
    And   I choose global yellow verification on Verification Type screen
    And   I tap on the first field on Add Doc Form Screen
    And   I fill out following fields on Field Screen
        | name                    | value           | type     | after_mask |
        | Фамилия мужа            | Иванов          | Text     |            |
        | Имя мужа                | Михаил          | Text     |            |
        | Дата рождения мужа      | 03.12.1980      | Date     |            |
        | Дети мужа               | 5               | Number   |            |
        | Номер паспорта          | 4444 333333     | Text     |            |
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Иванов                  |
        | Михаил                  |
        | 03.12.1980              |
        | 5                       |
        | 4444 333333             |
    When  I fold and unfold app
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Иванов                  |
        | Михаил                  |
        | 03.12.1980              |
        | 5                       |
        | 4444 333333             |
    When  I tap next button on Add Doc Form Screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | name         | Свидетельство о браке      |
        | type         | Photo                      |
        | photo_header | Паспорт мужа               |
    When  I tap Add Photo button
    And   I give all requested permissions
    And   I take a photo
    Then  I verify 1 attached photo
    When  I fold and unfold app
    Then  I verify 1 attached photo
    When  I tap back button on Add Doc Form Screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Иванов                  |
        | Михаил                  |
        | 03.12.1980              |
        | 5                       |
        | 4444 333333             |
    When  I tap system back button
    Then  I am on Verification Type screen
    When  I tap system back button
    Then  I am on Add Doc screen
    When  I tap system back button
    # TODO: first back for some reasons doesn't work properly
    And   I tap system back button
    Then  I am on My Docs screen
    When  I tap on "Add doc" button
    And   I choose "РОССИЙСКАЯ ФЕДЕРАЦИЯ" option on Choose Domen screen
    And   I choose "Свидетельство о браке" option on Add Doc screen
    And   I choose global yellow verification on Verification Type screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Иванов                  |
        | Михаил                  |
        | 03.12.1980              |
        | 5                       |
        | 4444 333333             |
    When  I tap next button on Add Doc Form Screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | name         | Свидетельство о браке      |
        | type         | Photo                      |
        | photo_header | Паспорт мужа               |
        | add_photo    | False                      |
    And   I verify 1 attached photo
    When  I tap next button on Add Doc Form Screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | name         | Свидетельство о браке      |
        | type         | Text                       |
    And   I verify following fields on Add Doc Form Screen
        | name                    |
        | Фамилия жены            |
        | Имя жены                |
        | Дата рождения жены      |
        | Дети жены               |
        | Номер паспорта          |
    When  I tap on the first field on Add Doc Form Screen
    And   I fill out following fields on Field Screen
        | name                    | value           | type     | after_mask |
        | Фамилия жены            | Буракова        | Text     |            |
        | Имя жены                | Анна            | Text     |            |
        | Дата рождения жены      | 11.02.1983      | Date     |            |
        | Дети жены               | 5               | Number   |            |
        | Номер паспорта          | 4444 111111     | Text     |            |
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Буракова                |
        | Анна                    |
        | 11.02.1983              |
        | 5                       |
        | 4444 111111             |
    When  I tap next button on Add Doc Form Screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | name         | Свидетельство о браке      |
        | type         | Photo                      |
        | photo_header | Паспорт жены               |
    When  I attach 1 photos on Attach Doc screen
    Then  I verify 1 attached photo
    When  I tap next button on Add Doc Form Screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | name         | Свидетельство о браке      |
        | type         | Photo                      |
        | photo_header | Свидетельство о браке      |
    When  I attach 1 photos on Attach Doc screen
    Then  I verify 1 attached photo
    When  I tap on agreement switch
    And   I tap system back button
    And   I tap system back button
    And   I tap on "5" field on Add Doc Form Screen
    And   I clean field on Field Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     | after_mask |
        | Дети жены               | 0               | Number   |            |
    And   I tap on confirm button on Field Screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Буракова                |
        | Анна                    |
        | 11.02.1983              |
        | 0                       |
        | 4444 111111             |
    When  I tap system back button
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | name         | Свидетельство о браке      |
        | type         | Photo                      |
        | photo_header | Паспорт мужа               |
        | add_photo    | False                      |
    When  I tap Next button on Attach Doc screen
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Буракова                |
        | Анна                    |
        | 11.02.1983              |
        | 0                       |
        | 4444 111111             |
    When  I tap Next button on Attach Doc screen
    And   I tap Next button on Attach Doc screen
    And   I tap on agreement switch
    And   I tap Next button on Attach Doc screen
    Then  I verify Request In Progress screen
    When  I tap system back button
    Then  I verify "Свидетельство о браке" doc is in status "Pending"

@marriage_doc @date_fields
Scenario: [Свидетельство о браке] Date field warnings
    Given I am on the first Tutorial screen
    And   I tap close button
    Then  I am on Start screen
    When  I tap "Create account" button
    Then  I am on Pin Code screen
    When  I enter "9833" on Pin Code screen
    And   I tap "Log in" button on Pin Code screen
    Then  I wait when loader disappeared
    And   I am on Wallet Info screen
    When  I tap "Next" button
    Then  I wait when loader disappeared
    And   I am on Main screen
    When  I tap on Docs tab
    And   I tap on Checking Docs Tab
    And   I tap on "Add doc" button
    And   I choose "РОССИЙСКАЯ ФЕДЕРАЦИЯ" option on Choose Domen screen
    And   I choose "Свидетельство о браке" option on Add Doc screen
    And   I choose global yellow verification on Verification Type screen
    And   I tap on the first field on Add Doc Form Screen
    And   I fill out following fields on Field Screen
        | name                    | value           | type     | after_mask |
        | Фамилия мужа            | Иванов          | Text     |            |
        | Имя мужа                | Михаил          | Text     |            |
        | Дата рождения мужа      | 8989899888      | Date     | 89.89.8998 |
        | Дети мужа               | 5               | Number   |            |
        | Номер паспорта          | 4444 333333     | Text     |            |
    Then  I verify following fields on Add Doc Form Screen
        | name                    |
        | Иванов                  |
        | Михаил                  |
        | 27.05.8998              |
        | 5                       |
        | 4444 333333             |
    When  I tap next button on Add Doc Form Screen
    Then  I verify field "27.05.8998" has warning "Недопустимая дата"
    When  I tap on "27.05.8998" field on Add Doc Form Screen
    And   I clean field on Field Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     | after_mask |
        | Дата рождения мужа      | 1999/03/03      | Date     | 19.99.0303 |
    And   I tap on confirm button on Field Screen
    Then  I verify field "19.03.0303" has warning "Недопустимая дата"
    When  I tap on "19.03.0303" field on Add Doc Form Screen
    And   I clean field on Field Screen
    # TODO: small bug
    # And   I fill out following field on Field Screen without confirmation
    #     | name                    | value           | type     | after_mask |
    #     | Дата рождения мужа      | 01.01.2050      | Date     | 01.01.2050 |
    # And   I tap on confirm button on Field Screen
    # Then  I verify field "01.01.2050" has warning "Недопустимая дата"
    # When  I tap on "01.01.2050" field on Add Doc Form Screen
    # And   I clean field on Field Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     | after_mask |
        | Дата рождения мужа      | 29.02.1943      | Date     | 29.02.1943 |
    And   I tap on confirm button on Field Screen
    Then  I verify field "01.03.1943" has no warning
    When  I tap on "01.03.1943" field on Add Doc Form Screen
    And   I clean field on Field Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     | after_mask |
        | Дата рождения мужа      | 20.02.1800      | Date     | 20.02.1800 |
    And   I tap on confirm button on Field Screen
    Then  I verify field "20.02.1800" has warning "Недопустимая дата"
    When  I tap on "20.02.1800" field on Add Doc Form Screen
    And   I clean field on Field Screen
    And   I fill out following field on Field Screen without confirmation
        | name                    | value           | type     | after_mask |
        | Дата рождения мужа      | 29.02.1980      | Date     | 29.02.1980 |
    And   I tap on confirm button on Field Screen
    Then  I verify all fields have no warning
    When  I tap next button on Add Doc Form Screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | name         | Свидетельство о браке      |
        | type         | Photo                      |
        | photo_header | Паспорт мужа               |

@retirement_doc @agreement
Scenario: [Заявление на пенсию] Agreement is on the multi-field page displays correct and opens browser
    Given I am on the first Tutorial screen
    And   I tap close button
    Then  I am on Start screen
    When  I tap "Create account" button
    Then  I am on Pin Code screen
    When  I enter "9833" on Pin Code screen
    And   I tap "Log in" button on Pin Code screen
    Then  I wait when loader disappeared
    And   I am on Wallet Info screen
    When  I tap "Next" button
    Then  I wait when loader disappeared
    And   I am on Main screen
    When  I tap on Docs tab
    And   I tap on Checking Docs Tab
    And   I tap on "Add doc" button
    And   I choose "РОССИЙСКАЯ ФЕДЕРАЦИЯ" option on Choose Domen screen
    And   I choose "Заявление на пенсию" option on Add Doc screen
    And   I choose global yellow verification on Verification Type screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                      |
        | name         | Заявление на пенсию        |
        | type         | Text                       |
    And   I verify following fields on Add Doc Form Screen
        | name                    |
        | Поле 1                  |
        | Поле 2                  |
        | Поле 3                  |
        | Поле 4                  |
        | Поле 5                  |
        | Поле 6                  |
        | Поле 7                  |
        | Поле 8                  |
        | Поле 9                  |
        | Поле 10                 |
        | Поле 11                 |
        | Поле 12                 |
        | Поле 13                 |
        | Поле 14                 |
        | Поле 15                 |
    When  I scroll down to agreement
    And   I tap on agreement link
    Then  I verify text "https://ya.ru/#pdp" on the screen

@drivers_license @photo
Scenario: [Водительские права] Camera can be closed, photo warning displays correct message
    Given I am on the first Tutorial screen
    And   I tap close button
    Then  I am on Start screen
    When  I tap "Create account" button
    Then  I am on Pin Code screen
    When  I enter "9833" on Pin Code screen
    And   I tap "Log in" button on Pin Code screen
    Then  I wait when loader disappeared
    And   I am on Wallet Info screen
    When  I tap "Next" button
    Then  I wait when loader disappeared
    And   I am on Main screen
    When  I tap on Docs tab
    And   I tap on Checking Docs Tab
    And   I tap on "Add doc" button
    And   I choose "РОССИЙСКАЯ ФЕДЕРАЦИЯ" option on Choose Domen screen
    And   I choose "Водительские права" option on Add Doc screen
    And   I choose global yellow verification on Verification Type screen
    Then  I verify Add Doc Form page with following attributes
        | attribute    | value                                                                                |
        | name         | Водительские права                                                                   |
        | type         | Photo                                                                                |
        | photo_header | Скан документа                                                                       |
    When I tap Add Photo button
    And  I give all requested permissions
    And  I take a photo
    Then I verify 1 attached photo
    When I tap on agreement switch
    And  I tap Next button on Attach Doc screen
    # TODO: change incorrect фотографиЙ
    Then I verify "Добавьте еще 2 фотографий" warning on Attach Doc screen
    When I tap Add Photo button
    Then I am on Camera screen
    When I tap system back button
    Then I verify 1 attached photo
    When I attach 2 photos on Attach Doc screen
    Then I verify 3 attached photo
    When I tap Next button on Attach Doc screen
    Then I wait when loader disappeared on Add Doc Form screen
    When I tap on Ready Docs Tab
    Then I verify "Водительские права" doc is in status "Ready"
