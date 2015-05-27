Title: Introduction a bottle 
Slug: introduction-a-bottle
Date: 2013-08-07 08:00:29
Tags: python,  bottle, peewee
Category: Programming
Author: Josue Kouka 
Lang: 
Status: draft
Summary: Simple introcudtion à un super génial micro-framework python

Hello guys !!!
Oui oui, ça fait des années.  Depuis le temps que j'ai envie d'écrire cette introduction à bottle . Je me suis levé comme d'habitude,
la flemme d'écrire un article. 
Enfin bref comme dirait [Franklin](http://www.youtube.com/watch?v=tYVNZrDh5y0).

## INSTALLATION ##

	:::console
	yosuke@loking:~$ mkvirtualenv bottle
	New python executable in bottle/bin/python
	Installing distribute............................................................................................................................................................................................................................done.
	Installing pip................done.
	(bottle)yosuke@loking:~$ pip install bottle 
	Requirement already satisfied (use --upgrade to upgrade): bottle in ./.virtualenvs/bottle/lib/python2.7/site-packages
	Cleaning up...
	(bottle)yosuke@loking:~$ 

On a créé un environement virtuel (virtualenvwrapper) puis fait l'installation de **bottle** dans cette envrinement.

## HELLO WORLD ##

    :::python
    from bottle import route, run, template

    @route('/hello')
    def hello():
        '''Returns a simple hello world
        '''
        return "Hello World"

    @route('/hello/<name>')
    def hello_name(name):
        '''Returns hello + name
        '''
        return "Hello %s" %(name,)

    @route('/hello/age/<age:int>') # <var:int>, 'int' est un filtre
    def tell_age(age):
    '''Returns Age
    '''
    return "You're %s" %(age,)

    run(host='localhost', port='8888', reloader=True, debug=True)

####Explications###

## REQUETTES ##

### -Get ###

### -Post ###




