Title: Openerp Module Development : Partie I
Date: 2012-10-04
Tags: openerp, python, xml
Category: Openerp
Author: Josue Kouka
Summary: Un petit guide sur le developpement de module Openerp

###__Pre-requis__

Connaissances en programmation [python](http://www.python.org/)

###__Context__

* OS : Ubuntu 12.04

* Python : 2.7

* Openerp : 6.1

* Host : localhost

On supposera que Openerp 6 est deja installe et tourne en [localhost:8069](http://localhost:8069) 

###__Architecture d'un module openerp (>=6)__

Un module openerp est généralement composé de fichiers et repertoires suivants. 

    :::console
     module_name/
        ├── module_name.py
        ├── module_name_view.xml
        ├── __init__.py
        ├── __openerp__.py
        ├── reports
        ├── wizards
        └── workflows

***__init__*** : Indique que le dossier est un package

***module_name.py*** : Il contient les objects de votre module 

***module_name_view.xml*** : Gere les donnees via une definition d'interface (view, les menu, les interactions ...)

***__openerp__*** : Decrit le module (nom , version, auteur, dependances,...)

___reports___ : Dossier contenant les objest et fichiers lies au reporting 

___wizards___ : Dossier contenant les objets definissant les interactions client-server ([voir](http://doc.openerp.com/v6.1/developer/04_wizard.html)) 

___workflow___ : Dossier contenant la definition d'un workflow ([voir](http://doc.openerp.com/v6.0/developer/3_9_Workflow_Business_Process/index.html))



###__A- Un hello world__ 

Pour notre __hello world__ j'ai pensé à un module nous permettant d'enregistrer une famille et ses membres . 

A vos terminaux !!!

Creer un dossier __family__ dans votre espace de travail avec les fichier suivants :

1- **__openerp__.py** dont le contenu est le suivant :

    :::python
    {
        "name":"family", # le nom du module, il apparait dans la liste des modules
        "version":"1.0", # la version
        "author":"Josue", # l'auteur
        "website":"none", # site web
        "category":"Generic Modules/Others", # category du module
        "depends":["base"], # liste des modules de dependances
        "description":"Simple module permettant d'enregistrer une famille est ses memebres",
        "update_xml":["family_view.xml"], #liste des vue, dans notre cas family_view.xml
        "demo_xml":[],
        "init_xml":[],
        "active":False,
        "installable":True,
    }

**NB** : Tous les modules dependent de ***base*** .

2- **__init__.py** contenant ceci :

    :::python
    import family

Simple _importation_ d'un module python 

3- **family.py** 

    :::python
    from osv import osv, fields

    class family_family(osv.osv):
        _name = 'family.family'
        _columns = {
            'name': fields.char('Family Name',size=128),
            'member_ids': fields.one2many('family.member','family_id','Members'),
        }


    family_family()

    class family_member(osv.osv):
        _name = 'family.member'
        _columns = { # dictionnaire des champs de l'object
            'firstname': fields.char('FirstName',size=128),
            'lastname': fields.char('LastName',size=128),
            'family_id': fields.many2one('family.family','Family',ondelete='cascade'),
            'gender': fields.selection(  # definition d'un champ de selection
                [('male','Male'),
                ('female','Female'),
                ],'Gender',readonly=False,select=True),
        }
        # default : dictionnaire des valeurs par defaut
        _defaults = {
            'lastname' : lambda self, cr, uid, context : self.pool.get('family.family').browse(cr, uid, context['family_id']).name if context and 'family_id' in context else None,
            'gender' : lambda *a: 'male', # "male" sera la valeur par defaut du champ "gender"
        }

    family_member() #instanciation de la classe , __N'oubliez jamais de le faire__ 

Ce fichier decrit les objects du modules et leur caracteristiques
 
Documentation sur l'objet [osv](http://doc.openerp.com/v6.0/developer/2_5_Objects_Fields_Methods/object_attributes.html)

Documentation sur l'objet [fields](http://doc.openerp.com/v6.0/developer/2_5_Objects_Fields_Methods/field_type.html)

####**explications** :

*_defaults['lastname']*, j'ai utilisé une fonction *lambda* afin de permettre que le champ _lastname_ soit automatiquement rempli en se servant du context *family_id* definit dans le fichier *family_view.xml* au sein de l'objet *family*. 
Mais cela ne se fera que dans la condition ou un *membre* sera crée à partir du menu(vue,interface) d'une *famille*. 

4- **family_view.xml**

    :::xml

    <?xml version="1.0" ?>

    <openerp>
            <data>

        <menuitem id="family" name="Family" /> 

        <!--Family-->
        <record model="ir.ui.view" id="family_form"> <!-- definition d'une vuew dont l'id est "family_form"--> 
            <field name="name">family.form</field> <!-- nom de la vue -->
            <field name="model">family.family</field> <!-- classe sur laquelle on se base pour creer la vue (une des classes de "family.py", dans notre cas "family.family")-->
            <field name="type">form</field> <!--type de vue : form/tree/graph -->
            <field name="arch" type="xml">
                <form string="Family" > <!-- declaration d'un formulaire -->
                    <field name="name"/>  <!-- declaration d'un champ -->
                    <notebook colspan="4"> 
                        <page string="Members">
                            <field name="member_ids" domain="[('family_id','=',active_id)]" context="{'family_id':active_id}"/> <!-- definition d'un context -->
                        </page>
                    </notebook>
                </form>
            </field>
        </record>

        <record model="ir.ui.view" id="family_tree">
            <field name="name">family.tree</field>
            <field name="model">family.family</field>
            <field name="type">tree</field> <!--type de vue : tree, correspond a l'affichage en liste d'elements --> 
            <field name="arch" type="xml">
                <tree string="Family" > <!-- on declare "tree" cette fois ci et non un "form"-->
                    <field name="name"/>
                    <field name="member_ids"/> <!-- declaration des champs -->
                </tree>
            </field>
        </record>

        <!-- Notez que tous les champs declarés ici sont dans family.py, sinon une erreur sera levée -->

        <!--Definition d'une action -->

        <record model="ir.actions.act_window" id="action_family"> <!-- le model est bien différent : "ir.actions" et non "ir.ui.view" -->
            <field name="name">Family</field> <!-- nom de l'action -->
            <field name="res_model">family.family</field> <!-- model sur lequel se base l'action -->
            <field name="view_type">form</field> 
            <field name="view_mode">tree,form</field>
        </record>
        
        <!-- Declaration d'un menu -->
        <menuitem id="family_menu" name="Family" parent="family" action="action_family"/>
        <!--
            id : identifiant du menu
            name : nom du menu
            parent : le menu dont depend celui-ci, il sera donc un sous-menu 
            action : action relier au menu
        -->
        <!-- "action_family" correspond à l'id de l'acton déclarée pécedement -->

        
        <!--Members-->

        <record model="ir.ui.view" id="member_form">
            <field name="name">member.form</field>
            <field name="model">family.member</field>
            <field name="type">form</field>
            <field name="arch" type="xml">
                <form string="Member" >
                    <field name="firstname"/>
                    <field name="lastname"/>
                    <field name="gender" />
                    <field name="family_id"/>
                </form>
            </field>
        </record>

        <record model="ir.ui.view" id="member_tree">
            <field name="name">member.tree</field>
            <field name="model">family.member</field>
            <field name="type">tree</field>
            <field name="arch" type="xml">
                <tree string="Member" >
                    <field name="firstname"/>
                    <field name="lastname"/>
                    <field name="gender" />
                    <field name="family_id"/>
                </tree>
            </field>
        </record>

        <record model="ir.actions.act_window" id="action_member">
            <field name="name">Member</field>
            <field name="res_model">family.member</field>
            <field name="view_type">form</field>
            <field name="view_mode">tree,form</field>
        </record>
        
        <menuitem id="member_menu" name="Members" parent="family" action="action_member"/>
        
        </data>
    </openerp>

Documentation sur les [vues](http://doc.openerp.com/v6.0/developer/2_6_views_events/views/design_element.html)

###__B- Installation du module__

Pour installer notre module, il nous faut l'ajouter au differents modules de OpenERP afin qu'il soit reconnu .
Ceci necessite de copier le dossier de notre module (__family__) dans le dossiers __addons__ du serveur 
Openerp.
Par defaut le dossier de addons est le suivant (Voir le context en haut de page, car il peut changer en fonction de la distribution)
    
    :::console
    /usr/local/lib/python2.7/dist-packages/openerp-6.1_20121021_233212-py2.7.egg/openerp/addons

Sinon vous pouvez le verifier en regardant votre fichier de configuration de serveur Openerp

* .openerp_serverrc (dans votre home directory)

* /etc/openerp-server.conf (dans /etc/)

Mais je conseille de faire des lien symboliques 

    :::console
    yosuke@loking:/usr/local/lib/python2.7/dist-packages/openerp-6.1_20121021_233212-py2.7.egg/openerp/addons$ ln -s ~/workspace/family/

Maintenant que nous avons notre module dans le dossier des ___addons___ du serveur, il ne nous reste plus qu'a l'installer .

Connexion au serveur [localhost](http://localhost:8069)

Allez dans Parametres => Modules

![Alt module](./static_files/openerp/module.png)

Mettre a jour la liste

![Alt update_list](./static_files/openerp/update_list.png)

![Alt module_not_installed](./static_files/openerp/module_not_installed.png)


Vous devriez voir le module __family__ apparaitre sur le menu 

![Alt family](./static_files/openerp/family.png)

![Alt members](./static_files/openerp/members.png)


Voila finie cette première partie , vous etes maintenant capable d'écrire un simple module openerp et de créer toutes les familles du [jeu des 7 familles](http://fr.wikipedia.org/wiki/7_familles) . 