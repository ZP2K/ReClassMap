from ReClassMap import *

OFFSET_DXRENDERER = 0x142738080
OFFSET_CLIENTGAMECONTEXT = 0x142670d80

r = Map("./BF4.reclass")

C = r.Class(name="OFFSET_ClientGameContext",offset=OFFSET_CLIENTGAMECONTEXT)
C[0x0000] = Pointer(classname="ClientGameContext",name="ClientGameContext")

C = r.Class(name="ClientGameContext",size=0x440)
C[0x0020] = Pointer(classname="GameTime",name="m_pGameTime")
C[0x0028] = Pointer(classname="Level",name="m_pLevel")
C[0x0060] = Pointer(classname="PlayerManager",name="m_pPlayerManager")
C[0x0068] = Pointer(classname="Online",name="m_pOnline")
C[0x0070] = Pointer(classname="GameView",name="m_pGameView")
C[0x0078] = Pointer(classname="InterpolationManager",name="m_pInterpolationManager")

C = r.Class(name="PlayerManager",size=0x550)
C[0x0000] = Vtable(name="VirtFuncs")
C[0x0000][1] = Vfunc(name="getPlayers")
C[0x0000][2] = Vfunc(name="getSpectators")
C[0x0008] = Pwchar(name="")
C[0x0010] = Pwchar(name="")
C[0x0018] = Hex64(name="")
C[0x0540] = Pointer(classname="ClientPlayer",name="m_pLocalPlayer")
C[0x0548] = Array(classname="PlayerArrayElem",name="m_pPlayers",total=70)

C = r.Class(name="PlayerArrayElem",size=0x8)
C[0x0] = Pointer(classname="ClientPlayer",name="m_pPlayer")

C = r.Class(name="ClientPlayer",size=0x14D8)
C[0x0018] = Pchar(name="m_Name")
C[0x14D0] = Pointer(classname="ClientSoldierEntity",name="m_pControlledControllable")

C = r.Class(name="ClientSoldierEntity",size=0x1228)
C[0x01E8] = Pointer(classname="AntAnimatableComponent",name="m_pAnimatable")
C[0x01F0] = Pointer(classname="AntAnimatableComponent",name="m_pAnimatable2") 
C[0x04F0] = Int32(name="m_PoseType")
C[0x04F4] = Int32(name="m_EngineChams")
C[0x0570] = Pointer(classname="SoldierWeaponComponent",name="m_pWeaponComponent") 
C[0x0578] = Pointer(classname="ClientSoldierBodyComponent",name="m_pBodyComponent") 
C[0x0580] = Pointer(classname="RagdollComponent",name="m_pRagdollComponent") 
C[0x05B0] = Byte(name="m_Sprinting")
C[0x05B1] = Byte(name="m_Occluded")
C[0x0B50] = Pointer(classname="ParachuteComponent",name="m_pParachute") 
C[0x0BF0] = Pointer(classname="SpottingComponent",name="m_pSpottingComp") 
C[0x0C10] = Pointer(classname="SpottingTargetComponent",name="m_pSpottingTargetComp") 
C[0x0C70] = Pointer(classname="SoldierSuppressionComponent",name="m_pSuppressionComp") 
C[0x0D30] = Pointer(classname="VaultComponent",name="m_pVaultComp")

C = r.Class(name="SoldierWeaponComponent",size=0x0ACC)
C[0x00D0] = Matrix(name="m_WeaponTransform")
C[0x0890] = Pointer(classname="AnimatedSoldierWeaponHandler",name="m_Handler") 
C[0x08C8] = Pointer(classname="ClientSoldierEntity",name="m_pOwner") 
C[0x0A98] = Int32(name="m_CurrentWeaponIndex")
C[0x0A9C] = Int32(name="m_LastWeaponIndex")
C[0x0AA0] = Int32(name="m_LastGunIndex")
C[0x0AC0] = Int32(name="m_CurrentZoomLevel")
C[0x0AC4] = Int32(name="m_ZoomLevelMax")
C[0x0AC8] = Int32(name="m_ZeroingDistanceLevel")

C = r.Class(name="AnimatedSoldierWeaponHandler",size=0x40)
C[0x0000] = Array(classname="SoldierWeaponArray",name="m_pWeaponList",total=7)

C = r.Class(name="SoldierWeaponArray")
C[0x0] = Pointer(classname="SoldierWeapon",name="m_pSoldierWeapon") 

C = r.Class(name="SoldierWeapon",size=0x4C80)
C[0x4988] = Pointer(classname="SoldierAimingSimulation",name="m_pAuthoritativeAiming") 
C[0x49A8] = Pointer(classname="ClientWeapon",name="m_pWeapon") 
C[0x49C0] = Pointer(classname="WeaponFiring",name="m_pPrimary") 

