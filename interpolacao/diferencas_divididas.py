def newton_polynomial(x, y):
    n = len(x)
    
    divided_differences = [y.copy()]
    for i in range(1, n):
        current_differences = []
        for j in range(n - i):
            diff = (divided_differences[i - 1][j + 1] - divided_differences[i - 1][j]) / (x[j + i] - x[j])
            current_differences.append(diff)
        divided_differences.append(current_differences)

    def newton_polynomial_function(x_val):
        result = divided_differences[0][0]
        product_term = 1
        for i in range(1, n):
            product_term *= (x_val - x[i - 1])
            result += divided_differences[i][0] * product_term
        return result

    return newton_polynomial_function

x = [0, 1, 2, 3, 4]
y = [1, 2, 3, 4, 5]

polynomial_function = newton_polynomial(x, y)

x_test = 7
print(f"P({x_test}) = {polynomial_function(x_test)}")
