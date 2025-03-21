cmake_minimum_required(VERSION 3.31.5)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(cocos2d VERSION 0.1.0)

#libcocos2d
add_library(libcocos2d SHARED
    cocos2dx/base_nodes/CCAtlasNode.cpp
    cocos2dx/base_nodes/CCNode.cpp
    cocos2dx/ccFPSImages.c
    cocos2dx/cocoa/CCAffineTransform.cpp
    cocos2dx/cocoa/CCArray.cpp
    cocos2dx/cocoa/CCAutoreleasePool.cpp
    cocos2dx/cocoa/CCDataVisitor.cpp
    cocos2dx/cocoa/CCDictionary.cpp
    cocos2dx/cocoa/CCGeometry.cpp
    cocos2dx/cocoa/CCNS.cpp
    cocos2dx/cocoa/CCObject.cpp
    cocos2dx/cocoa/CCSet.cpp
    cocos2dx/cocoa/CCString.cpp
    cocos2dx/cocoa/CCZone.cpp
    cocos2dx/draw_nodes/CCDrawingPrimitives.cpp
    cocos2dx/draw_nodes/CCDrawNode.cpp
    cocos2dx/effects/CCGrabber.cpp
    cocos2dx/effects/CCGrid.cpp
    cocos2dx/actions/CCAction.cpp
    cocos2dx/actions/CCActionCamera.cpp
    cocos2dx/actions/CCActionCatmullRom.cpp
    cocos2dx/actions/CCActionEase.cpp
    cocos2dx/actions/CCActionGrid.cpp
    cocos2dx/actions/CCActionGrid3D.cpp
    cocos2dx/actions/CCActionInstant.cpp
    cocos2dx/actions/CCActionInterval.cpp
    cocos2dx/actions/CCActionManager.cpp
    cocos2dx/actions/CCActionPageTurn3D.cpp
    cocos2dx/actions/CCActionProgressTimer.cpp
    cocos2dx/actions/CCActionTiledGrid.cpp
    cocos2dx/actions/CCActionTween.cpp
    cocos2dx/label_nodes/CCLabelAtlas.cpp
    cocos2dx/label_nodes/CCLabelBMFont.cpp
    cocos2dx/label_nodes/CCLabelTTF.cpp
    cocos2dx/layers_scenes_transitions_nodes/CCLayer.cpp
    cocos2dx/layers_scenes_transitions_nodes/CCScene.cpp
    cocos2dx/layers_scenes_transitions_nodes/CCTransition.cpp
    cocos2dx/layers_scenes_transitions_nodes/CCTransitionPageTurn.cpp
    cocos2dx/layers_scenes_transitions_nodes/CCTransitionProgress.cpp
    cocos2dx/menu_nodes/CCMenu.cpp
    cocos2dx/menu_nodes/CCMenuItem.cpp
    cocos2dx/misc_nodes/CCClippingNode.cpp
    cocos2dx/misc_nodes/CCMotionStreak.cpp
    cocos2dx/misc_nodes/CCProgressTimer.cpp
    cocos2dx/misc_nodes/CCRenderTexture.cpp
    cocos2dx/particle_nodes/CCParticleBatchNode.cpp
    cocos2dx/particle_nodes/CCParticleExamples.cpp
    cocos2dx/particle_nodes/CCParticleSystem.cpp
    cocos2dx/particle_nodes/CCParticleSystemQuad.cpp
    cocos2dx/platform/CCEGLViewProtocol.cpp
    cocos2dx/platform/CCFileUtils.cpp
    cocos2dx/platform/CCImageCommonWebp.cpp
    cocos2dx/platform/CCSAXParser.cpp
    cocos2dx/platform/CCThread.cpp
    cocos2dx/platform/platform.cpp
    cocos2dx/platform/win32/CCAccelerometer.cpp
    cocos2dx/platform/win32/CCApplication.cpp
    cocos2dx/platform/win32/CCCommon.cpp
    cocos2dx/platform/win32/CCDevice.cpp
    cocos2dx/platform/win32/CCEGLView.cpp
    cocos2dx/platform/win32/CCFileUtilsWin32.cpp
    cocos2dx/platform/win32/CCImage.cpp
    cocos2dx/platform/win32/CCStdC.cpp
    cocos2dx/shaders/CCGLProgram.cpp
    cocos2dx/shaders/ccGLStateCache.cpp
    cocos2dx/shaders/CCShaderCache.cpp
    cocos2dx/shaders/ccShaders.cpp
    cocos2dx/sprite_nodes/CCAnimation.cpp
    cocos2dx/sprite_nodes/CCAnimationCache.cpp
    cocos2dx/sprite_nodes/CCSprite.cpp
    cocos2dx/sprite_nodes/CCSpriteBatchNode.cpp
    cocos2dx/sprite_nodes/CCSpriteFrame.cpp
    cocos2dx/sprite_nodes/CCSpriteFrameCache.cpp
    cocos2dx/support/base64.cpp
    cocos2dx/support/CCNotificationCenter.cpp
    cocos2dx/support/CCPointExtension.cpp
    cocos2dx/support/CCProfiling.cpp
    cocos2dx/support/ccUTF8.cpp
    cocos2dx/support/ccUtils.cpp
    cocos2dx/support/CCVertex.cpp
    cocos2dx/support/component/CCComponent.cpp
    cocos2dx/support/component/CCComponentContainer.cpp
    cocos2dx/support/tinyxml2/tinyxml2.cpp
    cocos2dx/support/TransformUtils.cpp
    cocos2dx/support/data_support/ccCArray.cpp
    cocos2dx/support/image_support/TGAlib.cpp
    cocos2dx/support/user_default/CCUserDefault.cpp
    cocos2dx/support/zip_support/ioapi.cpp
    cocos2dx/support/zip_support/unzip.cpp
    cocos2dx/support/zip_support/ZipUtils.cpp
    cocos2dx/textures/CCTexture2D.cpp
    cocos2dx/textures/CCTextureAtlas.cpp
    cocos2dx/textures/CCTextureCache.cpp
    cocos2dx/textures/CCTextureETC.cpp
    cocos2dx/textures/CCTexturePVR.cpp
    cocos2dx/tileMap_parallax_nodes/CCParallaxNode.cpp
    cocos2dx/tileMap_parallax_nodes/CCTileMapAtlas.cpp
    cocos2dx/tileMap_parallax_nodes/CCTMXLayer.cpp
    cocos2dx/tileMap_parallax_nodes/CCTMXObjectGroup.cpp
    cocos2dx/tileMap_parallax_nodes/CCTMXTiledMap.cpp
    cocos2dx/tileMap_parallax_nodes/CCTMXXMLParser.cpp
    cocos2dx/touch_dispatcher/CCTouch.cpp
    cocos2dx/touch_dispatcher/CCTouchDispatcher.cpp
    cocos2dx/touch_dispatcher/CCTouchHandler.cpp
    cocos2dx/keypad_dispatcher/CCKeypadDelegate.cpp
    cocos2dx/keypad_dispatcher/CCKeypadDispatcher.cpp
    cocos2dx/text_input_node/CCIMEDispatcher.cpp
    cocos2dx/text_input_node/CCTextFieldTTF.cpp
    cocos2dx/script_support/CCScriptSupport.cpp
    cocos2dx/kazmath/src/aabb.c
    cocos2dx/kazmath/src/mat3.c
    cocos2dx/kazmath/src/mat4.c
    cocos2dx/kazmath/src/neon_matrix_impl.c
    cocos2dx/kazmath/src/plane.c
    cocos2dx/kazmath/src/quaternion.c
    cocos2dx/kazmath/src/ray2.c
    cocos2dx/kazmath/src/utility.c
    cocos2dx/kazmath/src/vec2.c
    cocos2dx/kazmath/src/vec3.c
    cocos2dx/kazmath/src/vec4.c
    cocos2dx/kazmath/src/GL/mat4stack.c
    cocos2dx/kazmath/src/GL/matrix.c
    cocos2dx/CCCamera.cpp
    cocos2dx/CCConfiguration.cpp
    cocos2dx/CCDirector.cpp
    cocos2dx/CCScheduler.cpp
    cocos2dx/cocos2d.cpp
)

