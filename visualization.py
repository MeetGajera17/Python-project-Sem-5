import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data, plot_type, x_col=None, y_col=None):
    try:
        # Set a Seaborn color palette for vibrant colors
        sns.set(style="darkgrid")  # Dark grid for contrast
        plt.figure(figsize=(10, 6))  # Set the figure size
        
        if plot_type == "Line Plot":
            if x_col and y_col:
                data.plot(x=x_col, y=y_col, color=sns.color_palette("rainbow"))
            else:
                data.plot(color=sns.color_palette("rainbow"))

        elif plot_type == "Scatter Plot":
            if x_col and y_col:
                # Use a color map for scatter plot points
                plt.scatter(data[x_col], data[y_col], c=data[y_col], cmap="coolwarm", edgecolor='k')
                plt.xlabel(x_col)
                plt.ylabel(y_col)
                plt.colorbar(label=y_col)  # Add color bar to show the gradient

        elif plot_type == "Histogram":
            if x_col:
                sns.histplot(data[x_col], kde=True, color="purple", bins=20)  # Add a nice color and kernel density estimate
                plt.xlabel(x_col)
            else:
                data.hist(color="skyblue", edgecolor="black", grid=False)

        elif plot_type == "Bar Graph":
            if x_col and y_col:
                sns.barplot(x=x_col, y=y_col, data=data, palette="viridis")  # Viridis is a vibrant color palette
            else:
                data.plot(kind='bar', color=sns.color_palette("Set3"))

        plt.title(plot_type, fontsize=16)
        plt.tight_layout()  # Ensure everything fits nicely
        plt.show()

    except Exception as e:
        print(f"Error visualizing data: {e}")
