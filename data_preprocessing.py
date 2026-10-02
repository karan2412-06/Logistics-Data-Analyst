from pathlib import Path
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "data" / "logistics_data.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "logistics_data_cleaned.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

print("Original shape:", df.shape)
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates().copy()

# Convert and clean numerical columns
numeric_cols = [
    "Distance_km", "Delivery_Time_hr",
    "Inventory_Units", "Shipping_Cost"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

# Detect possible shipping-cost outliers using IQR
q1 = df["Shipping_Cost"].quantile(0.25)
q3 = df["Shipping_Cost"].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

df["Cost_Outlier"] = (
    (df["Shipping_Cost"] < lower) |
    (df["Shipping_Cost"] > upper)
)

# Normalize selected features
scale_cols = ["Distance_km", "Delivery_Time_hr", "Shipping_Cost"]
scaler = MinMaxScaler()
df[scale_cols] = scaler.fit_transform(df[scale_cols])

df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaning completed successfully.")
print("Final shape:", df.shape)
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print(f"\nSaved to: {OUTPUT_FILE}")
