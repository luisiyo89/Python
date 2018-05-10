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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please enter NY, CH or WSH for New York, Chicago and Washington\n')

        if (city=='NY' or city=='CH' or city=='WSH'):
            print('Thank you for choosing {}.\n'.format(city))
            break
        else:
            print('Please select the appropriate city')


    # TO DO: get user input for month (all, january, february, ... , june)
    months ={1:'January', 2: 'February', 3:'March', 4:'April', 5 :'May', 6: 'June'}

    while True:
        month =int(input("Please choose which month (1-6) you would like more information or 'all' for all months, ex 1 = January\n"))

        try:
            if month in months:
                print('Thank you for your input')
                break
        except ValueError:
                print('Please Retry')

        else:
            print("Please retry")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    weekdays = {1: 'Monday', 2: 'Tuesday', 3 : 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    while True:
        day = int(input('Please choose a day (1-7) you would like more information on and type "weekdays" for the whole week, ex 1 = Monday\n'))

        try:
            if day in weekdays:
                print('Thank you for your input')
                break

        except ValueError:
                print('please retry your input')

        else:
                print("please retry your input")


    print('-'*40)
    return str(city), str(month), str(day)


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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()
    print("Most common month:" + " "+ common_month + "\n")

    # TO DO: display the most common day of week

    common_day = df['day'].mode()
    print("Most common day of the week:" + " "+ common_day + "\n")

    # TO DO: display the most common start hour

    common_start_hour = df['Start Time'].mode()
    print("Common Start Hour:"+" "+ str(common_start_hour)+"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print("Most common Start Station:"+ " " + common_start_station + "\n")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()
    print("Most common End Station:"+" "+ common_end_station +"\n")

    # TO DO: display most frequent combination of start station and end station trip
    print( "Best Start Time CombinationL"+" "+ common_start_station +"--&--"+ common_end_station+ "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Travel Duration'].sum()
    print("Total Travel Time:"+" "+ str(total_travel_time) + "\n")

    # TO DO: display mean travel time
    mean_travel_time = df['Travel Duration'].mean()
    print("Average Travel Time:"+" "+ str(mean_travel_time) + "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print("User Type Count:"+" "+ str(count_user_type) +"\n")


    # TO DO: Display counts of gender

    count_gender = df['Gender'].value_counts()
    print('Gender Count:'+" "+ str(count_gender) + "\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    recent_birth_year = df['Birth Year'].max()


    common_birth_year = df['Birth Year'].mode()

    print("The most recent year of birth is:" + " "+ str(recent_birth_year) + " & " + "the most common year of birth is:"+" "+str(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
