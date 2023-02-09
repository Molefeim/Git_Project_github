import time
import pandas as pd
import numpy as np
import pdb
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
     # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Would you like to see data for chicago, new york city or washington:?")
    cityname = input().lower() 
    # get user input for month (all, january, february, ... , june)
    print("Which month:? january, february, march, april, may or june?")
    month = input().lower() 
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print("which day:? monday, tuesday, wednesday, thursday, friday, saturday or sunday")
    day = input().lower()
    return cityname, month, day      

def load_data(city, month=None, day=None):
    if city in CITY_DATA.keys():
        df = pd.read_csv(CITY_DATA[city])
        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_of_week
        try:
            df['day_of_week'] = df['Start Time'].dt.day_of_week
        except:
            df['day_of_week'] = df['Start Time'].dt.weekday
        # extract hour from the Start Time column to create an hour column
        df['hour'] = df['Start Time'].dt.hour

        # filter by month if applicable
        if month != 'all' and month != '':
            # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            # filter by month to create the new dataframe        
            df = df[df['month'] == months.index(month)+1]

            # filter by day of week if applicable
        if day !=  'all' and day != '': 
            # filter by day of week to create the new dataframe
    
            days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        
            df = df[df['day_of_week'] == days.index(day)]   
    else:   
        df = None
        raise Exception('city does not exist: "{}"'.format(city))
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
       
    # find the most popular hour
    popular_month = df['month'].mode()[0]
    print()
    print('The most Popular month:', popular_month)
    print()
    # find the most pular_day_of_week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print()
    print('The Most Popular day_of_week:', popular_day_of_week)
    print()
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print()
    print('Most Popular Start Hour:', popular_hour)
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # find the most commonly used start station
    
    popular_start_station = df['Start Station'].value_counts().index[0]
    print()
    print('The most commonly used start station:', popular_start_station)
    print()
    # find the most commonly used end station
    popular_end_station = df['End Station'].value_counts().index[0]
    print()
    print('The most commonly used end station:', popular_end_station)
    print()
    # find the most frequent combination of start station and end station trip
    station_pairs = df['Start Station'] + ' - ' + df['End Station']
    Frequent_start_end_station = station_pairs.value_counts().index[0]
    print()
    print('The most frequent combination of start station and end station trip:', Frequent_start_end_station)
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # find Total travel time
    total_travel_time = df['Trip Duration'].sum()
    Hrs =int(total_travel_time/60/60)
    remaider_sec =total_travel_time%(60*60)
    Mins = int(remaider_sec/60)
    Sec = remaider_sec%60
    print()
    print("Total travel time:", Hrs, "hrs", Mins, 'mins', Sec, 'sec')
    print()       
    # find Mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    Hrs =int(mean_travel_time/60/60)
    remaider_sec =mean_travel_time%(60*60)
    Mins = int(remaider_sec/60)
    Sec = round(remaider_sec%60, 2)

    print()
    print("Mean travel time:", Hrs, "hrs", Mins, 'mins', Sec, 'sec')
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))    


def user_stats(df):
    """Displays statistics on bikeshare users."""
    try:

        print('\nCalculating User Stats...\n')
        start_time = time.time()
            
        # print value counts for each user type
        user_types = df['User Type'].value_counts()
        print()
        print('Breakdown of User Types:\n',user_types)
        print()

        # print counts_of_gender
        counts_of_gender = df['Gender'].value_counts()
        print()
        print('Counts of gender:\n',counts_of_gender)
        print()
    except KeyError as err:
        print("Column not found in the dataset:", err)
    try:
        # print most_common_year_of_birth
        most_common_year_of_birth = int(df['Birth Year'].value_counts().index[0])
        print()
        print('Most common year of birth:\n',most_common_year_of_birth)
        print()
        print("\nThis took %s seconds." % (time.time() - start_time))
    except KeyError as err:
        print("Column not found in the dataset:", err) 
        
def display_data(df, num_lines=5):

    show = input('Would you like to print {} lines of data?, enter Yes or No\n'.format(num_lines))
    if show.lower() == 'yes':
        first_row = 0
        while True:
    
            last_row = first_row + num_lines
            # print out 5 rows
            if last_row > df.shape[0]:
                last_row = df.shape[0]
            print(df.iloc[first_row:last_row])
            if last_row >= df.shape[0]:
                break
            else:
                first_row = last_row
            show = input('Would you like to print another {} lines of data?, enter Yes or No\n'.format(num_lines))
            if show.lower() != 'yes':
                break

def main():
    print()
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
    while True:
        city, month, day = get_filters()
        df = load_data(city, month=month, day=day)

        time_stats(df)
        print('-'*148)
        station_stats(df)
        print('-'*148)
        trip_duration_stats(df)
        print('-'*148)
        user_stats(df)
        print('-'*148)
        display_data(df, num_lines=5) 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == '__main__':    
    main()    