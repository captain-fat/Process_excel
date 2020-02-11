
def readtxt(file):
    lines = []
    with open(file, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines