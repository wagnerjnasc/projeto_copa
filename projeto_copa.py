import requests
from bs4 import BeautifulSoup

# URL da página da Copa de 2023
url = "https://www.fifa.com/fifaplus/pt/tournaments/womens/womensworldcup/australia-new-zealand2023"

# Fazer a solicitação para obter o conteúdo da página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parse do conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar as informações dos jogos (por exemplo, usando classes CSS)
    jogos = soup.find_all(class_='classe-dos-jogos')

    # Criar listas para armazenar os dados extraídos
    dados_jogos = []

    # Loop pelos jogos e extrair informações
    for jogo in jogos:
        resultado = jogo.find(class_='classe-do-resultado').text
        gol = jogo.find(class_='classe-dos-gols').text
        escalação = jogo.find(class_='classe-das-escalacoes').text

        dados_jogos.append({'Resultado': resultado, 'Gols': gol, 'Escalação': escalação})

    # Agora você tem os dados extraídos dos jogos nas lista "dados_jogos"
else:
    print("Erro ao acessar o site da FIFA")

import pandas as pd

# Suponha que você já tenha uma lista de dicionários chamada "dados_jogos" com os dados extraídos
# Exemplo de dados_jogos:
dados_jogos = [
    {'Resultado': 'Brasil 2-0 Argentina', 'Gols': 'Marta (2)', 'Escalação': '...'},
    {'Resultado': 'Brasil 3-1 Alemanha', 'Gols': 'Marta, Cristiane, Bia (1)', 'Escalação': '...'},
    # Mais dados dos jogos...
]

# Criar um DataFrame pandas com os dados
df = pd.DataFrame(dados_jogos)

# Dividir a coluna "Resultado" para obter o número de gols marcados por equipe
df[['Gols_Brasil', 'Gols_Adversario']] = df['Resultado'].str.split('-', expand=True)
df['Gols_Brasil'] = df['Gols_Brasil'].str.extract('(\d+)').astype(int)
df['Gols_Adversario'] = df['Gols_Adversario'].str.extract('(\d+)').astype(int)

# Calcular a média de gols por partida
df['Gols_Por_Partida'] = (df['Gols_Brasil'] + df['Gols_Adversario']) / 2

# Contar a quantidade de títulos (suponhamos que você tenha a informação)
quantidade_de_titulos = 2  # Atualize com o valor correto

# Criar um ranking com base na média de gols por partida
df = df.sort_values(by='Gols_Por_Partida', ascending=False)
df['Ranking'] = range(1, len(df) + 1)

# Exibir o DataFrame resultante
print(df)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('dados_transformados.csv', index=False)

import pandas as pd

# Carregar os dados transformados do arquivo CSV
df = pd.read_csv('dados_transformados.csv')

# Suponha que você tenha informações atualizadas sobre a Copa do Mundo
# Aqui, vamos definir o vencedor como "Brasil" (suponhamos que o Brasil ganhou)
vencedor = 'Brasil'

# Atualizar os dados com as informações mais recentes
dados_atualizados = {
    'InformacaoMaisAtual': 'ValorMaisAtual',
    'Vencedor': vencedor,
    # Outras informações atualizadas, se necessário
}

# Atualizar o DataFrame com as informações mais recentes
df = df.assign(**dados_atualizados)

# Salvar os dados atualizados em um arquivo CSV
df.to_csv('dados_atualizados.csv', index=False)

# Exibir os dados atualizados
print(df)
