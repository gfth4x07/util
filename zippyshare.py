'''
    Donwload de um arquivo do Zippyshare
'''

import urllib.request

inicio = 0  # Qual episodio começar
fim = 20  # quando parar
alls="""http://www30.zippyshare.com/v/Xk8Yjzuv/file.html
http://www30.zippyshare.com/v/U35Qoitc/file.html
http://www30.zippyshare.com/v/xXucE9K4/file.html
http://www30.zippyshare.com/v/gffxfSXk/file.html
http://www30.zippyshare.com/v/8BHvEUMI/file.html
http://www30.zippyshare.com/v/I9Zv7UzP/file.html
http://www30.zippyshare.com/v/5ZUnuqAz/file.html
http://www30.zippyshare.com/v/GNNLAwZk/file.html
http://www30.zippyshare.com/v/Xm8w6BxP/file.html
http://www30.zippyshare.com/v/isgPF0eY/file.html
http://www30.zippyshare.com/v/gfSAbltW/file.html
http://www30.zippyshare.com/v/84xiggEC/file.html
http://www30.zippyshare.com/v/BO1DeLs4/file.html
http://www30.zippyshare.com/v/SWNSIQ6c/file.html
http://www30.zippyshare.com/v/QrYQaVPA/file.html
http://www30.zippyshare.com/v/zfEGyPol/file.html
http://www30.zippyshare.com/v/uNGM68Ba/file.html
http://www30.zippyshare.com/v/5KSOp31M/file.html
http://www30.zippyshare.com/v/hxxJd0xU/file.html
http://www30.zippyshare.com/v/H4x81WQg/file.html
http://www30.zippyshare.com/v/GsGqXxcs/file.html
http://www30.zippyshare.com/v/Xy0qFGvU/file.html
http://www30.zippyshare.com/v/NgKmpWbC/file.html
http://www30.zippyshare.com/v/dG5AYytD/file.html
http://www30.zippyshare.com/v/399mn8nd/file.html
http://www30.zippyshare.com/v/KpmZeJuA/file.html
http://www30.zippyshare.com/v/YPagYDIC/file.html
http://www30.zippyshare.com/v/vYMkwqse/file.html
http://www30.zippyshare.com/v/QYG35IkP/file.html
http://www30.zippyshare.com/v/H87d74zF/file.html
http://www30.zippyshare.com/v/vkwtT4hE/file.html
http://www30.zippyshare.com/v/jp0shkJF/file.html
http://www30.zippyshare.com/v/GrUCSyTS/file.html
http://www30.zippyshare.com/v/G6fosmJr/file.html
http://www30.zippyshare.com/v/eFEGnBfQ/file.html
http://www30.zippyshare.com/v/7oaBkVga/file.html
http://www30.zippyshare.com/v/KubM4fqg/file.html
http://www30.zippyshare.com/v/Glk83IZX/file.html
http://www30.zippyshare.com/v/L9oQ6s4b/file.html
http://www30.zippyshare.com/v/ydXws4BV/file.html
http://www30.zippyshare.com/v/WqSMTlCK/file.html
http://www30.zippyshare.com/v/PTyAWMpi/file.html
http://www30.zippyshare.com/v/u9bixVL0/file.html
http://www30.zippyshare.com/v/RFSGshxd/file.html
http://www30.zippyshare.com/v/x4Su3dWh/file.html
http://www30.zippyshare.com/v/vzZgFf9y/file.html
http://www30.zippyshare.com/v/HSYsGSI1/file.html
http://www30.zippyshare.com/v/uqrqIPOf/file.html
http://www30.zippyshare.com/v/R3vcVhhL/file.html
http://www30.zippyshare.com/v/W8zsz09x/file.html
http://www30.zippyshare.com/v/lC5IB4Z6/file.html
http://www30.zippyshare.com/v/s6uRJW3F/file.html
http://www30.zippyshare.com/v/wkypjVjn/file.html
http://www30.zippyshare.com/v/D7ZBsxjP/file.html
http://www30.zippyshare.com/v/5wQi75Fh/file.html
http://www30.zippyshare.com/v/DXYaFWll/file.html
http://www30.zippyshare.com/v/9JDuwRcr/file.html
http://www30.zippyshare.com/v/W81C0LqS/file.html
http://www30.zippyshare.com/v/oIrhITEP/file.html
http://www30.zippyshare.com/v/rH0Fk3hE/file.html
http://www30.zippyshare.com/v/NGDy33qZ/file.html
http://www30.zippyshare.com/v/z76aFWBY/file.html
http://www30.zippyshare.com/v/y8oBd0dx/file.html
http://www30.zippyshare.com/v/aFgSdrk0/file.html
http://www30.zippyshare.com/v/n6DputnX/file.html
http://www30.zippyshare.com/v/bjS7Kf68/file.html
http://www30.zippyshare.com/v/Pac15lab/file.html
http://www30.zippyshare.com/v/nHfibmtT/file.html
http://www30.zippyshare.com/v/FKXJeuy6/file.html
http://www30.zippyshare.com/v/5YU93YGc/file.html
http://www30.zippyshare.com/v/eH15QKYC/file.html
http://www30.zippyshare.com/v/mfFqjep3/file.html
http://www30.zippyshare.com/v/6aQtwr6B/file.html
http://www30.zippyshare.com/v/RO3UpbYP/file.html
http://www30.zippyshare.com/v/WSaYsZMv/file.html
http://www30.zippyshare.com/v/7s8Mlxd6/file.html
http://www30.zippyshare.com/v/jwPw98Y9/file.html
http://www30.zippyshare.com/v/yZFPlj3i/file.html
http://www30.zippyshare.com/v/q4Sw6mPk/file.html
http://www30.zippyshare.com/v/0eBca9aB/file.html
http://www30.zippyshare.com/v/mMfI17MT/file.html
http://www30.zippyshare.com/v/jyZyHScx/file.html
http://www30.zippyshare.com/v/2VivbfH9/file.html
http://www30.zippyshare.com/v/iBU0VQup/file.html
http://www30.zippyshare.com/v/aUjN7lmT/file.html
http://www30.zippyshare.com/v/T3FvwYvU/file.html
http://www30.zippyshare.com/v/n6BngohV/file.html
http://www30.zippyshare.com/v/DR2NXxMA/file.html
http://www30.zippyshare.com/v/i8FhqKBX/file.html
http://www30.zippyshare.com/v/yq6S0CD3/file.html
http://www30.zippyshare.com/v/UWnlfRxt/file.html
http://www30.zippyshare.com/v/MNwzUN6c/file.html
http://www30.zippyshare.com/v/jZWIobD9/file.html
http://www30.zippyshare.com/v/yXrXZ3K5/file.html
http://www30.zippyshare.com/v/LC2o0lew/file.html
http://www30.zippyshare.com/v/wyXJvKxy/file.html
http://www30.zippyshare.com/v/43GKZQFc/file.html
http://www30.zippyshare.com/v/SNrYc2A5/file.html
http://www30.zippyshare.com/v/QScvF9Tw/file.html
http://www30.zippyshare.com/v/nxuGw9SX/file.html
http://www30.zippyshare.com/v/wDjGfxyx/file.html
http://www30.zippyshare.com/v/v9GzRIeY/file.html
http://www30.zippyshare.com/v/cRlknvOW/file.html
http://www30.zippyshare.com/v/enJgrpxq/file.html
http://www30.zippyshare.com/v/RyPHWE5L/file.html
http://www30.zippyshare.com/v/h3OF3I3M/file.html
http://www30.zippyshare.com/v/F0dgjnvd/file.html
http://www30.zippyshare.com/v/XVl3ZDXk/file.html
http://www30.zippyshare.com/v/RFoCVt3v/file.html
http://www30.zippyshare.com/v/vFDvO1fw/file.html
http://www30.zippyshare.com/v/jpHcHDHO/file.html
http://www30.zippyshare.com/v/dVHziNSv/file.html
http://www30.zippyshare.com/v/Zt41QWXr/file.html
http://www30.zippyshare.com/v/zpHCUPpZ/file.html
http://www30.zippyshare.com/v/uDMD3rzk/file.html
http://www30.zippyshare.com/v/a95HxUV0/file.html
http://www30.zippyshare.com/v/RZZqis5d/file.html
http://www30.zippyshare.com/v/1zyT23Cg/file.html
http://www30.zippyshare.com/v/GKo6bM3d/file.html
http://www30.zippyshare.com/v/sBidIL4O/file.html
http://www30.zippyshare.com/v/7goxvUYn/file.html
http://www30.zippyshare.com/v/5oOl8vwV/file.html
http://www30.zippyshare.com/v/LwiZG847/file.html
http://www30.zippyshare.com/v/NZm3yNcz/file.html
http://www30.zippyshare.com/v/zjs8l72q/file.html
http://www30.zippyshare.com/v/sbDq4AYQ/file.html
http://www30.zippyshare.com/v/B2aFo16Z/file.html
http://www30.zippyshare.com/v/iD6hQWco/file.html
http://www30.zippyshare.com/v/407Q5YIb/file.html
http://www30.zippyshare.com/v/dP1b8AkD/file.html
http://www30.zippyshare.com/v/mmFHP1Wo/file.html
http://www30.zippyshare.com/v/TmP4f8aT/file.html
http://www30.zippyshare.com/v/EkNrvdQ7/file.html
http://www30.zippyshare.com/v/jgZzubsD/file.html
http://www30.zippyshare.com/v/6ZXvMkNK/file.html
http://www30.zippyshare.com/v/ORGz1dHb/file.html
http://www30.zippyshare.com/v/eAKoUmh4/file.html
http://www30.zippyshare.com/v/6t36PTjq/file.html
http://www30.zippyshare.com/v/kjLRB9P5/file.html
http://www30.zippyshare.com/v/we5Dm4qB/file.html
http://www30.zippyshare.com/v/VDMstUDL/file.html
http://www30.zippyshare.com/v/HLfkYim5/file.html
http://www30.zippyshare.com/v/Ezpo6N7f/file.html
http://www30.zippyshare.com/v/bPnjBGKh/file.html
http://www30.zippyshare.com/v/2fs2rB3V/file.html
http://www30.zippyshare.com/v/k28kAZow/file.html
http://www30.zippyshare.com/v/57DprV3A/file.html
http://www30.zippyshare.com/v/M7c2FlIH/file.html""".split('\n')

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

for i in range(inicio-1,fim):
    get_zippyshare(alls[i])
