# Title: 
Python and the Semantic Web: Building a Linked Data Fragment Server with Asynco and Redis

# Category
Industry Uses

# Language 
English

# Duration 
No preference

# Description 
A barrier to wider adoption of the semantic web is scaling SPARQL endpoints for large Linked Datasets. A promising approach, Linked Data Fragments, allows for small queries instead of complex SPARQL. This talk is about a Python-based Linked Data Fragments Server project using the new Asynco Python module and Redis. Testing is being done with datasets from the Library of Congress and the DPLA.

# Audience:
Intermediate

# Objectives

*  Learn about developing Asynco Python application development
*  Semantic Web SPARQL Endpoints
*  Linked Data Fragments

# Details Abstract
In 2001, Sir Tim Berners-Lee and other originated the idea of the [semantic web][SW], an internet where web content is understandably and actionable by computers. Berners-Lee work along with many others, resulted in a large number of specifications from the W3C like [RDF][RDF], [OWL][OWL], [SKOS][SKOS], and other vocabularies  for both describing and enhancing content on the web through the use of RDF Graphs made up of large number triples made up **subject-predicate-object** statements.

Traditionally there have three methods for organizations to publish their RDF data on the web; providing a data-dump download, creating a subject page with linked-data, or by providing a SPARQL endpoint to query their RDF data.  There are problems with each approach with the data-dump and subject pages requiring extensive client programming to be usable or high-server overhead in the case of a SPARQL endpoint.

[Ruben Verborgh][RV] of [Ghent University] [GHENT] in Belgium originated the concept of Linked Data Fragments that offer a middle-ground between these options. Instead of requiring massive client or server processing, the Linked Data Fragments instead offer a lightweight querying pattern called **Triple Pattern Fragment** made up of data matching a **subject-predicate-object** triple pattern, metadata consisting of the total triple count, and controls for browsing all of the other fragments in the same dataset.  A Triple Pattern Fragments server is a server that offers this service. A Triple Pattern Fragments client can connect to the Triple Pattern Fragments server and can as well deconstruct SPARQL queries into the simpler triple pattern fragments queries to the server. 

At a recent digital library conference, a group made up of representatives from a variety of different academic, public, and non-profit organizations like [Digital Public Library of America](http://dp.la), [Amherst College](https://www.amherst.edu/), [Boston Public Library](http://www.bpl.org/), and [Colorado College](https://www.coloradocollege.edu) came together and organized what eventually became a Python-based implementation of an open-source  [Linked Data Fragments server](https://github.com/jermnelson/linked-data-fragments)  using the new Python 3.4 asyncio module for building a fast, lightweight network server that uses Redis, a NoSQL datastore technology, for caching results. 

This presentation will present the preliminary results from testing the Linked Data Fragments server with large datasets from college library catalogs as well as datasets from the Library of Congress and the DPLA.



[OWL]:  http://www.w3.org/TR/owl2-syntax/
[SW]:  http://www.cs.umd.edu/~golbeck/LBSC690/SemanticWeb.html
[RDF]: http://www.w3.org/RDF/
[RV]: http://ruben.verborgh.org/
[SKOS]: http://www.w3.org/2004/02/skos/
[GHENT]: http://www.ugent.be/

# Outline

1. Introduction
    1. What is SPARQL, RDF, and the Semantic Web
    1.  How do libraries and cultural heritages fit into the semantic web
    1.  Linked Data Fragments server Project team made up of representatives from Digital Public Library of America, Amherst College, Boston Public Library, and Colorado College.
1.  Challenges of scaling SPARQL queries
    1.  Scaling to billions of RDF triples
    1.   Multiple queries 
1.  Linked Data Fragments
    1.  Originated by Ruben Verborgh
    1.  A Hydra W3C [specification][SPEC] 
    1.  Datasets, Selectors, Metadata, and Hypermedia controls
    1.  Shifts processing from server to client
1. Python Linked Data Fragment Server
    1.  Quick overview of Python and new asyncio module
    1.  Triple Pattern Parser
    1.  NoSQL Redis technology is used as a caching a layer
1. Initial Testing Results
1.  Future plans
    
# Additional Notes
I have presented at a number of conferences including the following recent presentations that have web accessible links (my practice has been to create a dedicate website for each presentation instead of using Powerpoint or other presentation software):

- American Theological Library Association's  Annual Conference 2015 - [Introduction to BIBFRAME](http://intro2libsys.info/atla-2015)
- Open Repositories 2015 - [Learning to use Fedora 4 as a BIBFRAME Linked Data Platform](http://intro2libsys.info/or-2015)
- NISO Webinar 2015 - [Exploring BIBFRAME at a Small Academic Library](http://intro2libsys.info/niso-2015-webinar)
- Code4Lib 2015 Conference - [Building a BIBFRAME Catalog with a Catalog Pull Platform](http://intro2libsys.info/code4lib-2015)
- Digital Library Forum 2014 - [Using BIBFRAME, Flask, and Fedora4 as a Catalog Pull Platform](http://intro2libsys.info/dlf-forum-2014-poster)
- Pycon 2014 Poster presentation [Replacing a Legacy Library Catalog @ Colorado College][PYCON]

I have been very active in Library Open Source development including code contributions to [pymarc](https://github.com/edsu/pymarc), the Library of Congress [BIBFRAME Editor](http://bibframe.org/tools/editor/), and of course my own Semantic Web research focusing on building open-source catalogs like [bibcat.org](http://bibcat.org) being built as a result of a contract with the Library of Congress. All these projects, including the Linked Data Fragments server, is part of the larger Catalog Pull Platform for libraries, museums, and other cultural heritage organizations. 


[SPEC]:  http://www.hydra-cg.com/spec/latest/linked-data-fragments/

