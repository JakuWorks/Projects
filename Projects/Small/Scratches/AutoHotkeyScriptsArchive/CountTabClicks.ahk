; -------------------------------------------------------------------------------------------------------------------------------------
; OVERVIEW


    ; Date created: 28.04.2023
    ; This is a simple AutoHotkey v2.0 script I made to count all my passwords entries.


; -------------------------------------------------------------------------------------------------------------------------------------


#Requires AutoHotkey v2.0


Count := 0


; TAB - Count +1
#MaxThreadsPerHotkey 1 
$Tab:: {
    global Count := Count + 1
    SendInput "{Tab}"
}


; C - MsgBox(Count) and Count := 0
C:: {
    Global Count
    MsgBox Count + 1 ; +1, because You 'start' from 1 while tabbing
    Count := 0
}


; Emergency Exit
+Esc:: {
    ExitApp
}