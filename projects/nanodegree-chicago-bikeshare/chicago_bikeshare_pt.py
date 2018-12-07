# coding: utf-8

# Imports modules
import csv
import math
import matplotlib.pyplot as plt

# Defining script functions
def load_csv(file_path, access_mode = "r"):
    """
    Loads a CSV file.
    Arguments:
      file_path: Path to CSV file.
      access_mode: File access mode. Default Read Only.
    Return:
      A list containing all rows from the CSV file.

    """
    with open(file_path, access_mode) as f:
        return list(csv.reader(f))


def print_list(data):
    """
    Prints all elements of a list separated by line.
    Arguments:
      data: List.
    Return:
      No Return.

    """
    for i, line in enumerate(data):
        print("Linha {}: {}".format(i, line))


def mean_list(data):
    """
    Calculates the average of a numeric list.
    Arguments:
      data: List.
    Return:
      Average in float.

    """
    return sum(data) / len(data)


# withdrawn: https://www.quora.com/How-do-I-find-the-median-value-in-Python
def median_list(data):
    """
    Calculates the median of a numerical list.
    Arguments:
      data: List.
    Return:
      Median in float.

    """
    length = len(data)
    if (length % 2 == 0):
        median = (data[(length)//2] + data[(length)//2-1]) / 2
    else:
        median = data[(length-1)//2]
    return median


# TASK 3
def column_to_list(data, index):
    """
    Take a specific column from the list.
    Arguments:
      data: List.
      index: Index of the column you want to redeem.
    Return:
      List containing all rows of the rescued column.

    """
    return [line[index] for line in data]


# TASK 5
def count_gender(data):
    """
    Count the number of users by gender.
    Arguments:
      data: List.
    Return:
      A list containing the number of male and female users.

    """
    data = column_to_list(data, -2)
    male = data.count("Male")
    female = data.count("Female")
    return [male, female]


# TASK 6
def most_popular_gender(data):
    """
    Find the most popular genre.
    Arguments:
      data: List.
    Return:
      String with the most popular genre name.

    """
    answer = ""
    genders = count_gender(data)
    if genders[0] == genders[1]:
        answer = "Equal"
    elif genders[0] > genders[1]:
        answer = "Male"
    else:
        answer = "Female"
    return answer


# TASK 12
def count_items(column_list):
    """
    Counts the occurrence of a specific column.
    Arguments:
      column_list: List.
    Return:
      A tuple containing the type and their respective occurrences.

    """
    item_types = list(set(column_list))
    count_items = [column_list.count(t) for t in item_types]
    return item_types, count_items


# Carrying out the tasks

# Vamos ler os dados como uma lista
print("\n\nLendo o documento...")
data_list = load_csv("chicago.csv")
print("Ok!\n\n")

# Vamos verificar quantas linhas nós temos
print("Número de linhas: {}".format(len(data_list)))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")


# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
print_list(data_list[:20])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]
# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")


# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
print_list(column_to_list(data_list[:20], -2))

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")


# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
# funcao consta no inicio do arquivo
# >> Line 67
# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")

# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem


# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = column_to_list(data_list, -2).count("Male")
female = column_to_list(data_list, -2).count("Female")

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")

# Por que nós não criamos uma função para isso?


# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
# >> Line 81

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")

# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?


# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
# >> Line 97

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")


# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
types, quantity = count_items(column_to_list(data_list, -3))
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de Usuários')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo')
plt.show(block=True)

input("Aperte Enter para continuar...")


# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque além dos usuários masculinos e femininos, há usuários que não especificaram seu sexo.\nÉ possível constatar isso a partir dos dados abaixo, bem como na TAREFA 12:"
print("resposta:", answer)
users_types, user_types_counts = count_items(column_to_list(data_list, -2))
print("Gêneros:", users_types, "Quantidade:", user_types_counts)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")

# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.


# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = sorted([int(val) for val in column_to_list(data_list, 2)])
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
mean_trip = math.ceil(mean_list(trip_duration_list))
median_trip = median_list(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:

input("Aperte Enter para continuar...")


# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"
# >> Line 118

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
