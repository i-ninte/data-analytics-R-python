install.packages("DataExplorer")
library(DataExplorer)
install.packages("rmarkdown")
library(rmarkdown)
sales <- read_csv("sales.csv")
library(readr)
report <- DataExplorer::create_report(sales)

---
  title: "DataExplorer Report"
output:
  pdf_document:
  latex_engine: xelatex
---
  
  <iframe src="your_report.html" width="100%" height="800"></iframe>
  
  render("report.Rmd")


