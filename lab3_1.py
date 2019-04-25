mass = [[0] * 100 for i in range(100)] #матрица смежностей 100x100
D=[i for i in range(100)] #массив, хранящий минимальный путь (100 элементов)
used = [i for i in range(100)] #массив, отвечающий за проход узла

def shortWay(start : int, end : int, N : int, M : int) -> int: #N и M - количество узлов и ребер
    #используем алгоритм Дейкстры
    for i in range(N): #заполняем массив, который отвечает за проход узла(если побывали в узле, то присваиваем 1, иначе 0)
        used[i] = 0
    for i in range(N):
        D[i] = mass[start][i]
    used[start] = 1
    for i in range(N-2):
        min_v = 1000000
        for j in range(N):
            if used[j]==0 and D[j]<min_v:
                min_v = D[j]
                W = j #W - номер узла с наименьшим значением пути
        used[W] = 1
        for i in range(N):
            if used[i] == 0:
                D[i] = (D[i] if (D[i] < (D[W] + mass[W][i])) else (D[W]+mass[W][i])) #тройной операнд, чтобы выбрать минимальный узел

    if start == end: #если начальный узел является конечным,
        D[end] = 0 #то путь равен 0
    return D[end]

def main():
    with open("graf.txt", "r") as file:
        N,M = file.readline().split()
        N,M = int(N), int(M)
        for i in range(N):
            for j in range(N): #присваиваем элементам матрицы максимальные значения
                mass[i][j]=100000
                mass[j][i]=100000
        for i in range(M): #заполняем матрицу значениями из файла
            a,b,c = file.readline().split()
            a,b,c = int(a), int(b), int(c)
            mass[a][b]=c
            mass[b][a]=c
    start, end = map(int, input("Введите начальную и конечную цель через пробел: ").split()) #пример: 3 4; 3 - начало пути, 4 - его конец
    print("Самый короткий путь: ", shortWay(start, end, N, M))

main()