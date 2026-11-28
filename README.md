# TalentHub Recruiters Survey Dashboard

## Project Overview

This project focuses on cleaning and analyzing employee satisfaction and workplace-related data using Python and Pandas.

An interactive dashboard was developed using Streamlit and Plotly to explore employee satisfaction, salary levels, departments, and workplace-related information.

## Dataset

- Dataset file: `Employee Attrition.csv`
- Original records: 15,787
- Final records: 14,999
- Number of columns: 10
- Completely empty rows removed: 788
- Missing values in cleaned dataset: 0

**Note:** The downloaded file is named `Employee Attrition.csv`. It contains employee satisfaction and workplace-related information. The dataset file is not included in this repository. Place it in `data/raw/` before running the scripts.

## Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- Matplotlib
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
talenthub-survey-dashboard/
│
├── app.py
├── data/
│   ├── raw/
│   │   └── Employee Attrition.csv
│   └── processed/
│       └── employee_satisfaction_cleaned.csv
│
├── scripts/
│   ├── clean_data.py
│   └── summary_report.py
│
├── reports/
│   └── summary_statistics.csv
│
├── requirements.txt
└── README.md
```

## Data Cleaning Process

The following steps were performed:

1. Loaded the original CSV file using Pandas.
2. Inspected the dataset using `head()` and `info()`.
3. Checked missing values using `isnull().sum()`.
4. Identified and removed 788 completely empty rows.
5. Standardized column names to snake_case.
6. Corrected `average_montly_hours` to `average_monthly_hours`.
7. Checked for missing employee IDs.
8. Verified missing values after cleaning.
9. Saved the cleaned dataset as a new CSV file.

After removing completely empty rows, no missing values remained in the dataset.

## Output

Cleaned dataset:

`data/processed/employee_satisfaction_cleaned.csv`

Final dataset:
- 14,999 records
- 10 columns
- Zero missing values

## Summary Statistics Report

A summary statistics report was generated using Pandas.

**Report location:** `reports/summary_statistics.csv`

**Script location:** `scripts/summary_report.py`

The report includes:
- Count
- Mean
- Standard deviation
- Minimum
- Maximum
- 25th, 50th, and 75th percentiles

## Interactive Dashboard

The Streamlit dashboard includes:

- Department filter
- Salary level filter
- Work accident filter
- Total employee count
- Average satisfaction
- Average evaluation
- Average monthly hours
- Employee survey data table
- Employee satisfaction distribution chart
- Average satisfaction by department chart

## How to Run the Project

### 1. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 2. Prepare the dataset

Place `Employee Attrition.csv` inside:

`data/raw/`

### 3. Run the data cleaning script

```bash
python scripts/clean_data.py
```

### 4. Generate the summary statistics report

```bash
python scripts/summary_report.py
```

### 5. Launch the Streamlit dashboard

```bash
python -m streamlit run app.py
```

## Conclusion

The employee dataset was successfully loaded, inspected, and cleaned using Python and Pandas.

A summary statistics report was generated, and an interactive Streamlit dashboard was developed to explore employee satisfaction and workplace-related data.
