import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.hist(df['population'], bins=50, color='lightblue')
plt.title('Population Distribution')
plt.show()