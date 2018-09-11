"""Restaurant rating lister."""
scores_file = open("scores.txt")



def read_ratings(filename):

    """ Creates an empty dictionary called ratings, takes each line
    from the text file one by one, and adds it to the empty dictionary. """

    ratings = {}

    for eachline in scores_file:
        eachline = eachline.rstrip()
        restaurant, rating = eachline.split(":")

        ratings[restaurant] = rating

    return ratings #returns dictionary


def add_name_score(ratings):
    """Takes a name and rating as input from the user, and adds that as a new item
    to the dictionary 'ratings' from read_ratings() function"""

    name = input("Enter a restaurant name: ")
    score = input("Enter a rating: ")

    ratings[name] = score # Adds a new key and value to the dictionary


def sort_by_name(ratings):       
    """Sorts each rating aphabetically by name and prints out each set of restaurants
    and their corresponding ratings. """

    sorted_by_name = sorted(ratings.items())
    for eachname in sorted_by_name:
        print("{} is rated a {}.".format(eachname[0], eachname[1]))
# read_ratings(scores_file)


ratings = read_ratings(scores_file)

add_name_score(ratings)
sort_by_name(ratings)
# put your code here
