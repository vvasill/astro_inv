import numpy as np
import matplotlib.pyplot as plt

x, g = np.genfromtxt('g_func/gauss_func_d8.dat', unpack = True)
x, fi_in = np.genfromtxt('res_profs/res_prof_d8.dat', unpack = True)

n = (len(x)-1)//2
gauss = g[ n : 2*n+1 ]

tr_len = len(fi_in)//4
fi_t = fi_in[tr_len:-tr_len]

nn = n+1
P = np.zeros((nn,nn))
psi = np.ones(nn)
fi = np.zeros(nn)
fi_old = np.zeros(nn)
d_psi = np.zeros(nn)

norm = 0
norm = 2*np.sum(g) - g[0]
g /= norm

for i in range(nn):
	for j in range(nn):
		P[i,j] = gauss[abs(j-i)]

norm = 0
norm = np.sum(fi_t)
fi_t /= norm

norm = 0
norm = np.sum(psi)
psi /= norm

n_i = 0
sigma = 1
while ( n_i < 1000 ):
	sigma = 0.0
	for i in range(nn):
		for j in range(nn):
			fi[i] += psi[j]*P[i,j]
		sigma += (fi_t[i] - fi[i])**2
	for j in range(nn):
		suum = 0.0
		for i in range(nn):
			suum += fi_t[i]/fi[i]*P[i,j]
		d_psi[j] = psi[j]*(suum-1)
	sigma = np.sqrt(sigma)/nn
	n_i += 1	
	psi += d_psi
	print(n_i, sigma)

fig, ax = plt.subplots()
ax.plot(np.arange(len(psi)), psi)
plt.show()

