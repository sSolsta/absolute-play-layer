cmake_minimum_required(VERSION 3.31.5)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(cocos2d VERSION 0.1.0)


#  ================================ libcocos2d ================================

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


#  ================================ libcocosdenshion ================================

add_library(libCocosDenshion SHARED
    CocosDenshion/win32/MciPlayer.cpp
    CocosDenshion/win32/SimpleAudioEngine.cpp
)

target_include_directories(libCocosDenshion PUBLIC
    CocosDenshion/Include
    cocos2dx
    cocos2dx/include
    kazmath/include
    cocos2dx/platform/win32
    cocos2dx/platform/third_party/win32/OGLES
    CocosDenshion/proj.win32
)

target_link_libraries(libCocosDenshion
    winmm
    libcocos2d
)

target_compile_definitions(libCocosDenshion PRIVATE
    WIN32
    _DEBUG
    _WINDOWS
    _USRDLL
    COCOSDENSHIONWIN32_EXPORTS
    _EXPORT_DLL_
)


#  ================================ libextensions ================================

add_library(libExtensions STATIC
    extensions/AssetsManager/AssetsManager.cpp
    extensions/CCBReader/CCBAnimationManager.cpp
    extensions/CCBReader/CCBFileLoader.cpp
    extensions/CCBReader/CCBKeyframe.cpp
    extensions/CCBReader/CCBReader.cpp
    extensions/CCBReader/CCBSequence.cpp
    extensions/CCBReader/CCBSequenceProperty.cpp
    extensions/CCBReader/CCBValue.cpp
    extensions/CCBReader/CCControlButtonLoader.cpp
    extensions/CCBReader/CCControlLoader.cpp
    extensions/CCBReader/CCData.cpp
    extensions/CCBReader/CCLabelBMFontLoader.cpp
    extensions/CCBReader/CCLabelTTFLoader.cpp
    extensions/CCBReader/CCLayerColorLoader.cpp
    extensions/CCBReader/CCLayerGradientLoader.cpp
    extensions/CCBReader/CCLayerLoader.cpp
    extensions/CCBReader/CCMenuItemImageLoader.cpp
    extensions/CCBReader/CCMenuItemLoader.cpp
    extensions/CCBReader/CCNode+CCBRelativePositioning.cpp
    extensions/CCBReader/CCNodeLoader.cpp
    extensions/CCBReader/CCNodeLoaderLibrary.cpp
    extensions/CCBReader/CCParticleSystemQuadLoader.cpp
    extensions/CCBReader/CCScale9SpriteLoader.cpp
    extensions/CCBReader/CCScrollViewLoader.cpp
    extensions/CCBReader/CCSpriteLoader.cpp
    extensions/CocoStudio/Action/CCActionEaseEx.cpp
    extensions/CocoStudio/Action/CCActionFrame.cpp
    extensions/CocoStudio/Action/CCActionFrameEasing.cpp
    extensions/CocoStudio/Action/CCActionManager.cpp
    extensions/CocoStudio/Action/CCActionNode.cpp
    extensions/CocoStudio/Action/CCActionObject.cpp
    extensions/CocoStudio/Armature/animation/CCArmatureAnimation.cpp
    extensions/CocoStudio/Armature/animation/CCProcessBase.cpp
    extensions/CocoStudio/Armature/animation/CCTween.cpp
    extensions/CocoStudio/Armature/CCArmature.cpp
    extensions/CocoStudio/Armature/CCBone.cpp
    extensions/CocoStudio/Armature/datas/CCDatas.cpp
    extensions/CocoStudio/Armature/display/CCBatchNode.cpp
    extensions/CocoStudio/Armature/display/CCDecorativeDisplay.cpp
    extensions/CocoStudio/Armature/display/CCDisplayFactory.cpp
    extensions/CocoStudio/Armature/display/CCDisplayManager.cpp
    extensions/CocoStudio/Armature/display/CCSkin.cpp
    extensions/CocoStudio/Armature/physics/CCColliderDetector.cpp
    extensions/CocoStudio/Armature/utils/CCArmatureDataManager.cpp
    extensions/CocoStudio/Armature/utils/CCArmatureDefine.cpp
    extensions/CocoStudio/Armature/utils/CCDataReaderHelper.cpp
    extensions/CocoStudio/Armature/utils/CCSpriteFrameCacheHelper.cpp
    extensions/CocoStudio/Armature/utils/CCTransformHelp.cpp
    extensions/CocoStudio/Armature/utils/CCTweenFunction.cpp
    extensions/CocoStudio/Armature/utils/CCUtilMath.cpp
    extensions/CocoStudio/Components/CCComAttribute.cpp
    extensions/CocoStudio/Components/CCComAudio.cpp
    extensions/CocoStudio/Components/CCComController.cpp
    extensions/CocoStudio/Components/CCComRender.cpp
    extensions/CocoStudio/Components/CCInputDelegate.cpp
    extensions/CocoStudio/GUI/BaseClasses/UIWidget.cpp
    extensions/CocoStudio/GUI/Layouts/UILayout.cpp
    extensions/CocoStudio/GUI/Layouts/UILayoutDefine.cpp
    extensions/CocoStudio/GUI/Layouts/UILayoutParameter.cpp
    extensions/CocoStudio/GUI/System/CocosGUI.cpp
    extensions/CocoStudio/GUI/System/UIHelper.cpp
    extensions/CocoStudio/GUI/System/UITouchGroup.cpp
    extensions/CocoStudio/GUI/UIWidgets/ScrollWidget/UIListView.cpp
    extensions/CocoStudio/GUI/UIWidgets/ScrollWidget/UIPageView.cpp
    extensions/CocoStudio/GUI/UIWidgets/ScrollWidget/UIScrollView.cpp
    extensions/CocoStudio/GUI/UIWidgets/UIButton.cpp
    extensions/CocoStudio/GUI/UIWidgets/UICheckBox.cpp
    extensions/CocoStudio/GUI/UIWidgets/UIImageView.cpp
    extensions/CocoStudio/GUI/UIWidgets/UILabel.cpp
    extensions/CocoStudio/GUI/UIWidgets/UILabelAtlas.cpp
    extensions/CocoStudio/GUI/UIWidgets/UILabelBMFont.cpp
    extensions/CocoStudio/GUI/UIWidgets/UILoadingBar.cpp
    extensions/CocoStudio/GUI/UIWidgets/UIRichText.cpp
    extensions/CocoStudio/GUI/UIWidgets/UISlider.cpp
    extensions/CocoStudio/GUI/UIWidgets/UITextField.cpp
    extensions/CocoStudio/Json/DictionaryHelper.cpp
    extensions/CocoStudio/Reader/GUIReader.cpp
    extensions/CocoStudio/Reader/SceneReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/ButtonReader/ButtonReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/CheckBoxReader/CheckBoxReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/ImageViewReader/ImageViewReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/LabelAtlasReader/LabelAtlasReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/LabelBMFontReader/LabelBMFontReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/LabelReader/LabelReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/LayoutReader/LayoutReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/ListViewReader/ListViewReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/LoadingBarReader/LoadingBarReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/PageViewReader/PageViewReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/ScrollViewReader/ScrollViewReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/SliderReader/SliderReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/TextFieldReader/TextFieldReader.cpp
    extensions/CocoStudio/Reader/WidgetReader/WidgetReader.cpp
    extensions/CocoStudio/Trigger/ObjectFactory.cpp
    extensions/CocoStudio/Trigger/TriggerBase.cpp
    extensions/CocoStudio/Trigger/TriggerMng.cpp
    extensions/CocoStudio/Trigger/TriggerObj.cpp
    extensions/GUI/CCControlExtension/CCControl.cpp
    extensions/GUI/CCControlExtension/CCControlButton.cpp
    extensions/GUI/CCControlExtension/CCControlColourPicker.cpp
    extensions/GUI/CCControlExtension/CCControlHuePicker.cpp
    extensions/GUI/CCControlExtension/CCControlPotentiometer.cpp
    extensions/GUI/CCControlExtension/CCControlSaturationBrightnessPicker.cpp
    extensions/GUI/CCControlExtension/CCControlSlider.cpp
    extensions/GUI/CCControlExtension/CCControlStepper.cpp
    extensions/GUI/CCControlExtension/CCControlSwitch.cpp
    extensions/GUI/CCControlExtension/CCControlUtils.cpp
    extensions/GUI/CCControlExtension/CCInvocation.cpp
    extensions/GUI/CCControlExtension/CCScale9Sprite.cpp
    extensions/GUI/CCEditBox/CCEditBox.cpp
    extensions/GUI/CCEditBox/CCEditBoxImplWin.cpp
    extensions/GUI/CCScrollView/CCScrollView.cpp
    extensions/GUI/CCScrollView/CCSorting.cpp
    extensions/GUI/CCScrollView/CCTableView.cpp
    extensions/GUI/CCScrollView/CCTableViewCell.cpp
    extensions/LocalStorage/LocalStorage.cpp
    extensions/network/HttpClient.cpp
    extensions/network/Websocket.cpp
    extensions/physics_nodes/CCPhysicsDebugNode.cpp
    extensions/physics_nodes/CCPhysicsSprite.cpp
    extensions/spine/Animation.cpp
    extensions/spine/AnimationState.cpp
    extensions/spine/AnimationStateData.cpp
    extensions/spine/Atlas.cpp
    extensions/spine/AtlasAttachmentLoader.cpp
    extensions/spine/Attachment.cpp
    extensions/spine/AttachmentLoader.cpp
    extensions/spine/Bone.cpp
    extensions/spine/BoneData.cpp
    extensions/spine/CCSkeleton.cpp
    extensions/spine/CCSkeletonAnimation.cpp
    extensions/spine/extension.cpp
    extensions/spine/Json.cpp
    extensions/spine/RegionAttachment.cpp
    extensions/spine/Skeleton.cpp
    extensions/spine/SkeletonData.cpp
    extensions/spine/SkeletonJson.cpp
    extensions/spine/Skin.cpp
    extensions/spine/Slot.cpp
    extensions/spine/SlotData.cpp
    extensions/spine/spine-cocos2dx.cpp
    extensions/proj.win32/Win32InputBox.cpp
)

