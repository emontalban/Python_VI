class Usuario:
    def __init__(self, name, password ):
        self.name = name         
        self.password = password      


  
    def crea_usuario(self):
        return f"Mi nombre es: {self.name} y la contraseña: {self.password}"


user = Usuario("Keira", "Pass")


print(user.crea_usuario())


