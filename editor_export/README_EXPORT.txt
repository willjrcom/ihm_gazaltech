Export gerado para abrir no software oficial da IHM.

Abra o arquivo 'LCD Gazal.ump' desta pasta.
Os arquivos .hsc foram copiados para o mesmo nivel do .ump,
porque o projeto referencia as telas como 0.hsc, 7.hsc etc.

Depois de abrir no editor, recompile/exporte novamente para
regenerar os arquivos LCD Gazal.ehmt/LCD Gazal.eblb.

A pasta bruta G_Picture nao e copiada por padrao; as bibliotecas
.blb foram copiadas. Use --include-g-picture somente se o editor
pedir essa pasta ao abrir o projeto.
