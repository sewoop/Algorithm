import re

def solution(dartResult):
    p = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    scores = p.findall(dartResult)

    answer = []
    bonus_ = ['S','D','T']
    
    for idx, score in enumerate(scores):
        point, bonus, option = score[0], score[1], score[2]

        if bonus in bonus_:
            bonus = bonus_.index(bonus)+1
        
        if option == '*':
            if idx == 0:
                answer.append(int(point)**bonus*2)
            else:
                answer[-1] *= 2
                answer.append(int(point)**bonus*2)
        elif option == '#':
            answer.append(int(point)**bonus*-1)
        else: 
            answer.append(int(point)**bonus)

    return sum(answer)

if __name__ == "__main__":
    # dartResult = '1S2D*3T'
    dartResult = '1D2S#10S'
    # dartResult = '1D2S0T'
    # dartResult = '1S*2T*3S'
    # dartResult = '1D#2S*3S'
    # dartResult = '1T2D3D#'
    # dartResult = '1D2S3T*'

    print(solution(dartResult))