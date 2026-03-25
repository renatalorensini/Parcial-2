# Função para calcular o valor dos juros simples
def calcular_juros_simples(capital, taxa, tempo):
    juros = (capital * taxa * tempo) / 100
    return juros

# Cabeçalho estilizado com emojis
print("="*40)
print(" Cálculo de Juros Simples 💰".center(40))
print("="*40)

# Solicitando os valores de entrada com emojis e explicações
capital = float(input(" Digite o valor do capital (C) em R$: "))
taxa = float(input(" Digite a taxa de juros (I) em %: "))
unidade = input(" Escolha a unidade de tempo (segundos, horas, dias ou meses): ").strip().lower()

# Verifica a unidade de tempo e solicita o valor correspondente
if unidade == "segundos":
    tempo = float(input(" Digite o tempo (T) em segundos: "))
elif unidade == "horas":
    tempo = float(input(" Digite o tempo (T) em horas: "))
elif unidade == "dias":
    tempo = float(input(" Digite o tempo (T) em dias: "))
elif unidade == "meses":
    tempo = float(input(" Digite o tempo (T) em meses: "))
else:
    print(" Unidade de tempo inválida. Por favor, escolha estre 'segundos', 'horas', 'dias' ou 'meses'.")
    exit()

# Calculando os juros
juros = calcular_juros_simples(capital, taxa, tempo)

# Exibindo o resultado de forma mais elaborada
print("="*40)
print(f" O valor total dos juros simples é de: R$ {juros:.2f}")
print("="*40)
