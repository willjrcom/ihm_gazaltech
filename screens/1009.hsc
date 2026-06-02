<?xml version="1.0" encoding="UTF-8"?>
<ScrInfo ScreenNo="1009" ScreenType="" ScreenSize="0">
<Script>
		<TimerAction/>
		<TrigAction>
			<Trigger Action="1" BitAddr="HSX4077.0">'设置期数加1
@w_HSW004077 =0 
if @w_HSW004079&lt; @w_HSW004088 then   '当前设置的期数小于总期数
   @w_HSW004079=@w_HSW004079+1
 @W_HSW4073 =1 ' 用于触发当前期数信息给start Unit
  
endif


</Trigger>
			<Trigger Action="1" BitAddr="HSX4078.00">'设置期数减1
@w_HSW4078 =0 
if @w_HSW4079&gt;1 then   '当前设置的期数&gt;0
   @w_HSW4079=@w_HSW4079-1
   @w_HSW4073=1 '用于触发当前期数信息给start Unit
endif

</Trigger>
		</TrigAction>
		<InitialAction>@w_HSW004079=1
@w_HSW004073=1
</InitialAction>
	</Script>
<PartInfo PartType="Rect" PartName="BG_0">
<General Area="0 0 480 800" BorderColor="0xf4f7fb 0" Pattern="1" FrnColor="0xf4f7fb -1" BgColor="0xf4f7fb -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="HEADER_BG">
<General Area="0 0 480 112" BorderColor="0xf172a 0" Pattern="1" FrnColor="0xf172a -1" BgColor="0xf172a -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TITLE_0">
<General TextContent="Periodo Manutencao" LaFrnColor="0xffffff -1" IsBackColor="0" BgColor="0xf172a 0" CharSize="304" Bold="1" StartPt="92 22"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="SUBTITLE_0">
<General TextContent="Configuracao de validade" LaFrnColor="0xcbd5e1 -1" IsBackColor="0" BgColor="0xf172a 0" CharSize="233" Bold="0" StartPt="92 60"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="HEADER_ACCENT">
<General Area="92 92 204 97" BorderColor="0xf59e0b 0" Pattern="1" FrnColor="0xf59e0b -1" BgColor="0xf59e0b -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="FunctionSwitch" PartName="FS_MENU_OPEN">
<General Desc="FS_MENU_OPEN" Area="24 28 80 84" ScrSwitch="0" FuncFunc="2" ScreenNo="-1" ScreenNo2="1003" PointPos="0 0" PopupScreenType="1" PopupCloseWithParent="1" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 16777215" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="140" LaStartPt="12 12" Transparent="0" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="WordSwitch" PartName="WS_2">
		<General Desc="WS_1" WordAddr="HSW4075" WriteAddr="HSW4075" DataFormat="2" Const="1" Limit="12" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xd7dee8 0" BmpIndex="126" LaStartPt="0 0" IsIndirectR="0" IsIndirectW="0" IsWordOrder="0" Area="400 28 456 84" FrnColor="0xffffff -1" BgColor="0xffffff -1" Align="3"/>
		<Extension IsCheck="0" AckTime="20" UseShowHide="0" HideType="0" IsHideAllTime="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0x22c55e 0" BgColor="0x22c55e 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_PERIOD">
<General Area="24 132 456 360" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_PERIOD">
<General Area="24 132 30 360" BorderColor="0xf59e0b 0" Pattern="1" FrnColor="0xf59e0b -1" BgColor="0xf59e0b -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_TOTAL">
<General TextContent="Total de periodos" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 160"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_1">
		<General Desc="NUM_0" WordAddr="HSW4088" Fast="0" IsInput="1" WriteAddr="HSW4088" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0" Area="290 150 420 202"/>
		<DispFormat DispType="2" DigitCount="4 0" DataLimit="0 1094713344" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="233" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_START">
<General TextContent="Periodo inicial" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 230"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_5">
		<General Desc="NUM_0" WordAddr="HSW4089" Fast="0" IsInput="1" WriteAddr="HSW4089" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0" Area="290 220 420 272"/>
		<DispFormat DispType="2" DigitCount="4 0" DataLimit="0 1094713344" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="233" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_CURRENT">
<General TextContent="Periodo atual" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 300"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_0">
		<General Desc="NUM_0" WordAddr="HSW4079" Fast="0" IsInput="0" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xffffff 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0" Area="266 290 362 342"/>
		<DispFormat DispType="2" DigitCount="2 0" DataLimit="0 1120272384" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="233" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
		<Extension IsCheck="0" AckTime="20" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
