'''
    Donwload de um arquivo do Zippyshare
'''

import urllib.request

def get_zippyshare(url):
    """
    Faz o donwload do arquivo da url dada.
    Util para quantdo tem vários arquivos
    """ 
    sock = urllib.request.urlopen(url).read().decode("utf-8")
    l = sock.split('\n')

    name = l[3][36:-8]  # Nome do arquivo
    a = int(l[266][12:-1])  # var a
    b = int(l[267][12:-1])  # var b
    a3 = int(int(a)/3)

    url_split = url.split('/')
    donwload=url[:27]+'/d/'+url_split[4]+'/'+str(a3+a%b)+'/'+name  # junta tudo

    print("Donwloading",name)
    urllib.request.urlretrieve(donwload, name)
    print("OK")

urls = '''http://www11.zippyshare.com/v/ejS9viD6/file.html
http://www11.zippyshare.com/v/4fed2WyB/file.html
http://www11.zippyshare.com/v/z20vICYY/file.html'''.split('\n')

for i in alls:
    get_zippyshare(i)
