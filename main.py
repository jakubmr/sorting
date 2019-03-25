from ins import insertionSort as iSort
from ss import selectionSort as sSort
from hs import heapSort as hSort
from qs import mainQuickSort as qSort
from statistics import mean as mean
import time

list_type = ['aShape', 'constant', 'ordinary', 'random', 'reverse', 'vShape']
start, end, step = 1000, 4500, 500

def main():
    print("------INSERTION SORT------")
    for type in list_type:
        print(f'Lista {type}')
        for i in range(start, end, step):
            for j in range(5):
                t = []
                t.append(iSort(f'{type} {i}.txt')[0])
            print(f"{i} elementów: ", mean(t))

    print("------SELECTION SORT------")
    for type in list_type:
        for i in range(start, end, step):
            for j in range(5):
                t = []
                t.append(sSort(f'{type} {i}.txt')[0])
            print(f"{i} elementów: ", mean(t))

    print("------HEAP SORT------")
    for type in list_type:
        print(f'Lista {type}')
        for i in range(start, end, step):
            for j in range(5):
                t = []
                t.append(hSort(f'{type} {i}.txt')[0])
            print(f"{i} elementów: ", mean(t))
            
    # print("------QUICK SORT------")
    # for i in range(1000, 16000, 1000):
    #     for j in range(5):
    #         t = []
    #         t.append(qSort(f'random {i}.txt')[0])
    #     print(f"{i} elementów: ", mean(t))

    # print(iSort('random 4000.txt'))
    # print(sSort('random 4000.txt'))
    # print(hSort('random 4000.txt'))
    # print(qSort('aShape 4000.txt'))

if __name__ == "__main__":
    main()
