# AI & NLP Based Customer Review Analysis

## Overview

This project demonstrates the application of AI and NLP (Natural Language Processing) techniques to analyze a comprehensive dataset of customer reviews. The primary goal is to extract meaningful insights and summarize key themes from the reviews, with a particular focus on comprehending customer sentiments across various Starbucks locations.

## Objectives

- Apply AI summarization to extract key points from large sets of textual data.
- Utilize NLP techniques to preprocess and analyze customer reviews.
- Present findings in a clear and actionable manner for business insights.

## Key Features

* **Data Anonymization:** To safeguard privacy, sensitive information within reviews is anonymized.
* **Exploratory Data Analysis (EDA):** EDA provides valuable insights into the distribution and trends of customer ratings over time.
* **Review Summarization:** Leveraging OpenAI's GPT-3, the project generates concise summaries of customer reviews, highlighting key issues in negative reviews and top praised aspects in positive reviews.
* **Data Visualization:** Data visualization techniques are employed to enhance understanding of the underlying trends and patterns.
* **Text Preprocessing:** Text preprocessing steps, including converting to lowercase, removing punctuation, eliminating stopwords, and lemmatizing words, are applied to clean and normalize the review text, improving its suitability for analysis.

## Getting Started

### Prerequisites

To effectively run the project, ensure you have the following prerequisites installed:

* Python 3.x
* Jupyter Notebook
* Essential Python libraries: pandas, matplotlib, seaborn, openai, nltk (including word_tokenize, stopwords, and WordNetLemmatizer)

### Installation

1. Clone the repository to your local machine:

git clone https://github.com/suhedayldrm/AI_WEB_Emo.git

2. Navigate to the project directory and install the required Python packages:

>cd AI_NLP_Review_Analysis
pip install -r requirements.txt

## Downloading the Dataset

The dataset for this project is sourced from Kaggle. You can download it from the following link:
https://www.kaggle.com/datasets/harshalhonde/starbucks-reviews-dataset

## Running the Notebook

To launch the analysis, utilize Jupyter Notebook:

Navigate to 'scripts/Review_Summarization_with_NLP.ipynb' and execute the cells to witness the analysis in action.

## Contributing

Contributions, issues, and feature requests are warmly welcomed. Feel free to check the issues page if you're keen on contributing.

## Project Structure and Directory Organization

The project is structured into the following directories:

* **scripts:** Houses the scripts for data cleaning, preprocessing, anonymization, and review summarization

## Additional Notes and Considerations

* The project utilizes OpenAI's GPT-3 API for review summarization. Ensure you have an OpenAI API key and set it in the relevant script before running the summarization process.
* The project provides a comprehensive example of applying AI and NLP techniques to analyze customer reviews. The provided scripts can be adapted and extended to analyze other review datasets and perform additional analysis tasks.


