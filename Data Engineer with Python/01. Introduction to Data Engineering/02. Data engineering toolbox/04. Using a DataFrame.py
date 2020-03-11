'''
Using a DataFrame
In the previous exercise, you saw how to split up a task and use the low-level python multiprocessing.Pool API to do calculations on several processing units.

It's essential to understand this on a lower level, but in reality, you'll never use this kind of APIs. A more convenient way to parallelize an apply over several groups is using the dask framework and its abstraction of the pandas DataFrame, for example.

The pandas DataFrame, athlete_events, is available in your workspace.

Instructions 1/2
50 XP
1
Create 4 partitions of the athletes_events DataFrame using dd.from_pandas().
If you forgot the parameters of dd.from_pandas(), check out the slides again, or type help(dd.from_pandas) in the console!

2
Print out the mean age for each Year. Remember dask uses lazy evaluation.
'''
SOLUTION

1
import dask.dataframe as dd

# Set the number of partitions
athlete_events_dask = dd.from_pandas(athlete_events, npartitions = 4)

2
import dask.dataframe as dd

# Set the number of pratitions
athlete_events_dask = dd.from_pandas(athlete_events, npartitions = 4)

# Calculate the mean Age per Year
print(athlete_events_dask.groupby('Year').Age.mean().compute())