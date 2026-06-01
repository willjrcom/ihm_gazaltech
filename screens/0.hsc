<?xml version="1.0" encoding="UTF-8"?>
<ScrInfo ScreenNo="0" ScreenType="" ScreenSize="0">
<Script>
		<InitialAction>@iniciotransicao = 1 'tempo para inibir bug da ihm

if @des = 0 then 
@des = 60 
endif
</InitialAction>
		<TrigAction>
			<Trigger Action="3" BitAddr="Eco_command">' Armazena tela no temporario
 @W_HDW8300 = @w_1:46
 @W_HDW8301 = @w_1:4692

' Envia economico para tela
 @w_1:46 = @SP_Temperatura_ECO
 @w_1:4692 = @SP_speed_ECO
</Trigger>
			<Trigger Action="4" BitAddr="Eco_command">' Envia memorizado para tela
 @w_1:46 = @W_HDW8300
 @w_1:4692 = @W_HDW8301
</Trigger>
			<Trigger Action="3" BitAddr="outconfig">@W_hdw0 = 1
@outconfig = 0
</Trigger>
			<Trigger Action="3" BitAddr="turnon">'IF @liga_desliga = TRUE Then
@W_1:415 = 0 ' modo controle automatico
@W_1:4656 = 3	' o2F = AL 		- Função da saída out2 = Alarme de temperatura

' Alarme ação reversa
@W_1:4658 = 1	' o2AC = ReU 
@W_1:4658 = 0	' o2AC = ReU 

'ELSE
'	@W_1:415 = 2 ' modo stand-by
'	@W_1:4656 = 0	' o2F = None 		- Função da saída out2 = none
'	@W_1:4658 = 0	' o2AC = Dir 	- Alarme ação direta
'	@turnon = FALSE
'ENDIF
</Trigger>
			<Trigger Action="4" BitAddr="turnon">'@W_1:415 = 2 ' modo controle stand-by
'@W_1:4656 = 0	' o2F = nonE
'@W_1:4658 = 0	' o2AC = Dir	- Alarme ação direta
</Trigger>
			<Trigger Action="3" BitAddr="liga_desliga">@b_1:449.0 = 1		'run/stop speed out = start
@B_1:4550.0 = TRUE ' o3t = ON liga ventilacao e esteira



</Trigger>
			<Trigger Action="4" BitAddr="liga_desliga">@W_1:415 = 2 ' modo controle stand-by
@W_1:4656 = 0	' o2F = none	
@W_1:4658 = 0	' o2AC = dir

@B_1:4550.0 = 0 ' out3 = OFF liga ventilacao e esteira
</Trigger>
			<Trigger Action="1" BitAddr="ECO_ON">' Armazena tela no temporario
@ECO=TRUE
 @W_HDW8300 = @w_1:46
 @W_HDW8301 = @w_1:4692

' Envia economico para tela
 @w_1:46 = @SP_Temperatura_ECO
 @w_1:4692 = @SP_speed_ECO

IF  @w_1:46 = @SP_Temperatura_ECO AND @w_1:4692 = @SP_speed_ECO THEN
@ECO_ON=FALSE
ENDIF
</Trigger>
			<Trigger Action="1" BitAddr="ECO_OFF">' Envia memorizado para tela
 @w_1:46 = @W_HDW8300
 @w_1:4692 = @W_HDW8301

IF @w_1:46 = @W_HDW8300 AND @w_1:4692 = @W_HDW8301 THEN
@ECO_OFF=FALSE
@ECO=FALSE
ENDIF
</Trigger></TrigAction>
		<TimerAction>
			<Timer Interval="2">@controlpizza = @b_1:449.0 ' start saida velocidade


</Timer></TimerAction>
		<CloseAction>@fimtransicao = 0 'reset no temporizador do bug
