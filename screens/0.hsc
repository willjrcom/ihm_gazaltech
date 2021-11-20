<?xml version="1.0" encoding="UTF-8"?>
<ScrInfo ScreenNo="0" ScreenType="" ScreenSize="0">
	<Script>
		<InitialAction>@iniciotransicao = 1 'tempo para inibir bug da ihm

if @des = 0 then 
@des = 60 
endif
</InitialAction>
		<TrigAction>
			<Trigger Action="3" BitAddr="Eco_command">
@SP_MEM = @w_1:46
@VELOC_MEM = @w_1:4692


@w_1:4692 = @SP_speed_ECO
@w_1:46 = @SP_Temperatura_ECO



</Trigger>
			<Trigger Action="4" BitAddr="Eco_command">@w_1:46 = @SP_MEM
@w_1:4692 = @VELOC_MEM 



</Trigger>
			<Trigger Action="3" BitAddr="outconfig">@W_hdw0 = 1
@outconfig = 0
</Trigger>
			<Trigger Action="3" BitAddr="turnon">

IF @liga_desliga = TRUE Then
	@W_1:415 = 0 ' modo controle automatico
	@W_1:4656 = 3	' o2F = AL 		- Função da saída out2 = Alarme de temperatura
	@W_1:4658 = 1	' o2AC = ReU 	- Alarme ação reversa
ELSE
	@W_1:415 = 2 ' modo stand-by
	@W_1:4656 = 0	' o2F = None 		- Função da saída out2 = none
	@W_1:4658 = 0	' o2AC = Dir 	- Alarme ação direta
	@turnon = FALSE
ENDIF
</Trigger>
			<Trigger Action="4" BitAddr="turnon">@W_1:415 = 2 ' modo controle stand-by
@W_1:4656 = 0	' o2F = nonE
@W_1:4658 = 0	' o2AC = Dir	- Alarme ação direta
</Trigger>
			<Trigger Action="3" BitAddr="liga_desliga">@b_1:449.0 = 1		'run/stop speed out = start
@B_1:4550.0 = TRUE ' o3t = ON liga ventilacao e esteira



</Trigger>
			<Trigger Action="4" BitAddr="liga_desliga">@W_1:415 = 2 ' modo controle stand-by
@W_1:4656 = 0	' o2F = none	
@W_1:4658 = 0	' o2AC = dir

@turnon = false

@B_1:4550.0 = 0 ' out3 = OFF
</Trigger>
		</TrigAction>
		<TimerAction>
			<Timer Interval="2">@controlpizza = @b_1:449.0 ' start saida velocidade


</Timer></TimerAction>
		<CloseAction>@fimtransicao = 0 'reset no temporizador do bug
