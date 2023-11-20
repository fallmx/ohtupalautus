*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pentti  pentti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  pentti  pentti123
    Input Credentials  pentti  mikko123
    Output Should Contain  User with username pentti already exists

Register With Too Short Username And Valid Password
    Input Credentials  pe  pentti123
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  12345  pentti123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  pentti  pen1234
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pentti  penttimies
    Output Should Contain  Invalid password
