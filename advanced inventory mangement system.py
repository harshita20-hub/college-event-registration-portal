# ============================================================
# ADVANCED INVENTORY MANAGEMENT SYSTEM
# Python + DSA Project
#
# DSA Concepts:
# 1. Classes and Objects (OOP)
# 2. Python Lists
# 3. Binary Search Tree (BST)
# 4. Bubble Sort
# 5. Doubly Linked List
# 6. Queue (FIFO)
# 7. Tree Traversal
# ============================================================


# ============================================================
# PART 1: ITEM CLASS
# ============================================================

class Item:

    def _init_(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def display(self):
        print(
            self.item_id, "|", self.name,
            "| Quantity:", self.quantity,
            "| Price: Rs.", self.price
        )


# ============================================================
# PART 2: BINARY SEARCH TREE
# ============================================================

class TreeNode:

    def _init_(self, item):
        self.item = item
        self.left = None
        self.right = None


class BinarySearchTree:

    def _init_(self):
        self.root = None

    # Build a balanced BST from sorted item IDs
    def build_balanced(self, items):
        sorted_items = sorted(items, key=lambda x: x.item_id)

        def build(start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            node = TreeNode(sorted_items[mid])

            node.left = build(start, mid - 1)
            node.right = build(mid + 1, end)

            return node

        self.root = build(0, len(sorted_items) - 1)

    # Search using the Binary Search Tree
    def search(self, item_id):
        current = self.root

        while current is not None:
            if item_id == current.item.item_id:
                return current.item

            elif item_id < current.item.item_id:
                current = current.left

            else:
                current = current.right

        return None

    # In-order traversal displays IDs in sorted order
    def display_sorted(self):
        def traverse(node):
            if node is not None:
                traverse(node.left)
                node.item.display()
                traverse(node.right)

        if self.root is None:
            print("Tree is empty.")
        else:
            traverse(self.root)


# ============================================================
# PART 3: DOUBLY LINKED LIST FOR TRANSACTION HISTORY
# ============================================================

class HistoryNode:

    def _init_(self, data):
        self.data = data
        self.next = None
        self.previous = None


class TransactionHistory:

    def _init_(self):
        self.head = None
        self.tail = None

    def add_transaction(self, data):
        new_node = HistoryNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def display_forward(self):
        print("\n--- Transaction History (Oldest First) ---")
        current = self.head

        if current is None:
            print("No transactions.")
            return

        while current is not None:
            print(current.data)
            current = current.next

    def display_backward(self):
        print("\n--- Transaction History (Newest First) ---")
        current = self.tail

        if current is None:
            print("No transactions.")
            return

        while current is not None:
            print(current.data)
            current = current.previous


# ============================================================
# PART 4: QUEUE FOR RESTOCK REQUESTS
# ============================================================

class QueueNode:

    def _init_(self, item_id, quantity):
        self.item_id = item_id
        self.quantity = quantity
        self.next = None


class RestockQueue:

    def _init_(self):
        self.front = None
        self.rear = None

    # Add a request to the back of the queue
    def enqueue(self, item_id, quantity):
        new_node = QueueNode(item_id, quantity)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print("Restock request added to queue.")

    # Process the oldest request first
    def dequeue(self, inventory):
        if self.front is None:
            print("No pending restock requests.")
            return

        request = self.front
        item = inventory.search_item(request.item_id)

        if item is None:
            print("Item not found. Request cannot be processed.")
        else:
            item.quantity += request.quantity
            inventory.history.add_transaction(
                "Restocked " + item.item_id
                + " by " + str(request.quantity)
            )
            print("Restock completed for", item.name)

        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def display(self):
        print("\n--- Pending Restock Requests ---")
        current = self.front

        if current is None:
            print("Queue is empty.")
            return

        while current is not None:
            print(
                "Item ID:", current.item_id,
                "| Quantity to add:", current.quantity
            )
            current = current.next


# ============================================================
# PART 5: INVENTORY CLASS
# ============================================================

class Inventory:

    def _init_(self):
        self.items = []
        self.tree = BinarySearchTree()
        self.history = TransactionHistory()
        self.restock_queue = RestockQueue()

    def rebuild_tree(self):
        self.tree.build_balanced(self.items)

    # Add item
    def add_item(self, item):
        if self.search_item(item.item_id) is not None:
            print("An item with this ID already exists.")
            return

        self.items.append(item)
        self.rebuild_tree()

        self.history.add_transaction(
            "Added " + item.item_id + " - " + item.name
        )
        print("Item added successfully.")

    # Display inventory
    def display(self):
        if not self.items:
            print("Inventory is empty.")
            return

        print("\n--- Inventory ---")
        for item in self.items:
            item.display()

    # Search using BST
    def search_item(self, item_id):
        return self.tree.search(item_id)

    # Update quantity
    def update_quantity(self, item_id, change):
        item = self.search_item(item_id)

        if item is None:
            print("Item not found.")
            return

        if item.quantity + change < 0:
            print("Error: Stock cannot become negative.")
            return

        item.quantity += change

        self.history.add_transaction(
            "Updated " + item_id
            + " quantity by " + str(change)
        )
        print("Quantity updated successfully.")

    # Remove item
    def remove_item(self, item_id):
        item = self.search_item(item_id)

        if item is None:
            print("Item not found.")
            return

        self.items.remove(item)
        self.rebuild_tree()

        self.history.add_transaction(
            "Removed " + item.item_id + " - " + item.name
        )
        print("Item removed successfully.")

    # Bubble sort
    def bubble_sort(self, key):
        n = len(self.items)

        for i in range(n):
            swapped = False

            for j in range(n - i - 1):
                if getattr(self.items[j], key) > getattr(
                    self.items[j + 1], key
                ):
                    self.items[j], self.items[j + 1] = (
                        self.items[j + 1], self.items[j]
                    )
                    swapped = True

            if not swapped:
                break

        print("Inventory sorted successfully.")
        self.display()

    # Low stock report
    def low_stock(self, limit=10):
        print("\n--- Low Stock Report ---")
        found = False

        for item in self.items:
            if item.quantity <= limit:
                item.display()
                found = True

        if not found:
            print("No low-stock items.")


# ============================================================
# PART 6: MAIN PROGRAM
# ============================================================

inventory = Inventory()

# Sample inventory
inventory.add_item(Item("P001", "Laptop", 20, 55000))
inventory.add_item(Item("P002", "Mouse", 8, 500))
inventory.add_item(Item("P003", "Keyboard", 15, 1200))
inventory.add_item(Item("P004", "Monitor", 5, 9000))
inventory.add_item(Item("P005", "Printer", 12, 15000))


# ============================================================
# PART 7: MENU-DRIVEN APPLICATION
# ============================================================

while True:

    print("\n========== INVENTORY MANAGEMENT ==========")
    print("1. Display Inventory")
    print("2. Add New Item")
    print("3. Search Item Using BST")
    print("4. Update Quantity")
    print("5. Remove Item")
    print("6. Sort by Price")
    print("7. Sort by Quantity")
    print("8. Low Stock Report")
    print("9. Add Restock Request")
    print("10. Process Next Restock Request")
    print("11. Display Restock Queue")
    print("12. Display BST in Sorted Order")
    print("13. Transaction History (Forward)")
    print("14. Transaction History (Backward)")
    print("15. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        inventory.display()

    elif choice == "2":
        item_id = input("Enter item ID: ").strip().upper()
        name = input("Enter item name: ").strip()

        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))

            if not item_id or not name:
                print("ID and name cannot be empty.")
            elif quantity < 0 or price < 0:
                print("Quantity and price cannot be negative.")
            else:
                inventory.add_item(
                    Item(item_id, name, quantity, price)
                )
        except ValueError:
            print("Enter a valid number.")

    elif choice == "3":
        item_id = input("Enter item ID to search: ").strip().upper()
        result = inventory.search_item(item_id)

        if result is not None:
            print("Item found:")
            result.display()
        else:
            print("Item not found.")

    elif choice == "4":
        item_id = input("Enter item ID: ").strip().upper()

        try:
            change = int(input(
                "Enter quantity change (+ to add, - to subtract): "
            ))
            inventory.update_quantity(item_id, change)
        except ValueError:
            print("Enter a valid whole number.")

    elif choice == "5":
        item_id = input("Enter item ID to remove: ").strip().upper()
        inventory.remove_item(item_id)

    elif choice == "6":
        inventory.bubble_sort("price")

    elif choice == "7":
        inventory.bubble_sort("quantity")

    elif choice == "8":
        try:
            limit = int(input("Enter low-stock limit (default 10): "))
            if limit < 0:
                print("Limit cannot be negative.")
            else:
                inventory.low_stock(limit)
        except ValueError:
            inventory.low_stock()

    elif choice == "9":
        item_id = input("Enter item ID: ").strip().upper()

        try:
            quantity = int(input("Enter quantity to restock: "))

            if quantity <= 0:
                print("Restock quantity must be positive.")
            elif inventory.search_item(item_id) is None:
                print("Item not found.")
            else:
                inventory.restock_queue.enqueue(item_id, quantity)
        except ValueError:
            print("Enter a valid whole number.")

    elif choice == "10":
        inventory.restock_queue.dequeue(inventory)

    elif choice == "11":
        inventory.restock_queue.display()

    elif choice == "12":
        inventory.tree.display_sorted()

    elif choice == "13":
        inventory.history.display_forward()

    elif choice == "14":
        inventory.history.display_backward()

    elif choice == "15":
        print("Thank you for using Inventory Management System!")
        break

    else:
        print("Invalid choice. Please select 1-15.")