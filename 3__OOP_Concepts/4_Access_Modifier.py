# Access modifiers in Python are used to restrict access to class members (attributes and methods).

# There are three types of access modifiers in Python:
# 1. Public: Members are accessible from outside the class.                   -->> This is the default
# 2. Protected: Members are accessible within the class and its subclasses.   -->> Indicated by a single underscore prefix (_).
# 3. Private: Members are accessible only within the class itself.            -->> Indicated by a double underscore prefix (__).


class Mobile:
    def __init__(self, brand, model, price , mfg_date):
        self.brand = brand
        self.model = model
        self._price = price        # Protected attribute
        self.__mfg_date = mfg_date # Private attribute

    # Protected method
    def _mobile_info(self):
        print(self.brand, self.model, self._price, self.__mfg_date)

# instance
i = Mobile("Apple", "iPhone 14", 100000, "2022-09-16")


print(i._Mobile__mfg_date) # Accessing private attribute using name mangling
i._mobile_info()           # Accessing protected method