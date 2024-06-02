def find_password(n):
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n / j == i and n / i == j and i != j:
                pairs.append((i, j))
    password = ''.join(str(x) + str(y) for x, y in pairs)
    return password


expected_results = {
    3: '12',
    4: '13',
    5: '1423',
    6: '121524',
    7: '162534',
    8: '13172635',
    9: '1218273645',
    10: '141923283746',
    11: '11029384756',
    12: '12131511124210394857',
    13: '112211310495867',
    14: '1611325212343114105968',
    15: '1214114232133124115106978',
    16: '1317115262143531341251161079',
    17: '11621531441351261171089',
    18: '12151811724272163631545414513612711810',
    19: '118217316415514613712811910',
    20: '13141911923282183731746416515614713812911'}

for n in range(3, 21):
    result = find_password(n)
    if result != expected_results[n]:
        print(f"Не соответствие для  {n}: ожидаемый {expected_results[n]}, получено {result}")
