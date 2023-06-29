# Where I learned to get a specific column from a CSV file: https://www.w3resource.com/python-exercises/csv/python-csv-exercise-7.php
# Where I learned to remove commas from a number while removing the dollar sign at the same time: https://hackernoon.com/how-to-remove-commas-from-string-python
# Where I learned to extract different numbers from a string: https://www.geeksforgeeks.org/python-extract-numbers-from-string/

import requests
import csv
from keys import api_key
import re

def request_movie_data():
    with open('oscar_winners.csv') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            res = requests.get(f"https://www.omdbapi.com/?i={row['IMDB']}&apikey={api_key}")
            data = res.json()
            
            title = str(data['Title'])
            runtime = int(data['Runtime'].strip(" min"))
            genre = str(data['Genre'].split(", "))

            award_numbers = re.findall(r'\d+', data['Awards'])
            award_digits = list(map(int, award_numbers))

            award_wins = int(award_digits[1])
            award_nominations = int(award_digits[2])
            box_office = int(data['BoxOffice'].strip("$").replace(",", ""))
            language = str(data['Language'].split(", "))
            rating = str(data['Rated'])
            country = str(data['Country'].split(", "))

            headers = ['Movie Title', 'Runtime', 'Genre', 'Award Wins', 'Award Nominations', 'Box Office', 'Language', 'Rating', 'Country']
            info_data = [title, runtime, genre, award_wins, award_nominations, box_office, language, rating, country]
            # info = info_data.tolist()

            with open('movies.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                # writer.writerows(info)
                # json.load(info)
                # for row in info:
                # #     writer.writerow(info)
                # for row in info:
                #     writer.writerows(row)

                # writer.writerow(info)
                print(info_data)

request_movie_data()
