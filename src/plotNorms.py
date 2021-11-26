import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use("TkAgg")

#--------------

# fig, ax = plt.subplots()

# dt = 1000000.0
# ax.set_title(f"Evolution des normes absolues et relatives du champ\ndt = {dt}s")

# data = np.loadtxt("normsLog.asc")


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

datafiles = [
    "meshTestLogP1.asc",
    "meshTestLogP2.asc"
    ]

labels = ["P1", "P2"]


fig, ax = plt.subplots()

for p, file in zip(labels, datafiles):
    
    data = np.loadtxt(file)
    #ax.plot(data[:,0],data[:,1], "-+", lw=0.5, label=p)
    ax.plot(data[:,0],data[:,2], "-+", lw=0.5, label=p)
ax.set_xlabel("Finesse du maillage")

# ax.set_ylabel("Norme L2 du champ de température T")
ax.set_ylabel("Nombre de degrés de liberté")

#--------------

# fig, ax = plt.subplots()


# datafiles = [
#     "TmLog.asc",
#     "TmLogk1.asc",
#     "TmLogk005.asc",
#     "TmLogk015.asc"
#     ]
# k = [0.25, 1.0, 0.05, 0.15]


# for k,file in zip(k,datafiles):

#     data = np.loadtxt(file)
#     ax.plot(data[:,0],data[:,1], label=f"k = {k}W/m/K")

# # datafiles = [
# #     "TmLog.asc",
# #     "TmLogq1.asc",
# #     "TmLogq015.asc",
# #     "TmLogq+015.asc",
# #     ]
# # q = [-0.31, -1.0, -0.15, 0.15]


# # for q,file in zip(q,datafiles):

# #     data = np.loadtxt(file)
# #     ax.plot(data[:,0],data[:,1], label=f"q = {q}W/m2")



# ax.set_xlabel("Temps (s)")
# ax.set_ylabel("Température moyenne au sein du cercle")

# ax.hlines(19.0, data[0,0], data[-1,0], color="k", linestyle=":", label="Température critique $T_c$")

# ax.legend()

#--------------

plt.plot()
