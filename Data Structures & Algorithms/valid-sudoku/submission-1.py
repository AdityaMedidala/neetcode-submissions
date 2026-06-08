class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            count_row=[]
            for j in i:
                if j!="." and j in count_row:
                    return False
                else:
                    count_row.append(j)
        for col in range(9):
            count_column=[]
            for row in range(9):
                value=board[row][col]
                if value!="." and value in count_column:
                    return False
                count_column.append(value)
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                matrix=[]
                for k in range(3):
                    for m in range(3):
                        value=board[i+k][j+m]
                        if value!= '.' and value in matrix:
                            return False
                        matrix.append(value)
        return True





        