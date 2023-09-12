Para executar o projeto, você precisará de:

1. Um editor de texto ou IDE
2. Python 3
3. O pacote Flask

Para instalar o pacote Flask, você pode usar o seguinte comando: pip install Flask

Depois de instalar o pacote Flask, você pode criar um novo arquivo chamado api.py e colar o código.

Para executar o projeto, você pode usar o seguinte comando: python3 api.py

O servidor Flask será iniciado na porta 5000. Você pode enviar solicitações aos endpoints usando o comando curl ou um navegador da web.

Aqui estão algumas instruções passo a passo para executar o projeto:

1. Crie um novo arquivo chamado api.py.
2. Cole o código acima no arquivo api.py.
3. Instale o pacote Flask usando o comando pip install Flask.
4. Execute o projeto usando o comando python3 api.py.
5. Use o comando curl ou um navegador da web para enviar solicitações aos endpoints.

Aqui estão alguns exemplos de solicitações que você pode enviar:

# Criar um novo personagem
curl -X POST -H "Content-Type: application/json" -d '{
    "nome": "Mickey Mouse",
    "descricao": "Um rato antropomórfico",
    "link_imagem": "https://www.google.com/images/srpr/logo_google_ca.png",
    "programa": "Disney",
    "animador": "Walt Disney"
}' http://localhost:5000/characters/
# Recuperar todos os personagens
curl http://localhost:5000/characters/