Title: LokingYQL
Date: 2014-8-30 
Author: Josue Kouka
Category: Projects
Tags: yql, python, loking, wrapper, yahoo

lokingYQL : Yet another python YQL Wrapper
=========

LokingYQL is a Python wrapper of the Yahoo Query Language.

Yahoo! Query Langauge Documentation and Support
===============================================

* Yahoo! Query Language - http://developer.yahoo.com/yql/
* Yahoo! Developer Network: http://developer.yahoo.com
* Yahoo! Application Platform - http://developer.yahoo.com/yap/
* Yahoo! Social APIs - http://developer.yahoo.com/social/
* Yahoo! QUery Language Console https://developer.yahoo.com/yql/console/

version 1.0
===========

* Access to resources requiring authentication

version 0.5.6
=============
* fetch data
* access to community data
* select data format (xml/json)
* change data source
* filter data 

fixes:
------
* fix handling of default and on the fly response format
* fix limit on ***select(...).where(...)*** when no limit value is passed
* fix limit on ***get(...)***

installation
============

    :::shell
    $ python setup.py install 


how to use
==========

    :::python
    >>> import lokingyql
    >>> yql = lokingyql.LokingYQL()
    >>> yql.diagnostics = True # To turn diagnostics on


access to community tables
--------------------------

    :::python
    >>> yql = lokingyql.LokingYQL()
    >>> rep = yql.rawQuery('desc yahoo.finance.quotes ')
    >>> rep.json()
    {u'error': {u'lang': u'en-US', u'description': u'No definition found for Table yahoo.finance.quotes'}}
    >>> yql.community= True # Setting up access to community
    >>> rep = yql.rawQuery('desc yahoo.finance.quotes ')
    >>> rep.json()
    {u'query': {u'count': 1, u'lang': u'en-US', u'results': {u'table': {u'src': u'http://www.datatables.org/yahoo/finance/yahoo.finance.quotes.xml', u'hash': u'061616a1c033ae89aaf2cbe83790b979', u'name': u'yahoo.finance.quotes', u'request': {u'select': {u'key': {u'required': u'true', u'type': u'xs:string', u'name': u'symbol'}}}, u'meta': {u'sampleQuery': u'\n\t\t\tselect * from yahoo.finance.quotes where symbol in ("YHOO","AAPL","GOOG","MSFT")\n\t\t'}, u'security': u'ANY'}}, u'created': u'2014-08-24T11:26:48Z'}}
    >>>


***OR***

    :::python
    >>> import lokingyql
    >>> yql = lokingyql.LokingYQL(community=True)
    >>> # do your magic 


changing response format (xml or json)
--------------------------------------

The response format is by default ***json***.

    :::python
    >>> import lokingyql
    >>> yql = lokingyql.LokingYQL(format='xml', community=True)
    >>> rep = yql.rawQuery('select name, woeid from geo.states where place="Congo"')
    >>> rep.text
    u'<?xml version="1.0" encoding="UTF-8"?>\n<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="11" yahoo:created="2014-08-27T04:52:22Z" yahoo:lang="en-US"><results><place xmlns="http://where.yahooapis.com/v1/schema.rng"><name>Cuvette-Ouest Department</name><woeid>55998384</woeid></place><place xmlns="http://where.yahooapis.com/v1/schema.rng"><name>Cuvette Department</name><woeid>2344968</woeid></place><place xmlns="http://where.yahooapis.com/v1/schema.rng"><name>Plateaux District</name><woeid>2344973</woeid></place><place xmlns="http://where.yahooapis.com/v1/schema.rng"><name>Sangha</name><woeid>2344974</woeid></place><place xmlns="http://where.yahooapis.com/v1/schema.rng"><name>Lekoumou</name><woeid>2344970</woeid></place><place xmlns="http://where.yahooapis.com/v1/schema.rng"><name>Pool Department</name><woeid>2344975</woeid></place><place xmlns="http://where.yahooapis.com/v1/schema.rng"><name>Likouala Department</name><woeid>2344971</woeid></place><place xmlns="http://where.yahooapis.com/v1/schema.rng"><name>Niari Department</name><woeid>2344972</woeid></place><place xmlns="http://where.yahooapis.com/v1/schema.rng"><name>Brazzaville</name><woeid>2344976</woeid></place><place xmlns="http://where.yahooapis.com/v1/schema.rng"><name>Bouenza Department</name><woeid>2344967</woeid></place><place xmlns="http://where.yahooapis.com/v1/schema.rng"><name>Kouilou</name><woeid>2344969</woeid></place></results></query><!-- total: 19 -->\n<!-- engine7.yql.bf1.yahoo.com -->\n'
    >>> rep = yql.rawQuery('select name, woeid from geo.states where place="Congo"', format='json')
    >>> rep.json()
    {u'query': {u'count': 11, u'lang': u'en-US', u'results': {u'place': [{u'woeid': u'55998384', u'name': u'Cuvette-Ouest Department'}, {u'woeid': u'2344968', u'name': u'Cuvette Department'}, {u'woeid': u'2344973', u'name': u'Plateaux District'}, {u'woeid': u'2344974', u'name': u'Sangha'}, {u'woeid': u'2344970', u'name': u'Lekoumou'}, {u'woeid': u'2344975', u'name': u'Pool Department'}, {u'woeid': u'2344971', u'name': u'Likouala Department'}, {u'woeid': u'2344972', u'name': u'Niari Department'}, {u'woeid': u'2344976', u'name': u'Brazzaville'}, {u'woeid': u'2344967', u'name': u'Bouenza Department'}, {u'woeid': u'2344969', u'name': u'Kouilou'}]}, u'created': u'2014-08-27T04:52:38Z'}}
    >>>



