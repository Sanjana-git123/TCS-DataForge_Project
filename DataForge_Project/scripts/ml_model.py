import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

# Read dataset
df = pd.read_csv(
    "D:/DataForge_Project/dataset/Sample - Superstore.csv",
    encoding='latin1'
)

# Select Sales column
X = df[['Sales']]

# KMeans
kmeans = KMeans(n_clusters=3, random_state=42)

df['Customer_Segment'] = kmeans.fit_predict(X)

print(df[['Sales','Customer_Segment']].head())

# Plot graph
plt.figure()
plt.scatter(df.index, df['Sales'], c=df['Customer_Segment'])

plt.xlabel("Customers")
plt.ylabel("Sales")

# Save in screenshots folder
save_path = os.path.join(
    "D:/DataForge_Project",
    "screenshots",
    "customer_segments.png"
)

plt.savefig(save_path)

print("Saved at:", save_path)