def app(environ, start_response):
  resp = environ['QUERY_STRING'].split("&")
  res = ''
  for item in resp:
	res += item +"\r\n"
  start_response('200 OK', [('Content-Type', 'text/plain')])
  return [res]
