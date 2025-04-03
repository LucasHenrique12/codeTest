

class Usuario:
    
    def __init__(self, nome: str, email: str, idade: int):
        
        if not nome or not isinstance(nome, str):
            raise ValueError("Nome inválido")
        if not email or not isinstance(email, str) or "@" not in email:
            raise ValueError("E-mail inválido")
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("Idade deve ser um número positivo")
            
        self.nome = nome
        self.email = email
        self.idade = idade
    
    def __str__(self):
        return f"Nome: {self.nome}\nE-mail: {self.email}\nIdade: {self.idade}"

class SistemaCadastro:
   
    def __init__(self):
        # Criar lista vazia
        self.usuarios = []
        
    #Cadastro de usuarios
    def cadastrar_usuario(self):
       
        print("\n--- Cadastro de Usuário ---")
        
        try:
            nome = input("Digite o nome: ").strip()
            email = input("Digite o e-mail: ").strip()
            idade = int(input("Digite a idade: ").strip())
            
            # Verificar se e-mail já existe
            if any(u.email == email for u in self.usuarios):
                print("Erro: Este e-mail já está cadastrado!")
                return
                
            novo_usuario = Usuario(nome, email, idade)
            self.usuarios.append(novo_usuario)
            print("Usuário cadastrado com sucesso!")
            
        except ValueError as e:
            print(f"Erro no cadastro: {str(e)}")
    
    #listar todos  os usuarios cadastrados
    def listar_usuarios(self):
        
        print("\n--- Lista de Usuários Cadastrados ---")
        
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
            
        for i, usuario in enumerate(self.usuarios, 1):
            print(f"\nUsuário {i}:")
            print(usuario)
            
    #Buscar usuario por nome
    def buscar_usuario(self):
       
        print("\n--- Buscar Usuário ---")
        
        if not self.usuarios:
            print("Nenhum usuário cadastrado para buscar.")
            return
            
        termo = input("Digite o nome (ou parte) para buscar: ").strip().lower()
        
        if not termo:
            print("Termo de busca não pode ser vazio!")
            return
            
        encontrados = [u for u in self.usuarios if termo in u.nome.lower()]
        
        if not encontrados:
            print("Nenhum usuário encontrado.")
        else:
            print(f"\n{len(encontrados)} usuário(s) encontrado(s):")
            for i, usuario in enumerate(encontrados, 1):
                print(f"\nUsuário {i}:")
                print(usuario)
    
    #Menu principal
    def menu_principal(self):
        
        while True:
            print("1. Cadastrar novo usuário")
            print("2. Listar todos os usuários")
            print("3. Buscar usuário por nome")
            print("4. Sair do sistema")
            
            opcao = input("Escolha uma opção (1-4): ").strip()
            
            if opcao == "1":
                self.cadastrar_usuario()
            elif opcao == "2":
                self.listar_usuarios()
            elif opcao == "3":
                self.buscar_usuario()
            elif opcao == "4":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Escolha de 1 a 4.")


if __name__ == "__main__":
    
    sistema = SistemaCadastro()
    sistema.menu_principal()