target_include_directories(libExtensions PUBLIC
    external/chipmunk/include/chipmunk
    external/sqlite3/include
    external
    external/libwebsockets/win32/include
    cocos2dx
    cocos2dx/include
    cocos2dx/kazmath/include
    cocos2dx/platform/win32
    cocos2dx/platform/third_party/win32
    cocos2dx/platform/third_party/win32/pthread
    cocos2dx/platform/third_party/win32/OGLES
    cocos2dx/platform/third_party/win32/zlib
    CocosDenshion/include
    extensions
    extensions/proj.win32
)

target_compile_definitions(libExtensions PRIVATE
    WIN32
    _WINDOWS
    _DEBUG
    _LIB
    COCOS2D_DEBUG=1
    CC_ENABLE_CHIPMUNK_INTEGRATION=1
    _CRT_SECURE_NO_WARNINGS
    _SCL_SECURE_NO_WARNINGS
)


#  ================================ libbox2d ================================

add_library(libBox2D STATIC
    external/Box2D/Collision/b2BroadPhase.cpp
    external/Box2D/Collision/b2CollideCircle.cpp
    external/Box2D/Collision/b2CollideEdge.cpp
    external/Box2D/Collision/b2CollidePolygon.cpp
    external/Box2D/Collision/b2Collision.cpp
    external/Box2D/Collision/b2Distance.cpp
    external/Box2D/Collision/b2DynamicTree.cpp
    external/Box2D/Collision/b2TimeOfImpact.cpp
    external/Box2D/Collision/Shapes/b2ChainShape.cpp
    external/Box2D/Collision/Shapes/b2CircleShape.cpp
    external/Box2D/Collision/Shapes/b2EdgeShape.cpp
    external/Box2D/Collision/Shapes/b2PolygonShape.cpp
    external/Box2D/Common/b2BlockAllocator.cpp
    external/Box2D/Common/b2Draw.cpp
    external/Box2D/Common/b2Math.cpp
    external/Box2D/Common/b2Settings.cpp
    external/Box2D/Common/b2StackAllocator.cpp
    external/Box2D/Common/b2Timer.cpp
    external/Box2D/Dynamics/b2Body.cpp
    external/Box2D/Dynamics/b2ContactManager.cpp
    external/Box2D/Dynamics/b2Fixture.cpp
    external/Box2D/Dynamics/b2Island.cpp
    external/Box2D/Dynamics/b2World.cpp
    external/Box2D/Dynamics/b2WorldCallbacks.cpp
    external/Box2D/Dynamics/Contacts/b2ChainAndCircleContact.cpp
    external/Box2D/Dynamics/Contacts/b2ChainAndPolygonContact.cpp
    external/Box2D/Dynamics/Contacts/b2CircleContact.cpp
    external/Box2D/Dynamics/Contacts/b2Contact.cpp
    external/Box2D/Dynamics/Contacts/b2ContactSolver.cpp
    external/Box2D/Dynamics/Contacts/b2EdgeAndCircleContact.cpp
    external/Box2D/Dynamics/Contacts/b2EdgeAndPolygonContact.cpp
    external/Box2D/Dynamics/Contacts/b2PolygonAndCircleContact.cpp
    external/Box2D/Dynamics/Contacts/b2PolygonContact.cpp
    external/Box2D/Dynamics/Joints/b2DistanceJoint.cpp
    external/Box2D/Dynamics/Joints/b2FrictionJoint.cpp
    external/Box2D/Dynamics/Joints/b2GearJoint.cpp
    external/Box2D/Dynamics/Joints/b2Joint.cpp
    external/Box2D/Dynamics/Joints/b2MouseJoint.cpp
    external/Box2D/Dynamics/Joints/b2PrismaticJoint.cpp
    external/Box2D/Dynamics/Joints/b2PulleyJoint.cpp
    external/Box2D/Dynamics/Joints/b2RevoluteJoint.cpp
    external/Box2D/Dynamics/Joints/b2RopeJoint.cpp
    external/Box2D/Dynamics/Joints/b2WeldJoint.cpp
    external/Box2D/Dynamics/Joints/b2WheelJoint.cpp
    external/Box2D/Rope/b2Rope.cpp
)

