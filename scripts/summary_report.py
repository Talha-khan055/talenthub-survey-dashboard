
import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "data/processed/employee_satisfaction_cleaned.csv"
)

# Generate summary statistics
summary = df.describe()

# Save report
summary.to_csv("reports/summary_statistics.csv")

print("Summary statistics report created successfully!")
print("\nReport saved to reports/summary_statistics.csv")
