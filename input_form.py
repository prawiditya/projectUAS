from rating import Data, Process

def input_review():
    product_name = input("Masukkan nama produk: ")
    product_data = Data(product_name)

    while True:
        try:
            rating = int(input("Masukkan rating (1-5): "))
            if not Process.validate_rating(rating):
                continue
            comment = input("Masukkan komentar: ")
            Process.add_review(product_data, rating, comment)
        except ValueError:
            print("Rating harus berupa angka antara 1 hingga 5.")
            continue

        more = input("Apakah Anda ingin menambahkan review lain? (y/n): ")
        if more.lower() != 'y':
            break

    print(f"\nReview untuk {product_data.product_name}:")
    for review in product_data.reviews:
        print(f"Rating: {review.rating}, Komentar: {review.comment}")

if __name__ == "__main__":
    input_review()