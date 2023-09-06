<h1 align="center">
  Copa do Mundo Feminina de 2023 - ETL
</h1>

## Descrição

Este repositório contém um pipeline ETL (Extração, Transformação e Carregamento) criado para extrair informações da Copa do Mundo Feminina de 2023, transformá-las em um formato útil e, em seguida, carregá-las em um destino específico.

### Etapas do Processo ETL

#### Extração

- **Fonte de Dados:** A extração começa acessando o site oficial da Copa do Mundo Feminina de 2023 (https://www.fifa.com/fifaplus/pt/tournaments/womens/womensworldcup/australia-new-zealand2023).
- **Informações Extraídas:** A partir da página da web, os dados extraídos incluem informações sobre jogos, resultados, gols marcados, escalações de jogadoras e outras estatísticas relevantes.
- **Bibliotecas Utilizadas:** Para a extração, é usada a biblioteca Python `requests` para fazer solicitações à página da web e `Beautiful Soup` para analisar o HTML e extrair informações específicas.

#### Transformação

- **Limpeza de Dados:** Os dados extraídos são processados e limpos para remover qualquer informação desnecessária ou duplicada.
- **Cálculos de Estatísticas:** Durante a transformação, são realizados cálculos para determinar a média de gols por partida e quantos títulos cada equipe ganhou.
- **Classificação:** Com base nos cálculos, é criado um ranking das equipes de acordo com o desempenho na competição.
- **Estruturação:** Os dados são estruturados em um formato tabular adequado para análise, utilizando uma estrutura de DataFrame do Pandas.

#### Carregamento

- **Destino de Dados:** Os dados transformados são carregados em um arquivo CSV chamado "dados_copa_2023.csv", que servirá como destino final.
- **Atualização dos Dados:** O arquivo CSV é atualizado com as informações mais recentes da Copa do Mundo Feminina de 2023, incluindo os resultados atualizados, as estatísticas de gols e as classificações das equipes.

## Como Usar

Este pipeline ETL foi desenvolvido para fins de teste no Santander Dev Week 2023 (SDW2023). Ele serve como uma demonstração de um processo ETL simples e pode não conter muitas funcionalidades práticas para casos de uso reais.
...

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

- **E-mail:** wagnerjnascimento@live.com
- **LinkedIn:** [![LinkedIn](https://img.shields.io/badge/LinkedIn-Wagner-blue)](https://www.linkedin.com/in/wagnerjnascimento/)
- **Perfil da Digital Innovation One (DIO):** [![DIO](https://img.shields.io/badge/DIO-Wagner-blue)](https://www.dio.me/users/wagnerjnascimento)
