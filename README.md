# Week 2 – Logistics Data Collection, Cleaning and Preprocessing

This GitHub project documents the Week 2 internship task for logistics data analysis.

## Objective
Prepare a simulated logistics dataset for analysis by:
- inspecting the raw data
- identifying missing values and duplicate records
- handling missing numerical values
- detecting potential outliers using the IQR method
- normalizing selected numerical features
- validating the cleaned dataset

## Tools
Python, Pandas, NumPy, Scikit-learn.

## Structure
```text
week2-logistics-data-preprocessing/
├── data/
│   └── logistics_data.csv
├── src/
│   └── data_preprocessing.py
├── notebooks/
│   └── week2_preprocessing.ipynb
├── reports/
│   └── Week_2_Logistics_Data_Preprocessing_Report.docx
├── requirements.txt
├── PROJECT_NOTES.md
├── .gitignore
└── README.md
```

## Run the project
```bash
pip install -r requirements.txt
python src/data_preprocessing.py
```

The processed dataset will be saved in `data/processed/`.

## Methods Used
1. Duplicate removal using Pandas.
2. Missing numerical values handled with the median.
3. Potential shipping-cost outliers flagged using the IQR method.
4. Selected numerical features normalized using Min-Max scaling.

The dataset is simulated for educational/internship purposes and contains no confidential information.
