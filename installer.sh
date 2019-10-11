#!/bin/sh

## pyinstaller how to use
# https://pyinstaller.readthedocs.io/en/stable/usage.html


## variables globales
dist_folder="dist"
scripts_folder="scripts"


# creador de ejecutable
pyinstaller --distpath $dist_folder -F --clean -n ocho_y_media main.py


# crear carpetas necesarias para ejecutable
mkdir $dist_folder/$scripts_folder


## copiar scripts de prueba
cp $scripts_folder/* ./$dist_folder/$scripts_folder


## copiar archivos varios
cp ./README.md ./$dist_folder/
cp ./config.ini ./$dist_folder/


echo ""
echo "##################################################"
echo "Finalzado, presiona cualquier tecla para cerrar"
echo "##################################################"

read myothervar