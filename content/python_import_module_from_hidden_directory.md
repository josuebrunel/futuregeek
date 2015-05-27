Title: Importer un module depuis un dossier cachee en python
Slug: importer-un-module-depuis-un-dossier-cachee-en-python
Date: 2015-01-12 07:58:30
Tags: Python, Programming
Category: Programming
Author: Josue Kouka
Lang: fr
Summary: Comment importer un module depuis un dossier cache

Il arrive des cas ou pour certaines raisons, on voudrait loader un module python se trouvant dans un repertoire caché ( _.myfolder/mymodule_).
Dans mon cas, je devais charger un fichier _settings.py_ contenu dans le dossier de config de mon app ( _~/.monapp/settings.py_).
Si vous etes dans la meme situation et vous vous demandez comment le faire, ce qui suit peut vous etre utile:


    :::shell
    josue@LokingMac:/tmp/tests$tree -a
    .
    ├── .myapp
    │   ├── settings.py
    │   └── settings.pyc
    └── run.py

    1 directory, 3 files
    josue@LokingMac:/tmp/tests$

Notre fichier _.myapp/settings.py_ qui correspond au module a importer
    
    :::python
    import os

    def get_realpath(name='.'):
      return os.path.realpath(name)


    LOG_FILENAME = 'myapp.logs'
    LOG_FILESIZE = 1 * 1024 * 1024


Pour importer ce module depuis un run.py par exemple :

    :::python
    import os
    import imp

    settings = imp.load_source('settings', os.path.realpath('.myapp/settings.py'))

    from settings import LOG_FILENAME, LOG_FILESIZE

    print(LOG_FILENAME, LOG_FILESIZE)


Execution

    :::shell
    josue@LokingMac:/tmp/tests$python  run.py
    ('myapp.logs', 1048576)
    josue@LokingMac:/tmp/tests$


Le module a retenir est ***[imp](https://docs.python.org/2/library/imp.html?highlight=imp#imp.load_source)*** 

***NB*** : **IL MARCHE POUR TOUT**