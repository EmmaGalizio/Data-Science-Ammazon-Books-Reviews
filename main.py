#Dataset:
# https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews?select=books_data.csv

import pandas as pd


columns_books = ['Title', 'description', 'authors', 'image', 'previewLink', 'publisher', 'publishedDate', 'infoLink',
               'categories', 'ratingsCount']

columns_reviews = ['Id', 'Title', 'Price', 'User_id', 'profileName', 'review/helpfulness', 'review/score', 'review/time',
               'review/summary', 'review/text']


def print_df_stats(df, df_name):
    print("\nDatos de {}".format(df_name))
    print("\nDatos por columna:\n", df.count(), sep="", end="\n\n")
    print("\nDatos faltantes por columna:\n", df.isna().sum(), sep="", end="\n\n")
    print("\n% datos faltantes por columna:\n", df.isna().sum() * 100 / len(df), sep="", end="\n\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')

    print("Cargando libros")
    df_books = pd.read_csv('data/books_data.csv', usecols=columns_books)
    print("Cargando reviews")
    df_reviews = pd.read_csv('data/Books_rating.csv', usecols=columns_reviews)

    print("Descripcion Libros:")
    print(df_books.describe())
    print("\nDescripcion Reviews")
    print(df_reviews.describe())

    df_books_unique = df_books["Title"].drop_duplicates(ignore_index=True)
    df_reviews_unique_book_title = df_reviews["Title"].drop_duplicates(ignore_index=True)


    print_df_stats(df_books, "Dataframe libros")
    print_df_stats(df_reviews, "Dataframe reviews")

    df_books.sort_values(by='Title').to_csv('books_sorted_by_title.csv')
    df_reviews[['Id', 'Title']].value_counts().to_csv('reviews_counts.csv')








