import socket

# SERVIDOR
HOST = '127.0.0.1'  # IP LOCAL
PORT = 5000         # PORTA DE COMUNICAÇÃO

# SALDO INICIAL
saldo = 0

# LOGIN FIXO
MATRICULA = "2025001"
SENHA = "123456"

# FUNÇÕES
def autenticar(matricula, senha):
    return matricula == MATRICULA and senha == SENHA

def depositar(valor):
    global saldo
    saldo += valor
    return f"Depósito realizado com sucesso! \nSeu Saldo atual é de R${saldo:.2f}"

def sacar(valor):
    global saldo
    if valor <= saldo:
        saldo -= valor
        return f"Saque realizado no valor de R${valor:.2f} \nSeu Saldo atual é de R${saldo:.2f}"
    else:
        return "Saldo insuficiente!"

def ver_saldo():
    return f"Saldo atual: R${saldo:.2f}"

# INICIAR SERVIDOR
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print("Servidor iniciado. Aguardando conexão...")

conexao, endereco = servidor.accept()
print(f"Conectado ao cliente {endereco}")

# AUTENTICAÇÃO
while True:
    dados = conexao.recv(1024).decode()
    matricula, senha = dados.split(";")
    if autenticar(matricula, senha):
        conexao.send("OK".encode())
        break
    else:
        conexao.send("ERRO".encode())

# MENU EM LOOP
while True:
    opcao = conexao.recv(1024).decode()

    if opcao == "1":  # DEPÓSITO
        valor = float(conexao.recv(1024).decode()) # VALOR EM FLOAT SÓ PARA TESTE
        resposta = depositar(valor)
        conexao.send(resposta.encode())

    elif opcao == "2":  # SAQUE
        valor = float(conexao.recv(1024).decode()) # VALOR EM FLOAT SÓ PARA TESTE
        resposta = sacar(valor)
        conexao.send(resposta.encode())

    elif opcao == "3":  # VER SALDO
        resposta = ver_saldo()
        conexao.send(resposta.encode())

    elif opcao == "4":  # SAIR
        conexao.send("Até mais!".encode())
        break

conexao.close()
servidor.close()
