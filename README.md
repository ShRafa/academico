# Academico

O Objetivo deste projeto é desenvolver, praticar e aplicar ferramentas voltadas a todo o ambiente de desenvolvimento. O projeto ainda está em andamento e listarei abaixo os objetivos e ferramentas que será utilizado para concluir o mesmo.

> **Backend:** Foi utilizado Python com framework Django e está contemplado regras de negócio como as relações e cadastros de entidades. (concluído)

> **Frontend:** Para melhorar a experiência do usuário, será utilizado a ferramenta React.js. (não concluído)

> **Executar o projeto:** Como executor do projeto foi utilizado a ferramenta Docker para que seja mais eficiente e preciso no momento de experimentá-lo, Mais a frente neste documento será explicado a forma de executarmos o Docker (concluído)

Ao término deste projeto, teremos um Acadêmico que comportará Escolas com qualquer quantidade de  filias.

Importante: Mesmo que o backend já esteja concluído, o objetivo é manter constante atualizações de regras de negócios e entidades.

## Requisitos do Projeto

O projeto está sendo desenvolvido em Django (concluído) + React.js (não concluído) e compilado em Docker (concluído)

As depedências do backend ficam em requirements.txt.
As dependências do frontend ainda está em desenvimento,

O projeto pode ser executado de duas formas:
1. Via terminal Linux
2. Via Docker Compose


## 1. Terminal Linux:

Embora um pouco mais complexo, esta forma concede ao usuário mais acesso, visibilidade e manipulação ao código, podendo executar partes específicas do projeto de forma independente. Também facilita o debug do código na IDE que estiver utilizando.

### Para este modelo, sigaos passos a seguir:

Com sua virtualenv, na raíz do projeto instale as dependências do backend com
`pip install -r requirements.txt`

Com os pacotes todos instalados, na raiz do projeto rode:
- `./manage.py runserver 8000` para subir o backend na porta 8000


## 2. Docker compose:

Este modelo de execução é recomendado para quem pretende verificar o projeto em execução, sem analisar mais a fundo o código, uma vez que o docker já te oferece todos os componentes de instalação configurados, sem ter que se preocupar com virtualenvs ou portas no projeto.

### Para este modelo, sigaos passos a seguir:

Efetue a instalação do Docker, o seguinte link pode ser útil: https://docs.docker.com/compose/install/linux/
Com o docker compose instalado, execute o seguinte comando em seu terminal: docker compose up --build
