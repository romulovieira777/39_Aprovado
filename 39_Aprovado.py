nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")

elif media < 3:
    print("Reprovado")

elif (media == 3) or (media < 7):
    print("Prova Final")

else:
    print("erro")  

