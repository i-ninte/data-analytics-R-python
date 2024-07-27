# Install required packages
install.packages("DataExplorer")
install.packages("rmarkdown")
install.packages("readr")

# Load the libraries
library(DataExplorer)
library(rmarkdown)
library(readr)

# Read the data
data <- read_csv("Student_Performance.csv")

# Create a DataExplorer report
report <- DataExplorer::create_report(data, output_file = "student_performance.html")

# Create an RMarkdown file for the report
rmd_content <- "
---
title: 'DataExplorer Report'
output:
  pdf_document:
    latex_engine: xelatex
---

<iframe src='student_performance.html' width='100%' height='800'></iframe>
"

# Write the RMarkdown content to a file
writeLines(rmd_content, con = "report.Rmd")

# Render the RMarkdown file to PDF
render("report.Rmd")

