#!/bin/bash

# Atualizar pacotes
sudo apt update -y
sudo apt upgrade -y

# Instalar Python, pip e R
sudo apt install -y python3-pip r-base

# Instalar dependências Python
pip3 install -r app/requirements.txt

# Instalar dependências R
sudo Rscript -e "install.packages(c('plumber', 'textTinyR', 'tm', 'dplyr'))"
