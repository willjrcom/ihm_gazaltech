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
<PartInfo PartType="Rect" PartName="BG_0">
<General Area="0 0 480 800" BorderColor="0xf4f7fb 0" Pattern="1" FrnColor="0xf4f7fb -1" BgColor="0xf4f7fb -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="HEADER_BG">
<General Area="0 0 480 112" BorderColor="0xf172a 0" Pattern="1" FrnColor="0xf172a -1" BgColor="0xf172a -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TITLE_0">
<General TextContent="Sistema" LaFrnColor="0xffffff -1" IsBackColor="0" BgColor="0xf172a 0" CharSize="304" Bold="1" StartPt="92 22"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="SUBTITLE_0">
<General TextContent="Reset e seguranca" LaFrnColor="0xcbd5e1 -1" IsBackColor="0" BgColor="0xf172a 0" CharSize="233" Bold="0" StartPt="92 60"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="HEADER_ACCENT">
<General Area="92 92 204 97" BorderColor="0x94a3b8 0" Pattern="1" FrnColor="0x94a3b8 -1" BgColor="0x94a3b8 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="FunctionSwitch" PartName="FS_MENU_OPEN">
<General Desc="FS_MENU_OPEN" Area="24 28 80 84" ScrSwitch="0" FuncFunc="2" ScreenNo="-1" ScreenNo2="1003" PointPos="0 0" PopupScreenType="1" PopupCloseWithParent="1" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xffffff 16777215" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="140" LaStartPt="12 12" Transparent="0" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Bold="0" CharSize="6 12" LaFrnColor="0xffffff -1"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_RESET">
<General Area="24 128 456 320" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_RESET">
<General Area="24 128 30 320" BorderColor="0xef4444 0" Pattern="1" FrnColor="0xef4444 -1" BgColor="0xef4444 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_CAUTION">
<General TextContent="CUIDADO" LaFrnColor="0xef4444 -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="304" Bold="1" StartPt="48 154"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_RESET">
<General TextContent="Reset de fabrica" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 198"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_RESET_SUB">
<General TextContent="Segure para resetar." LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="48 234"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="BS_0">
<General Desc="BS_0" Area="264 226 432 286" OperateAddr="Reset_fabrica" Fast="0" BitFunc="1" Monitor="1" MonitorAddr="Reset_fabrica" FigureFile="TFT-type style\TFT010.pvg" BorderColor="0xef4444 -1" BmpIndex="-1" Align="3" LaStartPt="36 13" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" MinClickTime="2000" IsIndirectR="0" IsIndirectW="0" FrnColor="0xef4444 -1" BgColor="0xef4444 -1"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Pattern="1" FrnColor="0xef4444 1" BgColor="0xef4444 0" Bold="0" LaIndexID="RESET" CharSize="14" LaFrnColor="0xffffff -1"/>
<Label Status="1" Pattern="1" FrnColor="0x22c55e 0" BgColor="0x22c55e 0" Bold="0" CharSize="14" LaFrnColor="0xffffff -1" LaIndexID="RESET"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_PASS">
<General Area="24 350 456 456" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_PASS">
<General Area="24 350 30 456" BorderColor="0x94a3b8 0" Pattern="1" FrnColor="0x94a3b8 -1" BgColor="0x94a3b8 -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_PASS">
<General TextContent="Senha" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 386"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="String" PartName="STR_0">
<General Desc="STR_0" Area="260 384 432 430" WordAddr="hsw404" Fast="0" stCount="8" IsInput="0" WriteAddr="hsw404" KbdScreen="1004" IsPopKeyBrod="0" FigureFile="" BorderColor="0xd7dee8 0" FrnColor="0xf172a -1" BgColor="0xffffff -1" CharSize="233" IsHideNum="0" Transparent="0" IsShowPwd="0" IsIndirectR="0" IsIndirectW="0" IsInputDefault="1" InputDefault="2601" IsDWord="0" IsHiLowRever="0"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" LockMode="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="CARD_ALARM">
<General Area="24 486 456 606" BorderColor="0xd7dee8 0" Pattern="1" FrnColor="0xffffff -1" BgColor="0xffffff -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Rect" PartName="ACCENT_ALARM">
<General Area="24 486 30 606" BorderColor="0x22c55e 0" Pattern="1" FrnColor="0x22c55e -1" BgColor="0x22c55e -1" ActiveColor="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_ALARM">
<General TextContent="Alarme do gas" LaFrnColor="0xf172a -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="233" Bold="1" StartPt="48 516"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="Text" PartName="TXT_ALARM_SUB">
<General TextContent="Liga/desliga saida." LaFrnColor="0x64748b -1" IsBackColor="0" BgColor="0xffffff 0" CharSize="8 16" Bold="0" StartPt="48 552"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
<PartInfo PartType="BitSwitch" PartName="BS_1">
<General Desc="BS_0" Area="264 516 432 576" OperateAddr="output_timer" Fast="0" BitFunc="3" Monitor="1" MonitorAddr="output_timer" FigureFile="TFT-type style\TFT010.pvg" BorderColor="0x22c55e -1" BmpIndex="-1" Align="3" LaStartPt="36 13" BitShowReverse="0" UseGlint="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" FrnColor="0x22c55e -1" BgColor="0x22c55e -1"/>
<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
<Label Status="0" Pattern="1" FrnColor="0x22c55e 1" BgColor="0x22c55e 0" Bold="0" LaIndexID="ON/OFF" CharSize="14" LaFrnColor="0xffffff -1"/>
<Label Status="1" Pattern="1" FrnColor="0x22c55e 0" BgColor="0x22c55e 0" Bold="0" LaIndexID="ON/OFF" CharSize="14" LaFrnColor="0xffffff -1"/></PartInfo></ScrInfo>
