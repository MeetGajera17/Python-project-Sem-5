import numpy as np
import pandas as pd

def perform_analysis(data):
    try:
        # Separate numeric columns
        numeric_data = data.select_dtypes(include=[np.number])

        # Numeric data analysis
        if not numeric_data.empty:
            mean = numeric_data.mean()
            median = numeric_data.median()
            std_dev = numeric_data.std()
            correlation = numeric_data.corr()

            numeric_results = (f"Numeric Data Analysis:\n"
                               f"Mean:\n{mean}\n\n"
                               f"Median:\n{median}\n\n"
                               f"Standard Deviation:\n{std_dev}\n\n"
                               f"Correlation:\n{correlation}\n\n")
        else:
            numeric_results = "No numeric data available for analysis.\n\n"

        return numeric_results

    except Exception as e:
        return f"Error performing analysis: {e}"
