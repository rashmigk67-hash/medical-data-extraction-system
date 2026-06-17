import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/extracted_data.csv")

print("Total Patients:", len(df))

print("\nDisease Count:")
print(df["Disease"].value_counts())

print("\nAverage Age:", round(df["Age"].mean(), 2))

df["Disease"].value_counts().plot(kind="bar")

plt.title("Disease Distribution")
plt.xlabel("Disease")
plt.ylabel("Number of Patients")

plt.savefig("output/disease_distribution.png")

plt.show()