#nao.local.eth : 169.254.66.118
# nao.local.wif : 10.251.99.92
# => on redirige sur nao.local

import os
eth = "169.254.66.118"
wif = "192.168.0.1"
response = os.system("ping -c 1 " + eth)
def ipNao():
    if response == 0:
        print eth, ' \n nao est en local'
        return eth;
    else:
        resp = os.system("ping -c 1 " + wif)
        if resp == 0:
            print wif, ' \n nao est en wifi'
            return wif
        else:
            print "no host to root ! The program will be stopped"
            exit()

ipnao = ipNao()
