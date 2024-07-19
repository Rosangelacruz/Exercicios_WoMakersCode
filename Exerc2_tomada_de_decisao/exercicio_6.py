# 6. Crie um programa que solicite ao usuário um login e uma senha. O programa deve
# permitir o acesso apenas se o usuário for "admin" e a senha for "admin123",
# caso contrário imprima uma mensagem de erro.

# Solicita ao usuário login e senha
login = input('Digete seu login: ')
senha = input('Digite sua senha: ')

# Verifica se o login e a senha são
if login == 'admin' and senha == 'admin123':
    print('Acesso permitido!')
else:
    print('Acesso negado erro no login ou na senha.')