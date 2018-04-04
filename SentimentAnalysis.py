def sentAnalysis(l):
    # This method takes the list of tweets for each celebrity and performs a sentiment analysis for that
    # particular celebrity
    nfp = open("negative_words.txt", "r")
    pfp = open("positive_words.txt", "r")
    pst = pfp.readline()
    pst = pst.rstrip(r"\n")
    pcount = 0
    while pst != '':
        pst = pst.rstrip("\n")
        for i in l:
            i=i.lower()
            pcount += i.count(pst)
        pst = pfp.readline()
    nst = nfp.readline()
    ncount = 0
    while nst != '':
        nst = nst.rstrip("\n")
        for i in l:
            i = i.lower()
            ncount += i.count(nst)
        nst = nfp.readline()
    if pcount > ncount:
        return 1
    elif pcount < ncount:
        return -1
    else:
        return 0