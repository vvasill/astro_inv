import numpy as np
import matplotlib.pyplot as plt

dm_x, psf = np.genfromtxt('g_func/gauss_func_d2.dat', unpack = True)
psf_x, dm = np.genfromtxt('res_profs/res_prof_d2.dat', unpack = True)
cm = np.zeros(len(dm))
cm_temp = np.zeros(len(dm))

dm_max_init = np.max(dm) 
dm_max = dm_max_init

while (dm_max > 0.05*dm_max_init):	
	dm_max = np.max(dm) 
	max_pos = np.argmax(dm)

	cm[max_pos] = dm_max

	cm_temp[max_pos] = dm_max
	db = np.convolve(cm_temp, psf)
	cm_temp[max_pos] = 0.0
	db_max = np.max(db)

	diff_len = (len(db)-len(dm))//2
	db = db[diff_len:-diff_len]

	dm -= 1.0*db*dm_max/db_max

cb = np.convolve(cm, psf)
diff_len = (len(cb)-len(dm))//2
cb = cb[diff_len:-diff_len]

fig, ax = plt.subplots()
ax.plot(np.arange(len(cb)), cb)
plt.show()
