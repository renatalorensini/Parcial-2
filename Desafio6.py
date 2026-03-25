SEGUNDOS PARA HMS:
def converter_segundos_para_hms(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

# Exemplo de uso
segundos = int(input("Digite apenas o número de segundos: "))
horas, minutos, segundos_restantes = converter_segundos_para_hms(segundos)
print(f"{horas} hora(s), {minutos} minuto(s), {segundos_restantes} segundo(s)")

HMS PARA SEGUNDOS:
def converter_hms_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

# Exemplo de uso
horas = int(input("Digite somente o número de horas: "))
minutos = int(input("Digite somente o número de minutos: "))
segundos = int(input("Digite somente o número de segundos: "))

total_segundos = converter_hms_para_segundos(horas, minutos, segundos)
print(f"O número total de segundos é: {total_segundos} segundos")
