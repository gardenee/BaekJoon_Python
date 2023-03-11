for _ in range(int(input())):
    N = int(input())
    answer = 0

    is_prime_num = [True] * (N+1)
    is_prime_num[0] = False
    is_prime_num[1] = False

    for i in range(2, N+1):
        if is_prime_num[i]:
            for j in range(i*2, N+1, i):
                is_prime_num[j] = False

    for i in range(2, N//2 + 1):
        if is_prime_num[i] and is_prime_num[N-i]:
            answer += 1

    print(answer)
