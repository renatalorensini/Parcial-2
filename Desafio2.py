def eh_par(numero):
    """Função que retorna True se o número for par, False se for ímpar"""
    return numero % 2 == 0

def main():
    print("=== Verificador de Números Pares e Ímpares ===")
    numeros = input("Digite números separados por espaço: ").split()
    
    for num_str in numeros:
        # Tenta converter para inteiro, se não der, avisa o usuário
        try:
            numero = int(num_str)
            if eh_par(numero):
                print(f"O número {numero} é par ✅")
            else:
                print(f"O número {numero} é ímpar ❌")
        except ValueError:
            print(f"'{num_str}' não é um número válido! ⚠️")
    
    print("=== Fim da verificação ===")

if __name__ == "__main__":
    main()