</CloseAction></Script>
<PartInfo PartType="DirShow" PartName="DIW_2">
<General Desc="DIW_0" Area="0 0 480 800" TriggAddr="SP_EDIT_flag" ScreenNo="21" IsWindow="0" TriggerMode="0" IsTop="0" SetModuelWnw="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="DirShow" PartName="DIW_1">
<General Desc="DIW_1" Area="0 0 480 800" TriggAddr="ECO" ScreenNo="33" IsWindow="0" TriggerMode="0" IsTop="0" SetModuelWnw="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="BG_0">
<General Area="0 0 480 800" BorderColor="0xf4f7fb 0" Pattern="1" FrnColor="0xf4f7fb -1" BgColor="0xf4f7fb -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="HEADER_BG">
<General Area="0 0 480 116" BorderColor="0xf172a 0" Pattern="1" FrnColor="0xf172a -1" BgColor="0xf172a -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="FunctionSwitch" PartName="FS_MENU_OPEN">
<General Desc="FS_MENU_OPEN" Area="24 28 80 84" ScrSwitch="0" FuncFunc="2" ScreenNo="-1" ScreenNo2="1003" PointPos="0 0" PopupScreenType="1" PopupCloseWithParent="1" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 16777215" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="140" LaStartPt="12 12" Transparent="0" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="Text" PartName="TITLE_0">
<General TextContent="Forno Gazal" LaFrnColor="0xffffff -1" IsBackColor="0" BgColor="0xf172a 0" CharSize="304" Bold="1" StartPt="92 22"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="SUBTITLE_0">
<General TextContent="Painel principal" LaFrnColor="0xcbd5e1 -1" IsBackColor="0" BgColor="0xf172a 0" CharSize="233" Bold="0" StartPt="92 60"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="HEADER_ACCENT">
<General Area="92 94 204 100" BorderColor="0x22c55e 0" Pattern="1" FrnColor="0x22c55e -1" BgColor="0x22c55e -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="HEADER_CLOCK">
<General Area="292 20 456 88" BorderColor="0x22324c 0" Pattern="1" FrnColor="0x10213a -1" BgColor="0x10213a -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_CLOCK_HEAD">
<General TextContent="Horario" LaFrnColor="0xcbd5e1 -1" IsBackColor="0" BgColor="0x10213a 0" CharSize="8 16" Bold="0" StartPt="316 28"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="TimeDisplay" PartName="TIME_0">
<General Desc="TIME_0" Area="312 42 448 84" FigureFile="" BorderColor="0x10213a 0" FrnColor="0xffffff -1" BgColor="0x10213a -1" CharSize="304" Transparent="0"/>
<MoveZoom DataFormatMZ="4" DataLimitMZ="1174011904 1176256512" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_RECIPE">
<General Area="24 128 456 242" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_RECIPE">
<General Area="24 128 30 242" BorderColor="0xf59e0b 0" Pattern="1" FrnColor="0xf59e0b -1" BgColor="0xf59e0b -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_RECIPE">
<General TextContent="Receita ativa" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 150"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="String" PartName="STR_0">
<General Desc="STR_0" Area="48 180 360 226" WordAddr="nome_tela_0" Fast="0" stCount="13" IsInput="0" WriteAddr="nome_tela_0" KbdScreen="1001" IsPopKeyBrod="0" FigureFile="" Remark="Receita nº 1" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" CharSize="233" Align="1" IsHideNum="0" Transparent="0" IsShowPwd="0" IsIndirectR="0" IsIndirectW="0" IsInputDefault="0" IsDWord="1" IsHiLowRever="0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="FunctionSwitch" PartName="FS_0">
<General Desc="FS_0" Area="384 158 444 218" ScrSwitch="1" ScreenNo="8" ScreenNo2="-1" PointPos="0 0" PopupScreenType="0" PopupCloseWithParent="0" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 16777215" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="30" LaStartPt="30 30" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_RECIPE_BTN">
<General TextContent="Receitas" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="382 222"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_CURRENT">
<General Area="24 258 228 450" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_CURRENT">
<General Area="24 258 30 450" BorderColor="0xef4444 0" Pattern="1" FrnColor="0xef4444 -1" BgColor="0xef4444 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Bitmap" PartName="ICO_CURRENT">
<General StartPt="48 278" Width="46" Height="46" BmpIndex="141"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_CURRENT">
<General TextContent="Atual" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="104 278"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_CURRENT_SUB">
<General TextContent="Temperatura" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="104 312"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_0">
<General Desc="NUM_0" Area="44 342 180 426" WordAddr="1:41" Fast="0" IsInput="0" WriteAddr="1:41" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xef4444 -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="6" DigitCount="3 0" DataLimit="3296313344 1148829696" DataRange="-999.000000 999.000000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="304" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_CURRENT_UNIT">
<General TextContent="C" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="0" StartPt="184 372"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_DESIRED">
<General Area="252 258 456 450" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_DESIRED">
<General Area="252 258 258 450" BorderColor="0x22c55e 0" Pattern="1" FrnColor="0x22c55e -1" BgColor="0x22c55e -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Bitmap" PartName="ICO_DESIRED">
<General StartPt="276 278" Width="46" Height="46" BmpIndex="141"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_DESIRED">
<General TextContent="Desejada" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="332 278"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_DESIRED_SUB">
<General TextContent="Setpoint" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="332 312"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_1">
<General Desc="NUM_0" Area="272 342 408 426" WordAddr="1:46" Fast="0" IsInput="0" WriteAddr="1:46" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0x22c55e -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="6" DigitCount="3 0" DataLimit="0 1148829696" DataRange="0.000000 999.000000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="304" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_DESIRED_UNIT">
<General TextContent="C" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="0" StartPt="412 372"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_TIME">
<General Area="24 470 228 676" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_TIME">
<General Area="24 470 30 676" BorderColor="0x6366f1 0" Pattern="1" FrnColor="0x6366f1 -1" BgColor="0x6366f1 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Bitmap" PartName="ICO_TIME">
<General StartPt="48 498" Width="42" Height="42" BmpIndex="139"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_TIME">
<General TextContent="Tempo" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="104 498"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_2">
<General Desc="NUM_0" Area="48 570 166 642" WordAddr="1:4692" Fast="0" IsInput="0" WriteAddr="1:4692" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="1" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="2" DigitCount="1 2" DataLimit="0 1092605706" DataRange="0.000000 9.990000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="262" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_TIME_UNIT">
<General TextContent="min" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="170 595"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_MIN">
<General Area="252 470 456 676" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_MIN">
<General Area="252 470 258 676" BorderColor="0x0ea5e9 0" Pattern="1" FrnColor="0x0ea5e9 -1" BgColor="0x0ea5e9 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Bitmap" PartName="ICO_MIN">
<General StartPt="276 498" Width="42" Height="42" BmpIndex="145"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_MIN">
<General TextContent="Minimo" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="332 498"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Numeric" PartName="NUM_3">
<General Desc="NUM_0" Area="298 570 412 642" WordAddr="1:4690" Fast="0" IsInput="0" WriteAddr="1:4690" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" BmpIndex="-1" Transparent="0" IsHideNum="0" HighZeroPad="1" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="2" DigitCount="2 2" DataLimit="0 1120402145" DataRange="0.000000 99.990000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="262" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="FOOTER_BG">
<General Area="24 688 456 784" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="BS_3">
<General Desc="BS_3" Area="52 704 116 768" OperateAddr="SP_EDIT_flag" Fast="0" BitFunc="1" Monitor="1" MonitorAddr="SP_EDIT_flag" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 0" BmpIndex="127" LaStartPt="24 24" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="6 12" LaFrnColor="0xffffff -1"/>
<Label Status="1" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_FOOT_EDIT">
<General TextContent="Editar" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="58 766"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="BS_0">
<General Desc="BS_0" Area="208 704 272 768" OperateAddr="ECO_ON" Fast="0" BitFunc="1" Monitor="1" MonitorAddr="ECO_ON" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 0" BmpIndex="123" LaStartPt="32 32" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" CharSize="6 12" LaFrnColor="0xffffff -1"/>
<Label Status="1" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_FOOT_ECO">
<General TextContent="Eco" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="226 766"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="FunctionSwitch" PartName="FS_FOOT_RECIPE">
<General Desc="FS_FOOT_RECIPE" Area="364 704 428 768" ScrSwitch="1" ScreenNo="8" ScreenNo2="-1" PointPos="0 0" PopupScreenType="0" PopupCloseWithParent="0" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 16777215" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="30" LaStartPt="8 8" Transparent="0" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_FOOT_RECIPE">
<General TextContent="Receitas" LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="368 766"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="NewTimer" PartName="Timer_0">
<General Area="9 101 51 153" Timer_Describe="config" Timer_Unit="1" Timer_FuncSwitch="master" Timer_TimerRun="config" Timer_SetTimerEdit="tempocofig" Timer_BitAddrEdit="outconfig" Timer_SetTimerCanChange="0" Timer_Repead_Trigger="0" Timer_BitAddr="1" Timer_WordAddr="0" Timer_PassedTime="0" Timer_ResetPassedTime="0" Const="1"/></PartInfo>
<PartInfo PartType="NewTimer" PartName="Timer_1">
<General Area="8 61 63 112" Timer_Describe="transicao" Timer_Unit="1" Timer_FuncSwitch="master" Timer_TimerRun="iniciotransicao" Timer_SetTimerEdit="tempotransicao" Timer_BitAddrEdit="fimtransicao" Timer_SetTimerCanChange="0" Timer_Repead_Trigger="0" Timer_BitAddr="1" Timer_WordAddr="0" Timer_PassedTime="0" Timer_ResetPassedTime="0" Const="1"/></PartInfo>
<PartInfo PartType="Numeric" PartName="Numeric Input/Display0">
<General Desc="NUM_0" Area="470 4 476 10" WordAddr="1:4653" Fast="0" IsInput="0" WriteAddr="1:4653" KbdScreen="1000" IsPopKeyBrod="0" FigureFile="" BorderColor="0xf172a 0" FrnColor="0xf172a 0" BgColor="0xf172a 0" BmpIndex="-1" Transparent="1" IsHideNum="0" HighZeroPad="0" IsShowPwd="0" UseGlint="0" GlintFgClr="0x0 0" ZeroNoDisplay="0" IsIndirectR="0" IsIndirectW="0" IsAddFrame="0" IsWordOrder="0"/>
<DispFormat DispType="6" DigitCount="3 0" DataLimit="0 1148829696" DataRange="0.000000 999.000000" IsVar="0" Zoom="0" Mutiple="1.000000" Round="0" CharSize="6 12" IsInputLabelL="0" IsInputLabelR="0" IsInputDefault="0" bShowRange="0" IsVar1="0" ColorHText="0x0 0" ColorHBag="0x0 0" ColorLText="0x0 0" ColorLBag="0x0 0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></ScrInfo>
