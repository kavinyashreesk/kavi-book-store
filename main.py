class Book:
    def __init__(self, book_id, title, author, price, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        if quantity > 0:
            self.quantity += quantity
            print(f"Added {quantity} copies of '{self.title}'. New Stock: {self.quantity}")
        else:
            print("Quantity to add must be positive.")

    def sell_book(self, quantity):
        if quantity <= 0:
            print("Quantity to sell must be positive.")
        elif quantity > self.quantity:
            print(f"Not enough stock! Only {self.quantity} copies of '{self.title}' available.")
        else:
            self.quantity -= quantity
            print(f"Sold {quantity} copies of '{self.title}'. Remaining Stock: {self.quantity}")

    def display_details(self):
        print(f"[{self.book_id}] {self.title:<22} | Author: {self.author:<10} | ₹{self.price:<5} | Stock: {self.quantity}")


class Cart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.discount_percent = 0

    def add_item(self, book, quantity):
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        if quantity > book.quantity:
            print(f"Cannot add {quantity} copies of '{book.title}'. Only {book.quantity} available.")
            return
        self.items.append((book, quantity))
        print(f"Added {quantity}x '{book.title}' to cart.")

    def apply_discount(self, discount_percent):
        if 0 <= discount_percent <= 100:
            self.discount_percent = discount_percent
            print(f"{discount_percent}% discount applied.")
        else:
            print("Invalid Discount Percentage.")

    def calculate_total(self):
        return sum(book.price * qty for book, qty in self.items)

    def generate_bill(self):
        if not self.items:
            print("Cart is empty! Nothing to bill.")
            return

        line = "=" * 54
        print(f"\n{line}")
        print(f"{'KAVI BOOK STORE':^54}")
        print(f"{line}")
        print(f"Customer : {self.customer_name}")
        print(f"{'-' * 54}")
        print(f"{'Book':<22} {'Qty':>4} {'Rate':>8} {'Amount':>10}")
        print(f"{'-' * 54}")

        subtotal = self.calculate_total()
        for book, qty in self.items:
            amount = book.price * qty
            print(f"{book.title:<22} {qty:>4} {book.price:>8} {amount:>10}")

        print(f"{'-' * 54}")
        print(f"{'Subtotal':<44} ₹{subtotal:>8}")

        if self.discount_percent > 0:
            discount_amount = subtotal * (self.discount_percent / 100)
            final_amount = subtotal - discount_amount
            print(f"{f'Discount ({self.discount_percent}%)':<44} -₹{discount_amount:>7.2f}")
            print(f"{'Amount Payable':<44} ₹{final_amount:>8.2f}")
        else:
            print(f"{'Amount Payable':<44} ₹{subtotal:>8}")

        print(f"{line}")
        print("Updating Stock...")
        for book, qty in self.items:
            book.sell_book(qty)
        print("Order Completed Successfully!")
        print(f"{line}\n")


books = [
    Book(101, "Python Programming", "Deepak", 400, 500),
    Book(102, "Java", "Ganesh", 700, 400),
    Book(103, "SQL", "Ashwin", 600, 100),
    Book(104, "Machine Learning", "Pawan", 800, 300),
]

print("=== INITIAL STOCK ===")
for b in books:
    b.display_details()

print("\n=== CUSTOMER 1 ORDER ===")
cart1 = Cart("KAVINYA SHREE")
cart1.add_item(books[0], 4)
cart1.add_item(books[1], 2)
cart1.add_item(books[2], 1)
cart1.apply_discount(10)
cart1.generate_bill()

print("=== CUSTOMER 2 ORDER ===")
cart2 = Cart("HARIII")
cart2.add_item(books[0], 5)
cart2.add_item(books[1], 12)
cart2.add_item(books[2], 1)
cart2.add_item(books[3], 50)
cart2.apply_discount(50)
cart2.generate_bill()
