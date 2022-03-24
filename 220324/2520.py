for _ in range(int(input())):
    input()
    우유, 노른자, 설탕, 소금, 밀가루 = map(int, input().split())
    바나나, 딸기잼, 초콜릿, 호두 = map(int, input().split())
    반죽 = min(우유*2, 노른자*2, 설탕*4, 소금*16, int(밀가루//(9/16)))
    토핑 = 바나나 + 딸기잼//30 + 초콜릿//25 + 호두//10

    print(min(반죽, 토핑))
