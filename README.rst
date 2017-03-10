Store Parser
============

Easy to parse googleplay or appstore data.

Dependancy
----------
BeautifulSoup: Great html parser.

Usage
-----
.. code:: python

  import store_parser
  
  url = 'https://play.google.com/store/apps/details?id=com.android.chrome'
  data = store_parser.parse_googleplay(url)
  print data
