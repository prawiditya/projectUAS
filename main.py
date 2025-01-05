from rating import Data, Review, Process

def main():
    # Membuat objek Data untuk produk
    product_data = Data("Produk A")

    # Menambahkan beberapa review
    if Process.validate_rating(4):
        Process.add_review(product_data, 4, "Bagus sekali!")
    if Process.validate_rating(5):
        Process.add_review(product_data, 5, "Sangat memuaskan!")
    if Process.validate_rating(3):
        Process.add_review(product_data, 3, "Cukup baik.")

    # Menampilkan semua review
    print(f"Review untuk {product_data.product_name}:")
    for review in product_data.reviews:
        print(f"Rating: {review.rating}, Komentar: {review.comment}")

if __name__ == "__main__":
    main()