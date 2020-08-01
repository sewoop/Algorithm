def solution(strings, n):
    lists = [[string[n],string] for _,string in enumerate(strings)]
    temp = sorted(lists, key=lambda lists: lists[0], reverse=True)

    return [i[1] for i in sorted(temp)]

if __name__ == "__main__":
    # strings = ['sun', 'bed', 'car']
    # n = 1
    # strings = ['abce', 'abcd', 'cdx']
    # n = 2
    strings = ['abzcd','cdzab','abzfg','abzaa','abzbb','bbzaa']
    n = 2
    print(solution(strings,n))