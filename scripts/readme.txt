bilhetagem_coord.py -> 
	dado o arquivo RMBS_bilhetagem_no_botoeiras.txt, que contém as bilhetagens de RMBS sem os tipos BOTOEIRAS ou BOTOEIRA GRAT,
	e o arquivo transmissoes_86110001.csv que contém os dados de GPS do ônibus 8611, ele encontra para cada bilhetagem a localização
	(latitude e longitude). O match é feito considerando para cada horário de bilhetagem o dado de GPS com o horário mais próximo.

script.py -> 
	Esse script pega a saída do script acima e elimina todas as linhas cuja linha seja diferente de 904 e cujo ônibus seja diferente de 8611

count_duplicates.py ->
	esse script pega a saída gerada acima e conta a ocorrência de linhas com a mesma latitude e longitude. Estimamos assim frequência de um ponto.
