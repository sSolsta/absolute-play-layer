:: running cmake with vs2022

cmake -A win32 -S . -B "cmakew32" -T v140

cmake --build cmakew32 --config Debug
cmake --build cmakew32 --config Release

set DEST=cmakew32\Release

xcopy dlls\ %DEST% /e /y
xcopy samples\Cpp\HelloCpp\Resources %DEST%\Resources /e /y

