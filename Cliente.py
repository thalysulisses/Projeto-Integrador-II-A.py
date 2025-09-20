import socket

# CONFIGURAÇÕES DO CLIENTE
HOST = '127.0.0.1'
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# LOGIN
while True:
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    cliente.send(f"{matricula};{senha}".encode())
    resposta = cliente.recv(1024).decode()

    if resposta == "OK":
        print("\nLogin realizado com sucesso!\n")
        break
    else:
        print("Matrícula ou senha inválidos. Tente novamente.\n")

# MENU
while True:
    print("\n-----MENU-----")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    cliente.send(opcao.encode())

    if opcao == "1":  # DEPÓSITO
        valor = input("Digite o valor para depósito: ")
        cliente.send(valor.encode())
        print(cliente.recv(1024).decode())

    elif opcao == "2":  # SAQUE
        valor = input("Digite o valor para saque: ")
        cliente.send(valor.encode())
        print(cliente.recv(1024).decode())

    elif opcao == "3":  # VER SALDO
        print(cliente.recv(1024).decode())

    elif opcao == "4":  # SAIR
        print(cliente.recv(1024).decode())
        break

cliente.close()
