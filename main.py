# given 2d matrix write function that returns minimum cost path of reaching bottom rightmost cell when starting at top leftmost cell.  you can only move right and down.  all cells are non-negative. 

matrix1 = [[1,2,3], [4,8,2], [1,5,3]] # => 11

# RECURSIVE APPROACH (O(2^n))
def rec(matrix, row, col):
  if row==len(matrix) or col==len(matrix[0]): # if we go off either edge
    return float('inf') # highest possible number
  if row==len(matrix)-1 and col==len(matrix[0])-1: #
    return matrix[row][col] # 
  
  right = rec(matrix, row, col+1)
  down = rec(matrix, row+1, col)
  # diagonal = rec(matrix, row+1, col+1) # if diagonal allowed
  
  return matrix[row][col] + min(down, right)  
  # return matrix[row][col] + min(down, right, diagonal) # if diagonal allowed

# MEMOIZED APPROACH (O(n))
def memo_rec(matrix, row, col, memo):
  if row==len(matrix) or col==len(matrix[0]): # if we go off either edge
    return float('inf') # highest possible number

  key = (row, col)
  if key in memo:
    return memo[key]

  if row==len(matrix)-1 and col==len(matrix[0])-1: #
    return matrix[row][col] # 
  
  right = memo_rec(matrix, row, col+1, memo)
  down = memo_rec(matrix, row+1, col, memo)
  # diagonal = memo_rec(matrix, row+1, col+1, memo) # if diagonal allowed
  
  memo[key] = matrix[row][col] + min(down, right)  
  # memo[key] = matrix[row][col] + min(down, right, diagonal)  
  return memo[key]

print(rec(matrix1,0,0)) 
print(memo_rec(matrix1,0,0,{})) 
