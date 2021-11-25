import numpy as np
import matplotlib.pyplot as plt

#--------------

# fig, ax = plt.subplots()

# data = np.loadtxt("normsLog.asc")
# print(data[0,0])

# ax.plot(data[:,0], data[:,1],"+-",lw=0.1, color="tab:green", zorder=5)
# ax.set_ylabel("Absolute norm $T_n-T_{eq}$", color="tab:green")
# ax.tick_params(axis="y", colors="tab:green")
# #ax.set_yscale('log')

# ax2 = ax.twinx()
# ax2.plot(data[:,0], data[:,2],"+-",lw=0.1, color="tab:blue")
# ax2.set_ylabel("Relative Norm $(T_{n+1}-T_n)/T_n$", color="tab:blue")
# ax2.tick_params(axis="y", colors="tab:blue")
# ax2.set_yscale('log')

# ax.set_xlabel("Time (s)")

#--------------


# data = np.loadtxt("dichotLog.asc")

# Tc = 19.0

# fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True)

# ax1.plot(data[:,0],data[:,1], "-+",color="tab:green", lw=0.5)
# ax1.set_xlabel("Iteration")
# ax1.set_ylabel("Time (s)")

# ax2.plot(data[:,0], data[:,2]-Tc ,"-+", lw=0.5)
# ax2.set_ylabel("$T_m^n - T_c$")
# ax2.set_xlabel("Iteration")

# print(data[-1,:])

#--------------

# data = np.loadtxt("meshTestLog.asc")

# fig, ax = plt.subplots()

# ax.plot(data[:,0],data[:,1], "-+", lw=0.5)
# ax.set_xlabel("Finesse du maillage")
# ax.set_ylabel("Norme L2 du champ de température T")

#--------------

data = np.loadtxt("TmLog.asc")

fig, ax = plt.subplots()

ax.plot(data[:1000,0],data[:1000,1])
ax.set_xlabel("Temps (s)")
ax.set_ylabel("Température moyenne au sein du cercle")

ax.hlines(19.0, data[0,0], data[1000,0], color="k", linestyle=":", label="Température critique $T_c$")

ax.legend()

plt.draw()
plt.plot()
