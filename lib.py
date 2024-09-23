import pandas as pd
import matplotlib.pyplot as plt

# load the data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

# data description
def get_mean(df, col):
    return df[col].mean()

def get_median(df, col):
    return df[col].median()

def get_std(df, col):
    return df[col].std()

def get_quantile(df, col, q):
    return df[col].quantile(q)

# data visualization
def plot_hist(df):
    plt.figure(figsize=(15, 9))
    plt.hist(df['salary'], bins = 20, edgecolor="orange")
    plt.title("Salary of NBA Players")
    plt.xlabel("Annual Salary")
    plt.ylabel("Frequency")
    plt.savefig("Career_Salary_of_NBA_Players.png")
    plt.show()
    
def plot_lines(df):
    df[['career_PER', 'career_PTS', 'career_TRB']].plot(kind="line", figsize=(15, 9), colormap="Set1")
    plt.title("Career Data of NBA Players")
    plt.xlabel("Different Players")
    plt.ylabel("Data")
    plt.legend(title=['career_PER', 'career_PTS', 'career_TRB'])
    plt.savefig("Career_Data_of_NBA_Players.png")
    plt.show()
    
def plot_bar(df):
    df[['career_WS']].plot(kind="bar", figsize=(15, 9), width=0.3, colormap="Set1")
    plt.title("Career WS Data of NBA Players")
    plt.ylim(0, 240) 
    plt.xlabel("Different Players")
    plt.ylabel("WS Data")
    plt.legend(title=['career_WS'])
    plt.xticks([])
    plt.savefig("Career_WS_Data_of_NBA_Players.png")
    plt.show()