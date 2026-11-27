
import pandas as pd

# 1. Load the original dataset
df = pd.read_csv("data/raw/Employee Attrition.csv")

print("Original dataset shape:", df.shape)

# 2. Check completely empty rows
empty_rows = df.isnull().all(axis=1).sum()
print("Completely empty rows:", empty_rows)

# 3. Remove completely empty rows
df = df.dropna(how="all")

# 4. Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

# Correct a spelling mistake in the original column name
df = df.rename(columns={
    "average_montly_hours": "average_monthly_hours"
})

# 5. Remove records without an employee ID
missing_ids = df["emp_id"].isnull().sum()
print("Rows without employee ID:", missing_ids)

df = df.dropna(subset=["emp_id"])

# 6. Inspect missing values
print("\nMissing values before imputation:")
print(df.isnull().sum())

# 7. Fill missing numerical values using median
for column in df.select_dtypes(include="number").columns:
    if column != "emp_id":
        df[column] = df[column].fillna(df[column].median())

# 8. Fill missing text values using mode
for column in df.select_dtypes(exclude="number").columns:
    if df[column].isnull().any():
        mode_value = df[column].mode()
        if not mode_value.empty:
            df[column] = df[column].fillna(mode_value[0])

# 9. Check final missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# 10. Save cleaned dataset
df.to_csv(
    "data/processed/employee_satisfaction_cleaned.csv",
    index=False
)

print("\nFinal dataset shape:", df.shape)
print("Cleaned dataset saved successfully!")
