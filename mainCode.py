import pandas as pd
import matplotlib.pyplot as plt
csv_in_use = "children-born-per-woman.csv"


def read_fetrtility():
    '''
    reads Retirement_Age.csv file and parses the year column as a date and sets it as an index
    '''
    #GET RID OF HARDCODED PATH
    fertility_df = pd.read_csv(csv_in_use, parse_dates=['Year'])

    return fertility_df

fertility_df = read_fetrtility()


#maybe pass top function into this func???
def get_spanish_fertility():

    spain_fertility_df= fertility_df[fertility_df['Entity'] == 'Spain'].copy()
 
    return spain_fertility_df

spain_fertility_df = get_spanish_fertility()

print(spain_fertility_df)

def plot_fertility_women_graph():
#plotting both OECD women and UK same graph
    plot_fertility_graph= spain_fertility_df.plot(kind='line',y="Fertility rate (period), historical", label='Fertility rate (period), historical',  linestyle='-')
    plot_fertility_graph.set_title("Fertility rate in Spain  (1970-2018)")
    plt.show()

# fertility_graph = plot_fertility_women_graph()

x = spain_fertility_df["Year"]
y = spain_fertility_df["Fertility rate (period), historical"]
