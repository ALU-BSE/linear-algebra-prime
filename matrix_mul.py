import pandas as pd
import numpy as np

# Load data
# data = pd.read_csv('path/to/data')

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Calculate the result 
Ans = []

for i in range(len(Prices)):
          row_sum = 0 
          for j in range(len(Prices[0])):
                    # Calculate the product and add it to the row_sum
                    row_sum += Prices[i][j] * Array2[j]
                    # Append the row_sum to the Ans list
                    Ans.append(row_sum)

print(Ans)
