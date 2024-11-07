# Julian de Campos Teixeira - 10400765
# Luis Gustavo Aguirre Castanho - 10401017
# Luiz Henrique Bonilha Pasquinelli - 

# Sistema de Recomendação Colaborativo com API REST

Este projeto implementa um sistema de recomendação colaborativa usando Flask (Python) e plumber (R). Ele utiliza filtragem colaborativa para sugerir livros aos usuários.

## Estrutura do Projeto
- `app/`: Contém a API Flask e scripts de processamento de dados.
- `data/`: Contém os arquivos de dados `Books.csv`, `Ratings.csv` e `Users.csv`.
- `r_api/`: Contém o código da API em R para encontrar itens semelhantes.
- `deployment/`: Scripts para iniciar as APIs e configurar o ambiente na AWS.

## Instalação
1. Execute `setup_ec2.sh` para configurar o ambiente na instância EC2.
2. Use `start_flask.sh` e `start_plumber.sh` para iniciar as APIs Flask e R.

## Endpoints
- **`GET /users/<user_id>/recommendations`**: Retorna recomendações para o usuário.
- **`GET /items/<item_id>/similar`**: Retorna itens semelhantes ao item especificado.

