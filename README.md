# Introdução do Projeto
## MERX

Projeto desenvolvido como etapa de aprovação do processo seletivo. Tem como objetivo principal criar um pipeline de distribuição de dados passando pelas etapas de extração, tranformação e carregamento de dados. Sendo todas essa passos orquestrados por Apache Airflow.

## Pipeline
### Extração
- API com Autenticação via API Key: Escolhi uma API que exige o uso de uma chave de API, demonstrando o domínio na autenticação em APIs REST de terceiros. Utilizei essa API para obter dados de câmbio entre o BRL e o USD, com consumo a cada 5 minutos.

- API de Dados Públicos Governamentais: O outro consumo de API foi feito a partir de dados públicos fornecidos pelo governo, especificamente sobre o balanço de crédito no setor agrícola do Brasil. Este consumo ocorre semanalmente, conforme a atualização dos dados na fonte.

- Web Scraping de Portal de Finanças Internacional: Para atender a outro requisito, realizei um scraping em um portal de finanças internacional para obter índices econômicos do Brasil. Utilizei uma abordagem mais simples de scraping, sem a necessidade de simular navegação humana (como seria feito com Selenium) ou realizar extrações mais complexas e pesadas, para as quais o Scrapy seria mais adequado.

### Transformação
- Uso de Pandas: Optei pelo uso do Pandas devido à simplicidade dos dados. No entanto, caso o volume de dados fosse maior, poderia considerar o uso de Spark (no Databricks) ou Polars (se possível rodar localmente).

- Transformações Realizadas:
1. Renomeação das colunas para maior clareza e consistência.
2. Conversão de strings para floats, dado que os dados financeiros exigem esse tipo de formato.
3. Formatação das datas para o padrão convencional brasileiro.
4. Limpeza de dados, removendo valores nulos e duplicados para garantir a qualidade dos dados.

### Carregamento

- Verificação dos Dados: Antes de realizar a inserção no banco de dados, fiz a verificação e validação dos dados, garantindo que fossem consistentes e confiáveis.

- Inserção no Banco de Dados: A inserção foi feita de forma direta e eficiente, utilizando a própria biblioteca do PostgreSQL para garantir uma integração ágil e sem sobrecarga desnecessária.

# Instruções para Configuração do Projeto

Este projeto utiliza Docker para rodar os containers do Apache Airflow e do banco de dados PostgreSQL, além de um ambiente Python para gerenciar as dependências. Siga as instruções abaixo para configurar e rodar o projeto.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.8 ou superior](https://www.python.org/downloads/)

## Clonando o Repositório

Primeiro, clone o repositório do projeto:

```bash
git clone https://github.com/usuario/projeto.git
cd projeto
```

## Criando e Ativando o Ambiente Python
Aqui está o `README.md` com todas as instruções organizadas de forma contínua em um único arquivo:

```markdown
# Instruções para Configuração do Projeto

Este projeto utiliza Docker para rodar os containers do Apache Airflow e do banco de dados PostgreSQL, além de um ambiente Python para gerenciar as dependências. Siga as instruções abaixo para configurar e rodar o projeto.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.8 ou superior](https://www.python.org/downloads/)

## Clonando o Repositório

Primeiro, clone o repositório do projeto:

```bash
git clone https://github.com/usuario/projeto.git
cd projeto
```

## Criando e Ativando o Ambiente Python

Crie um ambiente virtual em Python para gerenciar as dependências do projeto:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

- **No Linux/macOS**:

  ```bash
  source venv/bin/activate
  ```

- **No Windows**:

  ```bash
  .\venv\Scripts\activate
  ```

## Instalando as Dependências Python

Com o ambiente virtual ativado, instale as dependências necessárias do projeto:

```bash
pip install -r requirements.txt
```

## Configuração do Docker

Este projeto utiliza Docker para rodar os containers do Apache Airflow e do PostgreSQL. O arquivo `docker-compose.yml` já está configurado para rodar esses containers.

### Subindo os Containers

Execute o Docker Compose para subir os containers definidos no `docker-compose.yml`:

```bash
docker-compose up -d
```

Isso irá subir o container do PostgreSQL e o container do Apache Airflow.

### Verificando os Containers

Verifique se os containers estão rodando corretamente:

```bash
docker ps
```

Você deverá ver os containers `postgres` e `airflow` em execução.

## Acessando o Apache Airflow

O Apache Airflow estará disponível em `http://localhost:8080`. Você pode acessar a interface web para monitorar e controlar suas DAGs.

Por padrão, o Apache Airflow usa as seguintes credenciais de login:

- **Usuário**: `airflow`
- **Senha**: `airflow`

## Parando os Containers

Quando terminar de usar os containers, você pode parar e remover os containers com o seguinte comando:

```bash
docker-compose down
```

Este comando irá parar e remover todos os containers, redes e volumes criados pelo `docker-compose up`.