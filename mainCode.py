import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
from datetime import date

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
    # Make sure Year is datetime first
    spain_fertility_df["Year"] = pd.to_datetime(spain_fertility_df["Year"], errors="coerce")

    # Extract the year as an integer
    spain_fertility_df["Year"] = spain_fertility_df["Year"].dt.year

    return spain_fertility_df

spain_fertility_df = get_spanish_fertility()


max_year = 2015
mask = spain_fertility_df["Year"] <= max_year

x_poly = spain_fertility_df["Year"]
y_poly = spain_fertility_df["Fertility rate (period), historical"]



x_df = spain_fertility_df.loc[mask, "Year"]
y_df = spain_fertility_df.loc[mask, "Fertility rate (period), historical"]



# Perform linear fit
coefficients = np.polyfit(x_poly, y_poly, deg=10, )
print("Linear Fit Coefficients:", coefficients)

# Create polynomial function
p = np.poly1d(coefficients)

plt.scatter(x_df, y_df, label='Data Points')
plt.plot(x_poly, p(x_poly), label='Linear Fit', color='red')
plt.legend()
plt.errorbar(x_poly, y_poly, yerr=0.05, fmt='o', capsize=4, label="Data with error bars")


# plt.show()

#FIGURE 3
sigma = 0.05 * y_poly


y_pred = p(x_poly)
plt.plot(x_poly, p(x_poly))

#chi Squared calculation
chi_squared = ((y_poly-y_pred)**2)/(sigma**2)
print(chi_squared)