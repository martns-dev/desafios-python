```python
# DESAFIO 1 - CALCULADORA DE TROCO

valor_compra = float(input("Digite o valor da compra: R$ "))
valor_pago = float(input("Digite o valor pago: R$ "))

troco = valor_pago - valor_compra

print(f"Troco: R$ {troco:.2f}")


# DESAFIO 2 - MÉDIA DE NOTAS

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"Média: {media:.2f}")


# DESAFIO 3 - CONVERSOR DE TEMPO

segundos = int(input("Digite o tempo em segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(
    f"{horas} hora(s), "
    f"{minutos} minuto(s) e "
    f"{segundos_restantes} segundo(s)"
)


# DESAFIO 4 - CALCULADORA DE DESCONTO

preco = float(input("Digite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

desconto = preco * (percentual_desconto / 100)
preco_final = preco - desconto

print(f"Preço final: R$ {preco_final:.2f}")


# DESAFIO 5 - PAR OU ÍMPAR

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


# DESAFIO 6 - INVERSOR DE NOME

nome = input("Digite seu nome: ")

nome_invertido = nome[::-1]

print(f"Nome invertido: {nome_invertido}")
```