target_include_directories(libcocos2d PUBLIC
    cocos2dx
    cocos2dx/platform/win32
    cocos2dx/platform/third_party/win32/iconv
    cocos2dx/platform/third_party/win32/zlib
    cocos2dx/platform/third_party/win32/libpng
    cocos2dx/platform/third_party/win32/libjpeg
    cocos2dx/platform/third_party/win32/libtiff
    cocos2dx/platform/third_party/win32/libwebp
    cocos2dx/platform/third_party/win32/pthread
    cocos2dx/platform/third_party/win32/OGLES
    cocos2dx/include
    cocos2dx/kazmath/include
)

target_link_libraries(libcocos2d
    #${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/legacy_stdio_definitions.lib
    #cocos2dx/platform/third_party/win32/libraries/opengl32.lib
    opengl32
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/glew32.lib
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/libzlib.lib
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/libpng.lib
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/libjpeg.lib
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/libtiff.lib
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/libwebp.lib
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/libiconv.lib
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/pthreadVCE2.lib
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/ucrtd.lib  # debug
)

target_compile_definitions(libcocos2d PRIVATE
    WIN32
    _DEBUG
    _WINDOWS
    _USRDLL
    COCOS2DXWIN32_EXPORTS
    GL_GLEXT_PROTOTYPES
    COCOS2D_DEBUG=1
    _CRT_SECURE_NO_WARNINGS
    _SCL_SECURE_NO_WARNINGS
)

# hello cpp
add_executable(HelloCppwin32 WIN32
    samples/Cpp/HelloCpp/Classes/AppDelegate.cpp
    samples/Cpp/HelloCpp/Classes/HelloWorldScene.cpp
    samples/Cpp/HelloCpp/proj.win32/main.cpp
)

target_include_directories(HelloCppwin32 PUBLIC
    cocos2dx
    cocos2dx/include
    cocos2dx/kazmath/include
    cocos2dx/platform/win32
    cocos2dx/platform/third_party/win32/OGLES
    samples/Cpp/HelloCpp/Classes
)

target_link_libraries(HelloCppwin32
    opengl32
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/glew32.lib
    libcocos2d
)

target_compile_definitions(HelloCppwin32 PRIVATE
    WIN32
    _DEBUG
    _WINDOWS
    COCOS2D_DEBUG=1
    _CRT_SECURE_NO_WARNINGS
    _SCL_SECURE_NO_WARNINGS   
)
