# restapi

* [OpenStack SDKs](https://wiki.openstack.org/wiki/SDKs)
* [Introduction to the OpenStack API](https://www.linux.com/learn/introduction-openstack-api)
* [OpenStack Python SDK](https://docs.openstack.org/user-guide/sdk.html)
* [Implement RESTful API with Python and Flask](http://blog.luisrei.com/articles/flaskrest.html)
* [Django REST Framework Tutorial](http://www.django-rest-framework.org/tutorial/quickstart/)
* [API Creation](https://www.fullstackpython.com/api-creation.html) on Full Stack Python
* [FlaskRESTful](https://flask-restful.readthedocs.io/en/0.3.5/) documentation
* [Designing a RESTful API using Flask-RESTful](https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful)
* Miguel Grinberg's [Complete REST Tutorial](https://github.com/miguelgrinberg/REST-tutorial) on Github
* [Designing a RESTful Web API](http://blog.luisrei.com/articles/rest.html) -- good high level resource (no pun intended)


*Implement RESTful API with Python and Flask*
Example code: [https://github.com/lrei/articles/tree/master/2012-05-02-flaskrest](https://github.com/lrei/articles/tree/master/2012-05-02-flaskrest)

~~~~
$ source activate py36
$ python -V
Python 3.6.1 :: Continuum Analytics, Inc.
$ conda install --name py36 flask
~~~~

*Six Design Rules for a REST system*
1. client-server
2. stateless
3. server indicates if requests are cacheable
4. layered system -- intermediaries can respond instead of server without client interaction
5. uniform interface
6. optional -- servers can provide scripts or executables for clients to run in their context

REST was originally designed to fit the HTTP protocol.

In REST, resources are represented and URIs.

Designing a REST service or API is an exercise in identifying the resources that will be exposed and how they will by affected by the different request methods.
