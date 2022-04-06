<?xml version="1.0" encoding="UTF-8"?>
<ScrInfo ScreenNo="5" ScreenType="" ScreenSize="0">
	<Script>
		<TrigAction>
			<Trigger Action="1" BitAddr="Reset_fabrica">@W_1:419 = -481

sleepA(8000)

@W_HSW19 = 0  	'buzzer ligado

@W_1:4686 = 0	' Spd.P = ASPr 	- repete o valor de velocidade antes de deligar
@W_1:4688 = 1	' Spd.t = tinE 	- refencia de velocidade = tempo
@W_1:4691 = 1	' n.SPd = 2 	- numero de setpoints de velocidade (normal/ECO)

@W_1:4653 = 1	' o1F = Hreg 	- Função da saída out1 = controle de temperatura
@W_1:4656 = 3	' o2F = AL 		- Função da saída out2 = Alarme de temperatura
@W_1:4657 = 1	' o2AL = AL1 	- alarme na saída 2 = Alarme 1
@W_1:4658 = 1	' o2AC = ReU 	- Alarme ação reversa
@W_1:4659 = 0	' o3F = nonE	- Não utilizado

@W_1:4662 = 2	' AL1t = HIab	- Alarme 1 = alarme de máxima absoluto
@W_1:4664 = 0	' AL1L = 0		- AL1L = 0
@W_1:4665 = 400	' AL1L = 400	- AL1H = 400

IF @W_1:4667 = 0 THEN 	
	@W_1:4667 = 1	' HAL1 = 1		- Histerese de alarme = 1 ºC
ENDIF 

@W_1:4670 = 0	' AL2t = 0		- Alarme 2 desligado
@W_1:4678 = 0	' AL3t = 0		- Alarme 3 desligado

@W_1:4702 = 1	' cont = onFA	- COntrole tipo On off assimetrico

@W_1:4640 = 0	'SEnS = 0		- Sensor tipo J
@W_1:4641 = 0	'dP = 0			- Sem ponto decimal


if @recipe = 0 then    ' caso nenhuma receita esteja selecionada seleciona a 1ª
@recipe = 1
endif

@tempocofig= 5  'tempo para abrir o menu de configuração 
@tempotransicao = 1 'tempo para inibir o bug em 1.0 segundo

@W_1:453 = 0 ' modo FULL
'@W_1:415 = 0 ' modo controle automatico

@SP_Temperatura_ativo = @w_1:46
@SP_speed_ativo = @W_1:W6692

@SP_Temperatura_ECO = 150
@SP_speed_ECO = 300
@des = 90

@plano_de_fundo = 0

'--- INVERSOR