C = r.Class(name="SoldierAimingSimulation",size=0x0174)
C[0x0010] = Pointer(classname="AimAssist",name="m_pFPSAimer") 
C[0x0018] = Float(name="m_Yaw")
C[0x001C] = Float(name="m_Pitch")
C[0x0020] = Float(name="m_AimYawTimer")
C[0x0024] = Float(name="m_AimPitchTimer")
C[0x0028] = Vec2(name="m_Sway")
C[0x0030] = Float(name="m_DeltaTime")
C[0x003C] = Vec2(name="m_ViewDelta")
C[0x0070] = Matrix(name="m_Transform")
C[0x00B0] = Vec4(name="m_Position")
C[0x00C0] = Vec4(name="m_View")
C[0x00D0] = Vec4(name="m_Velocity")
C[0x0138] = Float(name="m_Fov")
C[0x0158] = Pointer(classname="TypeInfo",name="m_RayResult") 
C[0x0160] = Vec4(name="m_RayHitPoint")
C[0x0170] = Int32(name="m_RayLength")


C = r.Class(name="WeaponFiring",size=0x01AF)
C[0x0078] = Pointer(classname="WeaponSway",name="m_Sway") 
C[0x0128] = Pointer(classname="PrimaryFire",name="m_pPrimaryFire") 
C[0x0148] = Int32(name="m_WeaponState")
C[0x014C] = Int32(name="m_LastWeaponState")
C[0x0150] = Int32(name="m_NextWeaponState")
C[0x015C] = Float(name="m_TimeToWait")
C[0x0160] = Float(name="m_ReloadTimer")
C[0x0164] = Float(name="m_HoldReleaseMinDelay")
C[0x0168] = Float(name="m_RecoilTimer")
C[0x016C] = Float(name="m_RecoilAngleX")
C[0x0170] = Float(name="m_RecoilAngleY")
C[0x0174] = Float(name="m_RecoilAngleZ")
C[0x0178] = Float(name="m_RecoilFOVAngle")
C[0x017C] = Float(name="m_RecoilTimeMultiplier")
C[0x0180] = Float(name="m_OverheatDropMultiplier")
C[0x01AC] = Byte(name="m_IsNotFiring");
C[0x01AD] = Byte(name="m_JustShot");
C[0x01AE] = Byte(name="m_IsOverheated");


C = r.Class(name="ClientWeapon",size=0x02B4)
C[0x0018] = Pointer(classname="PrimaryFire",name="m_pWeaponFiring") 
C[0x0020] = Pointer(classname="WeaponModifier",name="m_pWeaponModifier") 
C[0x0030] = Vec4(name="m_MoveSpeed")
C[0x0040] = Matrix(name="m_ShootSpace")
C[0x0080] = Matrix(name="m_ShootSpaceIdentity")
C[0x0290] = Float(name="m_CameraFOV")
C[0x0294] = Float(name="m_WeaponFOV")
C[0x0298] = Float(name="m_FOVScaleFactor")
C[0x02B0] = Int32(name="m_ZoomLevel")

C = r.Class(name="OFFSET_DxRenderer",offset=OFFSET_DXRENDERER)
C[0x0000] = Pointer(classname="DxRenderer",name="DxRenderer")

C = r.Class(name="DxRenderer",size=0x0838)
C[0x0028] = Int32(name="m_FrameCounter")
C[0x002C] = Byte(name="m_FrameInProgress")
C[0x0038] = Pointer(classname="Screen",name="m_pScreen")
C[0x0080] = Pointer(classname="DxDisplaySettings",name="m_pDisplaySettings")
C[0x0100] = Int64(name="m_pDevice")
C[0x0108] = Int64(name="m_pContext")

C = r.Class(name="DxDisplaySettings",size=0x0098)
C[0x0028] = Int32(name="m_FullscreenHeight")
C[0x002C] = Int32(name="m_FullscreenWidth")
C[0x0030] = Float(name="m_FullscreenRefreshRate")
C[0x0034] = Int32(name="m_FullscreenOutputIndex")
C[0x0038] = Int32(name="m_PresentInterval")
C[0x003c] = Int32(name="m_PresentImmediateThreshold")
C[0x0040] = Int32(name="m_RenderAheadLimit")
C[0x0044] = Float(name="m_StereoDepth")
C[0x0048] = Float(name="m_StereoConvergenceScale")
C[0x004c] = Float(name="m_StereoSeperationScale")
C[0x0050] = Float(name="m_StereoSoldierZoomConvergenceScale")
C[0x0054] = Int32(name="m_NvidiaMinDriverVersion")
C[0x0058] = Pchar(name="m_AmdMinDriverVersion")
C[0x0060] = Float(name="m_LowResDisplayPlaneScale")

C = r.Class(name="Screen",size=0x110)
C[0x0000] = Int64(name="m_HWND")
C[0x0048] = Int32(name="m_FullscreenMode")
C[0x004C] = Byte(name="m_TopWindow")
C[0x004D] = Byte(name="m_Minimized")
C[0x004E] = Byte(name="m_Maximized")
C[0x004F] = Byte(name="m_Resizing")
C[0x0058] = Instance(classname="RenderScreenInfo", name="m_ScreenInfo")
C[0x00E8] = Int64(name="m_pSwapChain")
C[0x00F0] = Int64(name="m_pBackBufferTexture")
C[0x0108] = Int64(name="m_pDefaultRenderTargetView")

C = r.Class(name="RenderScreenInfo",size=0x18)
C[0x0000] = Int32(name="m_Width")
C[0x0004] = Int32(name="m_Height")

r.write(hidepad=1,custompad=1)