<PartInfo PartType="WordSwitch" PartName="WS_0">
		<General Desc="WS_0" WordAddr="HSW4078" WriteAddr="HSW4078" DataFormat="2" Const="1" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xd7dee8 0" BmpIndex="128" LaStartPt="0 0" IsIndirectR="0" IsIndirectW="0" IsWordOrder="0" Area="208 290 256 342" FrnColor="0xffffff -1" BgColor="0xffffff -1" Align="3"/>
		<Extension IsCheck="0" AckTime="20" UseShowHide="0" HideType="0" IsHideAllTime="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0x94a3b8 0" BgColor="0x94a3b8 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="WordSwitch" PartName="WS_1">
		<General Desc="WS_1" WordAddr="HSW4077" WriteAddr="HSW4077" DataFormat="2" Const="1" Limit="12" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xd7dee8 0" BmpIndex="151" LaStartPt="0 0" IsIndirectR="0" IsIndirectW="0" IsWordOrder="0" Area="372 290 420 342" FrnColor="0xffffff -1" BgColor="0xffffff -1" Align="3"/>
		<Extension IsCheck="0" AckTime="20" UseShowHide="0" HideType="0" IsHideAllTime="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xf59e0b 0" BgColor="0xf59e0b 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_PASS">
<General Area="24 384 456 532" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_PASS">
<General Area="24 384 30 532" BorderColor="0x94a3b8 0" Pattern="1" FrnColor="0x94a3b8 -1" BgColor="0x94a3b8 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_ADMIN_PASS">
<General TextContent="Senha superior" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 414"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="String" PartName="STR_0">
		<General Desc="STR_0" WordAddr="HSW4084" Fast="0" stCount="8" IsInput="1" WriteAddr="HSW4084" KbdScreen="-1" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" CharSize="233" IsHideNum="0" Transparent="0" IsShowPwd="1" IsIndirectR="0" IsIndirectW="0" IsInputDefault="0" IsDWord="0" IsHiLowRever="0" Area="220 402 420 452"/>
		<Extension IsCheck="0" AckTime="5" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_PASS">
<General TextContent="Senha" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 478"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="String" PartName="STR_1">
		<General Desc="STR_0" WordAddr="HSW004090" Fast="0" stCount="8" IsInput="1" WriteAddr="HSW004090" KbdScreen="-1" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" CharSize="233" IsHideNum="0" Transparent="0" IsShowPwd="1" IsIndirectR="0" IsIndirectW="0" IsInputDefault="0" IsDWord="0" IsHiLowRever="0" Area="220 466 420 516"/>
		<Extension IsCheck="0" AckTime="5" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_DATE">
<General Area="24 548 456 704" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_DATE">
<General Area="24 548 30 704" BorderColor="0x0ea5e9 0" Pattern="1" FrnColor="0x0ea5e9 -1" BgColor="0x0ea5e9 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_DATE">
<General TextContent="Validade" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 572"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_6">
		<General Desc="NUM_0" WordAddr="HSW4096" Fast="0" IsInput="1" WriteAddr="HSW4096" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0" Area="58 610 154 662"/>
		<DispFormat DispType="2" DigitCount="2 0" DataLimit="1065353216 1106771968" DataRange="1.000000 31.000000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="233" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_4">
		<General Desc="NUM_0" WordAddr="HSW4095" Fast="0" IsInput="1" WriteAddr="HSW4095" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0" Area="192 610 288 662"/>
		<DispFormat DispType="2" DigitCount="2 0" DataLimit="1065353216 1094713344" DataRange="1.000000 12.000000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="233" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_2">
		<General Desc="NUM_0" WordAddr="HSW4094" Fast="0" IsInput="1" WriteAddr="HSW4094" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0" Area="326 610 422 662"/>
		<DispFormat DispType="2" DigitCount="4 0" DataLimit="1156988928 1161527296" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="233" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_DAY">
<General TextContent="Dia" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="1" StartPt="58 670"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_MONTH">
<General TextContent="Mes" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="1" StartPt="192 670"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_YEAR">
<General TextContent="Ano" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="1" StartPt="326 670"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="WordSwitch" PartName="WS_3">
		<General Desc="WS_1" WordAddr="HSW4076" WriteAddr="HSW4076" DataFormat="2" Const="1" Limit="12" FigureFile="" BorderColor="0xf4f7fb 0" BmpIndex="-1" LaStartPt="0 0" IsIndirectR="0" IsIndirectW="0" IsWordOrder="0" Area="0 0 1 1" FrnColor="0xf4f7fb 0" BgColor="0xf4f7fb 0" Align="3" Transparent="1"/>
		<Extension IsCheck="0" AckTime="20" UseShowHide="0" HideType="0" IsHideAllTime="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xf4f7fb 0" BgColor="0xf4f7fb 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xf4f7fb 0"/></PartInfo>
<PartInfo PartType="WordSwitch" PartName="WS_4">
		<General Desc="WS_1" WordAddr="HSW4074" WriteAddr="HSW4074" DataFormat="2" Const="1" Limit="12" FigureFile="" BorderColor="0xf4f7fb 0" BmpIndex="-1" LaStartPt="0 0" IsIndirectR="0" IsIndirectW="0" IsWordOrder="0" Area="0 0 1 1" FrnColor="0xf4f7fb 0" BgColor="0xf4f7fb 0" Align="3" Transparent="1"/>
		<Extension IsCheck="0" AckTime="20" UseShowHide="0" HideType="0" IsHideAllTime="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="760497748" FrnColor="0xf4f7fb 0" BgColor="0xf4f7fb 0" Bold="0" LaIndexID="" CharSize="6 12" LaFrnColor="0xf4f7fb 0"/></PartInfo></ScrInfo>
