# Logistics Analysis Notebook

Use this notebook to document the analysis in a step-by-step way.

## 1. Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

## 2. Load the Dataset

```python
df = pd.read_csv("../data/logistics_data.csv")
df.head()
```

## 3. Explore the Dataset

```python
df.shape
df.info()
df.describe()
df.isnull().sum()
```

## 4. Analyze Shipment Distributions

```python
df["Region"].value_counts()
df["Product_Category"].value_counts()
df["Transportation_Mode"].value_counts()
```

## 5. Delivery-Time Analysis

```python
df["Shipment_Date"] = pd.to_datetime(df["Shipment_Date"])

monthly = df.groupby(
    df["Shipment_Date"].dt.to_period("M")
)["Delivery_Time_Days"].mean()

monthly.plot(marker="o")
plt.title("Average Delivery Time Trend")
plt.show()
```

## 6. Correlation Analysis

```python
numeric_cols = [
    "Quantity",
    "Weight_kg",
    "Volume_m3",
    "Delivery_Time_Days",
    "Transportation_Cost"
]

corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()
```

## 7. Interpretation

Document the major findings after each visualization instead of only displaying the chart. Explain what changed, what relationship was observed, and why it may matter to logistics operations.
