def createMatrix(n):
    matrix = [[0 for x in range(n)] for x in range(n)]
    return matrix

def oddMagicSquare():
    
    order = int(input("Enter the order of Magic Square matrix: "))
    
    if(order<0):
        print("Sorry! Wrong input provided. Try again")
    elif(order==1):
        print("Magic Number for this matrix is 1.")
    elif(order%3 !=0):
        print("Please enter odd number - to get ODD Order Magic Square")
    else:
        matrix = createMatrix(order)
        n = order
        row = n//2
        col = n-1
        number = 1
        while(number <= n**2):
            if(row == -1 and col == n):
                row = 0
                col = n-2
            else:
                if(row < 0):
                    row = n-1
                
                if(col == n):
                    col = 0
            print(matrix[row][col], end= " ")        
            if(matrix[row][col] != 0):
                row = row+1
                col = col-2
                continue
            else:
                matrix[row][col] = number
                number += 1
            row = row-1
            col = col+1
        
        for row in range(n):
            for col in range(n):
                print(matrix[row][col], end = " ")
            print()
        
magicSquare()