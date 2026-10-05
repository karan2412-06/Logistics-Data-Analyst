import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/logistics_data.csv")

df["Shipment_Date"] = pd.to_datetime(df["Shipment_Date"])

print("Dataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

print("\nDescriptive statistics:")
print(df.describe())

print("\nShipments by region:")
print(df["Region"].value_counts())

print("\nAverage cost by transportation mode:")
print(df.groupby("Transportation_Mode")["Transportation_Cost"].mean())

# Delivery-time trend
monthly = df.groupby(
    df["Shipment_Date"].dt.to_period("M")
)["Delivery_Time_Days"].mean()

plt.figure(figsize=(8, 4))
monthly.plot(marker="o")
plt.title("Average Delivery Time Trend")
plt.xlabel("Month")
plt.ylabel("Average Delivery Time (days)")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("visualizations/delivery_trend.png", dpi=160)
plt.show()

# Shipments by region
plt.figure(figsize=(8, 4))
df["Region"].value_counts().plot(kind="bar")
plt.title("Shipment Volume by Region")
plt.xlabel("Region")
plt.ylabel("Number of Shipments")
plt.tight_layout()
plt.savefig("visualizations/shipments_by_region.png", dpi=160)
plt.show()

# Product categories
plt.figure(figsize=(8, 4))
df["Product_Category"].value_counts().plot(kind="bar")
plt.title("Shipments by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Shipments")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("visualizations/product_category.png", dpi=160)
plt.show()

# Average cost by mode
plt.figure(figsize=(8, 4))
df.groupby("Transportation_Mode")["Transportation_Cost"].mean().sort_values(
    ascending=False
).plot(kind="bar")
plt.title("Average Transportation Cost by Mode")
plt.xlabel("Transportation Mode")
plt.ylabel("Average Cost")
plt.tight_layout()
plt.savefig("visualizations/mode_cost.png", dpi=160)
plt.show()

# Correlation heatmap
numeric_cols = [
    "Quantity",
    "Weight_kg",
    "Volume_m3",
    "Delivery_Time_Days",
    "Transportation_Cost"
]
corr = df[numeric_cols].corr()

plt.figure(figsize=(8, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix of Key Logistics Variables")
plt.tight_layout()
plt.savefig("visualizations/correlation_heatmap.png", dpi=160)
plt.show()
