import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("covid.csv")
summary = df.groupby("Location")[["total_cases","total_deaths"]].max()
summary.head()
india = df[df["Location"]=="India"]
plt.plot(india["date"], india["total_cases"], label="Total Cases")
plt.plot(india["date"], india["total_deaths"], label="Total Deaths")
plt.xticks(india["date"][::30],rotation=45)
plt.title("Total Cases vs Total Deaths in India")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.show()
