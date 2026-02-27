"""
Beecrowd 1004 - Produto Simples

Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores
e atribua esta operação à variável PROD. A seguir mostre a variável PROD com
mensagem correspondente.

Entrada: O arquivo de entrada contém 2 valores inteiros.

Saída: Imprima a mensagem "PROD" conforme exemplo abaixo, com um espaço em branco
antes e depois da igualdade. Não esqueça de imprimir o fim de linha após o produto,
caso contrário seu programa apresentará a mensagem: "Presentation Error".
"""

# Link do problema: https://judge.beecrowd.com/pt/problems/view/1004

# Escreva sua solução abaixo
# Lê o primeiro valor inteiro
valor1 = int(input())

# Lê o segundo valor inteiro
valor2 = int(input())

# Calcula o produto
PROD = valor1 * valor2

# Imprime o resultado formatado
print(f"PROD = {PROD}")
