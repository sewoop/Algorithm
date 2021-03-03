def diff_check(begin, word):
    diff = 0
    for b, w in zip(begin, word):
        if b != w:
            diff += 1
    return diff

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    while words:
        word = words.pop(0)
        if diff_check(begin, word) == 1:
            answer += 1
            if diff_check(begin, target) == 1:
                return answer
            # print(f'{begin} -> {word} : {words}')
            begin = word
        else:
            words.append(word)
        
    return 0
        

begin = "hit"
target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ["hot", "dot", "dog", "lot", "log"]
# words = ["hot", "dit", "dgg", "lot", "lod", "cog"]
words = ["cog", "hot", "dit", "dgg", "log", "lod"]
print(solution(begin, target, words))