target_include_directories(libBox2D PUBLIC
    external
    external/Box2D/proj.win32
)
target_compile_definitions(libBox2D PRIVATE
    WIN32
    _DEBUG
    _LIB
)


#  ================================ libchipmunk ================================

add_library(libchipmunk STATIC
    external/chipmunk/src/chipmunk.c
    external/chipmunk/src/cpArbiter.c
    external/chipmunk/src/cpArray.c
    external/chipmunk/src/cpBB.c
    external/chipmunk/src/cpBBTree.c
    external/chipmunk/src/cpBody.c
    external/chipmunk/src/cpCollision.c
    external/chipmunk/src/cpHashSet.c
    external/chipmunk/src/cpPolyShape.c
    external/chipmunk/src/cpShape.c
    external/chipmunk/src/cpSpace.c
    external/chipmunk/src/cpSpaceComponent.c
    external/chipmunk/src/cpSpaceHash.c
    external/chipmunk/src/cpSpaceQuery.c
    external/chipmunk/src/cpSpaceStep.c
    external/chipmunk/src/cpSpatialIndex.c
    external/chipmunk/src/cpSweep1D.c
    external/chipmunk/src/cpVect.c
    external/chipmunk/src/constraints/cpConstraint.c
    external/chipmunk/src/constraints/cpDampedRotarySpring.c
    external/chipmunk/src/constraints/cpDampedSpring.c
    external/chipmunk/src/constraints/cpGearJoint.c
    external/chipmunk/src/constraints/cpGrooveJoint.c
    external/chipmunk/src/constraints/cpPinJoint.c
    external/chipmunk/src/constraints/cpPivotJoint.c
    external/chipmunk/src/constraints/cpRatchetJoint.c
    external/chipmunk/src/constraints/cpRotaryLimitJoint.c
    external/chipmunk/src/constraints/cpSimpleMotor.c
    external/chipmunk/src/constraints/cpSlideJoint.c
)

