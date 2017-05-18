# Home-Control
Um sistema de controle e automação residencial. Utilizando sensores, atuadores e perfis de usuário.

# Instruções
## Configurando ambiente de desenvolvimento

- Instale os seguintes programas e certifique-se de que as **versões** usadas estão sempre corretas e os serviços estão **ativos**:
    - [Python 3.6.1](https://www.python.org/downloads/release/python-361) (mas provavelmente qualquer versão acima de 3.3 irá servir)
        - Tenha certeza de que seu Python3 tem o ```pip``` adequado a ele (no Linux, às vezes é pip3), com módulo ```virtualenv``` instalado
- Prepare o ambiente virtual:
    - Crie um arquivo vazio ```logs/error.log```
    - Crie o ambiente virtual via console usando ```python -m venv env```
- Ative o ambiente virtual (e você irá **precisar refazer este único passo sempre que executar usar o sistema**):
    - No Windows, execute no prompt (cmd): ```env\Scripts\activate.bat```
    - No Unix ou MacOS, execute no terminal (bash): ```source env/bin/activate```
- Instale as dependências do sistema com ```pip install -r requirements.txt```.

## Rodando o servidor

Considerando que todo o ambiente foi corretamente instalado e configurado, sempre que for executar o sistema:

- Execute novamente o passo de ativação do ambiente virtual
- Inicie o servidor com ```python run.py``` e leia o output que lhe dirá em qual endereço IP e porta a aplicação está rodando
    - Se for "0.0.0.0" significa que está aberto para toda sua rede interna, e você deve encontrar seu IP público (no Linux, use ```ifconfig```)
