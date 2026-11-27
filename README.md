# Employee Satisfaction Data Cleaning Project

## Project Overview

This project focuses on loading, inspecting, and cleaning an employee dataset using Python and Pandas.

The goal is to prepare a clean dataset for future data analysis and visualization.

## Dataset

- Dataset file: Employee Attrition.csv
- Original records: 15,787
- Final records: 14,999
- Number of columns: 10
- Completely empty rows removed: 788

**Note:** The downloaded file is named Employee Attrition.csv. It contains employee satisfaction and workplace-related information.

## Technologies Used

- Python
- Pandas
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
talenthub-survey-dashboard/
│
├── data/
│   ├── raw/
│   │   └── Employee Attrition.csv
│   │
│   └── processed/
│       └── employee_satisfaction_cleaned.csv
│
├── scripts/
│   └── clean_data.py
│
├── reports/
│
└── README.md
```

## Data Cleaning Process

The following steps were performed:

1. Loaded the original CSV file using Pandas.
2. Inspected the dataset using head() and info().
3. Identified missing values using isnull().sum().
4. Identified and removed 788 completely empty rows.
5. Standardized column names to snake_case.
6. Corrected the column name average_montly_hours to average_monthly_hours.
7. Checked for missing employee IDs.
8. Used median imputation for missing numerical values, excluding employee IDs.
9. Used mode imputation for missing categorical values.
10. Verified that no missing values remained.
11. Saved the cleaned dataset as a new CSV file.

## Output

The cleaned dataset is saved at:

`data/processed/employee_satisfaction_cleaned.csv`

Final dataset:
- 14,999 records
- 10 columns
- Zero missing values

## How to Run the Project

### 1. Install Python dependencies

```bash
python -m pip install pandas
```

### 2. Run the cleaning script

```bash
python scripts/clean_data.py
```

## Conclusion

The dataset was successfully loaded, inspected, cleaned, and saved using Python and Pandas.

It is now ready for subsequent exploratory data analysis and visualization.

## Summary Statistics Report

A summary statistics report was generated using Pandas.

**Report location:**
`reports/summary_statistics.csv`

**Script location:**
`scripts/summary_report.py`

The report includes:
- Count
- Mean
- Standard deviation
- Minimum
- Maximum
- 25th, 50th, and 75th percentiles

To generate the report, run:

```bash
python scripts/summary_report.py
```