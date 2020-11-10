import numpy as np

def ahp():
    n = None

    while 1:
        try:
            print('Enter a number of categories: ')
            n = int(input())
        except ValueError:  # finding non-int values
            print('Incorrect input! Try again')
            continue
        break

    M = np.eye(n)     # creating (n, n) matrix filled with ones on main diagonal

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if i < j:
                while 1:
                    try:
                        wij = float(input(f'\nHow many times weight_{i}  more important than weight_{j}?\n'))
                    except ValueError:  # finding non-float values
                        print('Incorrect input! Try again')
                        continue
                    break

                M[i, j] = wij
                M[j, i] = 1 / wij

    rowsum_M = M.sum(axis=1)            # sum for each row
    sum = M.sum()                       # full sum
    weights = rowsum_M / sum            # normalization
    weights = np.around(weights, decimals=2)
    print('AHP weights: ', weights)



def main():
    ahp()  

if __name__ == '__main__':
    main()