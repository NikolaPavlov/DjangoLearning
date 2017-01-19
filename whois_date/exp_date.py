import whois # install python-whois


>>> import whois
>>> w = whois.whois('webscraping.com')
>>> w.expiration_date  # dates converted to datetime object
datetime.datetime(2013, 6, 26, 0, 0)
>>> w.text  # the content downloaded from whois server
u'\nWhois Server Version 2.0\n\nDomain names in the .com and .net
...'

>>> print w  # print values of all found attributes
creation_date: 2004-06-26 00:00:00
domain_name: [u'WEBSCRAPING.COM', u'WEBSCRAPING.COM']
emails: [u'WEBSCRAPING.COM@domainsbyproxy.com', u'WEBSCRAPING.COM@domainsbyproxy.com']
expiration_date: 2013-06-26 00:00:00
