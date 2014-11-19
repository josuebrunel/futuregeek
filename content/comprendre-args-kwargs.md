Title: Comprendre *, **, *args, **kwargs
Date: 2013-03-26
Author: Josue Kouka 
Tags: python
Category: Programming
Summary: Comprendre les deballeurs et les varargs en python

Hi guys !!!

**unpackers** et **varargs** ? It doesn't ring a bell ? oh come on (redneck accent).

Je suis sure que vous avez deja vu des instructions du genre :

    :::python
    >>>...
    >>>myfunc(*myliste) # Appel
    >>>...
    >>>myfunc(**mydict) # Appel
    >>>...
    >>>def myfunc(*args, **kwargs): # définition
          ...
    

Maintenant vous voyez tres bien de quoi je parle, c'est bien.

__unpackers__ : ___*___ et ___**___

__varargs__ : ___*args___ et ___**kwargs___

On va faire quelques petites experiences

###Experience 1 : ___*___


    :::python    
    >>> def my_func(a, b, c):
    ...   print a, b, c
    ... 
    >>> mylist = range(1,4)
    >>> mylist
    [1, 2, 3]
    >>> my_func(l) #Appel 1
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: my_func() takes exactly 3 arguments (1 given)
    >>> my_func(*mylist) #Appel 2
    1 2 3
    >>> mylist.append(4)
    >>> mylist
    [1, 2, 3, 4]
    >>> my_func(*mylist) #Appel 3
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: my_func() takes exactly 3 arguments (4 given)
    >>>
    

Lors du premier appel _Appel 1_, le shell nous a renvoyé une erreur, ce qui
est tout a fait logique. On a passe une **liste** a une fonction qui attend 3
paramètres.

Ensuite lors de _Appel 2_, aucune erreur du shell. Seul différence avec _Appel
1_, est le __*__ devant notre liste ___mylist___ .

Le ___*___ a __deballe__ les éléments de notre liste et les a envoyé à la
fonction, c'est à dire que ce n'est pas **_[1,2,4]_** (une liste) qui a été
envoyée mais **_1,2,3_**, en gros les éléments de la liste.

On ajoute un nouvel élément à la liste puis on rappelle la function ( _Appel
3_ ), cette fois ci **ERREUR**. Tout simplement parce que notre fonction
attends 3 paramètres et non 4.

Pour conclure , **_*_** sert a deballer les éléments d'une _liste_, d'un
_tuple_ ... On ne l'utilise que lors d'un appel de foncton ou méthode.

###Experience 2: ___*args___

    :::python    
    >>> def my_func(x, *args):
    ...   print "x est ", x
    ...   print "args est ", args
    ... 
    >>> my_func(1,2,3,4) #Appel 1
    x est  1
    args est  (2, 3, 4)
    >>> my_func(1,2,3,4,'varargs') #Appel 1 bis
    x est  1
    args est  (2, 3, 4, 'varargs')
    >>> my_func(1) # Appel 2
    x est  1
    args est  ()
    >>>
    >>> mylist
    [1, 2, 3]
    >>> my_func(1,*mylist) #Appel 3
    x est  1
    args est  (1, 2, 3)
    >>> my_func(1,mylist) #Appel 4
    x est  1
    args est  ([1, 2, 3],)
    >>>
    

On peut remarquer que dans les appels _Appel 1_ et _Appel 1 bis_, **x** est
eguale à **1**. Et que les autres paramètres sont assignés à ***args**, qui
les prend sous forme de tuples peu importe leur taille.

Dans l'appel _Appel 2_, un seul paramètre est passé à la fonction, et ce seul
paramètre est assigne a __x__ et vu qu'il n'y a pas d'autres paramètres,
__*args__ recoit un _tuple_ vide.

Dans l'appel _Appel 3_, on passe un paramètre et une ___liste deballee___
(\*mylist), les éléments de la liste sont donc assignés à __*args__ sous forme
de tuples.

Dans l'appel _Appel 4_, on passe un paramètre et une ___simple liste___
(mylist), la liste est donc assignée à __*args**__, ce qui nous donne un tuple
de liste (_([])_).

Un ***myvar** dans la **définition** d'une fonction/méthode est capable de
recevoir n'importe quoi et un nombre non defini de paramètre.

### Petit Use Case:

