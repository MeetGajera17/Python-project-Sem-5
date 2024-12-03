import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
from data_analysis import perform_analysis
from visualization import visualize_data

class DataVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Data Visualization and Analysis Tool")
        self.root.configure(bg="black")  # Set background color to black
        self.data = None
        
        # File Upload Button
        self.upload_button = tk.Button(root, text="Upload CSV", command=self.upload_file, bg="black", fg="white")
        self.upload_button.pack(pady=10)

        # Analysis Button
        self.analysis_button = tk.Button(root, text="Perform Analysis", command=self.perform_analysis, bg="black", fg="white")
        self.analysis_button.pack(pady=10)

        # Visualization Options Dropdown
        self.plot_type = tk.StringVar(root)
        self.plot_type.set("Select Plot Type")
        self.plot_menu = tk.OptionMenu(root, self.plot_type, "Line Plot", "Scatter Plot", "Histogram", "Bar Graph")
        self.plot_menu.config(bg="black", fg="white")
        self.plot_menu.pack(pady=10)

        # Column Selection Dropdowns for x and y axes
        self.x_col_label = tk.Label(root, text="Select X Column", bg="black", fg="white")
        self.x_col_label.pack(pady=5)
        self.x_col_menu = ttk.Combobox(root)
        self.x_col_menu.pack(pady=5)

        self.y_col_label = tk.Label(root, text="Select Y Column (Optional)", bg="black", fg="white")
        self.y_col_label.pack(pady=5)
        self.y_col_menu = ttk.Combobox(root)
        self.y_col_menu.pack(pady=5)

        # Visualization Button
        self.visualize_button = tk.Button(root, text="Visualize", command=self.visualize, bg="black", fg="white")
        self.visualize_button.pack(pady=10)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                # Load CSV with appropriate memory handling for large files
                self.data = pd.read_csv(file_path, low_memory=False)
                messagebox.showinfo("Success", "Data loaded successfully!", parent=self.root)

                # Filter only numeric columns (both int and float) for visualization
                numeric_columns = self.data.select_dtypes(include=['number']).columns.tolist()

                # Exclude columns that are mostly NaN or have fewer than 2 unique values
                numeric_columns = [col for col in numeric_columns if self.data[col].nunique() > 1]

                # Update the dropdowns with filtered numeric columns
                if numeric_columns:
                    self.x_col_menu['values'] = numeric_columns
                    self.y_col_menu['values'] = numeric_columns
                else:
                    messagebox.showerror("Error", "No suitable numeric columns available for visualization.", parent=self.root)
                    
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load data: {e}", parent=self.root)

    def perform_analysis(self):
        if self.data is not None:
            analysis_results = perform_analysis(self.data)
            messagebox.showinfo("Analysis Results", analysis_results, parent=self.root)
        else:
            messagebox.showerror("Error", "No data loaded", parent=self.root)

    def visualize(self):
        if self.data is not None:
            plot_type = self.plot_type.get()
            x_col = self.x_col_menu.get()
            y_col = self.y_col_menu.get()

            if plot_type != "Select Plot Type":
                if x_col:
                    # Limit to 100 rows by randomly sampling if the dataset exceeds 100 rows
                    if len(self.data) > 100:
                        sampled_data = self.data.sample(n=100, random_state=42)
                    else:
                        sampled_data = self.data
                    
                    # For graphs like Scatter Plot, Line Plot, and Bar Graph, ensure both X and Y are selected
                    if plot_type in ["Scatter Plot", "Line Plot", "Bar Graph"] and not y_col:
                        messagebox.showerror("Error", "Please select a Y column for the selected plot type.", parent=self.root)
                    else:
                        visualize_data(sampled_data, plot_type, x_col=x_col, y_col=y_col)
                else:
                    if plot_type == "Histogram":
                        visualize_data(self.data, plot_type, x_col=x_col)
                    else:
                        messagebox.showerror("Error", "Please select an X column.", parent=self.root)
            else:
                messagebox.showerror("Error", "Please select a plot type", parent=self.root)
        else:
            messagebox.showerror("Error", "No data loaded", parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataVisualizationApp(root)
    root.mainloop()
