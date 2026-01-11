import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("covid.csv")
summary = df.groupby("Location")[["total_cases","total_deaths"]].max()
summary.head()
india = df[df["Location"]=="India"]
india.tail(1)
plt.plot(india["date"], india["total_deaths"])
plt.xticks(rotation=45)
plt.title("COVID-19 Deaths in India over time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.show()

