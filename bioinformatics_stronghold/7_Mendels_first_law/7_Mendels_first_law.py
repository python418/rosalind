def dominant(a, b, c):
    k = a
    m = b
    n = c
    total = m+n+k
    Cm_n = n*m*0.5
    Cm_m = (m*(m-1))/2 *0.25
    Cn_n = (n*(n-1))/2
    rec_prob = (Cm_n + Cm_m + Cn_n)/((total * (total-1))/2)
    dom_prob = 1 - rec_prob
    return round(dom_prob, 5)
print(dominant(21, 30, 25))
