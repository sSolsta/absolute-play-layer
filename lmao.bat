
set VCVARS="C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars32.bat"
set COCOS_SLN=cocos2d-win32.vc2012.lmao.sln

:: piggyback off of envars incase we need them
call %VCVARS%




"C:\Program Files (x86)\MSBuild\12.0\Bin\MSBuild.exe" %COCOS_SLN% /t:Clean
"C:\Program Files (x86)\MSBuild\12.0\Bin\MSBuild.exe" %COCOS_SLN% /p:Configuration="Debug" /p:Platform="Win32" /m
"C:\Program Files (x86)\MSBuild\12.0\Bin\MSBuild.exe" %COCOS_SLN% /p:Configuration="Release" /p:Platform="Win32" /m