On doit écrire une fonction qui calcule la somme des nombres qui lui sont
passés, sans tenir compte du premier paramètre .

    :::python  
    >>> def calculer_somme(*args):
    ...   return sum(args)
    ... 
    >>> def calculer_somme_sans_premier(premier, *args):
    ...   print "Premier est ", premier
    ...   print "args est ", args
    ...   ma_somme = calculer_somme(*args) #Pourquoi le "*args" 
    ...   print "Ma somme est ", ma_somme
    ... 
    >>> calculer_somme(1,2,3) #Appel 1
    6
    >>> calculer_somme([1,2,3]) #Appel 2, je fais passer une liste
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 2, in calculer_somme
    TypeError: unsupported operand type(s) for +: 'int' and 'list'
    >>>
    >>> calculer_somme_sans_premier(10,1,2,3) #Appel 3
    Premier est  10
    args est  (1, 2, 3)
    Ma somme est  6
    

#### Explications:

**calculer_somme** est une simple fonction qui calcule la somme des nombres d'un iterable qui lui est passé en paramètre. (Easy)

**calculer_somme_sans_premier** calcule la somme des nombres qui lui sont passés en paramètres sans tenir compte du premier.

Dans l'appel _Appel 1_, je fais passer des nombres, on a le resultat escompté
car les paramètres sont transformés en un _tuple_ (un iterable) à cause du
***args** ensuite traités par **_sum_**.

Dans l'appel _Appel 2_, j'essaie de faire passer une liste, j'ai une
**TypeError**, parce que **sum** est une fonction _builtin_ qui renvoit la
somme des **nombres** d'un _iterable_. Or en passant _([1,2,3])_, ***args** =
([1,2,3],) qui est un tuple de liste.

A la question _pourquoi le *args ?_ dans **calculer_somme_sans_premier** lors
de l'appel de **calculer_somme**, la réponse est qu'il faut deballer ***args**
sinon on passerait _(1,2,3)_ a **calculer_somme**. Dans l'appel _Appel 3_ on
remarque bien que **args** est un tuple, or il faut passer des **nombres**,
qui ne sont que ses **éléments**, d'ou le **deballage**.


### **Experience 3:** ___**___

    :::python
    >>> def myfunc(a, b, c):
    ...   print a, b, c
    ... 
    >>> myfunc(1,2,3)
    1 2 3
    

Fonction toute simple à laquelle on fait passer des nombres et nous les
affichent.

    :::python
    >>> mydict = {'b':5,'c':6}
    >>> myfunc(1,**mydict)
    1 5 6
    >>> mydict['a']=4
    >>> myfunc(**mydict)
    4 5 6
    >>>
    

On crée un dictionnaire dont les _keys_ sont **'b'** et **'c'** et les
valeurs, respectivement, **5** et **6**. On fait passer ce dictionnaire à la
fonction en utilisant ******, le dictionnaire affiche correctement les
valeurs.

Le _unpackers_ ****** a déballé les valeurs du dictionnaire en fonction des
différentes **clés**. Euh oui les **clé**, remarquez qu'elles portent les
memes noms que nos paramètres lors de la définition de notre fonction ,
rappelez vous du : **_def myfunc(a, b, c):_**...

    :::python
    >>> mydict['d']=7
    >>> myfunc(**mydict)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: myfunc() got an unexpected keyword argument 'd'
    

On decide d'ajouter un élément a notre dictionnaire (keys+value). On essaie de
déballer le dictionnaire lors de l'appel, un **TypeError**. La **clé** **'d'**
est inattendue. Normal, pas definie lors de la declaration de la fonction.

    :::python
    >>> mydict.pop('d')
    7
    >>> mydict
    {'a': 4, 'c': 6, 'b': 5}
    >>> myfunc(*mydict)
    a c b
    >>>
    

On supprime le couple **'d':7**, on appelle la fonction avec un seul *****, et
les différentes clés du dictionnaire apparaissent.

Pour conclure, ****** permet de deballer les éléments d'un _dictionnaire_. Il
n'est utilisé que lors des appels de fonction, tout comme *****.


### **Experience 4:** ___**kwargs___


Redefinisson notre fonction _fun_

    :::python    
    >>> def fun(a, **kwargs):
    ...   print a, kwargs
    ...
    

Cette fonction n'a qu'un seul paramètre formel, **'a'**. Avec ****kwargs**
elle peut prendre autant de mot clés en argumants, mots clés ,qui seront
ajoutés à la liste des paramètres formels de la fonction temporairement.

    :::python
    >>> fun(1, b=2, c=3, z=26)
    1 {'c': 3, 'b': 2, 'z': 26}
    >>>
    

