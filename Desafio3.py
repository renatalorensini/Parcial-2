def listar_nomes():
    # Lista de 5 nomes :
    nomes = ["Renata", "Isane", "Lara", "Gabriel", "Margarida"]
    
    # Cabeçalho estilizado
    print("="*30)
    print("   Lista de Nomes:   ")
    print("="*30)
    
    # Iteração para imprimir cada nome
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}. {nome}")
    
    # Finalizando com um agradecimento estilizado
    print("="*30)
    print(" Esses foram os 5 nomes de pessoas que conheço! :) ")
    print("="*30)

# Chamando a função para exibir os nomes
listar_nomes()
