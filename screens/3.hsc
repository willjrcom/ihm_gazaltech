<?xml version="1.0" encoding="UTF-8"?>
<ScrInfo ScreenNo="31" ScreenType="" ScreenSize="0">
	<Script>
		<InitialAction>@W1:451 = 0
</InitialAction></Script>
	<PartInfo PartType="Rect" PartName="REC_0">
		<General Area="10 5 470 587" BorderColor="0x0 0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" ActiveColor="0"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo>
	<PartInfo PartType="WordShow" PartName="WL_0">
		<General Desc="WL_0" Area="38 99 442 473" WordAddr="1:451" StatsNum="4" Fast="0" DataFormat="2" FigureFile="Display Type Style\dp_zc00.pvg" BorderColor="0xcccccc 0" BmpIndex="-1" Align="3" LaStartPt="0 53" StatusCovType="0" AnimaReturn="0" ByAddr="0" Trigger="0" UseShowHide="0" HideType="0" IsHideAllTime="0" IsIndirectR="0" IsIndirectW="0" isNautomatic="0" IsCtrlStaTextByAddr="0" isReturn="0" isStateControl="0"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
		<Extension IsCheck="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0"/>
		<Label Status="0" Pattern="6881348" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" LaIndexID="OBSERVAÇÂO:
O ajuste do tempo da 
esteira pode ser feito
com o forno quente ou frio.

_____________________________

Clique em &quot;Avançar&quot;
Para iniciar o teste da esteira." CharSize="12 2414141414141414" LaFrnColor="0x0 -1" UseGlint="0" GlintFgClr="0x0 0"/>
		<Label Status="1" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" LaIndexID="ETAPA 1

Paramos a esteira para você
colocar uma &quot;Azeitona&quot; ou
outro objeto pequeno no
inicio do tunel do lado oposto
ao painel, com a esteira direcionada à direita.

_____________________________

Pressione &quot;Avançar&quot;" CharSize="12 246 126 126 126 126 126 126 12" LaFrnColor="0x0 -1" UseGlint="1" GlintFgClr="0x0 0"/>
		<Label Status="2" Pattern="1" FrnColor="0xffffff 1" BgColor="0xffffff 0" Bold="0" LaIndexID="ETAPA 2
Iniciando calibração do
tempo da esteira.

_____________________________

Quando o objeto atravessar
todo o tunel do forno, 
pressione &quot;Avançar&quot;
" CharSize="12 246 126 126 126 126 126 126 12" LaFrnColor="0x0 -1" UseGlint="0" GlintFgClr="0x0 0"/>
		<Label Status="3" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="1" LaIndexID="ETAPA 3
_____________________________

Calibração Realizada 
com Sucesso.

O valor está salvo no
parâmetro &quot;SPd.r&quot;.

Pode fechar a tela." CharSize="12 246 126 126 126 126 126 126 12" LaFrnColor="0x8000 -1" UseGlint="0" GlintFgClr="0x0 0"/></PartInfo>
	<PartInfo PartType="WordSwitch" PartName="WS_0">
		<General Desc="WS_0" Area="274 487 424 557" WordAddr="1:451" WriteAddr="1:451" DataFormat="2" ClickTime="2000" WordFunc="1" Const="1" Limit="3" FigureFile="TFT-type style\TFT010.pvg" BorderColor="0x9ed23 -1" BmpIndex="-1" Align="3" LaStartPt="28 22" IsIndirectR="0" IsIndirectW="0" IsWordOrder="0"/>
		<Extension IsCheck="0" UseShowHide="0" HideType="0" IsHideAllTime="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
		<Label Status="0" Pattern="4587604" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="Avançar" CharSize="12 2414141414141414" LaFrnColor="0x0 0"/></PartInfo>
	<PartInfo PartType="WordSwitch" PartName="WS_1">
		<General Desc="WS_0" Area="56 488 206 558" WordAddr="1:451" WriteAddr="1:451" DataFormat="2" ClickTime="2000" Limit="3" FigureFile="TFT-type style\TFT010.pvg" BorderColor="0x7636e7 -1" BmpIndex="-1" Align="3" LaStartPt="19 23" IsIndirectR="0" IsIndirectW="0" IsWordOrder="0"/>
		<Extension IsCheck="0" UseShowHide="0" HideType="0" IsHideAllTime="0" Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
		<Label Status="0" Pattern="4587604" FrnColor="0xffffff 0" BgColor="0xffffff 0" Bold="0" LaIndexID="Reiniciar" CharSize="12 2414141414141414" LaFrnColor="0x0 0"/></PartInfo>
	<PartInfo PartType="FunctionSwitch" PartName="FS_0">
		<General Desc="FS_0" Area="387 13 451 77" ScrSwitch="0" FuncFunc="8" ScreenNo2="-1" PointPos="0 0" PopupScreenType="0" PopupCloseWithParent="0" DispDirect="1" FigureFile="TFT-type style\TFT001.pvg" BorderColor="0xcccccc 0" FrnColor="0x0 0" BgColor="0x0 0" BmpIndex="130" LaStartPt="30 32" UseShowHide="0" HideType="0" IsHideAllTime="0"/>
		<Extension Lockmate="0" DrawLock="0" IsShowGrayScale="0" LockMode="0" TouchState="1" Buzzer="1" IsUesPartPassword="0" IsSetLowerLev="0" IsUseUserAuthority="0"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/>
		<Label Status="0" Bold="0" CharSize="1414141414141414" LaFrnColor="0x0 0"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_0">
		<General TextContent="Calibrar esteira" LaFrnColor="0x0 0" IsBackColor="0" BgColor="0xffffff 0" CharSize="146 126 126 126 126 126 126 12" Bold="0" StartPt="97 29"/>
		<MoveZoom DataFormatMZ="2" DataLimitMZ="0 1199570688" MutipleMZ="1.000000"/></PartInfo></ScrInfo>
