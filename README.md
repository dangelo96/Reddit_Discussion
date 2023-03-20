# Reddit Discussion
A NLP project developed to automatically classify a Reddit discussion, given some topics. It contains from data extraction to model evaluation.

## Tools

* re (built-in)
* Numpy and Scipy
* Pandas
* Matplotlib, Seaborn
* Scikit-Learn
* NLTK and spaCy

## Data Extraction

* Used the existent Reddit API for scrapping data.
* Used the topics 'r/datascience', 'r/MachineLearning', 'r/music' and 'r/Bitcoin' in this project.
* Data were evaluated with more than 100 chars, in order to get only meaningful posts.
* Scripts used: `extract.py`, `get_data.py` and `utils.py`. 
* Data actually used in this experiment: `reddit_data.csv`.

For the project itself, please read `Reddit_Discussion.ipynb`.
