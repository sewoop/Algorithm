def solution(phone_number):
    phone = [i for i in phone_number]

    for i in range(len(phone)-1, -1, -1):
        if i < len(phone)-4:
            phone[i] = '*'

    return ''.join(phone)


if __name__ == "__main__":
    # phone_number = "01033334444"
    phone_number = "027778888"

    print(solution(phone_number))
