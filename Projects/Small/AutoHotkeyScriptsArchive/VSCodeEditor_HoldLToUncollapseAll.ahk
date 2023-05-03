; -------------------------------------------------------------------------------------------------------------------------------------
; OVERVIEW


    ; Date created: 28.04.2023
    ; A really short and simple hotkey, I made for editing this repository to be easier - I could easily expand all explorer folds just by holding L (I didn't find any direct way to do that)

    
; -------------------------------------------------------------------------------------------------------------------------------------


#Requires AutoHotkey v2.0


; Because the only key USED IN THIS SCRIPT, that can interact with the "Do You want to save changes" window is SPACE, then 99% the not closed editor tabs' changes are going to be saved.
MsgBox "CLOSE ALL EDITOR WINDOWS UNLESS YOU WANT TO SUFFER THE CONSEQUENCES"


UserHasBeenWarned := 0


UncollapseOnce() {
    Send "{Ctrl Down}w{Ctrl Up}{Space}{Ctrl Down}w{Ctrl Up}"
    Sleep 100
    Send "{Ctrl Down}w{Ctrl Up}{Down}{Ctrl Down}w{Ctrl Up}"
    Sleep 100
}


#MaxThreadsPerHotkey 1
l:: {
    global UserHasBeenWarned
    if UserHasBeenWarned = 0 {
        MsgBox "CLOSE ALL EDITOR WINDOWS UNLESS YOU WANT TO SUFFER THE CONSEQUENCES; If You didn't - Stop holding L; If You did - Press Enter"
        UserHasBeenWarned := 1
    }

    loop {
        if GetKeyState("l") {
            UncollapseOnce()
        }

        else {
            UserHasBeenWarned := 0
            break
        }
    }
}


Esc:: ExitApp