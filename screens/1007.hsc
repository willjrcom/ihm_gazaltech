<?xml version="1.0" encoding="UTF-8"?>
<ScrInfo ScreenNo="1007" ScreenType="" ScreenSize="1">
<Script>
		<InitialAction>@W_HSW208=0
@W_HSW209=0
</InitialAction>
		<TrigAction/>
		<CloseAction/>
	</Script>
<PartInfo PartType="Rect" PartName="BG_0">
<General Area="0 0 480 800" BorderColor="0xf4f7fb 0" Pattern="1" FrnColor="0xf4f7fb -1" BgColor="0xf4f7fb -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="HEADER_BG">
<General Area="0 0 480 112" BorderColor="0xf172a 0" Pattern="1" FrnColor="0xf172a -1" BgColor="0xf172a -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TITLE_0">
<General TextContent="Faixa de Dados" LaFrnColor="0xffffff -1" IsBackColor="0" BgColor="0xf172a 0" CharSize="304" Bold="1" StartPt="92 22"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="SUBTITLE_0">
<General TextContent="Periodo das tendencias" LaFrnColor="0xcbd5e1 -1" IsBackColor="0" BgColor="0xf172a 0" CharSize="233" Bold="0" StartPt="92 60"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="HEADER_ACCENT">
<General Area="92 92 204 97" BorderColor="0x6366f1 0" Pattern="1" FrnColor="0x6366f1 -1" BgColor="0x6366f1 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="FunctionSwitch" PartName="FS_MENU_OPEN">
<General Desc="FS_MENU_OPEN" Area="24 28 80 84" ScrSwitch="0" FuncFunc="2" ScreenNo="-1" ScreenNo2="1003" PointPos="0 0" PopupScreenType="1" PopupCloseWithParent="1" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 16777215" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="140" LaStartPt="12 12" Transparent="0" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="WordSwitch" PartName="Word Switch1">
		<General Desc="WS_0" WordAddr="HSW000208" WriteAddr="HSW000208" DataFormat="2" Const="1" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xd7dee8 0" BmpIndex="126" LaStartPt="0 0" IsIndirectR="0" IsIndirectW="0" IsWordOrder="0" Area="400 28 456 84" FrnColor="0xffffff -1" BgColor="0xffffff -1" Align="3"/>
		<Extension IsCheck="0" UseShowHide="0" HideType="0" IsHideAllTime="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0x22c55e 0" BgColor="0x22c55e 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_RANGE">
<General Area="24 148 456 356" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_RANGE">
<General Area="24 148 30 356" BorderColor="0x6366f1 0" Pattern="1" FrnColor="0x6366f1 -1" BgColor="0x6366f1 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_UP">
<General TextContent="Inicio" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 174"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_UP_SUB">
<General TextContent="Valor superior" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="48 208"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="Numeric Input/Display1">
		<General Desc="NUM_0" WordAddr="HSW004586" Fast="0" IsInput="1" WriteAddr="HSW004586" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0" Area="248 170 420 232"/>
		<DispFormat DispType="6" DigitCount="5 0" DataLimit="3338665472 1191181824" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="233" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_DOWN">
<General TextContent="Fim" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 274"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_DOWN_SUB">
<General TextContent="Valor inferior" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="48 308"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="Numeric Input/Display0">
		<General Desc="NUM_0" WordAddr="HSW004587" Fast="0" IsInput="1" WriteAddr="HSW004587" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0" Area="248 270 420 332"/>
		<DispFormat DispType="6" DigitCount="5 0" DataLimit="3338665472 1191181824" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="233" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_LINES">
<General Area="24 390 456 632" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_LINES">
<General Area="24 390 30 632" BorderColor="0x0ea5e9 0" Pattern="1" FrnColor="0x0ea5e9 -1" BgColor="0x0ea5e9 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_LINES">
<General TextContent="Linhas do grafico" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 408"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="WordSwitch" PartName="Word Switch0">
		<General Desc="WS_0" WordAddr="HSW000209" WriteAddr="HSW000209" DataFormat="2" Const="1" FigureFile="" BorderColor="0xf4f7fb 0" BmpIndex="-1" LaStartPt="0 0" IsIndirectR="0" IsIndirectW="0" IsWordOrder="0" Area="0 0 1 1" FrnColor="0xf4f7fb 0" BgColor="0xf4f7fb 0" Align="3" Transparent="1"/>
		<Extension IsCheck="0" UseShowHide="0" HideType="0" IsHideAllTime="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xf4f7fb 0" BgColor="0xf4f7fb 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xf4f7fb 0"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_LINE_0">
<General TextContent="Linha 1" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="14" Bold="1" StartPt="48 470"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="Bit Switch0">
		<General Desc="BS_0" OperateAddr="HSX8780.00" Fast="0" BitFunc="3" Monitor="1" MonitorAddr="HSX8780.00" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 0" BmpIndex="143" LaStartPt="0 0" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" Area="134 458 218 504" FrnColor="0xffffff -1" BgColor="0xffffff -1" Align="3"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1"/>
		<Label Status="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1" Pattern="1"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_LINE_1">
<General TextContent="Linha 3" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="14" Bold="1" StartPt="246 470"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="Bit Switch2">
		<General Desc="BS_0" OperateAddr="HSX8780.02" Fast="0" BitFunc="3" Monitor="1" MonitorAddr="HSX8780.02" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 0" BmpIndex="143" LaStartPt="0 0" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" Area="344 458 428 504" FrnColor="0xffffff -1" BgColor="0xffffff -1" Align="3"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1"/>
		<Label Status="1" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_LINE_2">
<General TextContent="Linha 2" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="14" Bold="1" StartPt="48 568"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="Bit Switch1">
		<General Desc="BS_0" OperateAddr="HSX8780.01" Fast="0" BitFunc="3" Monitor="1" MonitorAddr="HSX8780.01" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 0" BmpIndex="143" LaStartPt="0 0" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" Area="134 556 218 602" FrnColor="0xffffff -1" BgColor="0xffffff -1" Align="3"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1"/>
		<Label Status="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1" Pattern="1"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_LINE_3">
<General TextContent="Linha 4" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="14" Bold="1" StartPt="246 568"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="Bit Switch3">
		<General Desc="BS_0" OperateAddr="HSX8780.03" Fast="0" BitFunc="3" Monitor="1" MonitorAddr="HSX8780.03" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 0" BmpIndex="143" LaStartPt="0 0" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" Area="344 556 428 602" FrnColor="0xffffff -1" BgColor="0xffffff -1" Align="3"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1"/>
		<Label Status="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1" Pattern="1"/></PartInfo></ScrInfo>
