def solution(s, times):
    answer = []
    newtime = []
    sy, sm, sd, sh, smm, ss = int(s[:4]), int(s[5:7]), int(s[8:10]), int(s[11:13]), int(s[14:16]), int(s[17:])
    for i in times :
        d, h, m, s = int(i[0:2]), int(i[3:5]), int(i[6:8]), int(i[9:])
        ny, nm, nd, nh, nmm, ns = sy, sm, sd + d, sh + h, smm + m, ss + s
        if ns >= 60 :
            ns = ns - ns//60*60
            nmm += ns//60
        if nmm >= 60 :
            nmm = nmm - nmm//60*60
            nh += nmm//60
        if nh >= 24 :
            nh = nh - nh//24*24
            nd += nh//24
        if nd > 30 :
            nd = nd - nd//30*30
            nm += nd//30
        if nm > 12 :
            nm = nm - nm//12*12
            ny += nm//12
        
        if ns < 10 :
            nns = str(0) + str(ns)
        else : 
            nns = str(ns)
        if nmm < 10 :
            nnmm = str(0) + str(nmm)
        else : 
            nnmm = str(nmm)
        if nh < 10 :
            nnh = str(0) + str(nh)
        else : 
            nnh = str(nh)
        if nd < 10 :
            nnd = str(0) + str(nd)
        else : 
            nnd = str(nd)
        if nm < 10 :
            nnm = str(0) + str(nm)
        else : 
            nnm = str(nm)

        newtime.append(str(ny) + nnm + nnd + nnh + nnmm + nns)

    ot = sm*30 + sd
    nt = int(newtime[-1][4:6])*30 + int(newtime[-1][6:8])
    rst = nt - ot
    if len(newtime) == rst :
        answer.append(1)
    else :
        answer.append(0)

    answer.append(rst)

    return answer


print(solution("2022:04:03:10:10:10",["00:04:04:04", "01:10:10:10"]))