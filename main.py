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
        print("-----------Book Details---------------------")
        print(f"Book ID        : {self.book_id}")
        print(f"Title          : {self.title}")
        print(f"Author         : {self.author}")
        print(f"Price          : {self.price}")
        print(f"Quantity       : {self.quantity}")
        print("--------------------------------------------")


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
            print(f"Discount of {discount_percent}% applied to the entire order.")
        else:
            print("Invalid Discount Percentage.")

    def calculate_total(self):
        total = sum(book.price * qty for book, qty in self.items)
        return total

    def generate_bill(self):
        if not self.items:
            print("Cart is empty! Nothing to bill.")
            return

        print("\n" + "==" * 30)
        print("--------------------- KAVI BOOK STORE -------------------------")
        print("==" * 30)
        print(f"Customer Name: {self.customer_name}")
        print("==" * 30)

        grand_total = 0
        for book, qty in self.items:
            amount = book.price * qty
            grand_total += amount
            print(f"{book.title} | {qty} x {book.price} = {amount}")

        print("---" * 33)
        print(f"Subtotal: {grand_total}")

        if self.discount_percent > 0:
            discount_amount = grand_total * (self.discount_percent / 100)
            final_amount = grand_total - discount_amount
            print(f"Discount ({self.discount_percent}%): -{discount_amount}")
            print(f"Amount Payable: {final_amount}")
        else:
            final_amount = grand_total
            print(f"Amount Payable: {final_amount}")

        print("==" * 30)

        # Update stock of all books
        print("\nUpdating Stock...")
        for book, qty in self.items:
            book.sell_book(qty)
        print("\nOrder Completed Successfully!")
        print("==" * 30 + "\n")


# Initialize Books
book1 = Book(101, "Python Programming", "Deepak", 400, 500)
book2 = Book(102, "Java", "Ganesh", 700, 400)
book3 = Book(103, "SQL", "Ashwin", 600, 100)
book4 = Book(104, "Machine Learning", "Pawan", 800, 300)

print("========== INITIAL STOCK ==========")
for b in [book1, book2, book3, book4]:
    b.display_details()

print("\n=============== CUSTOMER 1 ORDER =================")
cart1 = Cart("KAVINYA SHREE")
cart1.add_item(book1, 4)
cart1.add_item(book2, 2)
cart1.add_item(book3, 1)
cart1.apply_discount(10)
cart1.generate_bill()

print("\n=============== CUSTOMER 2 ORDER =================")
cart2 = Cart("HARIII")
cart2.add_item(book1, 5)
cart2.add_item(book2, 12)
cart2.add_item(book3, 1)
cart2.add_item(book4, 50)
cart2.apply_discount(50)
cart2.generate_bill()