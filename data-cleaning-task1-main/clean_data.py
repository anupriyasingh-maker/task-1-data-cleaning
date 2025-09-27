import pandas as pd

# Step 1: Load Data
df = pd.read_csv("retail_store_sales.csv")
print("Original data shape:", df.shape)

# Step 2: Handle Missing Values
df = df.dropna(subset=["Item", "Price Per Unit", "Quantity", "Total Spent"])
df["Discount Applied"] = df["Discount Applied"].fillna(False)

# Step 3: Remove Duplicates
df = df.drop_duplicates()

# Step 4: Standardize Column Names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 5: Fix Data Types
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors='coerce')
df["transaction_date"] = df["transaction_date"].dt.strftime('%d-%m-%Y')
df["quantity"] = df["quantity"].astype(int)
df["price_per_unit"] = df["price_per_unit"].astype(float)
df["total_spent"] = df["total_spent"].astype(float)

# Step 6: Save Cleaned Data
df.to_csv("cleaned_retail_data.csv", index=False)

# Step 7: Print Summary
print("\nCleaned data shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
