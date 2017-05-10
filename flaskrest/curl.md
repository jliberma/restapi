commands
~~~~
  $ curl http://127.0.0.1:5000/
  $ curl -i http://127.0.0.1:5000/
  $ curl -i http://127.0.0.1:5000/articles
  $ curl -i http://127.0.0.1:5000/articles/123
  $ curl -X PATCH http://127.0.0.1:5000/echo
  $ curl -X POST http://127.0.0.1:5000/echo
  $ curl -i http://127.0.0.1:5000/hello?name=Luis
  $ curl -i http://127.0.0.1:5000/hello
  $ for i in GET POST PATCH PUT DELETE; do curl -X $i http://127.0.0.1:5000/echo; done
  $ echo test > message.bin
  $ curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/messages -d '{"message":"Hello Data"}'
  $ curl -H "Content-type: application/octet-stream" -X POST http://127.0.0.1:5000/messages --data-binary @message.bin
  $ curl -i http://127.0.0.1:5000/users/2
  $ curl -i http://127.0.0.1:5000/users/4
  $ curl -v -u "admin:secret" http://127.0.0.1:5000/hello
  $ curl http://127.0.0.1:5000/hello
~~~~

option		purpose
*  -X		specify HTTP request method e.g. POST
*  -H		specify request headers e.g. "Content-type: application/json"
*  -d		specify request data e.g. '{"message":"Hello Data"}'
*  --data-binary	specify binary request data e.g. @file.bin
*  -i		shows the response headers
*  -u		specify username and password e.g. "admin:secret"
*  -v		enables verbose mode which outputs info such as request and response headers and errors

