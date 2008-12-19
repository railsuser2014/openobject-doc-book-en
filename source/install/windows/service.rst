
Windows Service installation for TinyERP Server Source Installation
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

HowTo start tinyerp-server (v4.2.2) as Service from source installation on Win2003 server.

(There's also a commandline tool called 'sc'. Just execute it on commandline to see how it works. If you don't want to use it, try the following steps:)

  1. download "Windows Server 2003 Resource Kit Tools" http://www.microsoft.com/downloads/details.aspx?FamilyID=9D467A69-57FF-4AE7-96EE-B18C4790CFFD&displaylang=en
  2. execute in command prompt instsrv.exe "TinyService" "C:\Program Files\Windows Resource Kits\Tools\srvany.exe"
     you'll get the message The service was successfully added
     Have a close look at how the quotes are set for the path to srvany.exe. If you get an error saying Code: The fully qualified path to the .EXE must be given
     then this might be due to problems of instsrv of dealing with spaces in pathnames. Just copy instsrv.exe and srvany.exe to temp-folder without spaces and try again.
  3. open regedit and go to [``HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\TinyService``] key. Rightclick on it, New->Key, name it "Parameters".
  4. select the newly created key and right click in the right pane. New->String Value. Name it "Application".
  5. double-click your new "Application" key, enter <path to python>python.exe <path to tinyserver\bin>tinyerp-server.py and save it. The service is now ready to run.
  6. test it from within the Control Panel->Administrator Tools->Services. You will see the service "TinyService" now listed and you can start it 

