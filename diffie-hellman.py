import random

# Função para obter um número primo grande
def numero_primo():
    while True:
        # Gerando um número aleatório maior que 10.000
        num = random.randint(10000, 100000)
        
        # Verificando se o número é primo
        if eh_primo(num):
            return num

# Função para verificar se um número é primo
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Função para encontrar uma raiz primitiva módulo p
def raiz_primitiva(p):
    for g in range(2, p):
        if all(pow(g, (p-1)//q, p) != 1 for q in range(2, p-1)):
            return g
    return None


def diffie_hellman(p):
    # Encontrar a raiz primitiva módulo p
    g = raiz_primitiva(p)
    
    #Se nenhuma raiz primitiva foi encontrada para o primo
    if g is None:
        raise ValueError("Nenhuma raiz primitiva encontrada para", p)

    # Chaves privadas para Alice e Bob
    a = random.randint(1, p-1)
    b = random.randint(1, p-1)

    # Chaves públicas para Alice e Bob
    A = pow(g, a, p)
    B = pow(g, b, p)
    
    # Calcular a chave secreta compartilhada
    s_A = pow(B, a, p)
    s_B = pow(A, b, p)
    
    # Verifica se as chaves secretas compartilhadas são iguais
    if s_A == s_B:
        print("Chave secreta compartilhada (s):", s_A)
    else:
        print("Erro na troca de chaves")
    
    # Print the results
    print("Número primo (p):", p)
    print("Raiz primitiva (g):", g)
    print("Chave secreta da Alice (a):", a)
    print("Chave secreta do Bob (b):", b)
    print("Chave pública da Alice (A):", A)
    print("Chave pública do Bob (B):", B)
    
def main():
    # Gerando um número primo
    p = numero_primo() 
    
    # Algoritmo
    diffie_hellman(p)

if __name__ == "__main__":
    main()
    

