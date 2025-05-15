top_level_domains = [
    ".com", ".org", ".net", ".gov", ".edu", ".mil", ".int",
    ".co.uk", ".co.in", ".co.jp", ".co.br", ".co.au",
    ".info", ".biz", ".me", ".io", ".ai"
]

def validate_name(name):
    if not isinstance(name, str) or len(name) <= 2:
        return False
    if not name.replace(" ", "").isalpha():
        return False
    return True


def validate_email(email):
    if not isinstance(email, str):
        return False
    if "@" not in email:
        return False
    try:
        username, domain = email.split("@", 1)
    except ValueError:
        return False
    if len(username) <= 1:
        return False
    if "." not in domain:
        return False
    if not any(domain.endswith(tld) for tld in top_level_domains):
        return False
    return True


def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True


def validate_user(name, email, password):
    if not validate_name(name):
        raise ValueError("Nome inválido: deve conter apenas letras, ter mais de 2 caracteres e ser do tipo string.")
    if not validate_email(email):
        raise ValueError("Email inválido: deve conter '@', domínio permitido e nome de usuário válido.")
    if not validate_password(password):
        raise ValueError("Senha inválida: deve ter mais de 8 caracteres, incluir letra maiúscula e número.")
    return True


def register_user(name, email, password):
    try:
        validate_user(name, email, password)
    except ValueError:
        return False
    return {
        "name": name,
        "email": email,
        "password": password
    }
# Testes
# Teste

print(register_user("Maycon", "emailcerto@gmail.com", "Senha123"))
print(register_user("Maycon", "emailerrado@gmail", "Senha123")) # False
