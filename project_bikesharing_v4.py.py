import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():

    """
    Asks users to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    # TO DO: get users input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the city you want see data for chicago , new_york_city or washington : ')
    city = city.lower()
    while city not in CITY_DATA:
        city = input('Invalid city name. Please Try Again!')
        city = city.lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Enter the month from january to june OR Enter "all" for no month filter : ')
    month = month.lower()
    while month not in months:
        month = input('Invalid month name. Please Try Again!')
        month = month.lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Enter the day from monday to sunday OR Enter "all" for no day filter : ')
    day = day.lower()
    while day not in days:
        day = input('Invalid day name.Please Try Again!')
        day = day.lower()  
        
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

    df = pd.read_csv(CITY_DATA[city])


    df.head()


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df.head()


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df.head()


    # filter by month if applicable
    if month != 'all':
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


    # filter by month to create the new dataframe
    print(month)
    if month != 'all':
        df = df[df['month'] == month]
    df.head()


    # Filtering by day of week to create the new dataframe
    print(day)
    if day != 'all':
        df = df[df['day'] == day.title()]
    df.head()


    df.info()


    df.head()
    
    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    common_month = df['month'].value_counts()
    print(common_month)


    # Converting the day column to string.
    df['day'] = df['day'].astype(str)


    # TO DO: display the most common day of week
    common_day = df['day'].value_counts()
    print(common_day)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station
    print('Most Popular Start Station: ', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('Most Popular End Station: ', df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost Frequent Combination of Start and End Station Trips:\n\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # TO DO: display total travel time
    df.groupby(['End Station'])['Trip Duration'].sum()


    # TO DO: display mean travel time
    df.groupby(['End Station'])['Trip Duration'].mean()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of user types
    count_types = df['User Type'].value_counts()
    print(count_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print(count_gender)
    else: print('\n washington dataset does not have Gender data included.')


    # TO DO: Display earliest year of birth
    if 'Birth Year' in df.columns:
        min_birth_year = df['Birth Year'].min()
        print(min_birth_year)
    else: print('\n washington dataset does not have Birth Year data included.')


    # TO DO: Display most recent year of birth
    if 'Birth Year' in df.columns:
        max_birth_year = df['Birth Year'].max()
        print(max_birth_year)
    else: print('\n washington dataset does not have Birth Year data included.')


    # TO DO: Display most common year of birth
    if 'Birth Year' in df.columns:
        common_birth_year = df['Birth Year'].mode()
        print(common_birth_year)
    else: print('\n washington dataset does not have Birth Year data included.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):

    """Displays 5 rows of raw data to the user."""
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        
    while view_data.lower() not in enter:
        view_data = input('Please Enter Yes or No:\n')
        view_data = view_data.lower()
    n = 0        
    while True :
        if view_data.lower() == 'yes':
        
            print(df.iloc[n : n + 5])
            n += 5
            view_data = input('\nWould you like to see more data? (Type:Yes/No).\n')
            while view_data.lower() not in enter:
                view_data = input('Please Enter Yes or No:\n')
                view_data = view_data.lower()
    
    return df

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Good Bye!')
            break
            


if __name__ == "__main__":
    main()

