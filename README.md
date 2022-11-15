# Hadoop-map-reduce

Input: yelp_business.csv on Kaggle <br>
Environment: ubuntu Linux <br>
Tool: Docker <br>
Jar: hadoop-streaming-3.0.0.jar <br>

## A. Computation of n-grams distribution
Output the occurrences of each n-bigram

## B. Distributed Computation of business popularity by day of the week
Compute the aggregated number of checkins per day of the week for each business

## C. Distributed Construction of an Inverted Index 
In information retrieval, an inverted index is an index data structure that stores a mapping from words to a collection of documents that they appear in. An inverted index is a dictionary where each category is associated with a list of the business ids that belong to that category. <br>
Example: <br>
Business 1 --> bakeries; bagels; food <br>
Business 2 --> bakeries; bagels <br>

Reverted Index: <br>
bakeries  --> business 1; Business 2 <br>
bagels    --> business 1; Business 2 <br>
food      --> business 1 <br>
