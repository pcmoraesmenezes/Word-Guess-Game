"""
Faça um jogo de advinhação
Você ira forecer uma plavra secreta e o usuario tentara adivinhar qual é
Faça o usuario digitar apenas uma palavra
O usuario só poderá digitar letras
A palavra deve ficar borrada de forma que a cada palavra descoberta pelo usuario vai liberando a palavra aos poucos, exemplo
******
a
*a*a**
"""
import os#Essa biblioteca servirá para limpar a tela do codigo apos o usuario acertar a palavra magica
import random #Importando a biblioteca random para poder gerar palavras aleatorias
letras = "abcdefhijklmnopqrstuvwxyz" #todas as letras possiveis que irão ser geradas na variavel
tamanho = input("Informe o tamanho da palavra mágica que deseja descobrir ") #O tamanho desejado da palavra
tamanho = int(tamanho)
palavra = ''#Aqui é onde a magica começa, essa variavel está armazenando uma string vazia
for i in range(tamanho): # Essa repetição serve para montar a palavra aleatoria
    indice = random.randint(0,len(letras)-1) #Aqui ele está usando uma função da biblioteca importada, essa função irá embaralhar as palavras
    palavra += letras[indice]
var = '' #Essa variavel serve para server de entrada do usuario da letra, caso ele digite uma letra correta irá aparecer
secreta = len(palavra) #Aqui a variavel secreta está recebendo o tamanho da palavra
magica = '*' * tamanho #Aqui a palavra secretá está escondida
print(magica) #Aqui está aparecendo a variavel magica escondida
print(f'A palavra mágica possuí {secreta} digitos') 
while magica != palavra: #A reetição seguirá até o usuario encontrar a palavra magica
    print(magica)#Aqui é um feedback do usuario de quantas palavras ja acertou
    print("Digite uma letra para tentar adivinhar")
    var = input()
    while len(var) > 1: #Caso o usuario digite mais de uma letra, o programa barrará e pedirá ao usuario que ele digite apenas uma letra
        print("Digite apenas uma letra!")
        var = input()
    if var in palavra: #Caso o valor de entrada do usuario esteja na palavra a magica ira acontecer
            for i in range(len(palavra)):  #A repetição executará até o tamanho da palavra
                    if var == palavra[i]: #Sé a letra digitada pelo usuario estiver na posição atual do vetor da palavra então acontecerá o seguinte
                        magica = magica[:i] + var + magica[i+1:] #Ocorrerá uma concatenação de strings, na qual a variavel magica que está com a palavra escondida irá começar a mostrar algumas palavras
    else:#Se não o usuario terá que digitar uma nova letra
         print("A letra não se encontra na palavra, tente novamente!")
         var = input()
        os.system('cls' if os.name == 'nt' else 'clear')#Apagará todo o terminal para que o usuario so veja a mensagem a baixo
print(f"Você encontrou a palavra!! A palavra era {palavra}")

