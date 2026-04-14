from time import sleep

usuarios = []

try:
    with open('usuarios.txt','r') as arquivo:
        for linha in arquivo:
            nome,idade = linha.strip().split(',')
            usuarios.append({'nome':nome,'idade':idade})
except FileNotFoundError:
    pass

while True:
    print('~' * 45)
    print(f"{'CADASTRO DE USUÁRIOS':^45}")
    print('~' * 45)
    print('''[1] Cadastrar usuário
[2] Listar usuários
[3] Remover usuário
[4] Sair''')

    opção = int(input('Qual a opção desejada? [1], [2], [3] ou [4]: '))

    if opção == 1:
        nome = input('Digite o nome do usuário: ')
        idade = input('Digite a idade do usuário: ')

        usuario = {'nome': nome, 'idade': idade}
        usuarios.append(usuario)
        with open('usuarios.txt','a') as arquivo:
            arquivo.write(f'{nome},{idade}\n')

    elif opção == 2:
        if len(usuarios) == 0:
            print('Nenhum usuário cadastrado!')
        else:
            for usuario in usuarios:
                print('=' * 45)
                print(f"NOME: {usuario['nome']} | IDADE: {usuario['idade']}")

    elif opção == 3:
        remove_nome = input('Digite o nome do usuário que deseja remover: ')
        encontrado = False
        for usuario in usuarios:
            if usuario['nome'] == remove_nome:
                usuarios.remove(usuario)
                encontrado = True
                print('Usuário removido com sucesso!')
                break
            if not encontrado:
                print('Usuário não encontrado')
    elif opção == 4:
        print('Saindo...')
        sleep(1)
        break
    else:
        print('Opção inválida!')
print('~=' * 23)
print('Fim do programa. Obrigado, Volte sempre!')

