# Netflix Viewing Data Analysis

## Overview

This project involves analyzing my personal Netflix viewing data to uncover actionable insights and viewing trends. By leveraging Python's powerful data manipulation and visualization libraries, I explored patterns in my viewing habits, identified favorite shows, peak viewing times, and device preferences. The analysis showcases how Python was integral in transforming raw data into meaningful information.

## Dataset Description

The dataset consists of my Netflix viewing activity, which includes the following columns:

- **Profile Name**: Name of the profile used during viewing.
- **Start Time**: Timestamp when the viewing session started.
- **Duration**: Length of the viewing session.
- **Attributes**: Additional information about the viewing session (e.g., autoplayed, user interaction).
- **Title**: Title of the content watched.
- **Supplemental Video Type**: Type of supplemental content (if any).
- **Device Type**: Device used for viewing.
- **Bookmark**: Timestamp of the last viewed point in the content.
- **Latest Bookmark**: Indicator if the bookmark is the latest.
- **Country**: Country where the viewing took place.

## Analysis Overview

The analysis was conducted using Python, primarily utilizing the `pandas` and `matplotlib` libraries. The key steps included:

1. **Data Loading and Preparation**:
   - Imported the CSV file containing the viewing activity.
   - Converted data types for accurate analysis (e.g., parsing dates and durations).
   - Handled missing or invalid data.

2. **Data Transformation**:
   - Extracted additional time-related features (e.g., date, hour) from the `Start Time`.
   - Calculated total and average viewing durations.

3. **Exploratory Data Analysis (EDA)**:
   - **Viewing Activity per Profile**: Assessed the number of sessions and total watch time per profile.
   - **Content Analysis**: Identified the most-watched shows overall and per profile.
   - **Device Usage**: Analyzed the devices most frequently used for streaming.
   - **Temporal Patterns**: Explored viewing habits over different days and hours to find peak times.

4. **Visualization**:
   - Created bar charts and line graphs to represent data visually.
   - Utilized horizontal bar charts for readability of show titles.
   - Applied appropriate labels, titles, and layouts for clarity.

## Python Code

Below is the Python code used for the analysis:

```python
# Imports
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('ViewingActivity.csv')

# Shape to get the size of data csv
print("DataFrame shape:", df.shape)

# Print first five rows
print(df.head())

# Now let's get some random rows
print(df.sample(n=10))

# Getting unique profile names
print("Unique profile names:", df["Profile Name"].unique())

# Getting unique device types
print("Unique device types:", df["Device Type"].unique())

# Transforming Data
# Convert 'Start Time' to datetime and 'Duration' to timedelta
df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True, errors='coerce')
df['Duration'] = pd.to_timedelta(df['Duration'], errors='coerce')

# Drop rows with invalid 'Start Time' or 'Duration'
df.dropna(subset=['Start Time', 'Duration'], inplace=True)

# Extract 'Date' and 'Hour' for time-based analysis
df['Date'] = df['Start Time'].dt.date
df['Hour'] = df['Start Time'].dt.hour

# Viewing counts per profile
profile_counts = df["Profile Name"].value_counts()
print("Viewing counts per profile:\n", profile_counts)

# Plotting the number of views per profile
profile_counts.plot(kind='bar', title='Number of Views per Profile')
plt.xlabel('Profile Name')
plt.ylabel('Number of Views')
plt.tight_layout()
plt.show()

# Total watch time per profile
total_watch_time = df.groupby('Profile Name')['Duration'].sum()
print("Total watch time per profile:\n", total_watch_time)

# Convert total watch time to hours for easier interpretation
total_watch_time_hours = total_watch_time / pd.Timedelta(hours=1)
print("Total watch time per profile (in hours):\n", total_watch_time_hours)

# Plotting total watch time per profile
total_watch_time_hours.plot(kind='bar', title='Total Watch Time per Profile (Hours)')
plt.xlabel('Profile Name')
plt.ylabel('Total Watch Time (Hours)')
plt.tight_layout()
plt.show()

# Average watch time per session per profile
average_watch_time = df.groupby('Profile Name')['Duration'].mean()
average_watch_time_minutes = average_watch_time / pd.Timedelta(minutes=1)
print("Average watch time per session per profile (in minutes):\n", average_watch_time_minutes)

# Analyzing the most watched shows
# Total duration watched per show
show_watch_time = df.groupby('Title')['Duration'].sum().sort_values(ascending=False)
print("Total duration watched per show:\n", show_watch_time)

# Top 10 most watched shows
top_10_shows = show_watch_time.head(10)

# Plotting the top 10 most watched shows
top_10_shows_hours = top_10_shows / pd.Timedelta(hours=1)
top_10_shows_hours.plot(kind='barh', figsize=(10, 6), title='Top 10 Most Watched Shows (Hours)')
plt.xlabel('Total Watch Time (Hours)')
plt.ylabel('Show Title')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Most watched shows per profile
profile_show_watch_time = df.groupby(['Profile Name', 'Title'])['Duration'].sum()

# Example: Shows most watched by each profile
profiles = df['Profile Name'].unique()
for profile in profiles:
    profile_shows = profile_show_watch_time[profile].sort_values(ascending=False).head(5)
    print(f"\nTop 5 shows watched by {profile}:\n", profile_shows)
    
    # Visualizing the profile's top 5 shows
    profile_shows_hours = profile_shows / pd.Timedelta(hours=1)
    profile_shows_hours.plot(kind='barh', figsize=(8, 4), title=f"{profile}'s Top 5 Shows (Hours)")
    plt.xlabel('Total Watch Time (Hours)')
    plt.ylabel('Show Title')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

# Analyzing device usage per profile
device_usage = df.groupby('Profile Name')['Device Type'].value_counts()
print("\nDevice usage per profile:\n", device_usage)

# Visualizing device usage per profile
for profile in profiles:
    profile_device_usage = df[df['Profile Name'] == profile]['Device Type'].value_counts()
    print(f"\nDevice usage for {profile}:\n", profile_device_usage)
    
    # Plotting device usage for the profile
    profile_device_usage.plot(kind='bar', figsize=(8, 4), title=f"{profile}'s Device Usage")
    plt.xlabel('Device Type')
    plt.ylabel('Number of Views')
    plt.tight_layout()
    plt.show()

# Analyzing viewing habits over time
# Number of views per day
views_per_day = df.groupby('Date').size()
print("\nNumber of views per day:\n", views_per_day)

# Plotting number of views over time
views_per_day.plot(kind='line', figsize=(12, 6), marker='o', title='Number of Views Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Views')
plt.tight_layout()
plt.show()

# Total watch time per day
watch_time_per_day = df.groupby('Date')['Duration'].sum()
watch_time_per_day_hours = watch_time_per_day / pd.Timedelta(hours=1)

# Plotting total watch time over time
watch_time_per_day_hours.plot(kind='line', figsize=(12, 6), marker='o', title='Total Watch Time Over Time (Hours)')
plt.xlabel('Date')
plt.ylabel('Total Watch Time (Hours)')
plt.tight_layout()
plt.show()

# Peak viewing hours
views_per_hour = df.groupby('Hour').size()
print("\nNumber of views per hour:\n", views_per_hour)

# Plotting number of views per hour
views_per_hour.plot(kind='bar', figsize=(10, 6), title='Number of Views per Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Views')
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()
