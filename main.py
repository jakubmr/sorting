from IS import insertionSort as iSort
from SS import selectionSort as sSort
from HS import heapSort as hSort
from statistics import mean as mean

def main():
    for i in range(1000, 8500, 500):
        print(f"{i} elementów: ", hSort(f'random {i}.txt')[0])
    # print(iSort('random 8000.txt'))
    # print(sSort('random 8000.txt'))
    # print(hSort('random 8000.txt'))

if __name__ == "__main__":
    main()
