#para dar a mensagem caso o usuário queira criar uma licença com um código que já existe
class LicenseCodeAlreadyExistsException(Exception):
    def __init__(self, message="Código da licença já existe"):
        self.message = message
        super().__init__(self.message)
