def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for x in range(n)] for y in range(n)]
    
    for length in range(2, n + 1):  # length of the chain
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
    
    return m[0][n - 1]

# Example usage
p = [10, 30, 5, 60]
min_cost = matrix_chain_order(p)
print("Minimum number of multiplications is:", min_cost)
