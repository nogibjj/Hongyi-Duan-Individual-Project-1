from lib import (
    load_data,
    get_mean,
    get_median,
    get_std,
    get_quantile,
    plot_bar,
    plot_hist,
    plot_lines
)

def general_describe(csv):
    general_df = load_data(csv)
    return general_df[['salary', 'season_start']].describe()

def custom_describe(csv, col):
    general_df = load_data(csv)
    describe_dict = {
        "name": col,
        "mean": get_mean(general_df, col),
        "std": get_std(general_df, col),
        "median": get_median(general_df, col),
        "25 quantile": get_quantile(general_df, col, 0.25),
    }
    return describe_dict

def general_plots(df1, df2):
    plot_hist(df1)
    plot_lines(df2)
    plot_bar(df2)

def save_to_markdown(csv1, csv2):
    df1 = load_data(csv1)
    df2 = load_data(csv2)
    describe_df = general_describe(csv1)
    markdown_table = describe_df.to_markdown()
    general_plots(df1, df2)
    # Write the markdown table to a file
    with open("NBA_Data_Summary.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table)
        file.write("\n\n")  
        file.write("![congress_viz](Career_Salary_of_NBA_Players.png)\n")
        file.write("\n\n")  
        file.write("![congress_viz2](Career_Data_of_NBA_Players.png)\n")
        file.write("\n\n")  
        file.write("![congress_viz3](Career_WS_Data_of_NBA_Players.png)\n")