target_include_directories(libchipmunk PUBLIC
    external/chipmunk/include/chipmunk
    external/chipmunk/proj.win32
)

target_compile_definitions(libchipmunk PRIVATE
    WIN32
    _DEBUG
    _LIB
)


#  ================================ hellocpp ================================

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


#  ================================ testcpp ================================

add_executable(test_win32 WIN32
    samples/Cpp/TestCpp/Classes/ChipmunkTest/ChipmunkTest.cpp
    samples/Cpp/TestCpp/Classes/ClippingNodeTest/ClippingNodeTest.cpp
    samples/Cpp/TestCpp/Classes/ConfigurationTest/ConfigurationTest.cpp
    samples/Cpp/TestCpp/Classes/DataVisitorTest/DataVisitorTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocosBuilderTest/AnimationsTest/AnimationsTestLayer.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocosBuilderTest/TimelineCallbackTest/TimelineCallbackTestLayer.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioArmatureTest/ArmatureScene.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioComponentsTest/ComponentsTestScene.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioComponentsTest/EnemyController.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioComponentsTest/GameOverScene.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioComponentsTest/PlayerController.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioComponentsTest/ProjectileController.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioComponentsTest/SceneController.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/CocosGUIScene.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/CocoStudioGUITest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/CustomGUIScene.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/CustomTest/CustomImageTest/CustomImageTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/CustomTest/CustomParticleWidgetTest/CustomParticleWidgetTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/CustomWidget/CustomImageView.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/CustomWidget/CustomImageViewReader.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/CustomWidget/CustomParticleWidget.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/CustomWidget/CustomParticleWidgetReader.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/CustomWidget/CustomReader.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/GUIEditorTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIButtonTest/UIButtonTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIButtonTest/UIButtonTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UICheckBoxTest/UICheckBoxTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UICheckBoxTest/UICheckBoxTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIImageViewTest/UIImageViewTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIImageViewTest/UIImageViewTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UILabelAtlasTest/UILabelAtlasTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UILabelAtlasTest/UILabelAtlasTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UILabelBMFontTest/UILabelBMFontTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UILabelBMFontTest/UILabelBMFontTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UILabelTest/UILabelTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UILabelTest/UILabelTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UILayoutTest/UILayoutTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UILayoutTest/UILayoutTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIListViewTest/UIListViewTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIListViewTest/UIListViewTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UILoadingBarTest/UILoadingBarTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UILoadingBarTest/UILoadingBarTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIPageViewTest/UIPageViewTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIPageViewTest/UIPageViewTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIRichTextTest/UIRichTextTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIScene.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UISceneManager.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UISceneManager_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIScene_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIScrollViewTest/UIScrollViewTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIScrollViewTest/UIScrollViewTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UISliderTest/UISliderTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UISliderTest/UISliderTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UITextFieldTest/UITextFieldTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UITextFieldTest/UITextFieldTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIWidgetAddNodeTest/UIWidgetAddNodeTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioGUITest/UIWidgetAddNodeTest/UIWidgetAddNodeTest_Editor.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioSceneTest/SceneEditorTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioSceneTest/TriggerCode/acts.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocoStudioSceneTest/TriggerCode/cons.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/ControlExtensionTest/CCControlPotentiometerTest/CCControlPotentiometerTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/ControlExtensionTest/CCControlStepperTest/CCControlStepperTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/EditBoxTest/EditBoxTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/NetworkTest/HttpClientTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/NetworkTest/WebSocketTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/TableViewTest/CustomTableViewCell.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/TableViewTest/TableViewTestScene.cpp
    samples/Cpp/TestCpp/Classes/FileUtilsTest/FileUtilsTest.cpp
    samples/Cpp/TestCpp/Classes/PerformanceTest/PerformanceAllocTest.cpp
    samples/Cpp/TestCpp/Classes/SpineTest/SpineTest.cpp
    samples/Cpp/TestCpp/Classes/TexturePackerEncryptionTest/TextureAtlasEncryptionTest.cpp
    samples/Cpp/TestCpp/Classes/VisibleRect.cpp
    samples/Cpp/TestCpp/proj.win32/main.cpp
    samples/Cpp/TestCpp/Classes/AppDelegate.cpp
    samples/Cpp/TestCpp/Classes/controller.cpp
    samples/Cpp/TestCpp/Classes/testBasic.cpp
    samples/Cpp/TestCpp/Classes/ActionsTest/ActionsTest.cpp
    samples/Cpp/TestCpp/Classes/TransitionsTest/TransitionsTest.cpp
    samples/Cpp/TestCpp/Classes/EffectsTest/EffectsTest.cpp
    samples/Cpp/TestCpp/Classes/ClickAndMoveTest/ClickAndMoveTest.cpp
    samples/Cpp/TestCpp/Classes/RotateWorldTest/RotateWorldTest.cpp
    samples/Cpp/TestCpp/Classes/ParticleTest/ParticleTest.cpp
    samples/Cpp/TestCpp/Classes/ActionsEaseTest/ActionsEaseTest.cpp
    samples/Cpp/TestCpp/Classes/MotionStreakTest/MotionStreakTest.cpp
    samples/Cpp/TestCpp/Classes/DrawPrimitivesTest/DrawPrimitivesTest.cpp
    samples/Cpp/TestCpp/Classes/ShaderTest/ShaderTest.cpp
    samples/Cpp/TestCpp/Classes/TouchesTest/Ball.cpp
    samples/Cpp/TestCpp/Classes/TouchesTest/Paddle.cpp
    samples/Cpp/TestCpp/Classes/TouchesTest/TouchesTest.cpp
    samples/Cpp/TestCpp/Classes/MenuTest/MenuTest.cpp
    samples/Cpp/TestCpp/Classes/ActionManagerTest/ActionManagerTest.cpp
    samples/Cpp/TestCpp/Classes/LayerTest/LayerTest.cpp
    samples/Cpp/TestCpp/Classes/SceneTest/SceneTest.cpp
    samples/Cpp/TestCpp/Classes/ParallaxTest/ParallaxTest.cpp
    samples/Cpp/TestCpp/Classes/TileMapTest/TileMapTest.cpp
    samples/Cpp/TestCpp/Classes/IntervalTest/IntervalTest.cpp
    samples/Cpp/TestCpp/Classes/LabelTest/LabelTest.cpp
    samples/Cpp/TestCpp/Classes/SpriteTest/SpriteTest.cpp
    samples/Cpp/TestCpp/Classes/SchedulerTest/SchedulerTest.cpp
    samples/Cpp/TestCpp/Classes/RenderTextureTest/RenderTextureTest.cpp
    samples/Cpp/TestCpp/Classes/EffectsAdvancedTest/EffectsAdvancedTest.cpp
    samples/Cpp/TestCpp/Classes/KeypadTest/KeypadTest.cpp
    samples/Cpp/TestCpp/Classes/CocosDenshionTest/CocosDenshionTest.cpp
    samples/Cpp/TestCpp/Classes/PerformanceTest/PerformanceNodeChildrenTest.cpp
    samples/Cpp/TestCpp/Classes/PerformanceTest/PerformanceParticleTest.cpp
    samples/Cpp/TestCpp/Classes/PerformanceTest/PerformanceSpriteTest.cpp
    samples/Cpp/TestCpp/Classes/PerformanceTest/PerformanceTest.cpp
    samples/Cpp/TestCpp/Classes/PerformanceTest/PerformanceTextureTest.cpp
    samples/Cpp/TestCpp/Classes/PerformanceTest/PerformanceTouchesTest.cpp
    samples/Cpp/TestCpp/Classes/ZwoptexTest/ZwoptexTest.cpp
    samples/Cpp/TestCpp/Classes/CurlTest/CurlTest.cpp
    samples/Cpp/TestCpp/Classes/TextInputTest/TextInputTest.cpp
    samples/Cpp/TestCpp/Classes/UserDefaultTest/UserDefaultTest.cpp
    samples/Cpp/TestCpp/Classes/BugsTest/Bug-1159.cpp
    samples/Cpp/TestCpp/Classes/BugsTest/Bug-1174.cpp
    samples/Cpp/TestCpp/Classes/BugsTest/Bug-350.cpp
    samples/Cpp/TestCpp/Classes/BugsTest/Bug-422.cpp
    samples/Cpp/TestCpp/Classes/BugsTest/Bug-624.cpp
    samples/Cpp/TestCpp/Classes/BugsTest/Bug-886.cpp
    samples/Cpp/TestCpp/Classes/BugsTest/Bug-899.cpp
    samples/Cpp/TestCpp/Classes/BugsTest/Bug-914.cpp
    samples/Cpp/TestCpp/Classes/BugsTest/BugsTest.cpp
    samples/Cpp/TestCpp/Classes/BugsTest/Bug-458/Bug-458.cpp
    samples/Cpp/TestCpp/Classes/BugsTest/Bug-458/QuestionContainerSprite.cpp
    samples/Cpp/TestCpp/Classes/Texture2dTest/Texture2dTest.cpp
    samples/Cpp/TestCpp/Classes/FontTest/FontTest.cpp
    samples/Cpp/TestCpp/Classes/CurrentLanguageTest/CurrentLanguageTest.cpp
    samples/Cpp/TestCpp/Classes/TextureCacheTest/TextureCacheTest.cpp
    samples/Cpp/TestCpp/Classes/AccelerometerTest/AccelerometerTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/ExtensionsTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/ControlExtensionTest/CCControlScene.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/ControlExtensionTest/CCControlSceneManager.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/ControlExtensionTest/CCControlButtonTest/CCControlButtonTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/ControlExtensionTest/CCControlColourPicker/CCControlColourPickerTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/ControlExtensionTest/CCControlSliderTest/CCControlSliderTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/ControlExtensionTest/CCControlSwitchTest/CCControlSwitchTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/NotificationCenterTest/NotificationCenterTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocosBuilderTest/CocosBuilderTest.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocosBuilderTest/ButtonTest/ButtonTestLayer.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocosBuilderTest/HelloCocosBuilder/HelloCocosBuilderLayer.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocosBuilderTest/MenuTest/MenuTestLayer.cpp
    samples/Cpp/TestCpp/Classes/ExtensionsTest/CocosBuilderTest/TestHeader/TestHeaderLayer.cpp
    samples/Cpp/TestCpp/Classes/NodeTest/NodeTest.cpp
    samples/Cpp/TestCpp/Classes/ActionsProgressTest/ActionsProgressTest.cpp
    samples/Cpp/TestCpp/Classes/Box2DTest/Box2dTest.cpp
    samples/Cpp/TestCpp/Classes/Box2DTestBed/Box2dView.cpp
    samples/Cpp/TestCpp/Classes/Box2DTestBed/GLES-Render.cpp
    samples/Cpp/TestCpp/Classes/Box2DTestBed/Test.cpp
    samples/Cpp/TestCpp/Classes/Box2DTestBed/TestEntries.cpp
    samples/Cpp/TestCpp/Classes/MutiTouchTest/MutiTouchTest.cpp
)

