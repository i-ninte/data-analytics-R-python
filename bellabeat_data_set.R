# importing dataset
library(readr)
daily_activity_merged<-read_csv("Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv")

#viewing dataset
View(daily_activity_merged)

head(daily_activity_merged)
str(daily_activity_merged)