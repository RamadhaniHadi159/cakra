import pandas as pd
import numpy as np

# Load data yang akan diolah
df = pd.read_csv("Csat.csv")

# Format time menjadi 2 digit
df["time"] = df["time"].astype(str).str.zfill(2)

# C_min, kondisi dimana langit cerah
# C_max, kondisi dimana langit mendung
# C_sat, nilai refelctance yang telah di normalisasi

Csat = df["Csat"]

cmin = df["Csat"].min()
cmax = df["Csat"].max()

CI = (
    (df["Csat"] - cmin)
    / (cmax - cmin)
)

# Bulatkan 3 angka belakang koma
CI = CI.round(3)


# CI = np.clip(CI, 0, 1) # jika diperlukan untuk dibatasia antaea 0 sampai 1

# Simpan hasil perhitungan CI
df["CI"] = CI
df.to_csv("CI.csv", index=False)

print("Cmin :", cmin)
print("Cmax :", cmax)
print(CI)