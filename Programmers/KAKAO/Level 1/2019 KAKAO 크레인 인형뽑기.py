# Refactor 
def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for b in board :
            if b[move-1]==0:
                continue
            else :
                if len(stack)==0 or stack[-1]!=b[move-1]:
                    stack.append(b[move-1])
                elif stack[-1]==b[move-1]:
                    stack.pop()
                    answer+=2
                b[move-1]=0
                break
    return answer

# def solution(board, moves):
#     answer = 0
#     stack = []
#     for move in moves:
#         for b in board :
#             if b[move-1]==0:
#                 continue
#             else :
#                 if len(stack)==0:
#                     stack.append(b[move-1])
#                     b[move-1]=0
#                     break

#                 if stack[-1]==b[move-1]:
#                     stack.pop()
#                     b[move-1]=0
#                     answer+=2
#                 else :
#                     stack.append(b[move-1])
#                     b[move-1]=0
#                 break
#     return answer

if __name__ == "__main__":
    '''
        [0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]
    '''
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]

    # board = [[0,0,1,0,0],[0,0,1,0,0],[0,2,1,0,0],[0,2,1,0,0],[0,2,1,0,0]]
    # moves = [1,2,3,3,2,3,1]

    print(solution(board, moves))