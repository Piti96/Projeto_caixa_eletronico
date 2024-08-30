menu  = """
__________MENU________
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
_______________________

"""
saldo = 0
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
           extrato += f"Deposito: R$ {valor:.2f}\n"
           print (f"Você realizou um depósito de R$  {valor:.2f}")
       else:
           print("A operação falhou! Tente novamente.")
           
           
           
    elif opcao == 2:
           valor = float(input(" Informe i valor que deseja sacar: "))
           
           saldo_insuficiente = valor > saldo
           limite_insuficiente = valor > limite
           excedeu_saques = numero_saque >= LIMITE_SAQUES
           
           if valor > 0 and not saldo_insuficiente and not limite_insuficiente and not excedeu_saques:
              saldo -= valor
              extrato += f" Saque: R$ {valor:.2f}\n"
              numero_saque += 1
              print (f"Você realizou um saque de R$ {valor:.2f}")
 
           elif saldo_insuficiente:
               print ("Saldo insuficiente para realizar a operação!")
           
           elif limite_insuficiente:
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
               
           