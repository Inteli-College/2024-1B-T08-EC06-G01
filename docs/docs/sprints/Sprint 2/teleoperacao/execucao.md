---
title: Instruções de Execução
sidebar_position: 1
---

# Instruções de Execução

Para instalar a CLI que controla o robô, siga os passos abaixo:

## Pré-requisitos

Clone o repositório do projeto:

```bash
git clone https://github.com/Inteli-College/2024-1B-T08-EC06-G01.git
```

## Instalação e Execução

Entre na pasta do projeto:

```bash
cd 2024-1B-T08-EC06-G01/src
```

Rode o script de instalação e execução automático:

```bash
chmod +x ros-run.bash
./ros-run.bash
```

O comando acima irá instalar todas as dependências necessárias para rodar o projeto.

## Explicação do Script de Instalação

```bash
#!/bin/bash

# if the directory "env" does not exist, create a virtual environment
if [ ! -d "env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv env
fi

source env/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt > /dev/null

cd meu_workspace

# get the site-packages path by getting pip show setuptools (setuptools always comes with pip)
VENV_PATH=$(pip show setuptools | grep "Location: " | awk '{print $2}')

export PYTHONPATH="$PYTHONPATH:$VENV_PATH"

echo "Building package..."
colcon build > /dev/null

source install/setup.bash

ROS_DOMAIN_ID=69 ros2 run cannabot cannabot
```

O script acima faz o seguinte:

1. Verifica se o diretório `env` existe. Se não existir, ele cria um ambiente virtual Python.
2. Ativa o ambiente virtual.
3. Instala as dependências do projeto.
4. Navega até o diretório `meu_workspace`.
5. Obtém o caminho do site-packages executando `pip show setuptools` e exporta o caminho para a variável de ambiente `PYTHONPATH`.
6. Compila o pacote ROS usando o `colcon`.
7. Ativa o pacote ROS.
8. Executa o pacote ROS `cannabot` que é a CLI que controla o robô usando o `ROS_DOMAIN_ID` `69`.
