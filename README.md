# US Bikeshare Data Exploration

## Project Overview

This project involves analyzing bikeshare data from three major US cities: Chicago, New York City, and Washington, DC. The goal is to uncover usage patterns by computing various descriptive statistics. The script provides an interactive cmd interface for users to specify the city and filters (month and/or day of the week) for which they want to see data.

## Datasets

The three data files used are:
* `chicago.csv`
* `new_york_city.csv`
* `washington.csv`

All three data files contain the following core six columns:
1.  **Start Time** (e.g., 2017-01-01 00:07:57)
2.  **End Time** (e.g., 2017-01-01 00:20:53)
3.  **Trip Duration** (in seconds - e.g., 776)
4.  **Start Station** (e.g., Broadway & Barry Ave)
5.  **End Station** (e.g., Sedgwick St & North Ave)
6.  **User Type** (Subscriber or Customer)


The Chicago and New York City files also include:
7.  **Gender**
8.  **Birth Year**

## Statistics Computed

The script calculates and displays the following information based on the user's selected filters:

1.  **Popular Times of Travel:**
    * Most common month
    * Most common day of week
    * Most common start hour of day

2.  **Popular Stations and Trip:**
    * Most common start station
    * Most common end station
    * Most common trip (combination of start and end station)

3.  **Trip Duration:**
    * Total travel time
    * Average travel time

4.  **User Info:**
    * Counts of each user type
    * Counts of each gender (only for NYC and Chicago)
    * Earliest, most recent, and most common year of birth (only for NYC and Chicago)

## How to Run the Script

1.  Ensure you have Python installed on your system.
2.  Make sure the following Python libraries are installed:
    * pandas
    * numpy
    You can install them using pip:
    ```bash
    pip install pandas numpy
    ```
3.  Place the `bikeshare.py` script in the same directory as the city data files (`chicago.csv`, `new_york_city.csv`, `washington.csv`).
4.  Open your terminal or command prompt, navigate to the directory where you saved the files, and run the script using:
    ```bash
    python bikeshare.py
    ```
5.  Follow the on-screen prompts to select a city and apply filters.

## Interactive Experience

The script offers an interactive experience:

1.  **City Selection:** Prompts the user to choose data for Chicago, New York City, or Washington.
2.  **Filter Selection:** Asks if the user wants to filter data by month, day, or not at all.
    * **Month Filter:** If chosen, prompts for the month (January to June).
    * **Day Filter:** If chosen, prompts for the day of the week (Monday to Sunday).
3.  **Data Display:** After processing, the script displays the computed statistics.
4.  **Raw Data View:** Prompts the user if they want to see 5 rows of the filtered data. If 'yes', it displays 5 rows and asks if they want to see 5 more, continuing until the user enters 'no'.
5.  **Restart:** Asks the user if they would like to restart the analysis or exit.

The script includes input validation to handle common user input errors (e.g., typos, incorrect case).

## File Structure

```text
├── bikeshare.py         # The main Python script
├── chicago.csv          # Dataset for Chicago
├── new_york_city.csv    # Dataset for New York City
└── washington.csv       # Dataset for Washington
```

## Dependencies

* Python 3.x
* pandas
* numpy

## Testing

The script's input handling has been designed to be robust. Test scenarios covering various user inputs (valid, invalid, edge cases) have been documented separately to ensure the script functions correctly under different conditions. (Refer to `bikeshare_test_scenarios.md` for details if available in the project repository).

