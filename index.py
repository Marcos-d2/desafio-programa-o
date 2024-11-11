import json

# Questão 1: Cálculo da variável SOMA
def questao1():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K += 1
        SOMA += K

    print("Questão 1 - Valor de SOMA:", SOMA)

# Questão 2: Verificar se um número pertence à sequência de Fibonacci
def questao2():
    def is_fibonacci(number):
        a, b = 0, 1
        while b < number:
            a, b = b, a + b
        return b == number or number == 0

    number = int(input("Questão 2 - Informe um número para verificar na sequência de Fibonacci: "))
    if is_fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")

# Questão 3: Análise de faturamento diário a partir de JSON
def questao3():
    try:
        with open('faturamento.json', 'r') as file:
            data = json.load(file)

        faturamento_diario = [dia["valor"] for dia in data if dia["valor"] > 0]

        menor_faturamento = min(faturamento_diario)
        maior_faturamento = max(faturamento_diario)
        media_mensal = sum(faturamento_diario) / len(faturamento_diario)
        dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

        print("Questão 3 - Menor faturamento:", menor_faturamento)
        print("Questão 3 - Maior faturamento:", maior_faturamento)
        print("Questão 3 - Dias acima da média:", dias_acima_da_media)
    except FileNotFoundError:
        print("Arquivo 'faturamento.json' não encontrado. Coloque o arquivo na mesma pasta do script.")

# Questão 4: Cálculo de percentual de faturamento por estado
def questao4():
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    total = sum(faturamento_estados.values())

    print("Questão 4 - Percentual de representação por estado:")
    for estado, valor in faturamento_estados.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}%")

# Questão 5: Inversão de uma string sem usar funções prontas
def questao5():
    def reverse_string(s):
        reversed_s = ""
        for char in s:
            reversed_s = char + reversed_s
        return reversed_s

    string = input("Questão 5 - Digite uma string para inverter: ")
    print("String invertida:", reverse_string(string))

# Função principal para executar todas as questões
def main():
    print("\nExecutando todas as questões:\n")
    questao1()
    questao2()
    questao3()
    questao4()
    questao5()

# Executa o código
if __name__ == "__main__":
    main()
