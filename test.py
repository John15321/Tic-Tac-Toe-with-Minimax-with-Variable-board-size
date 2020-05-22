# col = 5
# row = 5

# T = [[0 for i in range(col)] for j in range(row)]

# x = 1
# y = 0

# z = (4, 6)


# def a():
#     if int(input()) == 2:
#         return
#     else:
#         print("sraka")
# T[x][y] = 1

# c = 0
# for x in range(row):
#     for y in range(col):
#         T[x][y] = c
#         c+=1

# for i in range(len(T)):
#         print(T[i])

# a()
# print("A finished")

board_size = 4

# fields = [([0] * board_size) for j in range(0,board_size)]
fields = [0] * (board_size**2)
fields[0] = 1
print(fields)
# [print('s') for i in range(board_size)] for j in range(board_size)

print(len(fields))