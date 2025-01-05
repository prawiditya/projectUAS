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

# Class untuk menyimpan data produk dan review
class Data:
    def __init__(self, product_name):
        self.product_name = product_name
        self.reviews = []

# Class untuk menyimpan review dari pengguna
class Review:
    def __init__(self, rating, comment):
        self.rating = rating
        self.comment = comment

# Class untuk memproses data dan review
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

    @staticmethod
    def calculate_average_rating(data):
        """Menghitung rata-rata rating dari semua review"""
        if len(data.reviews) == 0:
            return 0
        total_rating = sum(review.rating for review in data.reviews)
        return total_rating / len(data.reviews)
    
    @staticmethod
    def display_reviews(data):
        """Menampilkan semua review untuk produk"""
        if len(data.reviews) == 0:
            print("Tidak ada review untuk produk ini.")
        else:
            print(f"\nReview untuk produk: {data.product_name}")
            for idx, review in enumerate(data.reviews, start=1):
                print(f"Review {idx}:")
                print(f"Rating: {review.rating}")
                print(f"Komentar: {review.comment}")
                print("-" * 20)

    @staticmethod
    def display_average_rating(data):
        """Menampilkan rata-rata rating produk"""
        average = Process.calculate_average_rating(data)
        print(f"Rata-rata rating untuk produk {data.product_name}: {average:.2f}")

# Fungsi utama untuk menjalankan program
def main():
    print("Selamat datang di sistem review produk!")
    
    # Input nama produk
    product_name = input("Masukkan nama produk: ")
    data = Data(product_name)
    
    # Loop untuk menambahkan review
    while True:
        print("\nTulis review untuk produk ini:")
        
        # Input rating dengan validasi
        while True:
            try:
                rating = int(input("Masukkan rating (1-5): "))
                if Process.validate_rating(rating):
                    break
            except ValueError:
                print("Masukkan angka yang valid untuk rating.")
        
        # Input komentar
        comment = input("Masukkan komentar: ")
        
        # Menambahkan review
        Process.add_review(data, rating, comment)
        
        # Tanya apakah ingin menambah review lagi
        continue_review = input("Apakah Anda ingin menambah review lain? (y/n): ").lower()
        if continue_review != 'y':
            break
    
    # Menampilkan semua review
    Process.display_reviews(data)
    
    # Menampilkan rata-rata rating
    Process.display_average_rating(data)

# Menjalankan program
if __name__ == "__main__":
    main()