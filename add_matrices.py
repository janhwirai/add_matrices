A= [[1,2,3],  
    [4,5,6],  
    [7,8,9]]  
  
B= [[1,2,3],  
    [4,5,6],  
    [7,8,9]]  


result = [[0,0,0],

         [0,0,0],

         [0,0,0]]

# iterate through rows

for x in range(len(A)):

   # iterate through columns

   for y in range(len(A[0])):

       result[x][y] = A[x][y] + B[x][y]

for q in result:

   print(q)