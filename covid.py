import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("covid.csv")
df.columns
total_infected = df["total_cases"].sum()
total_newcases = df["new_cases"].sum()
total_newdeath = df["new_deaths"].sum()
Location = df["Location"]
#print("total infected", total_infected)
#print("total cases", total_newcases)
#print("total deaths", total_newdeath)
summary = pd.DataFrame({
    "total_cases": ["infected","new_cases","death","Location"],
    "people": [total_infected,total_newcases,total_newdeath,Location]
   })
top = summary.sort_values(by="Location",ascending=False).head(10)
top.plot(kind="hist")
plt.title("Top 10 covid Affected location")
plt.ylabel("no of people")
plt.show()
summary.set_index("total_cases").plot(kind='hist')
plt.title("covid-19 cases Summary")
plt.ylabel("number of people")
#plt.show()































