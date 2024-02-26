import random
import string

while True:
    # Lista de senhas
    passwords_geradas = []
    print("\n----------PASSWORD GENERATOR----------")
    
    # Quantidade de senhas a serem geradas
    num_passwords = int(input("Quantas senhas você deseja gerar? "))

    # Quantidade de caracteres
    password_length = int(input('Qual a quantidade de caracteres da senha? '))

    # Tipos de caracteres que poderão ter na senha
    uppercase_character = input("Sua senha deve conter letras maiúsculas? (S/N)")
    lowercase_character = input("Sua senha deve conter letras minúsculas? (S/N)")
    numbers = input("Sua senha deve conter números? (S/N)")
    special_characters = input("Sua senha deve conter caracteres especiais? (S/N)")

    # Validação de password
    if uppercase_character != 's' or lowercase_character != 's' or numbers != 's' or special_characters != 's':
        print("Sua senha que será gerada não é segura. É recomendado optar por um modelo de senha mais robusta, para optar por esse modelo de senha mais robusto por favor selecione todas as opções acima sendo 'S'.")
        retorno = input("Deseja corrigir as opções? (S/N): ")
        if retorno.lower() == 's':
            continue  # Reinicia o loop para pedir as opções novamente
        else:
            break  # Encerra o programa se o usuário optar por não corrigir
    else:
        # Gerando passawords
        for _ in range(num_passwords):
            allowed_characters = ''
            if uppercase_character == 's':
                allowed_characters += string.ascii_uppercase
            if lowercase_character == 's':
                allowed_characters += string.ascii_lowercase
            if numbers == 's':
                allowed_characters += string.digits
            if special_characters == 's':
                allowed_characters += string.punctuation

            if len(allowed_characters) == 0:
                print("Não há caracteres permitidos para criar a senha.")
            else:
                senha_gerada = ''.join(random.choice(allowed_characters) for _ in range(password_length))
                passwords_geradas.append(senha_gerada)
        print("\n----------GERANDO PASSWORD'S----------")
        # Exibindo senhas
        if len(passwords_geradas) > 0:
            print("Sua senha gerada é:", passwords_geradas[0])
            if num_passwords > 1:
                print("Outras senhas geradas:")
                for senha in passwords_geradas[1:]:
                    print(senha)

    # Perguntar ao usuário se deseja gerar outra senha
    resposta = input("Deseja gerar outra senha? (S/N): ")
    if resposta.lower() != 's':
        print("\n----------PROGRAMA FINALIZADO.----------")
        
        break  # Encerra o loop se a resposta não for 's'
        
