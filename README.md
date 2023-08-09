# Acadêmico

O objetivo deste projeto é desenvolver, praticar e aplicar ferramentas voltadas a todo o ambiente de desenvolvimento. O projeto ainda está em andamento e listarei abaixo os objetivos e ferramentas que serão utilizados para concluí-lo.

> **Backend:** Foi utilizado Python com framework Django e estão contempladas regras de negócio, como as relações e cadastros de entidades. (Concluído)

> **Frontend:** Para melhorar a experiência do usuário, será utilizada a ferramenta React.js. (Não concluído)

> **Executar o projeto:** Como executor do projeto, foi utilizada a ferramenta Docker para que seja mais eficiente e preciso no momento de experimentá-lo. Mais adiante neste documento, será explicada a forma de executarmos o Docker (Concluído)

Ao término deste projeto, teremos um Acadêmico que comportará Escolas com qualquer quantidade de filiais.

Importante: Mesmo que o backend já esteja concluído, o objetivo é manter atualizações constantes de regras de negócios e entidades.

## Requisitos do Projeto

O projeto está sendo desenvolvido em Django (Concluído) + React.js (Não concluído) e compilado em Docker (Concluído).

As dependências do backend ficam em requirements.txt.
As dependências do frontend ainda estão em desenvolvimento.

O projeto pode ser executado de duas formas:
1. Via terminal Linux
2. Via Docker Compose

## 1. Terminal Linux:

Embora seja um pouco mais complexo, este método concede ao usuário mais acesso, visibilidade e manipulação ao código, permitindo a execução de partes específicas do projeto de forma independente. Também facilita a depuração do código na IDE que estiver sendo utilizada.

### Siga os passos a seguir para este modelo:

Com sua virtualenv, na raiz do projeto, instale as dependências do backend com
`pip install -r requirements.txt`

Com todos os pacotes instalados, na raiz do projeto, execute:
- `./manage.py runserver 8000` para subir o backend na porta 8000.

## 2. Docker Compose:

Este método de execução é recomendado para quem pretende verificar o projeto em execução sem analisar mais a fundo o código, uma vez que o Docker já oferece todos os componentes de instalação configurados, eliminando a necessidade de se preocupar com virtualenvs ou portas no projeto.

### Siga os passos a seguir para este modelo:

Efetue a instalação do Docker. O seguinte link pode ser útil: https://docs.docker.com/compose/install/linux/
Com o Docker Compose instalado, execute o seguinte comando em seu terminal: `docker-compose up --build`
