with open('t67.txt', 'r') as f:
    def validate(line):
        list = [int(v.replace('\n', '')) for v in line.split(' ')]
        if len(list) > 1:
            return list[:-1]
        return list


    def go(indX=0, indY=0, acc=d[0]):
        for i, a in enumerate(d):
            if i == indX and i < len(d) - 1:
                if indY + 1 < len(d[i + 1]) and d[i + 1][indY] > d[i + 1][indY + 1]:
                    go(i + 1, indY + 1, acc + [d[i + 1][indY + 1]])
                elif indY < len(d[i + 1]):
                    go(i + 1, indY, acc + [d[i + 1][indY]])
        total.append(acc)


    d = [validate(line) for line in f.readlines()]
    total = []
    go()
    print(max([sum(v) for v in total]))
