N, K = map(int, input().split())
belt = list(map(int, input().split()))
robots = []
on, out = 0, N-1

answer = 0
while K > 0:
    answer += 1
    on = (2*N+on-1) % (2*N)
    out = (2*N+out-1) % (2*N)

    if out in robots:
        robots.remove(out)

    for i in range(len(robots)):
        next = (robots[i]+1) % (2*N)
        if belt[next] and next not in robots:
            belt[next] -= 1
            robots[i] = next
            if not belt[next]:
                K -= 1

    if out in robots:
        robots.remove(out)

    if on not in robots and belt[on]:
        robots.append(on)
        belt[on] -= 1
        if not belt[on]:
            K -= 1

print(answer)
