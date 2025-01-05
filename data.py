class Data:
    def __init__(self, product_name):
        self.product_name = product_name
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def average_rating(self):
        if not self.reviews:
            return 0
        total = sum(review.rating for review in self.reviews)
        return total / len(self.reviews)

class Review:
    def __init__(self, rating, comment):
        self.rating = rating
        self.comment = comment