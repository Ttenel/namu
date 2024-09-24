line = []
with open('U1.txt', 'rt') as file:
    n = int(file.readline().strip())
    for i in range(n):
        line.append([int(item) for item in file.readline().split()])

stat = {}

for zaid in line:
    num = zaid[0]
    games = zaid[1]
    score = zaid[2]
    goal = zaid[3]
    mesti = zaid[4]

    if num in stat:
        stat[num]['games'] += games
        stat[num]['score'] += score
        stat[num]['goal'] += goal
        stat[num]['mesti'] += mesti
    else:
        stat[num] = {
            'games': games,
            'score': score,
            'goal': goal,
            'mesti': mesti
        }

for num, n in stat.items():
    print(f"Žaidėjo numeris: {num}")
    print(f"  Sužaistos rungtynės: {n['games']}")
    print(f"  Suminiai taškai: {n['score']}")
    print(f"  Pataikyti metimai: {n['goal']}")
    print(f"  Mesti metimai: {n['mesti']}")
    print("*"*40)
