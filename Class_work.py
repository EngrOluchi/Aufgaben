import pandas as pd
import matplotlib.pyplot as plt
infilename = "testfile.csv"
data = pd.read_csv(infilename)

plt.plot(data["T_degC"], "bo")
ax = plt.gca()
ax.set_ylabel("Temp in C")
ax.set_xlabel("Index")
plt.savefig("Temp.pdf")
plt.show()
