import numpy as np
import matplotlib.pyplot as plt

bin_sizes = ['0.5', '1.0', '10.5', '2.5', '20.0', '4.5', '6.5']

for bin_size in bin_sizes:
   mjd_dm = np.load('new_bin_' + bin_size + '_chi2_.npy')
   print(mjd_dm)
   plt.plot(mjd_dm[0], mjd_dm[1], 'ko')
plt.show()
	
