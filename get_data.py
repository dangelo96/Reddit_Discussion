import pandas as pd

from extract import extract_data

if __name__ == "__main__":
    # Extracting data from Reddit
    topics: list = ['datascience', 'MachineLearning', 'music', 'Bitcoin']
    data, labels = extract_data(topics)

    # Creating DataFrame
    df: pd.DataFrame = pd.DataFrame(
        data={
            'data': data,
            'label': labels
        }
    )

    print(df['label'].value_counts())

    # Exporting as csv
    df.to_csv(
        path_or_buf='reddit_data.csv',
        index=False,
        sep=','
    )
