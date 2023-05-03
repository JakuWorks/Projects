; -------------------------------------------------------------------------------------------------------------------------------------
; OVERVIEW


    ; Date created: 28.04.2023
    ; A really short and simple hotkey, I made for editing this repository to be easier - I could easily expand all explorer folds just by holding L (I didn't find any direct way to do that)

    
; -------------------------------------------------------------------------------------------------------------------------------------


#Requires AutoHotkey v2.0


; L - Open all folds; Detailed guide:
; 1. (optional) Close all editor tabs (or there'll be a havoc in them)
; 2. Collapse all Editor Folds (i.e. with the collapse all button or CTRL+P - ">Collapse Folders in Explorer")
; 3. Select the editor tab You want to start with (expand it and all below it, unless You stop holding L) 
; 4. Make sure the editor tab You want to start with is collapsed
; 5. Hold L until You expand everyting You want
#MaxThreadsPerHotkey 1
l:: {
    Send "{Ctrl Down}w{Ctrl Up}{Space}{Ctrl Down}w{Ctrl Up}"
    Sleep 100
    Send "{Ctrl Down}w{Ctrl Up}{Down}{Ctrl Down}w{Ctrl Up}"
    Sleep 100
}


Esc:: ExitApp