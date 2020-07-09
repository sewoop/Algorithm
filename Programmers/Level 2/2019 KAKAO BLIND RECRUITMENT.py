def solution(record):
    answer = []
    user = {}
    
    for line in record :
        items = line.split(' ')
        if items[0] in ['Enter','Change'] :
            user[items[1]] = items[2]
    for line in record :
        items = line.split(' ')
        if items[0] == 'Enter' : 
            answer.append(user[items[1]]+'님이 들어왔습니다.')
        elif items[0] == 'Leave' :
            answer.append(user[items[1]]+'님이 나갔습니다.')
    return answer