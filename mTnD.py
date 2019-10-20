mTnD = { }
estados = input()
sigma = input()
tal = input()
simbolo_inicio = input()
branco = input()

transicoes = int(input())

for i in range(transicoes):

	quintupla = input()
	quintupla = quintupla.split(' ')
	chave = (quintupla[0],quintupla[1])

	if chave not in mTnD:
		mTnD[chave] = []

	mTnD[chave].append([quintupla[2],quintupla[3],quintupla[4]])

inicio = input()
final = input()
palavras = input()
palavras = palavras.split(' ')

for palavra in palavras:
	estado = inicio
	pilha_de_exec = []
	fita = []
	fita.append(simbolo_inicio)

	for letra in palavra:
		fita.append(letra)

	fita.append(branco)
	cabecote = 1
	pilha_de_exec.append([fita,cabecote,estado])

	while True:
		if(len(pilha_de_exec) != 0):
				dados = pilha_de_exec.pop(0)
				estado = dados[2]
				cabecote = dados[1]
				fita = dados[0]
		if((estado,fita[cabecote]) in mTnD):
			for acao in mTnD[(estado,fita[cabecote])]:
				novafita = fita.copy()				
				novafita[cabecote] = acao[1]
				novoestado = acao[0]
				if(acao[2] == "D"):
					novoCabecote = cabecote + 1
				elif(acao[2]=="E"):
					novoCabecote = cabecote - 1
				else:
					novoCabecote = cabecote
				if(novoCabecote == len(novafita)):
					novafita.append(branco)
				pilha_de_exec.append([novafita,novoCabecote,novoestado])
					
		else:
			if estado in final:
				break

			if(len(pilha_de_exec) == 0):
				break

	if estado not in final:
		print('N')
	else:
		print('S')
