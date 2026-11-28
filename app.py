
import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------
# 1. Page Settings
# --------------------------------
st.set_page_config(
    page_title="TalentHub Survey Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------
# 2. Dashboard Title
# --------------------------------
st.title("📊 TalentHub Recruiters Survey Dashboard")
st.write("Employee Satisfaction and Attrition Analysis")

st.divider()

# --------------------------------
# 3. Load Cleaned Dataset
# --------------------------------
df = pd.read_csv(
    "data/processed/employee_satisfaction_cleaned.csv"
)

# --------------------------------
# 4. Department Filter
# --------------------------------
st.sidebar.header("Dashboard Filters")

departments = sorted(df["dept"].dropna().unique())

selected_departments = st.sidebar.multiselect(
    "Select Department",
    departments,
    default=departments
)

# Filter dataset
filtered_df = df[
    df["dept"].isin(selected_departments)
]

# --------------------------------
# Salary Filter
# --------------------------------

st.sidebar.subheader("Salary Filter")

salary_options = sorted(df["salary"].dropna().unique())

selected_salary = st.sidebar.multiselect(
    "Select Salary Level",
    salary_options,
    default=salary_options
)

# Apply salary filter
filtered_df = filtered_df[
    filtered_df["salary"].isin(selected_salary)
]

# --------------------------------
# Work Accident Filter
# --------------------------------

st.sidebar.subheader("Work Accident Filter")

accident_options = ["No", "Yes"]

selected_accidents = st.sidebar.multiselect(
    "Work Accident Status",
    accident_options,
    default=accident_options
)

# Apply work accident filter
filtered_df = filtered_df[
    filtered_df["work_accident"].isin(
        [1 if status == "Yes" else 0 for status in selected_accidents]
    )
]

# --------------------------------
# 5. Key Statistics
# --------------------------------
st.subheader("Key Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Employees",
    f"{len(filtered_df):,}"
)

if not filtered_df.empty:

    col2.metric(
        "Average Satisfaction",
        f"{filtered_df['satisfaction_level'].mean():.2f}"
    )

    col3.metric(
        "Average Evaluation",
        f"{filtered_df['last_evaluation'].mean():.2f}"
    )

    col4.metric(
        "Average Monthly Hours",
        f"{filtered_df['average_monthly_hours'].mean():.1f}"
    )

else:
    col2.metric("Average Satisfaction", "N/A")
    col3.metric("Average Evaluation", "N/A")
    col4.metric("Average Monthly Hours", "N/A")

st.divider()

# --------------------------------
# 6. Employee Survey Data
# --------------------------------
st.subheader("Employee Survey Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.divider()

# --------------------------------
# 7. Interactive Charts
# --------------------------------
st.subheader("Employee Satisfaction Analysis")

if not filtered_df.empty:

    col1, col2 = st.columns(2)

    # Chart 1: Satisfaction Distribution
    with col1:

        fig1 = px.histogram(
            filtered_df,
            x="satisfaction_level",
            nbins=20,
            title="Employee Satisfaction Distribution",
            labels={
                "satisfaction_level": "Satisfaction Level"
            }
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    # Chart 2: Satisfaction by Department
    with col2:

        dept_satisfaction = (
            filtered_df.groupby(
                "dept",
                as_index=False
            )["satisfaction_level"].mean()
        )

        fig2 = px.bar(
            dept_satisfaction,
            x="dept",
            y="satisfaction_level",
            title="Average Satisfaction by Department",
            labels={
                "dept": "Department",
                "satisfaction_level": "Average Satisfaction"
            }
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

else:
    st.warning("Please select at least one department.")

st.divider()

# --------------------------------
# 8. Dashboard Footer
# --------------------------------
st.caption(
    "TalentHub Recruiters Survey Dashboard | "
    "Built with Python, Pandas, Streamlit and Plotly"
)
