def nearly_equal(a,b,sig_fig=5):
    return ( a==b or 
             int(a*10**sig_fig) == int(b*10**sig_fig)
           )

def isclose(a, b, rel_tol=1e-09, abs_tol=0.8):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


print(isclose(2.2222222222222222222,2.11))