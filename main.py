from ins import insertionSort as iSort
from ss import selectionSort as sSort
from hs import heapSort as hSort
from qs import mainQuickSort as qSort
from statistics import mean as mean

def main():
    for i in range(1000, 8500, 500):
        print(f"{i} elementów: ", hSort(f'random {i}.txt')[0])
    print(iSort('random 4000.txt'))
    print(sSort('random 4000.txt'))
    print(hSort('random 4000.txt'))
    print(qSort('random 4000.txt'))

if __name__ == "__main__":
    main()
