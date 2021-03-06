Title: Exemple de custom Logger en shell
Slug: shell-custom-logger
Date: 2015-02-25 18:14:08
Tags: shell, bash, logging, logger
Category: Linux
Author: Josue Kouka
Lang: fr
Summary: Example d un logger customise en python

Hello guys !!! (Imaginez moi avec une tete requin en train de crier comme un fou :D)

Pour un de mes scripts shell j'avais besoin d'une sorte de logger. Et me suis demandé
comment avoir une sorte de module de logging pour mes scripts shell, et j'en ai écris un.

### Structure et Installation

Creer un dossier qui contiendra le module i.e:

    :::shell
    yosuke@loking$> mkdir .scripts


Dans votre fichier de ***profile*** (.bashrc, .profile)

    :::shell
    export MYSCRIPTS=$HOME/.scripts
    source $MYSCRIPST/mylogger.sh

Le ***source*** permet a *bash* de charger votre script lorsque vous lancez votre shell.

### Code de votre Shell Logger

    :::shell
    ## If a LOG_OUTPUT variable is defined,
    ## the logger will write to a file pointed to by the variable

    function _log(){
        level=$1
        message=$2
        output=$3

        if [ -z $output ]; then
            if [ `uname -s` != "Darwin" ]; then
                logger -s -i -t "[`date +'%Y-%m-%d %H:%M:%S'` ${HOSTNAME} ${USER}][`echo ${level} | tr '[:lower:]' '[:upper:]'`]" -p "user.${level}" "${message}" 2>&1
            else
                logger -s -p "user.${level}" "${message}" 2>&1
            fi
        else
             if [ `uname -s` != "Darwin" ]; then
                logger -s -i -t "[`date +'%Y-%m-%d %H:%M:%S'` ${HOSTNAME} ${USER}][`echo ${level} | tr '[:lower:]' '[:upper:]'`]" -p "user.${level}" "${message}" 2>> $output 
            else
                logger -s -p "user.${level}" "${message}" 2>> $output
            fi
        fi
    }

    function _process(){
        level=$1
        message=$2

        if [ ! "${message}" == "" ]; then
            _log "${level}" "${message}" $LOG_OUTPUT
        else
            echo -e "A message must be provided i.e : _${level} 'your message'"
        fi
    }

    function _info(){
        _process "info" "$1"
    }

    function _debug(){
        _process "debug" "$1"
    }

    function _warning(){
        _process "warning" "$1"
    }

    function _error(){
        _process "error" "$1"
    }

    function _notice(){
        _process "notice" "$1"
    }

    export -f _log
    export -f _process
    export -f _info
    export -f _debug
    export -f _warning
    export -f _error
    export -f _notice

**HELP**:

* *export -f* permet d'exporter une fonction bash et la rend accessible a bash et tous les processus fils de bash. Ce qui permet 
a ces differentes fonctions d'etre utilisées dans un script bash.

### Utilisation

Un test rapide dans votre shell

    :::shell
    yosuke@loking$> _info "Hello josh"
    [2015-03-05 09:44:29 loking yosuke][INFO][24044]: Hello josh    

Pour rediriger la sortie log vers un fichier 

    :::shell
    yosuke@loking$> LOG_OUTPUT=myfile.log
    yosuke@loking$> _debug "Hello josh"
    yosuke@loking$> cat myfile.log
    [2015-03-05 09:44:29 loking yosuke][DEBUG][24044]: Hello josh

Voila !!!

### Contribution 

Si vous trouvez des ameliorations n'hesitez pas a forker ce [repo](https://github.com/josuebrunel/myscripts) et a m'envoyer un pull request.


Merci
