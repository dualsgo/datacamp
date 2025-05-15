"""Verificação da inflação
O governo do UK solicitou sua ajuda na análise das estatísticas de inflação.

Eles forneceram a você os dados de setembro e agosto de 2023 armazenados como duas variáveis float, inflation_september e inflation_august, respectivamente.

Você precisará criar um fluxo de trabalho que compare essas estatísticas.

Instruções 1/3

Verifique se inflation_september é menor que inflation_august, imprimindo "Inflation decreased" se esse for o caso."""

inflation_september = 6.7
inflation_august = 7.0

# Check if September inflation is less than August inflation
if inflation_september < inflation_august:
	print("Inflation decreased")