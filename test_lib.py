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

csv1 = "salaries.csv"
csv2 = "players.csv"

def test_load():
    df_salary = load_data(csv1)
    df_data = load_data(csv2)
    assert df_salary is not None
    assert df_data is not None
    
def test_stats():
    df_salary = load_data(csv1)
    mean_test = get_mean(df_salary, "salary")
    quantile_test = get_quantile(df_salary, "salary", 0.75)
    median_test = get_median(df_salary, "salary")
    std_test = get_std(df_salary, "salary")
    describe_test = df_salary.describe()
    assert describe_test.loc["mean", "salary"] == mean_test
    assert describe_test.loc["std", "salary"] == std_test
    assert describe_test.loc["75%", "salary"] == quantile_test
    assert 1500000 == median_test
    
if __name__ == "__main__":
    test_load()
    test_stats()