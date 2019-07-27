from numpy.core.tests.test_mem_overlap import xrange


def basic():
    dn = 0
    step = 0
    progress = 0
    while dn < 500:
        tn = sum([x for x in xrange(step + 1)])
        s = [x for x in xrange(1, tn + 1) if tn % x == 0]
        dn = len(s)
        step += 1
        if dn > progress:
            progress = dn
            print("%s: %s\n" % (str(tn), str(progress)))
    print(tn)


basic()

# todo slow algorithm
