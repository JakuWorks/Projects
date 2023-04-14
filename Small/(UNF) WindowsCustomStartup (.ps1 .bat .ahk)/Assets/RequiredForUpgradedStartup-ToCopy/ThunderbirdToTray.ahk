#Requires AutoHotkey v2.0

ThunderbirdPath := "C:\Users\Jakub\AppData\Local\Programs\thunderbird.exe"

Run(ThunderbirdPath, , "Max", &ThunderbirdPID)

ThunderbirdHWND := WinWait("ahk_pid" ThunderbirdPID, , 8)

if ThunderbirdHWND != 0 {
    WinMinimize("ahk_id" ThunderbirdHWND) ; ahk_id expects a HWND (handle to window)
}