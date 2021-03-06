#write a program in python to implement Coin Change problem as below
#Given N, if we want to make chage N cents and have have infinite supply of each of S = {S1, S2,… , Sm} valued coins,
#How many ways can we make the change? The order of coins doesn’t matter.
# For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
# For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

def calculate(S, m, n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n >=1:
        return 0
    return calculate(S, m - 1, n) + calculate(S, m, n - S[m-1])

arr = [1,2,5]
m = len(arr)
print(calculate(arr, len(arr), 8))
