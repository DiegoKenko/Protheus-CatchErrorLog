import sys
import os
import connDB
import threaderror as TE
from datetime import date

path = '//10.2.0.5/Totvs 12/Microsiga/Protheus/Bin/'
servers = [
    'appserver_SLV1', 'appserver_SLV2', 'appserver_SLV3', 'appserver_SLV4',
    'appserver_SLV5', 'appserver_SLV9', 'appserver_WF', 'appserver_WEB',
    'appserver_SLVX', 'appserver_RMT', 'appserver_MEURH', 'appserver_MASTER',
    'appserver_JOB2', 'appserver_JOB_TMS', 'appserver_JOB_ABAX',
    'appserver_JOB', 'appserver_DEBUG', 'appserver_API', 'appserver_ACD'
]
nomeArquivo = 'console.log'
nomeArquivo1 = 'console.log.00001.log'
nomeArquivo2 = 'console.log.00002.log'
erroCount = 0
pastas = os.listdir(path)
listaAppserver = []
linhas = []
ativo = False
erro = ''
linhas = []
resultados = ['']
cont = 0
log = []


def lerArquivo():
    for e in pastas:
        if e in servers:
            try:
                with open(path + e + "/" + nomeArquivo,
                          encoding='cp1252',
                          errors='ignore') as arquivo:
                    log.append(arquivo.readlines())
            except IOError:
                print("File not accessible at " + path + e + "/" +
                      nomeArquivo1)

    for e in pastas:
        if e in servers:
            try:
                with open(path + e + "/" + nomeArquivo1,
                          encoding='cp1252',
                          errors='ignore') as arquivo:
                    log.append(arquivo.readlines())
            except IOError:
                print("File not accessible at " + path + e + "/" +
                      nomeArquivo1)
    for e in pastas:
        if e in servers:
            try:
                with open(path + e + "/" + nomeArquivo2,
                          encoding='cp1252',
                          errors='ignore') as arquivo:
                    log.append(arquivo.readlines())
            except IOError:
                print("File not accessible at " + path + e + "/" +
                      nomeArquivo1)

def arquivoData():
    if date.fromtimestamp(os.stat(path + e + "/" +
                                  nomeArquivo).st_mtime) == date.today():
        arquivoDeHoje = True
    else:
        arquivoDeHoje = False


def verificaVersao():
    """ verifica versao do appserver """


lerArquivo()

for l in log:
    porta = 'XXXX'
    for j in l:
        if j.find('Application Server started on port ') > 0:
            porta = '[porta:' + j[
                (j.find('Application Server started on port ') +
                 34):(j.find('started on port') + 40)]
        if j.startswith('THREAD ERROR'):
            ativo = True
        if j.endswith('*/\n'):
            ativo = False
            resultados.append('')
            resultados[cont] = resultados[cont] + ' ' + porta
            cont += 1
        if ativo:
            resultados[cont] += j + ' '

for k in resultados:
    dados = TE.threaderror(k)
    dados.Cria()
   