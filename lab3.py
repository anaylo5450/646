import pandas as pd
import matplotlib.pyplot as plt

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90],
               'Sam': [94, 77, 90], 'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)

# --- Bar plot: Test 2 results per student (style like lab2) ---
# create a plotting function similar to lab2.getBarPlot and call it

def getBarPlot(results):
    """Plot a simple bar chart for a pandas Series where index=labels and values=scores."""
    plt.bar(results.index, results.values)
    plt.xlabel('Student')
    plt.ylabel('Score')
    plt.title('Test 2 Scores')
    plt.ylim(0, 100)
    plt.xticks(rotation=30)
    plt.show()

# extract second test (index 1) and plot per student
test2 = grades.iloc[1]
getBarPlot(test2)   