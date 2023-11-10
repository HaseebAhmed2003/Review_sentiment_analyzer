# Review_sentiment_analyzer
**Review Analyzer**

**Table of Contents:**
•	Description

•	Installation

•	Usage

•	File Structure

•	Technologies Used

•	Contributing

•	License


**Description:**

The Review Analyzer is a Python project designed to analyze text sentiments and provide insights into the sentiment, polarity, and subjectivity of reviews. It includes two main components:
1.	Analyze Text: Users can input text, and the application will perform sentiment analysis, displaying the polarity, subjectivity, and an overall sentiment classification (Positive, Negative, or Neutral).
2.	Analyze CSV: Users can upload a CSV, Excel, or Parquet file containing a column of reviews. The application processes the reviews, conducts sentiment analysis, and adds columns for polarity, subjectivity, and sentiment to the dataset. Users can then download the analyzed data as a CSV file.

**Installation:**
1.	Clone the repository:
git clone https://github.com/your-username/review-analyzer.git 
2.	Install the required dependencies:
pip install -r requirements.txt

**Usage:**
1.	Run the main.py file:
streamlit run main.py 
2.	Open the provided link in your browser and interact with the web application.

**File Structure:**

•	main.py: The main Streamlit application file.

•	Review_Analyzer.py: Contains functions for text preprocessing, sentiment analysis, and data analysis.

•	requirements.txt: Lists the required Python packages.

**Technologies Used:**

•	Python

•	Streamlit

•	Pandas

•	NLTK

•	TextBlob

****License:****

Distributed under the MIT License. See LICENSE for more information.

