
"""Tracebacks de módulos e pacotes
Ao usar funções de módulos e pacotes, o código dos arquivos baixados será executado em segundo plano.

Se esse código produzir um erro, o traceback mencionará o nome do arquivo no qual o erro ocorreu.

A execução desse código produz o seguinte erro. Em que arquivo ocorre o erro?

import requests
requests.get(url="https://app.datacamp.com", content=True)

Traceback (most recent call last):
--> 73 -
return request("get", url, params=params, **kwargs)
File /usr/local/lib/python3.8/dist-packages/requests/api.py:59, in request (method, url, **kwargs)
55 # By using the 'with' statement we are sure the session is closed, thus we
56 # avoid leaving sockets open which can trigger a ResourceWarning in some
57 # cases, and look like a memory leak in others.
58 with sessions.Session() as session:
59 return session.request(method=method, url=url, **kwargs)
TypeError: request() got an unexpected keyword argument 'content'
"""

# base.py
# requests.py
# api.py

# A resposta correta é: api.py