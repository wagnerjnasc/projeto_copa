# ETL para Dados da Copa do Mundo Feminina de 2023

Este ETL foi projetado para extrair informações da Copa do Mundo Feminina de 2023, transformá-las em um formato útil e, em seguida, carregá-las em um destino específico. Abaixo está uma descrição detalhada de cada etapa do processo:

Extração:

Fonte de Dados: A extração começa acessando o site oficial da Copa do Mundo Feminina de 2023 (https://www.fifa.com/fifaplus/pt/tournaments/womens/womensworldcup/australia-new-zealand2023).
Informações Extraídas: A partir da página da web, os dados extraídos incluem informações sobre jogos, resultados, gols marcados, escalações de jogadoras e outras estatísticas relevantes.
Bibliotecas Utilizadas: Para a extração, é usada a biblioteca Python requests para fazer solicitações à página da web e Beautiful Soup para analisar o HTML e extrair informações específicas.
Transformação:

Limpeza de Dados: Os dados extraídos são processados e limpos para remover qualquer informação desnecessária ou duplicada.
Cálculos de Estatísticas: Durante a transformação, são realizados cálculos para determinar a média de gols por partida e quantos títulos cada equipe ganhou.
Classificação: Com base nos cálculos, é criado um ranking das equipes de acordo com o desempenho na competição.
Estruturação: Os dados são estruturados em um formato tabular adequado para análise, utilizando uma estrutura de DataFrame do Pandas.
Carregamento:

Destino de Dados: Os dados transformados são carregados em um arquivo CSV chamado "dados_copa_2023.csv", que servirá como destino final.
Atualização dos Dados: O arquivo CSV é atualizado com as informações mais recentes da Copa do Mundo Feminina de 2023, incluindo os resultados atualizados, as estatísticas de gols e as classificações das equipes.
Fluxo de Execução:

O ETL é executado periodicamente para manter os dados atualizados, permitindo análises em tempo real do torneio.
Os dados são disponibilizados no arquivo CSV para que sejam acessíveis e utilizados por outros sistemas ou análises posteriores.
Monitoramento e Controle:

O processo ETL é monitorado quanto a possíveis falhas ou erros durante a extração, transformação ou carregamento.
Logs detalhados são mantidos para rastrear o status de cada execução e identificar problemas.
Em caso de falha, o sistema é projetado para lidar com contingências e retomar a execução a partir do ponto de falha.
Documentação:

Uma documentação completa descrevendo o ETL, incluindo mapeamentos de dados, fontes, cronogramas de execução e informações de configuração, é mantida para referência futura e para facilitar a compreensão e manutenção contínuas do pipeline ETL.
Em resumo, este ETL permite a extração, transformação e carregamento de dados da Copa do Mundo Feminina de 2023, garantindo que as informações estejam disponíveis em um formato útil e atualizado para análises e tomada de decisões. É um componente fundamental para acompanhar e compreender o desempenho das equipes e o progresso do torneio em tempo real.
