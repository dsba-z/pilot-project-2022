def parse_link(a):
    a = str(a)
    tmp = a[a.find("j/")+2: a.find("/pwd")]
    if len(tmp) == 9:
        return(tmp[0:3]+ " "+ tmp[3:6]+ " " + tmp[6:9])
    if len(tmp) == 10:
        return (tmp[0:3]+ " " +tmp[3:6]+ " " + tmp[6:10])
    if len(tmp) == 9:
        return (tmp[0:3]+ " " +tmp[3:7]+ " " + tmp[7:11])