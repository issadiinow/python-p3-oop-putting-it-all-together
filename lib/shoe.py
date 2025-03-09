class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"  # 🔹 Fix: Ensure the condition starts as "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")  # 🔹 Fix: Print instead of raising error

    def cobble(self):
        self.condition = "New"  # 🔹 Fix: Ensure condition resets to "New" after cobbling
        print("Your shoe is as good as new!")
