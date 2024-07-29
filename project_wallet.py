import time
import datetime
# Menu de funções

saldo = 0.0
entrada = 0.0
saida = 0.0
despesa_total = 0.0
economia = 0.0

# categorias
lazer = 0.0
alimentacao = 0.0
moradia = 0.0
educacao = 0.0
despesas_fixas = 0.0
transporte = 0.0
saude = 0.0
vestuario = 0.0
outro = 0.0


while True:
    print("Qual operação deseja realizar?")
    print("1️⃣ - Ver Saldo")
    print("2️⃣ - Cadastrar entrada de valores")
    print("3️⃣ - Cadastrar saída de valores")
    print("4️⃣ - Cadastrar meta de economia")
    print("5️⃣ - Relatórios")
    print("6️⃣ - Sair")

    print("-------------------------------------")

    opcao = int(input())
   
    if opcao == 1:
        print("-------------------------------------")
        print(f"Saldo: R${saldo:.2f}")
        print("-------------------------------------")
        time.sleep(1)

    
    elif opcao == 2:
        print("-------------------------------------")
        print("Insira o valor que entrou na conta: ")
        
        while True:
            entrada = float(input())

            if entrada < 0:
                print("Valor inválido! Tente novamente.")
                time.sleep(1)
                continue
            else:
                break

        saldo += entrada
        print("-------------------------------------")
    
    elif opcao == 3:
        while True:
            print("-------------------------------------")
            print("Insira o valor gasto: ")
            print("Digite '0' para sair: ")

            saida = float(input())

            if saida < 0:
                print("Valor inválido! Tente novamente.")
                time.sleep(1)
                continue
            elif saida == 0:
                break
            else:
                        
                while True: 
                    print("Onde esse dinheiro foi gasto?")
                    print("1️⃣ - Alimentação")
                    print("2️⃣ - Transporte")
                    print("3️⃣ - Moradia")
                    print("4️⃣ - Saúde")
                    print("5️⃣ - Educação")
                    print("6️⃣ - Lazer")
                    print("7️⃣ - Vestuário")
                    print("8️⃣ - Outro")
                    opt = int(input())

                    if opt == 1:
                        alimentacao += saida
                        break
                    elif opt == 2:
                        transporte += saida
                        break
                    elif opt == 3:
                        moradia += saida
                        break
                    elif opt == 4:
                        saude += saida
                        break
                    elif opt == 5:
                        educacao += saida
                        break
                    elif opt == 6:
                        lazer += saida
                        break
                    elif opt == 7:
                        vestuario += saida
                        break
                    elif opt == 8:
                        outro += saida
                        break
                    else:
                        print("Opção inválida! Tente novamente.")
                        time.sleep(1)
                        continue

                saldo -= saida
                despesa_total += saida
                print("-------------------------------------")



    elif opcao == 4:
        print("-------------------------------------")
        print("Qual é a meta de economia mensal desejada?")

        while True:
            economia = float(input())

            if economia < 0:
                print("Valor inválido! Tente novamente.")
                time.sleep(1)
                continue

            else:
                break
        print("-------------------------------------")



    elif opcao == 5:
        print("-------------------------------------")
        while True: 
            print("Qual relatório deseja visualizar?")
            print("1️⃣ - Entrada de valores")
            print("2️⃣ - Saída de valores")
            print("3️⃣ - Despesas por categoria")
            print("4️⃣ - Meta de economia")
            print("5️⃣ - Imprimir relatório total")
            opt = int(input())

            if opt == 1:
                print(f"Entrada de valores: R${entrada:.2f}")
                time.sleep(1)
                break


            elif opt == 2:
                print(f"Saída de valores: R${despesa_total:.2f}")
                time.sleep(1)
                break


            elif opt == 3:
                print("📊 --- DESPESAS POR CATEGORIA --- 📊")
                time.sleep(0.5)
                print(f"🍽️ Alimentação: R${alimentacao:.2f}")
                time.sleep(0.5)
                print(f"🏠 Moradia: R${moradia:.2f}")
                time.sleep(0.5)
                print(f"🚗 Transporte: R${transporte:.2f}")
                time.sleep(0.5)
                print(f"🩺 Saúde: R${saude:.2f}")
                time.sleep(0.5)
                print(f"📚 Educação: R${educacao:.2f}")
                time.sleep(0.5)
                print(f"🎉 Lazer: R${lazer:.2f}")
                time.sleep(0.5)
                print(f"👗 Vestuário: R${vestuario:.2f}")
                time.sleep(0.5)
                print(f"📦 Outro: R${outro:.2f}")
                time.sleep(0.5)
                break


            elif opt == 4:
                print(f"🎯 Saldo Atual: R${saldo:.2f}")
                time.sleep(0.5)
                print(f"Meta de economia: R${economia:.2f}")
                if saldo >= economia:
                    print("Status: ATINGIDA!")
                    time.sleep(1)
                else:
                    print("Status: PENDENTE")
                    print(f"Faltam R${economia - saldo:.2f} para atingir a meta!")
                    time.sleep(1)
                break

            #opcao nova (imprimir relatório total)
            elif opt == 5:
                print("💰💼 Relatório Financeiro 💼💰")
                time.sleep(0.5)
                print(f"📥 Entrada de valores: R${entrada:.2f}")
                print()
                time.sleep(0.5)
                print(f"📤 Saída de valores: R${despesa_total:.2f}")
                print()
                time.sleep(0.5)
                print("📊 --- DESPESAS POR CATEGORIA --- 📊")
                time.sleep(0.5)
                print(f"🍽️ Alimentação: R${alimentacao:.2f}")
                time.sleep(0.5)
                print(f"🏠 Moradia: R${moradia:.2f}")
                time.sleep(0.5)
                print(f"🚗 Transporte: R${transporte:.2f}")
                time.sleep(0.5)
                print(f"🩺 Saúde: R${saude:.2f}")
                time.sleep(0.5)
                print(f"📚 Educação: R${educacao:.2f}")
                time.sleep(0.5)
                print(f"🎉 Lazer: R${lazer:.2f}")
                time.sleep(0.5)
                print(f"👗 Vestuário: R${vestuario:.2f}")
                time.sleep(0.5)
                print(f"📦 Outro: R${outro:.2f}")
                print()
                time.sleep(0.5)
                print(f"🎯 Meta de economia: R${economia:.2f}")
                time.sleep(0.5)
                print(f"🎯 Saldo Atual: R${saldo:.2f}")
                time.sleep(0.5)
                if saldo >= economia:
                    print("🎉 Status: ATINGIDA! 🎉")
                else:
                    print("⚠️ Status: PENDENTE ⚠️")
                    print(f"Faltam R${economia - saldo:.2f} para atingir a meta!")
                time.sleep(1)
                break



            else:
                print("Opção inválida! Tente novamente.")
                continue
        print("-------------------------------------")
    elif opcao == 6:
        break

    else:
        print("Opção inválida! Tente novamente.")
        continue