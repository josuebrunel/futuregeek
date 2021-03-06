Title: Environement Python : exemple d'un fichier .pythonenv
Slug: environement-python-exemple-dun-fichier-pythonenv
Date: 2014-11-19 21:03:02
Tags: python, programming
Category: Programming
Author: Josue Kouka
Status: draft
Lang: fr
Summary: Quelques lib que j'utilise souvent dans mon shell python



    :::python
    import os
    import abc
    import datetime
    import logging
    import sqlite3

    import readline, rlcompleter
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")

    def get_real_path(f):
        """Retuns the realpath of a file
        """
        return os.path.realpath(f)

    def get_joined_path(a, b):
        """Returns joined path of to file
        """
        return os.path.join(a,b)

    class Database(object):
        """Just an usual class
        """
        __metaclass__ = abc.ABCMeta

        def __init__(self,):
            """
            """
            self.con = None
            self.cr = None

        @abc.abstractmethod
        def connect(self,):
            """Connects to the db
            """
            return None

        def create_table(self, *args, **kwargs):
            """Creates a table
            """
            query = "CREATE TABLE {} ".format(args[0])
            print query

        def executeQuery(self, query):
            """Executes a SQL query
            """
            try:
                self.cr.execute(query)
                return self.cr
            except Exception, e:
                print(e)

            return False

        def commit(self,):
            """Commits the  last change
            """
            try:
                self.con.commit()
                self.last_id()
            except Exception, e:
                print(e)

        def last_id(self,):
            """Returns the id of the last affected row
            """
            return self.cr.rowcount

      class MySqlite(Database):
        """Simple SQlite3 class handler
        """

        def __init__(self, dbfile):
            """
            """
            super(MySqlite, self).__init__()

            self.dbfile = dbfile

        def connect(self,):
            """Connects to the db
            """
            try:
                self.con = sqlite3.connect(self.dbfile)
                self.cr = self.con.cursor()
                return self.con
            except Exception, e:
                print(e)

            return None

