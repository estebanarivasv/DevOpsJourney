#!/bin/bash

#variable
VALOR1=$1
VALOR2=$2

# si el directorio existe
if [ -d "prueba" ] ;
then
	echo "existe el directorio"
else
	echo "no existe el directorio"
fi

