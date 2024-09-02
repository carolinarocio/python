#Python

#1)Função contador: Converte um número de horas em minutos e segundos. Por exemplo, 42 horas se tornam 2520 minutos e 0 segundos.
def contador(horas):
    segundos = horas * 3600
    minutos = 0
    while segundos >= 60:
        segundos -= 60
        minutos += 1
    return f'{minutos} minutos e {segundos} segundos'

print(contador(42))

#2)Calcula o montante total de um investimento após um período de tempo,

def montante(capital_inicial, juros_por_ano, periodo_em_ano):
    montante = capital_inicial * (1 + juros_por_ano) * periodo_em_ano
    return montante
print(montante(100,12,1))

#3)Converte um valor em reais para dólares usando uma taxa de câmbio fixa de 5.1 reais por dólar, e arredonda o resultado para duas casas decimais.

def cambio(real):
    dolar = real / 5.1
    return round(dolar,2)

print(cambio(1200))

#4)Função primos: Encontra e retorna todos os números primos em um intervalo específico, por exemplo, entre 2 e 100.

def primos(x, y):
    primos = []
    for numero in range(x, y + 1):
        if numero > 1: 
            for i in range(2, numero):
                if (numero % i) == 0: 
                    break
            else:
                primos.append(numero) 
    return primos

print(primos(2, 100))