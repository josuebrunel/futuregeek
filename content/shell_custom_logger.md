Title: Exemple de custom Logger en shell
Slug: shell-custom-logger
Date: 2015-02-25 18:14:08
Tags: shell, bash, logging, logger
Category: Programming
Author: Josue Kouka
Status: draft
Lang: fr
Summary: Example d un logger customise en python

Hello guys !!! (Imaginez avec un tete requin en train de crier comme un fou :D)

Pour un de mes scripts shell j'avais besoin d'une sorte de logger. Et me suis demandé
comment avoir une sorte de module de logging pour mes scripts shell, et j'en ai écris un.

### Structure et Installation

Creer un dossier qui contiendra le module i.e:

    :::shell
    yosuke@loking$> mkdir .scripts


Dans votre fichier de ***profile*** (.bashrc, .profile)

    :::bash
    export MYSCRIPTS=$HOME/.scripts
    source $MYSCRIPST/

### Code de votre Shell Logger

    :::shell
    