****kwargs** dans cette fonction, on recoit un **_dictionnaire_** contenant des _arguments mot clés_. Et oui ! _kwargs_ sera un dictionnaire, mais on ne passe pas de dictionnaire à la fonction. 
    
    :::python
    >>> def fun(a, **kwargs):
    ...   print "a est ", a
    ...   print "On attends kwargs[b] et kwargs[z]"
    ...   print "kwargs[b] ", kwargs['b']
    ...   print "kwargs[z] ", kwargs['z']
    ... 
    >>> fun(1, b=2, c=36, z=26)
    a est  1
    On attends kwargs[b] et kwargs[z]
    kwargs[b]  2
    kwargs[z]  26
    

On peut definir tous les mots clés que l'on veut, à l'exception de **'a'**
parce que il apprtient deja à un paramètre formel. **c = 36** n'apparait pas
parce qu'on a decidé de ne pas l'afficher. Les nouveaux paramètres sont
considérés comme les couples **(key,value)** d'un dictionnaire normal.

Déclarons un dictionnaire et éssayons de le passer à la fonction.

    :::python
    >>> d = {'b': 10, 'f':'hello maman', 'z':'je suis z'}
    >>> d
    {'b': 10, 'z': 'je suis z', 'f': 'hello maman'}
    >>> fun(1, d)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: fun() takes exactly 1 argument (2 given)
    

Oui oui !!! **ERROR**. La fonction prends des éléments du type **(key,value)**
et non un **dictionnaire**. Ces éléments sont transformés en dictionnaire
après, pas avant leur passage.

Si l'on déballe les éléments du dictionnaire :

    :::python
    >>> fun(1, **d)
    a est  1
    On attends kwargs[b] et kwargs[z]
    kwargs[b]  10
    kwargs[z]  je suis z
    >>> d['z'] = 26
    >>> fun(1, **d)
    a est  1
    On attends kwargs[b] et kwargs[z]
    kwargs[b]  10
    kwargs[z]  26
    >>>
    

En utilisant ****** on a débalé les éléments de notre dictionnaire.

****kwargs** est tout simplement un dictionnaire vide a qui l'on dit : voila une **clé** et sa **valeur**, considere les comme un de tes éléments.


### **Quand faut il les utiliser ?**


Brièvement, je dirai toutes les fois que l'on **hérite** d'une _classe_ ou que
l'on **surcharge** l'une des méthodes de la classes heritée.

    :::python
    >>> class Papa(object):
    ...   def __init__(self, name):
    ...     self._name = name 
    ...   def save(self, insert=False, update=False):
    ...     if update and insert :
    ...       raise ValueError("Impossible de faire un insert et un update au meme moment")
    ...     if update :
    ...       print "Ligne mise a jour"
    ...     if insert :
    ...       print "Nouvelle ligne creee"
    ... 
    >>>
    

On a crée une classe _Papa_, dont les objets peuvent etre enregistrés dans une
base de données grace à la méthode **save()**. En fonction de l'argument, on
met à jour un enregistrement ou on en ajoute un.

    :::python
    >>> class Filston(Papa):
    ...   def save(self, *args, **kwargs): # 1
    ...     if self.name == 'josue' :
    ...       super(Filston, self).save(*args, **kwargs)# 2 
    ...     else:
    ...       return None
    ... 
    >>>
    

Ensuite on definit une class _Filston_ héritant de _Papa_ permettant de créer
ou mettre a jour des enregistrements sous une condition. Or nous savons que la
manipulation des enregistrements se fait grace à la méthode **save()**, alors
il faut appeler la méthode **save()** de la classe **Papa**. En plus,
**save()** de **Filston** doit etre capable tous les arguments que **save()**
de **Papa** peut recevoir et les faire passer a cette derniere. D'ou
l'utilisation de **_args__ et de ___*kwargs** dans **save()** de **Filstion**.

#### Execution

    :::python
    >>> foo = Filston('josue')
    >>> foo.save()
    >>> foo.save(insert=True)
    Nouvelle ligne creee
    >>> foo.save(update=True)
    Ligne mise a jour
    >>> foo.save(update=True)
    

#### Explications

On crée une instance de **Filston** et on appelle sa méthode **save()**. On
invoque un _save(insert=True)_ ,couple **clé** et **valeur**, donc
**kwargs['insert']=True** (kwargs est devenu un dictionnaire) #1. Ensuite en
passe **kwargs** en le deballant grace a ******. ce qui fait a ce que le
deuxieme appel de **save()** soit **_super(Fislton, self).save(insert=True)_**
#2, ce qui correspond a notre définition dans la classe **Papa**.

Voila, c'est fini, j'espère que vous avez une meilleur comprehension des
**unpackers** et des **varargs** en python.
