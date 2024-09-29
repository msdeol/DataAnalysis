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
