# Matrices in Python, in this code i create a matrix 3x3 in Python
matrixNumber = [[0, 0, 0], 
                [0, 0, 0],
                [0, 0, 0]]
for r in range(0,3):
  for c in range(0,3):
        matrixNumber[r][c] = int(input(f'Write one value [{r},{c}]:'))
        print('-=' * 30)
for r in range(0,3):
  for c in range(0,3):
    print(f'[{matrixNumber[r][c]:^5}]',end='')
  print()

print(matrixNumber)

# ================================================================

