# Lista para armazenar os personagens
personagens = []

# Inicia um loop infinito, que continuará executando até que o usuário escolha a opção de sair (opção '3').
while True:
    
    # Exibe o menu de opções
    print("\nOpções:")
    print("1. Criar um novo personagem")
    print("2. Visualizar personagens")
    print("3. Sair")

    # Solicita ao usuário que escolha uma opção
    opcao = input("Escolha uma opção digitando o número: ")

    # Cria um novo personagem pedindo informações ao usuário
    if opcao == '1':
        
        nome = input("Digite o nome do personagem: ")
        descricao = input("Digite uma descrição do personagem: ")
        link_imagem = input("Digite o link da imagem do personagem: ")
        programa = input("Digite o programa do personagem: ")
        animador = input("Digite o nome do animador responsável pelo personagem: ")

        personagem = {
            'nome': nome,
            'descricao': descricao,
            'link_imagem': link_imagem,
            'programa': programa,
            'animador': animador
        }

        personagens.append(personagem)
        print("Personagem criado com sucesso!")

    # Se não houver personagens cadastrados, informa ao usuário
    elif opcao == '2':
        if not personagens:
            print("Nenhum personagem cadastrado.")
        # Caso contrário, exibe informações de todos os personagens cadastrados
        else:
            print("\nLista de Personagens:")
            for i, personagem in enumerate(personagens, start=1):
                print(f"{i}. Nome: {personagem['nome']}")
                print(f"   Descrição: {personagem['descricao']}")
                print(f"   Link da imagem: {personagem['link_imagem']}")
                print(f"   Programa: {personagem['programa']}")
                print(f"   Animador: {personagem['animador']}")

    # Encerra o programa quando o usuário escolhe a opção '3'
    elif opcao == '3':
        print("Saindo do programa. Até logo!")
        break
    # Caso o usuário escolha uma opção inválida
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
