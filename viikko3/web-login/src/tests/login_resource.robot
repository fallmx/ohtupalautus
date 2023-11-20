*** Settings ***
Resource  resource.robot

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Go To Login Page
    Go To  ${LOGIN_URL}

Submit Login
    Click Button  Login

Login Page Should Be Open
    Title Should Be  Login
