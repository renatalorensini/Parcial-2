# Função para calcular a área do triângulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Cabeçalho estilizado
print("="*40)
print("  Cálculo da Área do Triângulo  ".center(40))
print("="*40)

# Solicita os dados de entrada com mensagens mais detalhadas
base = float(input("Digite o valor da base do triângulo (em unidades): "))
altura = float(input("Digite o valor da altura do triângulo (em unidades): "))

# Calculando a área
area = calcular_area_triangulo(base, altura)

# Exibindo o resultado de forma mais elaborada
print("="*40)
print(f"A área do triângulo com base {base} e altura {altura} é: {area:.2f} unidades quadradas.")
print("="*40)

# Mensagem final
print("Obrigado por testar o meu calculador de áreas :)")
print("="*40)
