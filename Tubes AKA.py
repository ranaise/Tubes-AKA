from functools import lru_cache
import sys

sys.setrecursionlimit(10**9)

def dp_bookshelf(books, shelf_width):
    books = tuple(books)

    @lru_cache(None)
    def min_shelves(index, remaining_width):
        if index == len(books):
            return 1
        
        option_new_shelf = 1 + min_shelves(index + 1, shelf_width - books[index])

        option_same_shelf = float('inf')
        if books[index] <= remaining_width:
            option_same_shelf = min_shelves(index + 1, remaining_width - books[index])

        return min(option_new_shelf, option_same_shelf)

    return min_shelves(0, shelf_width)

def ffd_bookshelf(books, shelf_width):
    books.sort(reverse=True)
    shelves = []

    for book in books:
        placed = False
        for shelf in shelves:
            if sum(shelf) + book <= shelf_width:
                shelf.append(book)
                placed = True
                break
        if not placed:
            shelves.append([book])
    
    return len(shelves)


def main():
    print("Program untuk menghitung jumlah rak minimum berdasarkan lebar rak")

    try:
        books = list(map(int, input("Masukkan ukuran buku (dipisahkan dengan spasi): ").split()))
        shelf_width = int(input("Masukkan lebar rak: "))

        if not books or any(book <= 0 for book in books) or shelf_width <= 0:
            print("Ukuran buku dan lebar rak harus positif dan tidak boleh kosong.")
            return

        dp_result = dp_bookshelf(books, shelf_width)

        ffd_result = ffd_bookshelf(books, shelf_width)

        print(f"\nHasil:")
        print(f"Jumlah rak minimum (Dynamic Programming): {dp_result}")
        print(f"Jumlah rak minimum (First-Fit Decreasing): {ffd_result}")
    except ValueError:
        print("Masukan tidak valid. Pastikan ukuran buku dan lebar rak berupa bilangan bulat positif.")

if __name__ == "__main__":
    main()
