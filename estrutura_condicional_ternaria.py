saldo = 2000
saque = 5000

#A string "sucesso" vai ser exibida caso o saldo seja maior ou igual ao saque, caso ao contrário, a string "falha".
status = "Sucesso" if saldo >= saque else "Falha" 
print(f"{status} ao realizar o saque!") 