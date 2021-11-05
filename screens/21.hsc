<?xml version="1.0" encoding="UTF-8"?>
<ScrInfo ScreenNo="21" ScreenType="" ScreenSize="0">
	<Script>
		<TrigAction>
			<Trigger Action="1" BitAddr="grava">@w_1:46 = @SP_Temperatura_ativo
@w_1:4692 = @SP_speed_ativo


IF  @SP_Temperatura_ativo&lt;&gt;@SP_REC_MEM  OR @SP_speed_ativo&lt;&gt;@VEL_REC_MEM THEN
	bmov (@nome_tela_0,@nome_vazio,10) 'nome vazio
ENDIF





@SP_EDIT_flag = FALSE
@grava = FALSE
</Trigger></TrigAction></Script>
<PartInfo PartType="WordShow" PartName="WL_0">
<General Desc="WL_0" Area="10 0 470 479" WordAddr="plano_de_fundo" StatsNum="3" Fast="0" DataFormat="2" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff -1" BmpIndex="-1" LaStartPt="230 284" StatusCovType="0" AnimaReturn="0" ByAddr="0" Trigger="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" isNautomatic="0" IsCtrlStaTextByAddr="0" isReturn="0" isStateControl="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0"/>
<Label Status="0" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/>
<Label Status="1" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/>
<Label Status="2" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_1">
<General Desc="NUM_0" Area="64 73 214 173" WordAddr="SP_Temperatura_ativo" Fast="0" IsInput="1" WriteAddr="SP_Temperatura_ativo" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="TFT-type style\dp_zc03.pvg" BorderColor="0xcccccc 16777215" FrnColor="0xff -1" BgColor="0xffffff 0" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="6" DigitCount="3 0" DataLimit="0 1137180672" DataRange="0.000000 400.000000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="32" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="BS_0">
<General Desc="BS_0" Area="316 264 457 360" OperateAddr="grava" Fast="0" BitFunc="1" Monitor="1" MonitorAddr="grava" FigureFile="TruecolorStyle\TrueColor20.pvg" BorderColor="0xcccccc 0" BmpIndex="-1" LaStartPt="0 0" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Pattern="1" FrnColor="0x80ff00 1" BgColor="0xffffff 0" Bold="0" LaIndexID="OK" CharSize="24114141414141414" LaFrnColor="0x0 0"/>
<Label Status="1" Pattern="1" FrnColor="0x8080ff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="OK" CharSize="24814141414141414" LaFrnColor="0x0 0"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_0">
<General TextContent="Tempo" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="16 326 126 126 126 126 126 126 12" Bold="0" StartPt="62 207"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_1">
<General TextContent="Temperatura desejada" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="16 326 126 126 126 126 126 126 12" Bold="0" StartPt="56 32"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_2">
<General Desc="NUM_0" Area="243 404 298 449" WordAddr="1:4690" Fast="0" IsInput="0" WriteAddr="1:4690" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xcccccc 0" FrnColor="0x0 -1" BgColor="0xffffff 0" BmpIndex="27" Transparent="0" IsHideNum="0" HighZeroPad="1" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="2" DigitCount="2 2" DataLimit="0 1120402145" DataRange="0.000000 99.990000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="232" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_2">
<General TextContent="mínimo:" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="16 326 126 126 126 126 126 126 12" Bold="0" StartPt="67 409"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_3">
<General TextContent="ºC" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="2396 126 126 126 126 126 126 12" Bold="0" StartPt="229 76"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_4">
<General TextContent="seg" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="2436 126 126 126 126 126 126 12" Bold="0" StartPt="226 244"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_0">
<General Desc="NUM_0" Area="67 245 217 345" WordAddr="SP_speed_ativo" Fast="0" IsInput="1" WriteAddr="SP_speed_ativo" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="TFT-type style\dp_zc03.pvg" BorderColor="0xcccccc 16777215" FrnColor="0x0 -1" BgColor="0xffffff 0" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="1" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="2" DigitCount="2 2" DataLimit="0 1120402145" DataRange="0.000000 99.990000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="156" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></ScrInfo>
