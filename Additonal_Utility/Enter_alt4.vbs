Dim mySendKeys

Set mySendKeys = CreateObject("WScript.Shell")
mySendKeys.SendKeys "{ENTER}"
WScript.Sleep(4000)
mySendKeys.SendKeys "^w"
