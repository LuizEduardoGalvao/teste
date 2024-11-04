"""indice = 13;
soma = 0;
k = 0;

while(k < indice):
   k = k+1
   soma = soma + k

print(soma)#

-----------------------------------------------------------------
#2
def fibo(n):

    fibo_sequencia = [0, 1]
    while fibo_sequencia[-1] < n:
        proxima_fibo = fibo_sequencia[-1] + fibo_sequencia[-2]
        fibo_sequencia.append(proxima_fibo)
    return fibo_sequencia

num = int(input("Informe um número: "))


sequencia = fibo(num)

if num in sequencia:
    print(f"O número {num} pertence à sequência de Fibonacci: {sequencia}")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci. A sequência até {sequencia} é: {sequencia}")





-----------------------------------------------------------------
3
faturamento_diario = [100, 200, 150, 300, 250, 400]

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_media = sum(1 for faturamento in faturamento_diario if faturamento > media_mensal)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

-----------------------------------------------------------------
4
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento.values())

print("Percentual de representação por estado:")
for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")


-----------------------------------------------------------------
5
string = "Isso e um teste"

def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

resultado = inverter_string(string)

print("String original:", string)
print("String invertida:", resultado)