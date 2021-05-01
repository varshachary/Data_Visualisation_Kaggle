"""
setup
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

Step 1: Load the data
Your first assignment is to read the LA Museum Visitors data file into museum_data. Note that:

The filepath to the dataset is stored as museum_filepath. Please do not change the provided value of the filepath.
The name of the column to use as row labels is "Date". (This can be seen in cell A1 when the file is opened in Excel.)
To help with this, you may find it useful to revisit some relevant code from the tutorial, which we have pasted below:

# Path of the file to read
spotify_filepath = "../input/spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)
The code you need to write now looks very similar!
"""
# Path of the file to read
museum_filepath = "../input/museum_visitors.csv"

# Fill in the line below to read the file into a variable museum_data
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)

# Run the line below with no changes to check that you've loaded the data correctly
step_1.check()
# Print the last five rows of the data 
df_last_5 = museum_data.iloc[-5:]
  
# Printing df_last_3
print(df_last_5)# Your code here
"""
Step 3: Convince the museum board
The Firehouse Museum claims they ran an event in 2014 that brought an incredible number of visitors, and that they should get extra budget to run a similar event again. The other museums think these types of events aren't that important, and budgets should be split purely based on recent visitors on an average day.

To show the museum board how the event compared to regular traffic at each museum, create a line chart that shows how the number of visitors to each museum evolved over time. Your figure should have four lines (one for each museum).

(Optional) Note: If you have some prior experience with plotting figures in Python, you might be familiar with the plt.show() command. If you decide to use this command, please place it after the line of code that checks your answer (in this case, place it after step_3.check() below) -- otherwise, the checking code will return an error!

"""
# Set the width and height of the figure
plt.figure(figsize=(12,6))
# Line chart showing the number of visitors to each museum over time
sns.lineplot(data=museum_data)
# Add title
plt.title("Monthly Visitors to Los Angeles City Museums")
# Check your answer
step_3.check()
"""
Step 4: Assess seasonality
When meeting with the employees at Avila Adobe, you hear that one major pain point is that the number of museum visitors varies greatly with the seasons, with low seasons (when the employees are perfectly staffed and happy) and also high seasons (when the employees are understaffed and stressed). You realize that if you can predict these high and low seasons, you can plan ahead to hire some additional seasonal employees to help out with the extra work.

Part A
Create a line chart that shows how the number of visitors to Avila Adobe has evolved over time. (If your code returns an error, the first thing that you should check is that you've spelled the name of the column correctly! You must write the name of the column exactly as it appears in the dataset.)
"""
# Line plot showing the number of visitors to Avila Adobe over time
____ # Your code here
# Set the width and height of the figure
plt.figure(figsize=(12,6))
sns.lineplot(data=museum_data, x="Date", y="Avila Adobe")

# Check your answer
step_4.a.check()
