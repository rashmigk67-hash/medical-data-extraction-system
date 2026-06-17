import os
import re
import pandas as pd

records = []

folder = "reports"

for filename in os.listdir(folder):

    filepath = os.path.join(folder, filename)

    with open(filepath, "r") as file:
        text = file.read()

    name = re.search(r"Patient Name:\s*(.*)", text)
    age = re.search(r"Age:\s*(\d+)", text)
    gender = re.search(r"Gender:\s*(.*)", text)
    disease = re.search(r"Disease:\s*(.*)", text)
    medicine = re.search(r"Medicine:\s*(.*)", text)
    doctor = re.search(r"Doctor:\s*(.*)", text)

    records.append({
        "Name": name.group(1),
        "Age": age.group(1),
        "Gender": gender.group(1),
        "Disease": disease.group(1),
        "Medicine": medicine.group(1),
        "Doctor": doctor.group(1)
    })

df = pd.DataFrame(records)

df.to_csv("output/extracted_data.csv", index=False)

print(df)
print("\nData extracted successfully!")