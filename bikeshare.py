import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington).
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please choose from Chicago, New York City, or Washington.")

    while True:
        filter_type = input("Would you like to filter the data by month, day, or not at all? Type 'none' for no time filter. ").lower()
        if filter_type in ['month', 'day', 'none']:
            break
        else:
            print("Invalid input. Please choose 'month', 'day', or 'none'.")

    month = 'all'
    day = 'all'

# Get user input for month if applicable.
    if filter_type == 'month':
        while True:
            month = input("Which month - January, February, March, April, May, or June? ").lower()
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if month in months:
                break
            else:
                print("Invalid input. Please choose a month between January and June.")

    # Get user input for day of week if applicable.
    if filter_type == 'day':
        while True:
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ").lower()
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            if day in days:
                break
            else:
                print("Invalid input. Please choose a day of the week.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour # Extract hour for later use

    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print(f"Most Common Month: {months[common_month-1]}")

    # Display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most Common Day of Week: {common_day}")

    # Display the most common start hour
    common_hour = df['hour'].mode()[0]
    print(f"Most Common Start Hour: {common_hour}:00")

    print(f"\nThis took {(time.time() - start_time):.2f} seconds.")
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"Most Commonly Used Start Station: {common_start_station}")

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"Most Commonly Used End Station: {common_end_station}")

    # Display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print(f"Most Frequent Trip: {common_trip}")

    print(f"\nThis took {(time.time() - start_time):.2f} seconds.")
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    # Convert seconds to days, hours, minutes, seconds for readability
    days = total_travel_time // (24 * 3600)
    total_travel_time = total_travel_time % (24 * 3600)
    hours = total_travel_time // 3600
    total_travel_time %= 3600
    minutes = total_travel_time // 60
    seconds = total_travel_time % 60
    print(f"Total Travel Time: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds.")


    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_minutes = mean_travel_time // 60
    mean_seconds = mean_travel_time % 60
    print(f"Average Travel Time: {int(mean_minutes)} minutes and {int(mean_seconds)} seconds.")

    print(f"\nThis took {(time.time() - start_time):.2f} seconds.")
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of User Types:")
    print(user_types.to_string())

    # Display counts of gender (only available for NYC and Chicago)
    if city != 'washington':
        if 'Gender' in df.columns:
            gender_counts = df['Gender'].value_counts()
            print("\nCounts of Gender:")
            print(gender_counts.to_string())
        else:
            print("\nGender data is not available for this dataset.")
    else:
         print("\nGender data is not available for Washington.")


    # Display earliest, most recent, and most common year of birth (only available for NYC and Chicago)
    if city != 'washington':
        if 'Birth Year' in df.columns:
            earliest_birth_year = df['Birth Year'].min()
            most_recent_birth_year = df['Birth Year'].max()
            common_birth_year = df['Birth Year'].mode()[0]
            print("\nBirth Year Statistics:")
            print(f"Earliest Year of Birth: {int(earliest_birth_year)}")
            print(f"Most Recent Year of Birth: {int(most_recent_birth_year)}")
            print(f"Most Common Year of Birth: {int(common_birth_year)}")
        else:
             print("\nBirth Year data is not available for this dataset.")
    else:
        print("\nBirth Year data is not available for Washington.")


    print(f"\nThis took {(time.time() - start_time):.2f} seconds.")
    print('-'*40)

def display_raw_data(df):
    """Displays 5 rows of raw data upon user request."""
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue seeing 5 more rows? Enter yes or no.\n").lower()
        if view_data != 'yes':
            break
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thank you for using the US Bikeshare Data Explorer!")
            break

        
if __name__ == "__main__":
	main()
