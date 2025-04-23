# # Pattern Questions

# # Pattern1: Print a square.
# string = ""
# n = 5
# for i in range(n):
#     for j in range(n):
#         string += ' * '
#     string += '\n'
# print(string)

# # Pattern2: Print a left-Triangle
# string = ""
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         string += ' * '
#     string += '\n'
# print(string)

# # Pattern3: Print a left-Triangle with numbers.
# string = ""
# n = 6
# for i in range(1, n):
#     for j in range(1, i+1):
#         string += f" { j } "
#     string += '\n'
# print(string)

# # Pattern4: Print a left-Triangle with same number in each row.
# string = ""
# n = 6
# for i in range(1, n):
#     for j in range(1, i+1):
#         string += f" { i } "
#     string += '\n'
# print(string)

# # Pattern5: Print a reverse left-Triangle.
# string = ""
# n = 6
# for i in range(1, n):
#     for j in range(i, n):
#         string += ' * '
#     string += '\n'
# print(string)

# # Pattern6: Print a reverse left-Triangle with numbers.
# string = ""
# n = 6
# for i in range(1, n):
#     for j in range(1, n+1-i):
#         string += f' { j } '
#     string += '\n'
# print(string)

# #pattern7: Print a triangle with stars.
# string = ""
# n = 5
# for i in range(0, n):
#     for j in range(0, n-i-1): #Adds space to string.
#         string += " "
#     for j in range (0, 2*i+1): #Adds star to string.
#         string += "*"
#     for j in range(0, n-i-1): #Adds space to string.
#         string += " "
#     string += '\n'
# print(string)

# #pattern8: Print a reverse triangle.
# string = ""
# n = 5
# for i in range(0, n):
#     for j in range(0, i): #Adds space to string.
#         string += " "
#     for j in range (0, 2*n -(2*i +1)): #Adds star to string.
#         string += "*"
#     for j in range(0, i): #Adds space to string.
#         string += " "
#     string += '\n'
# print(string)

# #pattern9: Print a normal and reverse triangle joined with each other.
# string = ""
# n = 5
# for i in range(0, n):
#     for j in range(0, n-i-1): #Adds space to string.
#         string += " "
#     for j in range (0, 2*i+1): #Adds star to string.
#         string += "*"
#     for j in range(0, n-i-1): #Adds space to string.
#         string += " "
#     string += '\n'
# for i in range (0, n):
#     for j in range(0, i): #Adds space to string.
#         string += " "
#     for j in range (0, 2*n -(2*i +1)): #Adds star to string.
#         string += "*"
#     for j in range(0, i): #Adds space to string.
#         string += " "
#     string += '\n'
# print(string)

# #pattern10: print a triangle in right direction
# string = ""
# n = 5
# N = 4
# for i in range(0, n):
#     for j in range(0, i+1):
#         string += ' * '
#     for j in range(0, n-(i+1)):
#         string += ' '
#     string += '\n'
# for i in range(0, N):
#     for j in range(0, N-i):
#         string += ' * '
#     for j in range(0, j+1):
#         string += ' '
#     string += '\n'
# print(string)

# # Pattern11: Print a left-Triangle with numbers 0 and 1.
# string = ""
# n = 6
# start = 1
# for i in range(1, n):
#     if( i % 2 == 0):
#         start = 1
#     else:
#         start = 0
    
#     for j in range(1, i+1):
#         string += f" { start } "
#         start = 1 - start
#     string += '\n'
# print(string)

# # Pattern12: Print a left-Triangle with incremental numbers.
# string = ""
# n = 6
# start = 1
# for i in range(1, n):
#     for j in range(1, i+1):
#         string += f" { start } "
#         start += 1
#     string += '\n'
# print(string)


# Pattern13: Print a U shape pattern numbers.
string = ""
n = 5
for i in range(1, n):
    for j in range(1, i+1):
        string += f'{j}'
    for j in range(0, (n*2)-(2*i)):
        string += ' '
    for j in range(1, i+1):
        string += f'{j}'
    string += '\n'
print(string)