target_include_directories(test_win32 PUBLIC
    cocos2dx
    cocos2dx/include
    cocos2dx/kazmath/include
    cocos2dx/platform/win32
    cocos2dx/platform/third_party/win32
    cocos2dx/platform/third_party/win32/OGLES
    cocos2dx/platform/third_party/win32/pthread
    external
    external/chipmunk/include/chipmunk
    external/libwebsockets/win32/include
    CocosDenshion/include
    extensions
    extensions/network
    samples/Cpp/TestCpp/Classes
    samples/Cpp/TestCpp
    samples/Cpp/TestCpp/proj.win32
)

target_link_libraries(test_win32
    libExtensions
    libcocos2d
    libCocosDenshion
    opengl32
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/glew32.lib
    libBox2D
    libchipmunk
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/libcurl_imp.lib
    ${CMAKE_CURRENT_SOURCE_DIR}/external/libwebsockets/win32/lib/websockets.lib
    ${CMAKE_CURRENT_SOURCE_DIR}/cocos2dx/platform/third_party/win32/libraries/pthreadVCE2.lib
)

target_compile_definitions(test_win32 PRIVATE
    WIN32
    _DEBUG
    _WINDOWS
    _USE_MATH_DEFINES
    GL_GLEXT_PROTOTYPES
    CC_ENABLE_CHIPMUNK_INTEGRATION=1
    COCOS2D_DEBUG=1
    _CRT_SECURE_NO_WARNINGS
    _SCL_SECURE_NO_WARNINGS
)
