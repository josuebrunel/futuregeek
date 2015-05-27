Title: Attacher une methode a une classe en python
Slug: attacher-une-methode-a-une-classe-en-python
Date: 2015-01-17 15:25:31
Tags: python, programming, poo, oop
Category: Programming
Author: Josue Kouka 
Lang: fr
Summary: Comment attacher une methode a une classe ou une instance de classe

Serieusement, je ne vois pas trop dans quelle condition ceci peut etre utile, disons que c'est juste bon a savoir.

Soit un object *Person*

    :::python
    >>> class Person(object):
    ...   def __init__(self, name, age=None):
    ...     self.name = name
    ...     self.age = age
    ...   def introduce(self,):
    ...     print("Hi! My name is {0}".format(name))
    ...
    >>> p = Person('josh', 25)
    >>> p.introduce()
    Hi ! My name is Josh


Disons que l'on veut ajouter une methode permettant de _dire son age_

    :::python
    >>> def iam(self,):
    ...   print("I'm {0}".format(self.age))
    ...
    >>> p.iam = iam
    >>> p.iam()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: iam() takes exactly 1 argument (0 given)


Le code ci dessus ne marche pas, assez evident. 

Parcontre si on passe bien notre instance a la methode celle ci s'execute normalement. Encore evident, vu que **self** designe l'instance a laquelle appartient la **methode**. 

    :::python
    >>> p.iam(p)
    I'm 25
    >>>


Tout ceci a un sens en faisant ceci.

    :::python
    >>> type(p.introduce)
    <type 'instancemethod'>
    >>> type(p.iam)
    <type 'function'>
    >>>


On voit clairement que **introduce** est une **methode d'instance**, ce qui n'est pas le cas de **iam** (Je ne parle pas du groupe de musique lol).

On a toujours pas repondu a notre seule question : **Comment ajouter une methode a une classe ou une instance de classe**


### Le mecanisme permettant de *binder* une methode a une classe ou une de ses instances

    :::python
    >>> from types import MethodType
    >>> p.iam = MethodType(iam, p, Person)
    >>> p.iam()
    I'm 25
    >>> 
    >>> type(p.iam)
    <type 'instancemethod'>
    >>>

On voit bien que notre **iam** est bien une ***Methode d'instance*** et qu'on peut y faire un appel sans passer l'_instance_ comme argument.

    :::python
    >>> pf = Person('Sarah', '24')
    >>> pf.iam()
    >>> Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    AttributeError: 'Person' object has no attribute 'iam'
    >>> Person.iam = MethodType(iam, None, Person)
    >>> pf = Person('Sarah', 24)
    >>> pf.iam()
    I'm 24
    >>>


Dans le code ci dessus, on voit bien que pour l'appliquer a toutes les _nouvelles instances_ il faut ajouter la **nouvelle methode** a la **classe**.

Ben voila, pas sure que ce soit utile, mais plutot interressant a savoir.





