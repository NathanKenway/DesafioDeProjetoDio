MAIOR_IDADE = 18 
IDADE_ESPECIAL = 17 #Definiu duas constantes


idade = int(input("Informe sua idade: ")) #Deixar o usuário atribuir um valor a variável idade


#Testando as condicionais IF e ELSE
if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar a CNH.")
else:
    print("Somente maiores de 18 anos podem tirar a CNH!") #Aqui termina o teste


#Testando duas condicionais IF
if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH. ") #Aqui termina o teste


#Testando as condicionais IF ,ELIF e ELIF no mesmo código
if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas,\nMas não pode fazer as aulas práticas. ")
else:
    print("Somente maiores de 18 anos podem tirar a CNH!") #Aqui termina o teste





