import pandas as pd
import matplotlib.pyplot as plt

"""Plot MFI components fetched from the visualization API."""

import requests

def fetch_mfi(api_url: str = "http://localhost:8000/mfi") -> pd.DataFrame:
    resp = requests.get(api_url, timeout=10)
    resp.raise_for_status()
    df = pd.DataFrame(resp.json()).set_index("timestamp")
    df.index = pd.to_datetime(df.index)
    return df

try:
    df = fetch_mfi()
except Exception:
    print("⚠️ Failed to fetch data; using empty placeholder")
    df = pd.DataFrame({
        'mfi': [],
        'mfi_sq': [],
        'mfi_green': [],
        'mfi_fade': [],
        'mfi_fake': []
    })

mfi_columns_corrected = ["mfi", "mfi_sq", "mfi_green", "mfi_fade", "mfi_fake"]
mfi_df = df[mfi_columns_corrected].copy()

plt.figure(figsize=(14, 8))
plt.plot(mfi_df.index, mfi_df["mfi"], label="MFI Value", color="black")
plt.scatter(mfi_df.index[mfi_df["mfi_sq"] == 1.0], mfi_df["mfi"][mfi_df["mfi_sq"] == 1.0],
            color="yellow", label="MFI Squat", s=60, marker='o')
plt.scatter(mfi_df.index[mfi_df["mfi_green"] == 1.0], mfi_df["mfi"][mfi_df["mfi_green"] == 1.0],
            color="green", label="MFI Green", s=40, marker='o')
plt.scatter(mfi_df.index[mfi_df["mfi_fade"] == 1.0], mfi_df["mfi"][mfi_df["mfi_fade"] == 1.0],
            color="red", label="MFI Fade", s=40, marker='x')
plt.scatter(mfi_df.index[mfi_df["mfi_fake"] == 1.0], mfi_df["mfi"][mfi_df["mfi_fake"] == 1.0],
            color="blue", label="MFI Fake", s=40, marker='^')

plt.title("MFI Signal Components (SPX500 H4)")
plt.xlabel("Date")
plt.ylabel("MFI Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
