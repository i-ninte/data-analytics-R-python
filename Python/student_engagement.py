import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the DataFrame
# Replace 'your_data.csv' with the actual data file path
df = pd.read_csv('your_data.csv')

# Convert date columns to datetime objects if they're not already
df['course_start_date'] = pd.to_datetime(df['course_start_date'])
df['course_end_date'] = pd.to_datetime(df['course_end_date'])
df['enrollment_date'] = pd.to_datetime(df['enrollment_date'])


df.shape
df.isnull().sum()
df= df.fillna(0)
df.describe()
df.info()

# Calculate student engagement score (example: the sum of forum posts, forum replies, and forum likes)
df['engagement_score'] = df['forum posts'] + df['forum replies'] + df['forum likes']

# 1. How student engagement affects overall performance
# You can analyze the correlation between engagement_score and other performance metrics like assignment_score, quiz_scores, etc.
engagement_vs_performance = df[['engagement_score', 'assignment_score', 'quiz_scores', 'course_completion']].corr()

# 2. Correlation plot between all numeric columns
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Plot')
plt.show()

# 3. Course with the highest average passing rate and relation to student engagement
highest_passing_rate_course = df.groupby('course_name')['course_completion'].mean().idxmax()
avg_passing_rate = df.groupby('course_name')['course_completion'].mean().max()
engagement_for_highest_passing_rate_course = df[df['course_name'] == highest_passing_rate_course]['engagement_score'].mean()

# 4. How time spent on course materials affects quiz and assignment scores
# You can analyze the correlation between time_spent_on_course_materials and assignment_score/quiz_scores.
time_vs_scores = df[['time_spent_on_course_materials', 'assignment_score', 'quiz_scores']].corr()

# 5. How time spent on course materials contributes to course completion
# You can analyze the correlation between time_spent_on_course_materials and course_completion.
time_vs_completion = df[['time_spent_on_course_materials', 'course_completion']].corr()

# 6. How student engagement contributes to course completion
# You can analyze the correlation between engagement_score and course_completion.

# Print the results
print("1. How student engagement affects other overall performance:")
print(engagement_vs_performance)

print("\n3. Course with the highest average passing rate:")
print("Course Name:", highest_passing_rate_course)
print("Average Passing Rate:", avg_passing_rate)
print("Engagement Score for this Course:", engagement_for_highest_passing_rate_course)

print("\n4. How time spent on course materials affects quiz and assignment scores:")
print(time_vs_scores)

print("\n5. How time spent on course materials contributes to course completion:")
print(time_vs_completion)


