# Sales_and_User_Engagement_project
In this project, I used Python and its libraries (NumPy, Pandas, Matplotlib) to analyze and answer key business questions based on 12 months of sales data from an electronics store. The dataset contains hundreds of thousands of purchase records, including details such as the month of purchase, product type, cost, and purchase address.

## Data Cleaning
We begin by cleaning the data to ensure accurate analysis. Key tasks include:
- Dropping rows with NaN values
- Removing invalid rows based on specific conditions
- Converting column data types using to_numeric, to_datetime, and astype

## Data Exploration
After cleaning, we explore the data to answer five high-level business questions:
- Which month had the highest sales? How much revenue was generated?
- Which city had the most sales?
- What is the optimal time to display advertisements to maximize purchases?
- Which products are sold most frequently?
- Does product price impact the quantity ordered?

## Tools and Techniques
To answer these questions, we use various Pandas and Matplotlib techniques, including:
- Concatenating multiple CSV files using pd.concat
- Creating new columns for additional insights
- Extracting data from strings using .str
- Applying functions across columns with .apply()
- Aggregating and grouping data using groupby
- Visualizing insights through bar charts and line graphs
- Labeling graphs for clear interpretation
