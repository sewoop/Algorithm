while True:
    n = input()
    if n == "0": break
    if n == n[::-1]: 
        print("yes")
    else: 
        print("no")

# def is_palin(n):
#     l, r = 0, len(n) - 1
#     while l <= r:
#         if n[l] != n[r]:
#             return False
#         l += 1
#         r -= 1
#     return True

# while True:
#     n = input()
#     if n == '0': break
#     if is_palin(n):
#         print("yes")
#     else:
#         print("no")