import os
import base64
file1 = raw_input('File 1: ') #inserir caminho do arquivo
file2 = raw_input('File 2: ') #iserir camiho do arquivo
File1 = os.path.basename(file1) #obtem o nome do arquivo em vez do caminho completo
File2 = os.path.basename(file2)
with open(file1, 'rb') as arquivo1:
	with open(file2, 'rb') as arquivo2:
		with open('final.py', 'w') as gerado: #arquivo responsavel por extrair e executar codigo na pasta temporaria do widows
			gerado.write(''' import os, base64

def join(binario,nameFile):
	if not os.path.exists(os.environ["TEMP"]+ "\\\" + nameFile):
		with open(os.environ["TEMP"]+ "\\\" + nameFile, "wb")
			as temporario:
 		    temporario.write(binario)
	os.startfile(os.environ["TEMP"]+ "\\\" + nameFile)
file1base64 = "%s"
join(base64.b64decode(file1base64), "%s")
file2base64 = "%s"
join(base64.b64decode(file2base64), "%s")
'''%(base64.b64encode(arquivo1.read()), File1, \
	base64.b64encode(arquivo2read()), File2))

