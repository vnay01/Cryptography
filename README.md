# Cryptography

This repo is in development phase. I am stuck with a 'MemoryError' while calling
prim_factor() : 

"""
for i in range(len(rSqrModN)):
    a = prim.prim_factor(rSqrModN[i])
    if max(a) < B:
        rValue_B_smooth.append(rSqrModN[i])
"""

Once I figure the issue causing this, I can proceed further...