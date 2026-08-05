<?xml version="1.0" encoding="UTF-8"?>
<ScrInfo ScreenNo="21" ScreenType="" ScreenSize="0">
<Script>
		<TrigAction>
			<Trigger Action="1" BitAddr="grava">' Popup para tela
@w_1:46 = @SP_Temperatura_ativo
@w_1:4692 = @SP_speed_ativo


IF  @SP_Temperatura_ativo&lt;&gt;@SP_REC_MEM  OR @SP_speed_ativo&lt;&gt;@VEL_REC_MEM THEN
	bmov (@nome_tela_0,@nome_vazio,10) 'nome vazio
ENDIF





@SP_EDIT_flag = FALSE
@grava = FALSE
</Trigger></TrigAction></Script>
<PartInfo PartType="WordShow" PartName="WL_0">
		<General Desc="WL_0" Area="0 0 1 1" WordAddr="plano_de_fundo" StatsNum="3" Fast="0" DataFormat="2" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff -1" BmpIndex="-1" LaStartPt="230 239" StatusCovType="0" AnimaReturn="0" ByAddr="0" Trigger="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" isNautomatic="0" IsCtrlStaTextByAddr="0" isReturn="0" isStateControl="0"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="14 14 14 14 14 14 14 14" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/>
		<Label Status="1" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="14 14 14 14 14 14 14 14" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/>
		<Label Status="2" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" CharSize="14 14 14 14 14 14 14 14" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/></PartInfo>
<PartInfo PartType="Rect" PartName="BG_0">
<General Area="0 0 480 800" BorderColor="0xf4f7fb 0" Pattern="1" FrnColor="0xf4f7fb -1" BgColor="0xf4f7fb -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="HEADER_BG">
<General Area="0 0 480 112" BorderColor="0xf172a 0" Pattern="1" FrnColor="0xf172a -1" BgColor="0xf172a -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TITLE_0">
<General TextContent="Ajuste Manual" LaFrnColor="0xffffff -1" IsBackColor="0" BgColor="0xf172a 0" CharSize="304" Bold="1" StartPt="92 22"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="SUBTITLE_0">
<General TextContent="Temperatura e tempo ativos" LaFrnColor="0xcbd5e1 -1" IsBackColor="0" BgColor="0xf172a 0" CharSize="233" Bold="0" StartPt="92 60"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="HEADER_ACCENT">
<General Area="92 92 204 97" BorderColor="0x22c55e 0" Pattern="1" FrnColor="0x22c55e -1" BgColor="0x22c55e -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="FunctionSwitch" PartName="FS_MENU_OPEN">
<General Desc="FS_MENU_OPEN" Area="24 28 80 84" ScrSwitch="0" FuncFunc="2" ScreenNo="-1" ScreenNo2="1003" PointPos="0 0" PopupScreenType="1" PopupCloseWithParent="1" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 16777215" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="140" LaStartPt="12 12" Transparent="0" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="BS_0">
		<General Desc="BS_0" Area="400 28 456 84" OperateAddr="grava" Fast="0" BitFunc="1" Monitor="1" MonitorAddr="grava" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 0" BmpIndex="126" Align="3" LaStartPt="12 12" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" FrnColor="0x22c55e -1" BgColor="0x22c55e -1"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
		<Label Status="0" Pattern="1" FrnColor="0x22c55e 1" BgColor="0x22c55e 0" Bold="0" LaIndexID="Confirmar" CharSize="6 12" LaFrnColor="0xffffff -1"/>
		<Label Status="1" Pattern="1" FrnColor="0x22c55e 0" BgColor="0x22c55e 0" Bold="0" LaIndexID="Aguarde" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_TEMP">
<General Area="24 132 456 280" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_TEMP">
<General Area="24 132 30 280" BorderColor="0xef4444 0" Pattern="1" FrnColor="0xef4444 -1" BgColor="0xef4444 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_TEMP">
<General TextContent="Nova temperatura" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 154"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_TEMP_MIN">
<General TextContent="Min: 150 C" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="48 190"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_TEMP_MAX">
<General TextContent="Max: 400 C" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="48 222"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_1">
			<General Desc="NUM_0" Area="282 156 416 236" WordAddr="SP_Temperatura_ativo" Fast="0" IsInput="1" WriteAddr="SP_Temperatura_ativo" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0x0000ff -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
			<DispFormat DispType="6" DigitCount="3 0" DataLimit="1125515264 1137180672" DataRange="150.000000 400.000000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="304" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
			<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
			<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_TEMP_UNIT">
<General TextContent="C" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="0" StartPt="424 186"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_SPEED">
<General Area="24 312 456 460" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_SPEED">
<General Area="24 312 30 460" BorderColor="0x0ea5e9 0" Pattern="1" FrnColor="0x0ea5e9 -1" BgColor="0x0ea5e9 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_SPEED">
<General TextContent="Novo tempo" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 334"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_SPEED_MIN">
<General TextContent="Min: 0.00 min" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="48 370"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_SPEED_MAX">
<General TextContent="Max: 9.99 min" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="48 402"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_0">
			<General Desc="NUM_0" Area="282 336 416 416" WordAddr="SP_speed_ativo" Fast="0" IsInput="1" WriteAddr="SP_speed_ativo" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="1" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
			<DispFormat DispType="2" DigitCount="1 2" DataLimit="0 1092605706" DataRange="0.000000 9.990000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="304" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
			<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
			<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_SPEED_UNIT">
<General TextContent="min" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="12 24" Bold="0" StartPt="420 366"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_MIN">
<General Area="24 492 456 620" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_MIN">
<General Area="24 492 30 620" BorderColor="0x94a3b8 0" Pattern="1" FrnColor="0x94a3b8 -1" BgColor="0x94a3b8 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_MIN">
<General TextContent="Minimo da esteira" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 516"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_MIN_SUB">
<General TextContent="Referencia atual para ajuste." LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="48 552"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_2">
			<General Desc="NUM_0" Area="282 524 390 586" WordAddr="1:4690" Fast="0" IsInput="0" WriteAddr="1:4690" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xffffff 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="1" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
			<DispFormat DispType="2" DigitCount="2 2" DataLimit="0 1120402145" DataRange="0.000000 99.990000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="262" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
			<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
			<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_MIN_UNIT">
<General TextContent="min" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="12 24" Bold="1" StartPt="398 552"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="Bit Switch0">
		<General Desc="BS_3" Area="0 0 1 1" OperateAddr="SP_EDIT_flag" Fast="0" Monitor="1" MonitorAddr="SP_EDIT_flag" FigureFile="" BorderColor="0xf4f7fb 0" BmpIndex="-1" LaStartPt="16 16" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" FrnColor="0xf4f7fb 0" BgColor="0xf4f7fb 0" Transparent="1"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
		<Label Status="0" FrnColor="0xf4f7fb 0" BgColor="0xf4f7fb 0" Bold="0" CharSize="6 12" LaFrnColor="0xf4f7fb 0" LaIndexID=""/>
		<Label Status="1" Pattern="1" FrnColor="0xf4f7fb 0" BgColor="0xf4f7fb 0" Bold="0" CharSize="6 12" LaFrnColor="0xf4f7fb 0" LaIndexID=""/></PartInfo></ScrInfo>
