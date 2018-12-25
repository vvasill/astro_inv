# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

import numpy as np
import matplotlib.pyplot as plt

#data = open('spec001.dat', 'r')
res_x, res_y = np.genfromtxt('spec001.dat', unpack = True)
gx8, gy8 = np.genfromtxt('g_func/gauss_func_d8.dat', unpack = True)
x1, y1 = np.genfromtxt('res_profs/res_prof_d8.dat', unpack = True)
#data = np.loadtxt('spec001.dat')


fft_func = np.fft.fft(y1)
fft_gauss = np.fft.fft(gy8)

s = fft_func/fft_gauss

ifft_s = np.fft.ifftshift(np.fft.ifft(np.fft.fftshift((s))))

print(fft_func)

fig, ax = plt.subplots()
fig, ax1 = plt.subplots()
fig, ax2 = plt.subplots()
fig, ax3 = plt.subplots()
fig, ax4 = plt.subplots()
fig, ax5 = plt.subplots()

ax.plot(x1,y1)
ax1.plot(gx8,gy8)
ax2.plot(fft_func)
ax3.plot(fft_gauss)
ax4.plot(ifft_s)
ax5.plot(res_x, res_y)

#plt.plot(xfft1, yfft1)

plt.show()
