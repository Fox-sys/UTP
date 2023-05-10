import numpy as np

a = '2*x^3+5*x^2+3*x-3'

coefs = []
elms = a.split('*')
for i, elm in enumerate(elms):
    if i == 0:
        coefs.append(float(elm))
        continue
    try:
        if '+' in elm:
            coefs.append(float(elm.split('+')[1]))
        if '-' in elm:
            coefs.append(-float(elm.split('-')[1]))
    except IndexError:
        coefs.append(float(elm))

roots = np.roots(coefs)

print(', '.join(list(set(map(str, roots)))))

roots_upd = []
for i in roots:
    if len(roots_upd) != 0:
        cont = False
        for j in roots_upd:
            if abs(i.real - j.real) < 0.0000001 and abs(abs(i.imag) - abs(j.imag)) < 0.0000001:
                cont = True
                break
        if cont:
            continue
        roots_upd.append(i)
    else:
        roots_upd.append(i)

print(roots_upd)
