from main import general_describe, general_plots, custom_describe, save_to_markdown

csv1 = "salaries.csv"
csv2 = "players.csv"

def test_general_describe():
    describe_test = general_describe(csv1)
    print(describe_test.shape)
    #assert describe_test.shape == (8, 2)
    
def test_custom_describe():
    describe_test = general_describe(csv1)
    custom_test = custom_describe(csv1, "salary")
    assert describe_test.loc["mean", "salary"] == custom_test["mean"]
    assert describe_test.loc["std", "salary"] == custom_test["std"]
    assert describe_test.loc["25%", "salary"] == custom_test["25 quantile"]

def test_markdown():
    """converts to markdown()"""
    save_to_markdown(csv1, csv2)
    
if __name__ == "__main__":
    test_general_describe()
    test_custom_describe()
    test_markdown()
