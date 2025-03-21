import traceback
import os
import shutil

from pathlib import Path

SRC = Path(r"C:\Users\Daniella\Downloads\cocos2d-x-2.2.6\cocos2d-x-2.2.6")
DST = Path(r"E:\cocos2d-x-2.2.3")

def search(folder):
    for f in os.scandir(folder):
        if f.is_dir():
            search(f.path)
        else:
            path = str(f.path)
            if path.endswith(".REMOVED.git-id"):
                #print(path)
                
                rel = os.path.relpath(path.split(".REMOVED.git-id")[0], DST)
                #print(rel)
                copyfrom = os.path.normpath(SRC / rel)
                copyto = os.path.normpath(DST / rel)
                if os.path.exists(copyfrom):
                    shutil.copy(copyfrom, copyto)
                else:
                    print(f"Couldn't find: {rel}")

try:
    search(DST)
except Exception:
    traceback.print_exc()

input()