</CloseAction></Script>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="DirShow" PartName="DIW_0">
<General Desc="DIW_2" Area="0 63 480 463" TriggAddr="alarme_gas" ScreenNo="9" IsWindow="0" TriggerMode="0" IsTop="0" SetModuelWnw="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="DirShow" PartName="DIW_1">
<General Desc="DIW_1" Area="0 86 480 486" TriggAddr="Eco_command" ScreenNo="22" IsWindow="0" TriggerMode="0" IsTop="0" SetModuelWnw="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="DirShow" PartName="DIW_2">
<General Desc="DIW_0" Area="0 110 480 610" TriggAddr="SP_EDIT_flag" ScreenNo="21" IsWindow="0" TriggerMode="0" IsTop="0" SetModuelWnw="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo>
<PartInfo PartType="Rect" PartName="REC_0">
<General Area="10 690 470 790" BorderColor="0x0 0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Rect" PartName="REC_5">
<General Area="13 12 468 163" BorderColor="0x0 0" Pattern="1" FrnColor="0x0 -1" BgColor="0x0 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Bitmap" PartName="BMP_0">
<General Desc="BMP_0" StartPt="11 10" Width="458" Height="154" BmpIndex="86"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo>
<PartInfo PartType="Rect" PartName="REC_4">
<General Area="10 170 470 290" BorderColor="0x0 0" Pattern="1" FrnColor="0xffffff 0" BgColor="0x0 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Text" PartName="TXT_12">
<General TextContent="Receita:" LaFrnColor="0x0 0" IsBackColor="0" BgColor="0xffffff 0" CharSize="2986 126 126 126 126 126 126 12" Bold="0" StartPt="148 181"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="String" PartName="STR_0">
<General Desc="STR_0" Area="148 230 465 280" WordAddr="nome_tela_0" Fast="0" stCount="16" IsInput="0" WriteAddr="nome_tela_0" KbdScreen="1001" IsPopKeyBrod="0" FigureFile="" Remark="Receita nº 1" BorderColor="0xe8ceba 0" FrnColor="0x0 -1" BgColor="0xc0c0c0 -1" CharSize="298" Align="1" IsHideNum="0" Transparent="1" IsShowPwd="0" IsIndirectR="0" IsIndirectW="0" IsInputDefault="0" IsDWord="1" IsHiLowRever="0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Rect" PartName="REC_3">
<General Area="10 495 235 685" BorderColor="0x0 0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Text" PartName="TXT_5">
<General TextContent="Tempo" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="2986 126 126 126 126 126 126 12" Bold="0" StartPt="84 510"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Bitmap" PartName="BMP_2">
<General Desc="BMP_2" StartPt="46 518" Width="30" Height="40" BmpIndex="107"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Numeric" PartName="NUM_2">
<General Desc="NUM_0" Area="22 572 172 672" WordAddr="1:4692" Fast="0" IsInput="0" WriteAddr="1:4692" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xcccccc 16777215" FrnColor="0x0 -1" BgColor="0xffffff 0" BmpIndex="27" Transparent="0" IsHideNum="0" HighZeroPad="1" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="2" DigitCount="1 2" DataLimit="0 1092605706" DataRange="0.000000 9.990000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="299" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_4">
<General TextContent="sec" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="2986 126 126 126 126 126 126 12" Bold="0" StartPt="174 624"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Rect" PartName="REC_2">
<General Area="10 302 235 492" BorderColor="0x0 0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Bitmap" PartName="BMP_1">
<General Desc="BMP_1" StartPt="59 313" Width="25" Height="50" BmpIndex="106"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_1">
<General TextContent="Atual" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="2986 126 126 126 126 126 126 12" Bold="0" StartPt="91 315"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Numeric" PartName="NUM_0">
<General Desc="NUM_0" Area="25 382 175 482" WordAddr="1:41" Fast="0" IsInput="0" WriteAddr="1:41" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xcccccc 16777215" FrnColor="0xd7 -1" BgColor="0xffffff 0" BmpIndex="27" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="6" DigitCount="3 0" DataLimit="3296313344 1148829696" DataRange="-999.000000 999.000000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="299" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_0">
<General TextContent="ºC" LaFrnColor="0xd7 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="2986 126 126 126 126 126 126 12" Bold="0" StartPt="178 394"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo></PartInfo>
<PartInfo PartType="NewTimer" PartName="Timer_0">
<General Area="1 746 43 798" Timer_Describe="config" Timer_Unit="1" Timer_FuncSwitch="master" Timer_TimerRun="config" Timer_SetTimerEdit="tempocofig" Timer_BitAddrEdit="outconfig" Timer_SetTimerCanChange="0" Timer_Repead_Trigger="0" Timer_BitAddr="1" Timer_WordAddr="0" Timer_PassedTime="0" Timer_ResetPassedTime="0" Const="1"/></PartInfo>
<PartInfo PartType="NewTimer" PartName="Timer_1">
<General Area="1 693 56 744" Timer_Describe="transicao" Timer_Unit="1" Timer_FuncSwitch="master" Timer_TimerRun="iniciotransicao" Timer_SetTimerEdit="tempotransicao" Timer_BitAddrEdit="fimtransicao" Timer_SetTimerCanChange="0" Timer_Repead_Trigger="0" Timer_BitAddr="1" Timer_WordAddr="0" Timer_PassedTime="0" Timer_ResetPassedTime="0" Const="1"/></PartInfo>
<PartInfo PartType="Rect" PartName="REC_6">
<General Area="245 302 470 492" BorderColor="0x0 0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Bitmap" PartName="Picture0">
<General Desc="BMP_1" StartPt="265 313" Width="25" Height="50" BmpIndex="106"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="Text0">
<General TextContent="Desejada" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="2986 126 126 126 126 126 126 12" Bold="0" StartPt="297 315"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Numeric" PartName="NUM_1">
<General Desc="NUM_0" Area="255 382 405 482" WordAddr="1:46" Fast="0" IsInput="0" WriteAddr="1:46" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xcccccc 16777215" FrnColor="0x8000 -1" BgColor="0xffffff 0" BmpIndex="27" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="6" DigitCount="3 0" DataLimit="0 1148829696" DataRange="0.000000 999.000000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="299" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_2">
<General TextContent="ºC" LaFrnColor="0x8000 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="2986 126 126 126 126 126 126 12" Bold="0" StartPt="408 394"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo>
<PartInfo PartType="Rect" PartName="REC_1">
<General Area="245 495 470 685" BorderColor="0x0 0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="FunctionSwitch" PartName="FS_0">
<General Desc="FS_0" Area="46 198 110 262" ScrSwitch="1" ScreenNo="7" ScreenNo2="-1" PointPos="0 0" PopupScreenType="0" PopupCloseWithParent="0" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xcccccc 0" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="112" LaStartPt="25 25" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/></PartInfo>
<PartInfo PartType="TimeDisplay" PartName="TIME_0">
<General Desc="TIME_0" Area="256 515 459 571" FigureFile="" BorderColor="0xcccccc 0" FrnColor="0x0 0" BgColor="0xffffff 0" CharSize="14" Transparent="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="WordShow" PartName="WL_0">
<General Desc="WL_0" Area="10 690 470 790" WordAddr="plano_de_fundo" StatsNum="3" Fast="0" DataFormat="2" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xcccccc 0" BmpIndex="61" LaStartPt="230 50" StatusCovType="0" AnimaReturn="0" ByAddr="0" Trigger="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" isNautomatic="0" IsCtrlStaTextByAddr="0" isReturn="0" isStateControl="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0"/>
<Label Status="0" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/>
<Label Status="1" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/>
<Label Status="2" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0" UseGlint="0" GlintFgClr="0x0 0"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="BS_3">
<General Desc="BS_3" Area="49 708 113 772" OperateAddr="SP_EDIT_flag" Fast="0" BitFunc="1" Monitor="1" MonitorAddr="SP_EDIT_flag" FigureFile="" BorderColor="0xcccccc 0" BmpIndex="116" LaStartPt="32 32" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/>
<Label Status="1" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/></PartInfo>
<PartInfo PartType="FunctionSwitch" PartName="FS_1">
<General Desc="FS_1" Area="368 708 432 772" ScrSwitch="1" ScreenNo="1" ScreenNo2="-1" PointPos="0 0" PopupScreenType="0" PopupCloseWithParent="0" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xcccccc 0" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="111" LaStartPt="43 38" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="BS_0">
<General Desc="BS_0" Area="208 708 272 772" OperateAddr="Eco_command" Fast="0" BitFunc="3" Monitor="1" MonitorAddr="Eco_command" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xcccccc 0" BmpIndex="123" LaStartPt="32 32" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/>
<Label Status="1" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/></PartInfo>
<PartInfo PartType="NewTimer" PartName="Timer_2">
<General Area="101 754 172 785" Timer_Describe="config" Timer_Unit="1" Timer_FuncSwitch="master" Timer_TimerRun="config" Timer_SetTimerEdit="tempocofig" Timer_BitAddrEdit="outconfig" Timer_SetTimerCanChange="0" Timer_Repead_Trigger="0" Timer_BitAddr="1" Timer_WordAddr="0" Timer_PassedTime="0" Timer_ResetPassedTime="0" Const="1"/></PartInfo>
<PartInfo PartType="NewTimer" PartName="Timer_3">
<General Area="102 722 171 753" Timer_Describe="transicao" Timer_Unit="1" Timer_FuncSwitch="master" Timer_TimerRun="iniciotransicao" Timer_SetTimerEdit="tempotransicao" Timer_BitAddrEdit="fimtransicao" Timer_SetTimerCanChange="0" Timer_Repead_Trigger="0" Timer_BitAddr="1" Timer_WordAddr="0" Timer_PassedTime="0" Timer_ResetPassedTime="0" Const="1"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_3">
<General TextContent="mínimo:" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="2336 126 126 126 126 126 126 12" Bold="0" StartPt="283 584"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_3">
<General Desc="NUM_0" Area="311 624 403 655" WordAddr="1:4690" Fast="0" IsInput="0" WriteAddr="1:4690" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xcccccc 0" FrnColor="0x0 0" BgColor="0xffffff 0" BmpIndex="27" Transparent="0" IsHideNum="0" HighZeroPad="1" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="2" DigitCount="2 2" DataLimit="0 1120402145" DataRange="0.000000 99.990000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="232" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></ScrInfo>
