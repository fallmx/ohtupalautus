*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  jarmo
    Set Password And Confirmation  jarmo123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ja
    Set Password And Confirmation  jarmo123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Invalid Password
    Set Username  mikko
    Set Password And Confirmation  mikkomies
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  pertti
    Set Password  pertti123
    Set Password Confirmation  pretti123
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

*** Keywords ***
Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Set Password And Confirmation
    [Arguments]  ${password}
    Set Password  ${password}
    Set Password Confirmation  ${password}
