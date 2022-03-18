nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# i - string, k - column, n - number in mini-list
new_list = [nice_list[i][k][n] for i in range(2) for k in range(3) for n in range(3)]

print(new_list)
