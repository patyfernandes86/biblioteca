class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.status_emprestimo = 'Disponível'

class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimos = []

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.registro_membros = []

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    def adicionar_membro(self, membro):
        self.registro_membros.append(membro)

    def emprestar_livro(self, livro, membro):
        if livro.status_emprestimo == 'Disponível':
            livro.status_emprestimo = 'Emprestado'
            membro.historico_emprestimos.append(livro)
            print("Livro emprestado com sucesso!")
        else:
            print("O livro não está disponível para empréstimo.")

    def devolver_livro(self, livro, membro):
        if livro in membro.historico_emprestimos:
            livro.status_emprestimo = 'Disponível'
            membro.historico_emprestimos.remove(livro)
            print("Livro devolvido com sucesso!")
        else:
            print("Este livro não está registrado como emprestado por este membro.")

    def pesquisar_livro_por_titulo(self, titulo):
        for livro in self.catalogo:
            if livro.titulo == titulo:
                return livro
        print("Livro não encontrado.")

    def pesquisar_livro_por_autor(self, autor):
        for livro in self.catalogo:
            if livro.autor == autor:
                return livro
        print("Livro não encontrado.")

    def pesquisar_livro_por_id(self, id):
        for livro in self.catalogo:
            if livro.id == id:
                return livro
        print("Livro não encontrado.")

# Interface de linha de comando simples para interação com o usuário
def main():
    biblioteca = Biblioteca()

    while True:
        print("\n1. Adicionar Livro")
        print("2. Adicionar Membro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Pesquisar Livro por Título")
        print("6. Pesquisar Livro por Autor")
        print("7. Pesquisar Livro por ID")
        print("8. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            id = input("Digite o ID do livro: ")
            livro = Livro(titulo, autor, id)
            biblioteca.adicionar_livro(livro)

        elif escolha == '2':
            nome = input("Digite o nome do membro: ")
            numero_membro = input("Digite o número de membro: ")
            membro = Membro(nome, numero_membro)
            biblioteca.adicionar_membro(membro)

        elif escolha == '3':
            titulo = input("Digite o título do livro a ser emprestado: ")
            membro_numero = input("Digite o número de membro: ")
            livro = biblioteca.pesquisar_livro_por_titulo(titulo)
            membro = next((membro for membro in biblioteca.registro_membros if membro.numero_membro == membro_numero), None)
            if livro and membro:
                biblioteca.emprestar_livro(livro, membro)

        elif escolha == '4':
            titulo = input("Digite o título do livro a ser devolvido: ")
            membro_numero = input("Digite o número de membro: ")
            livro = biblioteca.pesquisar_livro_por_titulo(titulo)
            membro = next((membro for membro in biblioteca.registro_membros if membro.numero_membro == membro_numero), None)
            if livro and membro:
                biblioteca.devolver_livro(livro, membro)

        elif escolha == '5':
            titulo = input("Digite o título do livro a ser pesquisado: ")
            livro = biblioteca.pesquisar_livro_por_titulo(titulo)
            if livro:
                print(f"O livro '{livro.titulo}' está disponível.")
        
        elif escolha == '6':
            autor = input("Digite o autor do livro a ser pesquisado: ")
            livro = biblioteca.pesquisar_livro_por_autor(autor)
            if livro:
                print(f"O livro '{livro.titulo}' do autor '{livro.autor}' está disponível.")
        
        elif escolha == '7':
            id = input("Digite o ID do livro a ser pesquisado: ")
            livro = biblioteca.pesquisar_livro_por_id(id)
            if livro:
                print(f"O livro '{livro.titulo}' com ID '{livro.id}' está disponível.")

        elif escolha == '8':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()