#!/bin/sh

# [ATTENTION] Si on change la destination du volume (/data) il faut adapter le code Python pour récupérer les fichiers au bon endroit
docker run -i -v shared:/data train 