; -------------------------------------------------------------------------------------------------------------------------------------
; OVERVIEW

 
    ; Date created: from  15.01.2023  to  28.04.2023 (the day of editing this README)
    ; This is a simple AutoHotkey v2.0 script I put in my startup apps (usually: "DRIVE:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup") to implement simple custom hotkeys I find useful.


; -------------------------------------------------------------------------------------------------------------------------------------
; Setup


#Requires AutoHotkey v2.0


; -------------------------------------------------------------------------------------------------------------------------------------
; Cmd Toolkit


; Run Cmd - Ctrl+LeftAlt+T
^<!t:: {
    Run "cmd.exe"
}


; Run Cmd as Admin - Ctrl+LeftAlt+Shift+T
^<!+t:: {
    Run "C:\Users\Jakub\Desktop\Useful Shortcuts\cmd-admin - Shortcut.lnk"
}


; -------------------------------------------------------------------------------------------------------------------------------------
; PowerShell Toolkit


; Run PowerShell - Ctrl+LeftAlt+P
^<!p:: {
    Run "Powershell.exe"
}


; Run PowerShell as Admin - Ctrl+LeftAlt+Shift+P
^<!+p:: {
    Run "C:\Users\Jakub\Desktop\Useful Shortcuts\Windows PowerShell (x86) - Admin.lnk"
}


; -------------------------------------------------------------------------------------------------------------------------------------
; Notepad Toolkit


; Run notepad - Ctrl+LeftAlt+N
^<!n:: {
    Run "notepad.exe"
}


; -------------------------------------------------------------------------------------------------------------------------------------