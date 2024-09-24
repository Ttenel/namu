line = []
with open('U1.txt', 'rt') as file:
    n = int(file.readline().strip())
    
    for i in range(n):
        line.append([int(item) for item in file.readline().split()])

stat = {}

for zaid in line:
    num = zaid[0]
    pt_baudos = zaid[1]
    mt_baudos = zaid[2]
    pt_dvit = zaid[3]
    mt_dvit = zaid[4]
    pt_trit = zaid[5]
    mt_trit = zaid[6]
    
    suma = pt_baudos * 1 + pt_dvit * 2 + pt_trit * 3

    if num in stat:
        stat[num]['zaidimu_sk'] += 1
        stat[num]['suma'] += suma
        stat[num]['pt_baudos'] += pt_baudos
        stat[num]['mt_baudos'] += mt_baudos
        stat[num]['pt_dvit'] += pt_dvit
        stat[num]['mt_dvit'] += mt_dvit
        stat[num]['pt_trit'] += pt_trit
        stat[num]['mt_trit'] += mt_trit
    else:
        stat[num] = {
            'zaidimu_sk': 1,
            'suma': suma,
            'pt_baudos': pt_baudos,
            'mt_baudos': mt_baudos,
            'pt_dvit': pt_dvit,
            'mt_dvit': mt_dvit,
            'pt_trit': pt_trit,
            'mt_trit': mt_trit
        }

for num, statistika in stat.items():
    avg_suma = round(statistika['suma'] / statistika['zaidimu_sk'], 1)
    all_mt = statistika['mt_baudos'] + statistika['mt_dvit'] + statistika['mt_trit']
    all_pt = statistika['pt_baudos'] + statistika['pt_dvit'] + statistika['pt_trit']
    
    if all_mt > 0:
        pt_proc = round((all_pt / all_mt) * 100)
    else:
        pt_proc = 0 
    print(f"Žaidėjo numeris: {num}")
    print(f"  Sužaisti žaidimai: {statistika['zaidimu_sk']}")
    print(f"  Bendri taškai: {statistika['suma']}")
    print(f"  Vidutiniškai taškų per žaidimą: {avg_suma}")
    print(f"  Pataikymo procentas: {pt_proc}%")
    print(f"  Baudos: {statistika['pt_baudos']} pataikytos iš {statistika['mt_baudos']} mestų")
    print(f"  Dvitaškiai: {statistika['pt_dvit']} pataikyti iš {statistika['mt_dvit']} mestų")
    print(f"  Tritaškiai: {statistika['pt_trit']} pataikyti iš {statistika['mt_trit']} mestų")
    print("*"*80)
