# for i in range(3):
#    for j in range(3):
#        print('|', j+3*i, end=" ")
#    print('|')

#number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
#for row in number_board:
 #  print('| ' + ' | '.join(row) + ' |')
#print(number_board)


board = [[' ' for i in range(j*3, (j+1)*3)] for j in range(3)]
print(board)