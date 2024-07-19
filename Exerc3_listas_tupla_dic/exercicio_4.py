# 4. Crie um dicionário representando contatos (nome, telefone).Permita ao usuário procurar por um contato pelo nome

# Criando um dicionário com contatos (nome, telefone)
contatos = {
    'Alice': '1234-5678',
    'Bob': '2345-6789',
    'Carlos': '3456-7890',
    'Diana': '4567-8901',
    'Eve': '5678-9012'
}

# Convertendo todas as chaves do dicionário para minúsculas
contatos_lower = {nome.lower(): telefone for nome, telefone in contatos.items()}

# Solicitar ao usuário que digite o nome do contato que deseja procurar
nome_procurado = input("Digite o nome do contato que deseja procurar: ").strip().lower()

# Procurar pelo nome no dicionário e exibir o telefone
if nome_procurado in contatos_lower:
    print(f"Telefone de {nome_procurado.capitalize()}: {contatos_lower[nome_procurado]}")
else:
    print("Contato não encontrado.")