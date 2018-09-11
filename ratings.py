"""Restaurant rating lister."""
scores_file = open("scores.txt")




def read_ratings(filename):

    """ Reads the ratings from the file"""

    ratings = {}

    for eachline in scores_file:
        eachline = eachline.rstrip()
        restaurant, rating = eachline.split(":")

        ratings[restaurant] = rating

    return ratings #returns dictionary


def sort_by_name(ratings):       
    sorted_by_name = sorted(ratings.items())
    for eachname in sorted_by_name:
        print("{} is rated a {}.".format(eachname[0], eachname[1]))
# read_ratings(scores_file)


def add_name_score(ratings):

    name = input("Enter a restaurant name: ")
    score = input("Enter a rating: ")

    ratings[name] = score


ratings = read_ratings(scores_file)

print(add_name_score(ratings))
sort_by_name(ratings)
# put your code here
