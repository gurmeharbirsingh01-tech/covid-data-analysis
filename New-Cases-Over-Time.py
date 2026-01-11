import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("covid.csv")
summary = df.groupby("Location")[["total_cases","total_deaths"]].max()
summary.head()
india = df[df["Location"] == "India"]
plt.plot(india["date"], india["new_cases"])
plt.xticks(india["date"][::30],rotation=45)
plt.title("Daily New COVID-19 Cases in India")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.show()
