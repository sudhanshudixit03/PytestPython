Feature: Order Transaction
    test related to order transactions


#for sending some data into scenario like username and password we should use 'scenario Outline'

  Scenario Outline: Verify order success message shown in details page
    Given place the item order with <username> and <password>
    And the user is on landing page
    When I login to portal with <username> and <password>
    And navigate to order page
    And select the orderId
    Then order message is successfully displayed
    Examples:
      | username                      | password |
      | sudhanshudixit078@gmail.com   | Sud@1234 |


