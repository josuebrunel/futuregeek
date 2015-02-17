Title: oeutils
Date: 2013-03-23
Author: Josue Kouka
Tags: openerp, python, xmlrpc, api
Category: Projects
Summary: Small python wrapper of the xml-rpc api for Openerp


##OEUTILS

__oeutils__ is a small python wrapper of the xml-rpc API for OpenERP. It is useful when it comes to  manipulate your OpenERP objects.
It is not as powerful as __erppeek__ yet but i hope that with your help one day it will ^_^.
It's inspired from [__erpeek__](https://github.com/florentx/erppeek) and we can say thanks to Florent for that.
It's kind of a personal project and i wanted to be able to do almost the same thing as __erppeek__ but the easiest way.
This tool lacks a lot of thing so far, but i hope that over time i will be able to improve it.
I'm sure that i'll be laughing in the next 2 years while seeing this.

###Features
With __oeutils__ you are able to :

* Create objects

* Read objects

* Update objects

* Delete objects

* Search objects

* Search models

* Get models fields


###How to

####Connexion

    :::python
    >>>from oeutils import Openerp
    >>>o = Openerp(login,pwd,dbname)
    >>>o.connect()

####Methods

    :::python
    >>>m = 'family.family'
    >>>ids = o.search(m,[]) # or juste o.search(m)
    >>>ids
    [1, 2]
    >>>
    >>> famliy = {
    ... 'name': 'kouka',
    ... }
    >>> o.create('family.family',famliy)
    2
    >>>o.read(m,ids,[])
    [{'member_ids': [1], 'name': 'loking', 'id': 1}, {'member_ids': [], 'name': 'kouka', 'id': 2}]
    >>> o.edit(m,2,{'name':'koukson'})
    True
    >>> o.read(m,o.search(m,[]),[])
    [{'member_ids': [1], 'name': 'loking', 'id': 1}, {'member_ids': [], 'name': 'koukson', 'id': 2}]
    >>> o.read(m,o.search(m,[]),[])
    [{'member_ids': [1], 'name': 'loking', 'id': 1}, {'member_ids': [], 'name': 'koukson', 'id': 2}, {'member_ids': [], 'name': 'kim', 'id': 3}]
    >>> o.delete(m,3)
    True
    >>> o.read(m,o.search(m,[]),[])
    [{'member_ids': [1], 'name': 'loking', 'id': 1}, {'member_ids': [], 'name': 'koukson', 'id': 2}]
    >>> o.models('family')    
    ['family.family', 'family.member']
    >>> o.keys(m)
    ['member_ids', 'name']

That's all, thanks in advance for your feebacks

Please check this docstring for more informations ^_~.
