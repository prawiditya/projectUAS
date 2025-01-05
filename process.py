from data import Data
from review import Review

class Process:
    @staticmethod
    def validate_rating(rating):
        """Validasi input rating agar antara 1 hingga 5"""
        if rating < 1 or rating > 5:
            print("Rating harus antara 1 hingga 5.")
            return False
        return True
    
    @staticmethod
    def add_review(data, rating, comment):
        """Menambahkan review ke dalam data produk"""
        review = Review(rating, comment)
        data.reviews.append(review)