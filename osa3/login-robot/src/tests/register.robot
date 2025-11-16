*** Settings ***
Resource  resource.robot
Test Setup  Input New Commando

*** Test Cases ***
Register With Valid Username And Password
    Create User  kalle  kalle123
    Input Login Command
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

# Register With Already Taken Username And Valid Password
# ...

Register With Too Short Username And Valid Password
    Create User  ka  kalle123
    Output Should Contain  Käyttäjätunnuksen pituus on oltava vähintään 3 merkkiä.

Register With Enough Long But Invalid Username And Valid Password
    Create User  kalle!  kalle123
    Output Should Contain  Käyttäjätunnuksen on oltava merkeistä a-z koostuva.

Register With Valid Username And Too Short Password
    Create User  kalle  ka
    Output Should Contain  Salasanan on oltava pituudeltaan vähintään 8 merkkiä.

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  kalle  kallekalle
    Output Should Contain  Salasanassa on oltava vähintään 1 ei-kirjain merkki.


*** Keywords ***
Input New Commando
    Input New Command