Methods
-------

use(data_provider_url)
-----------------------

Changes the data provider

    :::python
    >>> yql.use('http://myserver.com/mytables.xml') 


desc(tablename)
---------------
 returns table description
 
    :::python
    >>> response = yql.desc('weather.forecast')
    >>> response.json()
    {u'query': {u'count': 1, u'lang': u'en-US', u'results': {u'table': {u'request': {u'select': [{u'key': [{u'required': u'true', u'type': u'xs:string', u'name': u'location'}, {u'type': u'xs:string', u'name': u'u'}]}, {u'key': [{u'required': u'true', u'type': u'xs:string', u'name': u'woeid'}, {u'type': u'xs:string', u'name': u'u'}]}]}, u'security': u'ANY', u'meta': {u'documentationURL': u'http://developer.yahoo.com/weather/', u'sampleQuery': u'select * from weather.forecast where woeid=2502265', u'description': u'Weather forecast table', u'author': u'Yahoo! Inc'}, u'hash': u'aae78b1462a6a8fbc748aec4cf292767', u'name': u'weather.forecast'}}, u'created': u'2014-08-16T19:31:51Z'}}
    >>>


rawQuery(query)
----------------

Allows you to directly type your query

    :::python
    >>> response = yql.rawQuery("select * from geo.countries where place='North America'")
    >>> # deal with the response


select(table, fields, limit).where(filters, ...)
------------------------------------------------

Select a table i.e *weather.forecast*.
If *table* not provided, it will use the default table. If there's no such thing as a default table, it will raise a *NoTableSelectedError*

***NB*** : A simple select doesn't return any data. Use ***GET*** instead.

    :::python
    >>> response = yql.select('geo.countries', [name, code, woeid]).where(['name', '=', 'Canada'])
    >>> response.json()
    {u'query': {u'count': 1, u'lang': u'en-US', u'results': {u'place': {u'woeid': u'23424775', u'name': u'Canada'}}, u'created': u'2014-08-16T19:04:08Z'}}
    >>> ...
    >>> rep = yql.select('geo.countries', ['name', 'woeid'], 2).where(['place', '=', 'Africa'])
    >>> rep.json()
    {u'query': {u'count': 2, u'lang': u'en-US', u'results': {u'place': [{u'woeid': u'23424740', u'name': u'Algeria'}, {u'woeid': u'23424745', u'name': u'Angola'}]}, u'created': u'2014-08-17T10:52:49Z'}}
    >>>
    >>> rep = yql.select('geo.countries', ['name', 'woeid'], 2).where(['place', 'in', ('Africa', 'Europe')])
    >>> rep.json()
    {u'query': {u'count': 2, u'lang': u'en-US', u'results': {u'place': [{u'woeid': u'23424740', u'name': u'Algeria'}, {u'woeid': u'23424745', u'name': u'Angola'}]}, u'created': u'2014-08-17T11:22:49Z'}}
    >>>


get(table, fields, limit)
--------------------------

Same as ***SELECT***, but instead returns data.

**REMINDER** : Some tables require a **where clause**, therefore ***GET*** won't work on those tables, use *select(...).where(...)* instead .

    :::python
    >>> yql.get('geo.countries', ['name', 'woeid'], 1)
    >>> rep.json()
    {u'query': {u'count': 1, u'lang': u'en-US', u'results': {u'place': {u'woeid': u'23424966', u'name': u'Sao Tome and Principe'}}, u'created': u'2014-08-17T10:32:25Z'}}
    >>>

