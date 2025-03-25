import os
import traceback

from fgen import gen_files

THINGS = """PlayLayer/cocos2d::CCLayer
GameObject/CCSpritePlus
CCSpritePlus/cocos2d::CCSprite
StartPosObject/GameObject
SpeedObject/cocos2d::CCObject
SongObject/cocos2d::CCObject
RingObject/GameObject
PlayerObject/GameObject
PlayerCheckpoint/cocos2d::CCNode
PauseLayer/cocos2d::CCBlockLayer
GameSoundManager/cocos2d::CCNode
EndPortalObject/GameObject
CheckpointObject/cocos2d::CCNode"""

try:
    for thing in THINGS.split("\n"):
        classname, include = thing.split("/")
        if include.startswith("cocos2d::"):
            headers = []
        else:
            headers = [f"gj/{include}"]
        cpp, h = gen_files(classname, include, headers)
        
        cname, hname = f"{classname}.cpp", f"{classname}.h"
        if not os.path.exists(cname) and not os.path.exists(hname):
            with open(cname, "w") as f:
                f.write(cpp)
            
            with open(hname, "w") as f:
                f.write(h)
        
except Exception:
    traceback.print_exc()

input("now imagine a bus")
    