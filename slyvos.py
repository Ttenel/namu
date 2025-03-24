def slyvavalgiai(input, output):
    with open(input, 'r') as f:
        duomenys = list(map(int, f.readline().split()))
    
    mokyniai = [0] * 20 

    for i in range(10):
        mokyniai[i] += duomenys[i]
    
    for i in range(10):
        slyvos = 10 - duomenys[i]
        for j in range(i + 1, 20):
            if slyvos > 0:
                mokyniai[j] += 1
                slyvos -= 1
            else:
                break
    
    with open(output, 'w') as f:
        f.write(' '.join(map(str, mokyniai)))


slyvavalgiai('U1D.txt', 'U1rez.txt')