@Reset_fabrica = FALSE
</Trigger></TrigAction></Script>
<PartInfo PartType="Rect" PartName="REC_1">
<General Area="10 690 470 790" BorderColor="0x0 0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="FunctionSwitch" PartName="FS_1">
<General Desc="FS_3" Area="41 708 105 772" ScrSwitch="1" ScreenNo="4" ScreenNo2="-1" PointPos="0 0" PopupScreenType="0" PopupCloseWithParent="0" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xcccccc 0" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="128" LaStartPt="50 50" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/></PartInfo>
<PartInfo PartType="FunctionSwitch" PartName="Function Switch1">
<General Desc="FS_3" Area="208 708 272 772" ScrSwitch="1" ScreenNo2="-1" PointPos="0 0" PopupScreenType="0" PopupCloseWithParent="0" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xcccccc 0" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="125" LaStartPt="22 64" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/></PartInfo>
<PartInfo PartType="Rect" PartName="REC_0">
<General Area="10 111 470 592" BorderColor="0x0 0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Bitmap" PartName="BMP_0">
<General Desc="BMP_0" StartPt="0 0" Width="480" Height="90" BmpIndex="40"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_1">
<General TextContent="Mais opções" LaFrnColor="0x0 0" IsBackColor="0" BgColor="0xffffff 0" CharSize="2986 126 126 126 126 126 126 12" Bold="0" StartPt="121 23"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_2">
<General TextContent="CUIDADO" LaFrnColor="0x0 0" IsBackColor="0" BgColor="0xffffff 0" CharSize="3046 126 126 126 126 126 126 12" Bold="0" StartPt="123 142"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_5">
<General TextContent="Reset de fabrica" LaFrnColor="0x0 0" IsBackColor="0" BgColor="0xffffff 0" CharSize="3046 126 126 126 126 126 126 12" Bold="0" StartPt="37 189"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="BS_0">
<General Desc="BS_0" Area="39 253 301 317" OperateAddr="Reset_fabrica" Fast="0" BitFunc="1" Monitor="1" MonitorAddr="Reset_fabrica" FigureFile="TFT-type style\TFT010.pvg" BorderColor="0x1b1bcb -1" BmpIndex="-1" Align="3" LaStartPt="96 10" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" MinClickTime="2000" IsIndirectR="0" IsIndirectW="0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Pattern="4587604" FrnColor="0xff 1" BgColor="0xffffff 0" Bold="0" LaIndexID="Reset" CharSize="1414141414141414" LaFrnColor="0x0 0"/>
<Label Status="1" Pattern="1" FrnColor="0x40ff00 0" BgColor="0xffffff 0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_4">
<General TextContent="Segurar
por 5 seg." LaFrnColor="0x0 0" IsBackColor="0" BgColor="0xffffff 0" CharSize="2156 126 126 126 126 126 126 12" Bold="0" StartPt="315 252"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Line" PartName="LN_0">
<General BorderColor="0x0 0" StartPt="30 351" EndPt="450 351" AutoAdsorption="20"/></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Text" PartName="TXT_0">
<General TextContent="Alterar senha" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="16 326 126 126 126 126 126 126 12" Bold="0" StartPt="37 388"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="String" PartName="STR_0">
<General Desc="STR_0" Area="277 385 443 424" WordAddr="hsw404" Fast="0" stCount="8" IsInput="1" WriteAddr="hsw404" KbdScreen="1004" IsPopKeyBrod="0" FigureFile="TFT-type style\dp_zc03.pvg" BorderColor="0xcccccc 0" FrnColor="0x0 -1" BgColor="0xffffff -1" CharSize="16 32" IsHideNum="0" Transparent="0" IsShowPwd="0" IsIndirectR="0" IsIndirectW="0" IsInputDefault="1" InputDefault="6384" IsDWord="0" IsHiLowRever="0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></PartInfo>
<PartInfo PartType="GroupPart" PartName="Group part">
<PartInfo PartType="Text" PartName="Text0">
<General TextContent="Desativar
alarme do gás" LaFrnColor="0x0 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="16 326 126 126 126 126 126 126 12" Bold="0" StartPt="37 482"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="BS_1">
<General Desc="BS_0" Area="255 483 455 547" OperateAddr="output_timer" Fast="0" BitFunc="3" Monitor="1" MonitorAddr="output_timer" FigureFile="TFT-type style\TFT010.pvg" BorderColor="0xff00 -1" BmpIndex="-1" Align="3" LaStartPt="63 10" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Pattern="4587604" FrnColor="0xff 1" BgColor="0xffffff 0" Bold="0" LaIndexID="OFF" CharSize="1414141414141414" LaFrnColor="0x0 0"/>
<Label Status="1" Pattern="1" FrnColor="0x40ff00 0" BgColor="0xffffff 0" Bold="0" LaIndexID="ON" CharSize="1414141414141414" LaFrnColor="0x0 0"/></PartInfo></PartInfo>
<PartInfo PartType="Line" PartName="LN_1">
<General BorderColor="0x0 0" StartPt="30 454" EndPt="450 454" AutoAdsorption="20"/></PartInfo></ScrInfo>
