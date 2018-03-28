import pandas as pd
import numpy as np
import time

chicago = 'chicago.csv'
nyu = 'new_york_city.csv'
washington = 'washington.csv'

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n').lower()
    # TODO: handle raw input and complete function
    city_name = ""
    if city.lower() == "chicago":
        city_name = chicago

    elif city.lower() == "new york":
        city_name = nyu

    elif city == "washington":
        city_name = washington

    else:
        print("Invalid Entry..... Kindly re-enter")
        get_city()
    return (city_name)

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns: time_period
    '''
    time_period = input('\nWould you like to filter the data by month, day, or none at'
                        ' all? Type "none" for no time filter.\n')

    if time_period.lower() == "month" or time_period.lower() == "day" or time_period.lower() == "none":
        print("Time Period selected :{}".format(time_period.title()))

    else:
        print("{} is Invalied entry, Kindly re-enter".format(time_period.title()))
        get_time_period()

    return(time_period)


def get_names(gtp,gc):


    if gtp == "month":

            month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
            # TODO: handle raw input and complete function
            if month == "january" or month == "february" or month == "march" or month == "april" or month == "may" or month == "june":
                print("Month selected :{}".format(month.title()))
                df = pd. read_csv(gc)
                df['Start Time'] = pd.to_datetime(df['Start Time'])
                df['months'] = df['Start Time'].dt.month
                mapping = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'}
                df = df.applymap(lambda s: mapping.get(s) if s in mapping else s)
                df = df.loc[df['months'] == month]

                return(df)

            else:
                print("{} is Invalied entry, Kindly re-enter".format(month.title()))
                month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()



    elif gtp == "day":
            month = input('\nWhich day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or saturday?\n').lower()

            if month == "sunday" or month == "monday" or month == "tuesday" or month == "wednesday" or month == "thursday" or month == "friday" or month == "saturday" :
                print("Month selected :{}".format(month.title()))
                df = pd. read_csv(gc)
                df['Start Time'] = pd.to_datetime(df['Start Time'])
                df['Days of week'] = df['Start Time'].dt.dayofweek
                mapping = {0:'monday', 1:'tuesday', 2:'wednesday', 3:'thursday', 4:'friday', 5:'saturday', 6:'sunday'}
                df = df.applymap(lambda s: mapping.get(s) if s in mapping else s)
                df = df.loc[df['Days of week'] == month]

                return(df)

            else:
                print("{} is Invalied entry, Kindly re-enter".format(month.title()))
                month = input('\nWhich day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or saturday?\n').lower()



    elif gtp == "none":
            df = pd.read_csv(gc)
            return(df)


def popular_month(get_city):
    '''Returns: the month with highest no of trips
    Question: What is the most popular month for start time?
    '''
    df = pd. read_csv(get_city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['months'] = df['Start Time'].dt.month
    mapping = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'}
    df = df.applymap(lambda s: mapping.get(s) if s in mapping else s)
    print('Popular month is {} '.format((df['months'].mode()[0])))

def popular_day(get_city):
    '''
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    df = pd. read_csv(get_city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['days of week'] = df['Start Time'].dt.dayofweek
    mapping = {0:'monday', 1:'tuesday', 2:'wednesday', 3:'thursday', 4:'friday', 5:'saturday', 6:'sunday'}
    df = df.applymap(lambda s: mapping.get(s) if s in mapping else s)
    print('Popular day is {} '.format(df['days of week'].mode()[0]))


def popular_hour(df):
    '''
    Question: What is the most popular hour of day for start time?
    '''
    """gets the hour of each datetime object"""
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hours'] = df['Start Time'].dt.hour
    df['hours'] = df['hours'] +1
    print('Popular hour is {}'.format(df['hours'].mode()[0]))

def trip_duration(df):
    '''
    Question: What is the total trip duration and average trip duration?
    time in seconds .filtered dataset.
    '''
    print('Total trip duration {} and average trip duaration {}'.format( df['Trip Duration'].
                                                                        sum(), df['Trip Duration'].mean()))

def popular_stations(df):
    '''
    Question: What is the most popular start station and most popular end station?
    '''

    print('Popular start station is {} \nPopular end station is {}'.format(df['Start Station'].
                                                                           mode()[0], df['End Station'].mode()[0]))

def popular_trip(df):
    '''
    Question: What is the most popular trip?
    '''
    df['pop_sta'] = 'from ' +df['Start Station'].str.cat(' to ' +df['End Station'])
    df['pop_sta'].mode()[0]
    print('Popular trip is {}'.format(df['pop_sta'].mode()[0]))

def users(df):
    '''
    Question: What are the counts of each user type?
    '''
    counts = df['User Type'].value_counts().to_dict()
    print ('The count of each user type is {}'.format(counts))


def gender(df,city_name):
    '''
    Question: What are the counts of gender?
    '''
    if city_name == 'washington.csv':
        return('No data on gender')

    else:
        counts = df['Gender'].value_counts().to_dict()
        print ('The count of gender is {}'.format(counts))


def birth_years(df, city_name):
    '''
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?   '''
    if city_name == 'washington.csv':
        return('No data on birth year')

    else:
        print('The oldest user birth year is {} \nThe youngest user birth year is {} \nThe popular birth year is {}'.
              format(int(df['Birth Year'].max()),int(df['Birth Year'].min()),int(df['Birth Year'].mode()[0])))


def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    gc = get_city()
    while True:
        displayy = input('\nWould you like to view individual trip data?'
                        'Type \'yes\' or \'no\'.\n')
        if displayy == 'no':
            break
        elif displayy == 'yes':
            df1 = pd.read_csv(gc)
            display(df1.head())
        else:
            print ('Type valid input')


def statistics():
    gc = get_city()
    gtt = get_time_period()
    df_filtered = get_names(gtt,gc)

    start_time = time.time()
    popular_month(gc)
    print("That took %s seconds.\n\n" % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()
    gender(df_filtered, gc)
    print("That took %s seconds.\n\n" % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()
    birth_years(df_filtered, gc)
    print("That took %s seconds.\n\n" % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()
    users(df_filtered)
    print("That took %s seconds.\n\n" % (time.time() - start_time))\

    print("Calculating the next statistic...")
    start_time = time.time()
    popular_trip(df_filtered)
    print("That took %s seconds.\n\n" % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()
    popular_stations(df_filtered)
    print("That took %s seconds.\n\n" % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()
    trip_duration(df_filtered)
    print("That took %s seconds.\n\n" % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()
    popular_hour(df_filtered)
    print("That took %s seconds.\n\n" % (time.time() - start_time))

        # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


statistics()

display_data()
