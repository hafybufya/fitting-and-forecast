
# Importing functions used in the program

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy as np

# ---------------------------------------------------------------------
# Defined CSV file name and column used in program
#  -> make the code flexible if used dataset changed
#  -> or to reuse the same function for a different file.
# ---------------------------------------------------------------------

csv_in_use = "children-born-per-woman.csv"
x_axis = "Year"
y_axis = "Fertility rate (period), historical"


def read_fertility():
    
    """

    Loads the fertility dataset definied in 'csv_in_use'

    Notes:
    -> Year column is not parsed as a date to allow for scatterfit graphs

    Returns:
    pandas Dataframe -> converts csv to df containing fertility data

    """

    fertility_df = pd.read_csv(csv_in_use, parse_dates=[x_axis])

    return fertility_df

# Calls function so to be used in spanish_fertility()

fertility_df = read_fertility()


#maybe pass top function into this func???
def get_spanish_fertility():
    """

    Filter the fertility dataset to include only Spanish data

    Notes:
    -> Apply a mask to select rows in 'Entity' == 'Spain'
    -> Extract the year as an integer for creation of plots

    Returns:
    pandas Dataframe -> Filtered dataframe containg only Spanish fertility data
                         with the 'Year' column as integers.

    """

    spain_fertility_df= fertility_df[fertility_df['Entity'] == 'Spain'].copy()
  
    # Extract the year as an integer
    spain_fertility_df[x_axis] = spain_fertility_df[x_axis].dt.year

    return spain_fertility_df

spain_fertility_df = get_spanish_fertility()


def plot_prediction_graph(x, y, degree):
    # Convert to numpy arrays
    x = np.array(x)
    y = np.array(y)


    cutoff_year = x.max() - 10

    mask_sample = x <= cutoff_year
    x_sample = x[mask_sample]
    y_sample = y[mask_sample]


    # Perform linear fit
    coefficients = np.polyfit(x, y, degree )
  

    # Create polynomial function
    p = np.poly1d(coefficients)

    plt.scatter(x_sample, y_sample, label='Historial Date')
    plt.plot(x, p(x), label='Polynomial order 6', color='red')
    plt.legend()
    plt.show()
    

def plot_full_graph(x, y, degree ):

    # Perform linear fit
    coefficients = np.polyfit(x, y, degree )
  
    # Create polynomial function
    p = np.poly1d(coefficients)

    plt.scatter(x, y, label='Data Points')
    plt.plot(x, p(x), label='Linear Fit', color='red')
    plt.legend()
    plt.show()


def polynomial_best_fit(x , y, sigma):

   
    degrees = [x for x in np.arange(1, 10.5, 0.5)]

    chi2_list = []

    chi2_reduced_list = []

    for d in degrees:
        # Perform linear fit
        coefficients = np.polyfit(x, y, deg = d )

        # Create polynomial function
        p = np.poly1d(coefficients)
        y_pred = p(x)
        

        chi2 = np.sum(((y - y_pred) / sigma)**2)

        dof = len(x) - (d + 1)

        chi2_reduced = chi2/dof

        chi2_list.append(chi2)
        chi2_reduced_list.append(chi2_reduced)


    plt.plot(degrees, chi2_reduced_list, marker="o")
    plt.xlabel("Polynomial order (n)")
    plt.ylabel("Weighted x**2 per degrees of freedom")
    plt.title("Model comparison by polynomial order ")
    plt.grid(True)
    plt.show()



x = spain_fertility_df[x_axis]
y = spain_fertility_df[y_axis]



if __name__ == "__main__":

    plot_prediction_graph(x, y, degree= 6)

    plot_full_graph(x, y, degree=6)

    polynomial_best_fit(x , y, 0.05*y)

