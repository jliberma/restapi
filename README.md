# restapi

Background:
* [Designing a RESTful Web API](http://blog.luisrei.com/articles/rest.html) -- good high level resource (no pun intended)
* [OpenStack SDKs](https://wiki.openstack.org/wiki/SDKs)
* [Introduction to the OpenStack API](https://www.linux.com/learn/introduction-openstack-api)
* [OpenStack Python SDK](https://docs.openstack.org/user-guide/sdk.html)
* [API Creation](https://www.fullstackpython.com/api-creation.html) on Full Stack Python
* [FlaskRESTful](https://flask-restful.readthedocs.io/en/0.3.5/) documentation
* [RESTful Web API with Python, Flask and MongoDB](https://www.slideshare.net/slideshow/embed_code/13539139)

Tutorials:
* [Django REST Framework Tutorial](http://www.django-rest-framework.org/tutorial/quickstart/)
* [Implement RESTful API with Python and Flask](http://blog.luisrei.com/articles/flaskrest.html) -- [Example code](https://github.com/lrei/articles/tree/master/2012-05-02-flaskrest)
* [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) -- [Github repo](https://github.com/miguelgrinberg/REST-tutorial)
* [Designing a RESTful API using Flask-RESTful](https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful)
* [REST API with Flask + MongoDB](http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_RESTAPI_with_Flask.php)
* [Creating a REST Api using Flask-Restful and MongoDB](http://salmanwahed.github.io/2015/05/01/flask-restful-mongodb-api/)
* [csvtojson Quick Start](https://www.npmjs.com/package/csvtojson#quick-start)

Environment setup
~~~~
$ conda install --name py36 flask
$ conda list -n py36
# packages in environment at /Users/jacobliberman/miniconda2/envs/py36:
#
aniso8601                 1.2.1                     <pip>
click                     6.7                      py36_0  
flask                     0.12.1                   py36_0  
Flask-HTTPAuth            3.2.2                     <pip>
Flask-RESTful             0.3.5                     <pip>
itsdangerous              0.24                     py36_0  
jinja2                    2.9.6                    py36_0  
markupsafe                0.23                     py36_2  
mkl                       2017.0.1                      0  
numpy                     1.12.1                   py36_0  
openssl                   1.0.2k                        1  
pep8                      1.7.0                    py36_0  
pip                       9.0.1                    py36_1  
pygame                    1.9.3                     <pip>
python                    3.6.1                         0  
python-dateutil           2.6.0                     <pip>
pytz                      2017.2                    <pip>
readline                  6.2                           2  
setuptools                27.2.0                   py36_0  
six                       1.10.0                    <pip>
sqlite                    3.13.0                        0  
tk                        8.5.18                        0  
werkzeug                  0.12.1                   py36_0  
wheel                     0.29.0                   py36_0  
xz                        5.2.2                         1  
zlib                      1.2.8                         3  
$ source activate py36
$ python -V
Python 3.6.1 :: Continuum Analytics, Inc.
~~~~

*Six Design Rules for a REST system*
1. client-server
2. stateless
3. server indicates if requests are cacheable
4. layered system -- intermediaries can respond instead of server without client interaction
5. uniform interface
6. optional -- servers can provide scripts or executables for clients to run in their context

REST was originally designed to fit the HTTP protocol.

In REST resources are represented as URIs.

Designing a REST API is an exercise in identifying resources to expose and writing request methods to affect them.
