python-blekko
=============

This module provides simple bindings to the `Blekko`_ API. To use the API,
`contact Blekko for an API key`_.

This module currently only supports **search queries** and **page statistics**.
The API also provides tools for manipulating slashtags, but this library doesn't
support that yet.

The library is internally rate-limited to one query per second in accordance
with Blekko's guidelines.

.. _Blekko: https://blekko.com/
.. _contact Blekko for an API key: http://help.blekko.com/index.php/tag/api/

Searching
---------

To use the API, first create a ``Blekko`` object using your "source" or "auth"
API key::

    import blekko
    api = blekko.Blekko(source='my_api_key')

Then, to perform searches, use the ``query`` method. Its arguments are the
search terms (as a string) and, optionally, the page number::

    results = api.query('peach cobbler')

The returned object is a sequence containing ``Result`` objects, which
themselves have a number of useful fields::

    for result in results:
        print result.url_title
        print result.url
        print result.snippet

Errors in communicating with the server are raised as ``BlekkoError``
exceptions, so you'll want to handle these exceptions when making calls to the
API.

An Example
''''''''''

Putting it all together, here's a short script that gets a single link for
search terms on the command line::

    import blekko
    import sys

    _api = blekko.Blekko(source='my_api_key')

    def get_link(terms):
        try:
            res = _api.query(terms + ' /ps=1')
        except blekko.BlekkoError as exc:
            print >>sys.stderr, str(exc)
            return None
        if len(res):
            return res[0].url

    if __name__ == '__main__':
        link = get_link(' '.join(sys.argv[1:]))
        if link:
            print(link)
        else:
            sys.exit(1)

Page Statistics
---------------

Blekko provides an API for getting SEO-related statistics for a URL. Use the
``pagestats`` method, which takes a URL as its only parameter, to get a
dictionary containing information about a page::

   >>> api.pagestats('http://python.org/')
   {u'cached': True, u'ip': u'82.94.164.162', u'host_rank': 3835.107267,
   u'host_inlinks': 467267, u'adsense': None, u'dup': True,
   u'rss': u'http://www.python.org/channews.rdf'}

Credits
-------

These bindings were written by `Adrian Sampson`_ and modeled after the `Perl
bindings`_ by Greg Lindahl. The source is made available under the `MIT
license`_.

.. _Adrian Sampson: https://github.com/sampsyo/
.. _Perl bindings: http://search.cpan.org/~wumpus/WebService-Blekko-1.00_07/
.. _MIT license: http://www.opensource.org/licenses/MIT
