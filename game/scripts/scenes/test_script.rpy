image bg room = "room.jpg"

label test_script:
    $linesToSay = getDialogs()

    scene bg room
    
    "[linesToSay[5]]"

    custom_command "in his head: true"

    with vpunch

    Lars "[linesToSay[6]]"

    Lars "[linesToSay[7]]"

    Lars "[linesToSay[8]]"

    Lars "[linesToSay[9]]"

    custom_command "in his head: false"

    "[linesToSay[11]]"

    Claude "[linesToSay[12]]"
