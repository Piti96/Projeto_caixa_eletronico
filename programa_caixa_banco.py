menu  = """
__________MENU________
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
_______________________

"""
saldo = 100
limite = 500
extrato = " "
numero_saque = 0
LIMITE_SAQUES = 3


while True:
    print(menu)
    
    opcao = int(input("Ecolha a opção desejada: "))
    
    if opcao == 1:
       valor = float(input("Digite o valor do deposito: "))
       if valor > 0:
           saldo += valor
           extrato += f"Deposito: R$ {valor}\n"
           
       else:
           print("A operação falhou! Tente novamente.")
           
           
           
    elif opcao == 2:
           valor = float(input(" Informe i valor que deseja sacar: "))
           
           saldo_insuficiente = valor > saldo
           
           limite_insuficiente = valor > limite
           
           excedeu_saques = numero_saque >= LIMITE_SAQUES
           
           if valor > 0:
              saldo -= valor
              extrato += f" Saque: R$ {valor}\n"
              numero_saque += 1
            
           
           
           elif saldo_insuficiente:
               print ("Saldo insuficiente para realizar a operação!")
           
           elif limite_insufuciente:
                  print ("Você não possui limite disponivel para realizar essa operação!")
            
           elif excedeu_saques:
                  print ("A operação não pode ser realizada, pois você atingiu o limite diário de saques!")
               
             
           
           else:
               print("A operacao falhou")
               
               
    elif opcao == 3:
           print ("\n__________EXTRATO__________")
           print (" Não foram realizadas movimentações no período."   if not extrato   else extrato)
           print (f"\n Saldo: R$ {saldo}")
           print ("________________________________")
               
               
               
    elif opcao ==4:
               print("Saindo, obrigado por utilizar nossos serviços!")
               break
               
               
    else:
               print("Operção falhou. tente novamente!")
               
           