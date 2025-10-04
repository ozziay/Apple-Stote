class Apple:
    def __init__(self, model, price, storage, color):
        self.brand = "Apple"
        self.model = model
        self.price = price
        self.storage = storage
        self.color = color

    def show_info(self):
        print(f"{self.brand} {self.model}")
        print(f"Price: ${self.price}")
        print(f"Storage: {self.storage} GB")
        print(f"Color: {self.color}")

class Iphone(Apple):
    def __init__(self, model, price, storage, color, camera_mp, dual_sim, face_ID):
        super().__init__(model, price, storage, color,)
        self.camera_mp = camera_mp 
        self.dual_sim = dual_sim,
        self.face_ID = face_ID

    def show_info(self):
        super().show_info()
        print(f"Camera: {self.camera_mp} MP")
        print(f"Dual SIM: {'Yes' if self.dual_sim else 'No'}")
        print(f"Face ID: {'Yes' if self.face_ID else 'No'}")
        print("-"*40)

class Ipad(Apple):
    def __init__ (self, model, price, storage, color, pencil_support,screen_size, keyboard_support ):
        super().__init__(model, price, storage, color)
        self.pencil_support = pencil_support
        self.screen_size = screen_size
        self.keyboard_support = keyboard_support

    def show_info(self):
        super().show_info()
        print(f"Pencil Support: {'Yes' if self.pencil_support else 'No'}")
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Keyboard Support: {'Yes' if self.keyboard_support else 'No'}")
        print("-"*40)

class iMac(Apple):
    def __init__(self,model, price, storage, color, ram, resolution, gpu):
        super().__init__(model, price, storage, color)
        self.ram = ram
        self.resolution = resolution
        self.gpu = gpu

    def show_info(self):
        super().show_info()
        print(f"RAM: {self.ram} GB")
        print(f"Resolution: {self.resolution}")
        print(f"GPU: {self.gpu}")
        print("-"*40)

class Apple_Watch(Apple):
    def __init__(self, model, price, storage, color, heart_rate_sensor, water_resistance, strap_type):
        super().__init__(model, price, storage, color)
        self.heart_rate_sensor = heart_rate_sensor
        self.water_resistance = water_resistance
        self.strap_type = strap_type

    def show_info(self):
        super().show_info()
        print(f"Heart Rate Sensor: {'Yes' if self.heart_rate_sensor else 'No'}")
        print(f"Water Resistance: {'Yes' if self.water_resistance else 'No'}")
        print(f"Strap Type: {self.strap_type}")
        print("-"*40)


iph17 = Iphone("Iphone 17 Pro Max", 1899, 512, "Black", 48, True, True)
iph14 = Iphone("Iphone 14 PRo Max", 1399, 256, "Silver", 12, False, True)
ipadpro = Ipad("iPad Pro (M2, 12.9)", 1299, 512, "Space Gray", True, 12.9, True)
ipadair = Ipad("iPad Air (M1, 10.9)", 899, 256, "Blue", True, 10.9, False)
imac = iMac("iMac 24 (M1, 2021)", 1499, 512, "Green", 8, "4.5K Retina", "Apple GPU")
imac2 = iMac("iMac 27 (Intel, 2020)", 1999, 1000, "Silver", 16, "5K Retina", "Radeon Pro")
watchultr = Apple_Watch("Apple Watch Ultra 2", 799, 64, "Titanium", True, 50, "Sport Loop" )
watch9 = Apple_Watch("Apple Watch Series 9", 499, 32, "Red", True, 50, "Leather")

products = [iph17, iph14, ipadpro, ipadair, imac, imac2, watchultr, watch9]
for product in products:
    product.show_info()

print ("📱 Welcome to Apple Store!")

while True:
    print("Which product category are you interested in?")
    print("1 - iPhone")
    print("2 - iPad")
    print("3 - iMac / Macbook")
    print("4 - Apple Watch")
    print("0 - Exit")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        while True:
            print("\nAvailable iPhone Models:\n")
            iph17.show_info()
            iph14.show_info()
            print("0 - Return to Store Menu")
            sub_choice = input("Your choice: ")
            if sub_choice == "0":
                break

    elif choice == "2":
        while True:
            print("\nAvailable iPad Models:\n")
            ipadpro.show_info()
            ipadair.show_info()
            print("0 - Return to Store Menu")
            sub_choice = input("Your choice: ")
            if sub_choice == "0":
                break

    elif choice == "3":
        while True:
            print("\nAvailable iMac Models:\n")
            imac.show_info()
            imac2.show_info()
            print("0 - Return to Store Menu")
            sub_choice = input("Your choice: ")
            if sub_choice == "0":
                break

    elif choice == "4":
        while True:
            print("\nAvailable Apple Watch Models:\n")
            watchultr.show_info()
            watch9.show_info()
            print("0 - Return to Store Menu")
            sub_choice = input("Your choice: ")
            if sub_choice == "0":
                break

    elif choice == "0":
        print("Logging out...")
        break

    else:
        print("\n❌ Invalid choice. Please try again.")


