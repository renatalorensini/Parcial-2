# calculadora_simples.py

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

def main():
    print("=== Calculadora Simples ===")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    escolha = input("Escolha a operação (1/2/3/4): ")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: digite apenas números!")
        return

    if escolha == "1":
        resultado = soma(num1, num2)
    elif escolha == "2":
        resultado = subtracao(num1, num2)
    elif escolha == "3":
        resultado = multiplicacao(num1, num2)
    elif escolha == "4":
        resultado = divisao(num1, num2)
    else:
        print("Operação inválida!")
        return

    print(f"O resultado é: {resultado}")

if __name__ == "__main__":
    main()
