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
		<General Desc="WL_0" Area="10 117 470 612" WordAddr="plano_de_fundo" StatsNum="3" Fast="0" DataFormat="2" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff -1" BmpIndex="-1" LaStartPt="230 239" StatusCovType="0" AnimaReturn="0" ByAddr="0" Trigger="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" isNautomatic="0" IsCtrlStaTextByAddr="0" isReturn="0" isStateControl="0"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/>
		<Label Status="1" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/>
		<Label Status="2" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/></PartInfo>
	<PartInfo PartType="GroupPart" PartName="Group part">
		<PartInfo PartType="Numeric" PartName="NUM_1">
			<General Desc="NUM_0" Area="165 188 315 288" WordAddr="SP_Temperatura_ativo" Fast="0" IsInput="1" WriteAddr="SP_Temperatura_ativo" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="TFT-type style\dp_zc03.pvg" BorderColor="0xcccccc 16777215" FrnColor="0xff -1" BgColor="0xffffff 0" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
			<DispFormat DispType="6" DigitCount="3 0" DataLimit="1125515264 1137180672" DataRange="150.000000 400.000000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="299" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
			<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
			<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
		<PartInfo PartType="Text" PartName="TXT_3">
			<General TextContent="??C" LaFrnColor="0xff -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="2396 126 126 126 126 126 126 12" Bold="0" StartPt="318 191"/>
			<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo>
	<PartInfo PartType="BitSwitch" PartName="BS_0">
		<General Desc="BS_0" Area="140 489 340 549" OperateAddr="grava" Fast="0" BitFunc="1" Monitor="1" MonitorAddr="grava" FigureFile="TFT-type style\TFT010.pvg" BorderColor="0x80ff00 -1" BmpIndex="-1" Align="3" LaStartPt="4 5" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
		<Label Status="0" Pattern="4587604" FrnColor="0x80ff00 1" BgColor="0xffffff 0" Bold="0" LaIndexID="Confirmar" CharSize="29814141414141414" LaFrnColor="0x0 0"/>
		<Label Status="1" Pattern="1" FrnColor="0x8080ff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="Aguarde" CharSize="29814141414141414" LaFrnColor="0x0 0"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_1">
		<General TextContent="Nova temperatura" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="16 326 126 126 126 126 126 126 12" Bold="0" StartPt="104 147"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
	<PartInfo PartType="GroupPart" PartName="Group part">
		<PartInfo PartType="Numeric" PartName="NUM_2">
			<General Desc="NUM_0" Area="266 562 321 607" WordAddr="1:4690" Fast="0" IsInput="0" WriteAddr="1:4690" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xcccccc 0" FrnColor="0x0 -1" BgColor="0xffffff 0" BmpIndex="27" Transparent="0" IsHideNum="0" HighZeroPad="1" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
			<DispFormat DispType="2" DigitCount="2 2" DataLimit="0 1120402145" DataRange="0.000000 99.990000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="232" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
			<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
			<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
		<PartInfo PartType="Text" PartName="TXT_2">
			<General TextContent="m??nimo:" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="16 326 126 126 126 126 126 126 12" Bold="0" StartPt="134 574"/>
			<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo>
	<PartInfo PartType="GroupPart" PartName="Group part">
		<PartInfo PartType="Text" PartName="TXT_4">
			<General TextContent="Min" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="2436 126 126 126 126 126 126 12" Bold="0" StartPt="335 415"/>
			<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
		<PartInfo PartType="Numeric" PartName="NUM_0">
			<General Desc="NUM_0" Area="165 360 327 460" WordAddr="SP_speed_ativo" Fast="0" IsInput="1" WriteAddr="SP_speed_ativo" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="TFT-type style\dp_zc03.pvg" BorderColor="0xcccccc 16777215" FrnColor="0x0 -1" BgColor="0xffffff 0" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="1" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
			<DispFormat DispType="2" DigitCount="1 2" DataLimit="0 1092605706" DataRange="0.000000 9.990000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="299" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
			<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
			<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
		<PartInfo PartType="Text" PartName="TXT_0">
			<General TextContent="Novo tempo" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="16 326 126 126 126 126 126 126 12" Bold="0" StartPt="164 322"/>
			<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo>
	<PartInfo PartType="Line" PartName="LN_0">
		<General BorderColor="0x0 0" StartPt="25 309" EndPt="445 309" AutoAdsorption="20"/></PartInfo>
	<PartInfo PartType="BitSwitch" PartName="Bit Switch0">
		<General Desc="BS_3" Area="401 120 465 184" OperateAddr="SP_EDIT_flag" Fast="0" Monitor="1" MonitorAddr="SP_EDIT_flag" FigureFile="" BorderColor="0xcccccc 0" BmpIndex="131" LaStartPt="32 32" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
		<Label Status="0" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/>
		<Label Status="1" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/></PartInfo></ScrInfo>
