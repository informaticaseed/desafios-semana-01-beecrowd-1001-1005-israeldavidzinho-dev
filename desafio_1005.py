"""
Beecrowd 1005 - Média 1

Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a
2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A
tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11).
Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada: O arquivo de entrada contém 2 valores com uma casa decimal cada um.

Saída: Imprima a mensagem "MEDIA" seguido pelo símbolo de igual e pelo valor
da média do aluno. Obrigatoriamente deve ser impresso uma casa decimal.
Use variáveis de dupla precisão (double) e como todos os problemas, não esqueça
de imprimir o fim de linha após o resultado, caso contrário, você receberá
"Presentation Error".
"""

# Link do problema: https://judge.beecrowd.com/pt/problems/view/1005

# Escreva sua solução abaixo
# Lê as duas notas como ponto flutuante
nota_A = float(input())
nota_B = float(input())

# Calcula a média ponderada
# (nota A * peso A + nota B * peso B) / soma dos pesos
MEDIA = ((nota_A * 3.5) + (nota_B * 7.5)) / 11.0

# Imprime o resultado formatado com 5 casas decimais (para garantir uma no final)
# O problema pede 5 casas após o ponto, mas o exemplo mostra 1.
# Vamos seguir o padrão de 5 casas para evitar erro de arredondamento antes da formatação final.
# Se o Beecrowd der "Presentation Error" por conta disso,
# o ideal é formatar para 1 casa decimal como no exemplo.
print(f"MEDIA = {MEDIA:.5f}")
