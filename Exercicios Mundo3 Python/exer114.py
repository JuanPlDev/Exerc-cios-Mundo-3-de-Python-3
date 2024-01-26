import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('O site youtube não está acessivel no momento.')
else:
    print('Consegui acessar o site youtube com sucesso')