# Imports
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\conta\Desktop\Netflixa\CONTENT_INTERACTION\ViewingActivity.csv')

# Transforming Data
# Convert 'Start Time' to datetime and 'Duration' to timedelta
df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True, errors='coerce')
df['Duration'] = pd.to_timedelta(df['Duration'], errors='coerce')

# Drop rows with invalid 'Start Time' or 'Duration'
df = df.dropna(subset=['Start Time', 'Duration'])

# Extract 'Date' and 'Hour' for time-based analysis
df['Date'] = df['Start Time'].dt.date
df['Hour'] = df['Start Time'].dt.hour

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
