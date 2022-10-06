from abc import ABCMeta, abstractmethod
from tkinter import *
import uuid, os

window = Tk()
window.title("My shopping cart")
#Maximize window to screen size
window.state("zoomed")

#Creating login frame
login_frame = Frame(window, height = "500", width = "500")
#Creating signup frame
signup_frame = Frame(window, bg = "yellow", height = "200", width = "500")
#Creating shelves frame
shelves_frame = Frame(window, bg = "yellow", height = "500", width = "500")
#Creating label to display background image
background_image = PhotoImage(file = 'static/bg.png')
background_label = Label(login_frame, image = background_image)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#Generating receipt code for new cart
receipt_code = str(uuid.uuid4().hex[:6])

#Super abstract class
class Super(metaclass = ABCMeta):
    @abstractmethod
    def login(self):
        pass

#Shelves class
class Shelves:
    #Display shelf method
    def shelfDisplay(self, acc_type):
        self.acc_type = acc_type

        #Display clothing items shelf
        def clothing():
            shelves_frame.place_forget()
            category = Category()
            category.shelfDisplay("C", self.acc_type)

        #Display food items shelf
        def food():
            shelves_frame.place_forget()
            category = Category()
            category.shelfDisplay("F", self.acc_type)
        
        #Display electronics items shelf
        def electronics():
            shelves_frame.place_forget()
            category = Category()
            category.shelfDisplay("E", self.acc_type)

        #Display home and kitchen items shelf
        def homeAndKitchen():
            shelves_frame.place_forget()
            category = Category()
            category.shelfDisplay("HK", self.acc_type)

        #Go back to admin/customer home page
        def back():
            shelves_frame.place_forget()

            if self.acc_type == "C":
                customer_obj = Customer()
                customer_obj.customer()
            else:
                admin_obj = Admin()
                admin_obj.admin()

        #SHELVES FRAME
        shelves_frame.place(relheight = 1, relwidth = 1, relx = 0.5, rely = 0.5, anchor = CENTER)
        #background label to diplay background image
        background_label = Label(shelves_frame, image = background_image)
        background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #available categories label
        availablecategs_label = Label(shelves_frame, bg = "White", fg = "Black", text = "Available Categories", width = 20, height = 3, font = 3)
        availablecategs_label.place(x = 630, y = 180)
        #clothing items button
        clothing_button = Button(shelves_frame, width = 15, height = 2, text = "Clothing", bg = "Black", fg = "White", command = clothing)
        clothing_button.place(x = 470, y = 400)
        #food items button
        food_button = Button(shelves_frame, height = 2, width = 15, text = "Food", bg = "Black", fg = "White", command = food)
        food_button.place(x = 600, y = 400)
        #electronics item buttons
        electronics_button = Button(shelves_frame, height = 2, width = 15 , text = "Electronics", bg = "Black", fg = "White", command = electronics)
        electronics_button.place(x = 730, y = 400)
        #home and kitchen item buttons
        homeandkitchen_button = Button(shelves_frame, height = 2, width = 15 , text = "Home&Kitchen", bg = "Black", fg = "White", command = homeAndKitchen)
        homeandkitchen_button.place(x = 860, y = 400)
        #back button
        back_button = Button(shelves_frame, height = 2, width = 15, text = "Back", bg = "Black", fg = "Orange", command = back)
        back_button.place(x = 670, y = 450)

#Customer class
class Customer:
    #Display customer home page method
    def customer(self):
        #Remove login frame
        login_frame.place_forget()

        #Display shelves method
        def browseShelves():
            customerhome_frame.place_forget()
            shelves = Shelves()
            shelves.shelfDisplay("C")

        #Display shopping history method
        def shoppingHistory():
            customerhome_frame.place_forget()
            cart = Cart("SH")
            cart.display()

        #Display cart method
        def viewCart():
            customerhome_frame.place_forget()
            cart = Cart(receipt_code)
            cart.display()
            
        #Place order method
        def placeOrder():
            customerhome_frame.place_forget()
            order = Order(receipt_code)
            order.placeOrder()

        #Go back to login page
        def logout():
            #Remove customer home page
            customerhome_frame.place_forget()
            #Place login frame
            login_frame.place(relheight = 1, relwidth = 1, relx = 0.5, rely = 0.5, anchor = CENTER)

        #CUSTOMER HOME FRAME
        customerhome_frame = Frame(window, height = "400", width = "400")
        customerhome_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
        #background label to diplay background image
        background_label = Label(customerhome_frame, image = background_image)
        background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #customer greeting label
        customergreeting_label = Label(customerhome_frame, width = 50, height = 3, font = 3, text = "Welcome to Customer home page. Please select one option!")
        customergreeting_label.place(x = 465, y = 180)
        #browse shelves button
        browseshelves_button = Button(customerhome_frame, text = 'Browse shelves', bg = 'black', fg = 'White', width = 15, height = 2, command = browseShelves)
        browseshelves_button.place(x = 450, y = 400)
        #shopping history button
        shoppinghistory_button = Button(customerhome_frame, width = 15, height = 2, text = 'shopping history', bg = 'black', fg = 'White', command = shoppingHistory)
        shoppinghistory_button.place(x = 575, y = 400)
        #view cart button
        viewcart_button = Button(customerhome_frame, width = 15, height = 2, text = 'view cart', bg = 'black', fg = 'White', command = viewCart)
        viewcart_button.place(x = 700, y = 400)
        #place order button
        placeorder_button = Button(customerhome_frame, widt = 15, height = 2, text = 'place order', bg = 'black', fg = 'White', command = placeOrder)
        placeorder_button.place(x = 825, y = 400)
        #logout button
        logout_button = Button(customerhome_frame, text = "logout", height = 2, width = 15, bg = "black", fg = "orange", command = logout)
        logout_button.place(x = 640, y = 450)

#Admin class
class Admin:
    #Display admin home page method
    def admin(self):
        #Remove login frame
        login_frame.place_forget()

        #Display shelves method
        def browseShelves():
            adminhome_frame.place_forget()
            shelves = Shelves()
            shelves.shelfDisplay("A")

        #Display add stock menu
        def addStock():
            adminhome_frame.place_forget()
            self.addStock()

        #Go back to login page
        def logout():
            #Remove admin home page
            adminhome_frame.place_forget()
            #Place login frame
            login_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)

        #ADMIN HOME FRAME
        adminhome_frame = Frame(window, bg = 'yellow', height = "700", width = "400")
        adminhome_frame.place(relheight = 1, relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
        #background label to diplay background image
        background_label = Label(adminhome_frame, image = background_image)
        background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #admin greeting label
        admingreeting_label = Label(adminhome_frame, width = 50, height = 3, font = 3, bg = 'White', fg = "Black", text = "Welcome to Admin home page. Please select one option!")
        admingreeting_label.place(x = 465, y = 180)
        #browse shelves button
        browseshelves_button = Button(adminhome_frame, text = "Browse shelves", bg = 'black', fg = "White", width = 15, height = 2, command = browseShelves)
        browseshelves_button.place(x = 500, y = 400)
        #add stock button
        addstock_button = Button(adminhome_frame, text = "Add stock", bg = "Black", fg = "White", command = addStock, width = 15, height = 2)
        addstock_button.place(x = 780, y = 400)
        #logout button
        logout_button = Button(adminhome_frame, text = "logout", bg = "Black", fg = "Orange", command = logout, width = 15, height = 2)
        logout_button.place(x = 640, y = 500)

    #Add stock method
    def addStock(self):
        #Confirm add stock
        def confirm():
            #Get entered item id and stock to add
            item_id = item_id_textbox.get("1.0", "end").replace('\n', '')
            item_qty = item_qty_textbox.get("1.0", "end").replace('\n', '')

            #Break item id into two pieces
            item_category = item_id[0] #Item category eg: F - Food
            item_type = item_id[1] + item_id[2] #Item type eg: VG - Vegetables

            #Set file path according to item category and item type
            if item_category == 'F' and item_type == 'VG':
                stock_file_path = 'data/stock/Food/Vegetables.txt'
            elif item_category == 'F' and item_type == 'ME':
                stock_file_path = 'data/stock/Food/Meat.txt'
            elif item_category == 'F' and item_type == 'SP':
                stock_file_path = 'data/stock/Food/Spices.txt'
            elif item_category == 'F' and item_type == 'BV':
                stock_file_path = 'data/stock/Food/Beverages.txt'
            elif item_category == 'C' and item_type == 'MC':
                stock_file_path = 'data/stock/Clothing/Male.txt'
            elif item_category == 'C' and item_type == 'FC':
                stock_file_path = 'data/stock/Clothing/Female.txt'
            elif item_category == 'C' and item_type == 'CC':
                stock_file_path = 'data/stock/Clothing/Child.txt'
            elif item_category == 'C' and item_type == 'US':
                stock_file_path = 'data/stock/Clothing/Unisex.txt'
            elif item_category == 'E' and item_type == 'DK':
                stock_file_path = 'data/stock/Electronics/Desktops.txt'
            elif item_category == 'E' and item_type == 'LP':
                stock_file_path = 'data/stock/Electronics/Laptops.txt'
            elif item_category == 'E' and item_type == 'SP':
                stock_file_path = 'data/stock/Electronics/Smartphones.txt'
            elif item_category == 'E' and item_type == 'SW':
                stock_file_path = 'data/stock/Electronics/Smartwatches.txt'
            elif item_category == 'H' and item_type == 'CW':
                stock_file_path = 'data/stock/Home&Kitchen/Cookware.txt'
            elif item_category == 'H' and item_type == 'CR':
                stock_file_path = 'data/stock/Home&Kitchen/Crockery.txt'
            elif item_category == 'H' and item_type == 'SW':
                stock_file_path = 'data/stock/Home&Kitchen/Silverware.txt'
            elif item_category == 'H' and item_type == 'UT':
                stock_file_path = 'data/stock/Home&Kitchen/Utensils.txt'

            #Get stock data in file
            try:
                with open(stock_file_path, "r") as stock_file_read:
                    stock_file_data = stock_file_read.readlines()

                #Add eneterd stock to current stock
                stock_file_data = [i.replace('\n', '') for i in stock_file_data]
                
                if item_id in stock_file_data:
                    id_index = stock_file_data.index(item_id)
                    stock_file_data[id_index + 3] = str(int(stock_file_data[id_index + 3]) + int(item_qty))
                    
                    #Write new stock data to stock file
                    with open(stock_file_path, "w+") as stock_file_write:
                        stock_file_write.write("\n".join(stock_file_data))

                    #Display result
                    result_label.configure(text = "Stock added successfully")
                
                else:
                    #Dsiplay result
                    result_label.configure(text = "Item id does not exist")

            except UnboundLocalError:
                #Dsiplay result
                result_label.configure(text = "Item id does not exist")

        #Go back to admin home page
        def back():
            #Remove add stock frame
            addstock_frame.place_forget()
            #
            admin_obj = Admin()
            admin_obj.admin()

        #ADIM ADD STOCK FRAME
        addstock_frame = Frame(window, bg = "Black", height = "700", width = "400")
        addstock_frame.place(relheight = 1, relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
        #background label to diplay background image
        background_label = Label(addstock_frame, image = background_image)
        background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #item id label
        item_id_label = Label(addstock_frame, bg = "Black", fg = "White", text = "Item id: ", font = 3)
        item_id_label.place(x = 300, y = 200)
        #item id textbox
        item_id_textbox = Text(addstock_frame, height = 1, width = 20, font = ("Helvetica", 14))
        item_id_textbox.place(x = 360, y = 200)
        #item qty label
        item_qty_label = Label(addstock_frame, bg = "Black", fg = "White", text = "Item qty to add: ", font = 3)
        item_qty_label.place(x = 300, y = 300)
        #item qty textbox
        item_qty_textbox = Text(addstock_frame, height = 1, width = 10, font = ("Helvetica", 14))
        item_qty_textbox.place(x = 420, y = 300)
        #confirm button
        confirm_button = Button(addstock_frame, text = 'Confirm', bg = 'Black', fg = 'White', command = confirm)
        confirm_button.place(x = 300, y = 400)
        #back button
        back_button = Button(addstock_frame, text = 'back', bg = 'Black', fg = 'White', command = back)
        back_button.place(x = 400, y = 400)
        #result label
        result_label = Label(addstock_frame, bg = "Black", fg = "White")
        result_label.place(x = 500, y = 400)

#Main class
class Main(Super, Customer, Admin):
    def __init__(self):
        self.login()

    #Login method
    def login(self):
        def login():
            #Get user entered username and password
            self.username = username_textbox.get("1.0", "end").replace('\n', '')
            self.password = password_textbox.get("1.0", "end").replace('\n', '')
            #Check if username or password fields are empty
            if self.username == "" or self.password == "":
                result_label.place(x = 300, y = 500)
                result_label.configure(text = "Missing username and/or password!")
            else:
                self.loginCheck(self.username, self.password)

        #Display signup frame
        def signup():
            login_frame.place_forget()
            signup_frame.place(relheight = 1, relwidth = 1, relx = 0.5, rely = 0.5, anchor = CENTER)

        #Confirm signup
        def signup_confirm():
            #Get user entered username, password and account type
            username_signup = usernamesignup_textbox.get("1.0", "end")
            password_signup = passwordsignup_textbox.get("1.0", "end")
            acctype_signup = acctypesignup_textbox.get("1.0", "end")
            #Call signup method
            self.signUp(username_signup, password_signup, acctype_signup)

        #Go back to login page
        def back():
            signup_frame.place_forget()
            login_frame.place(relheight = 1, relwidth = 1, relx = 0.5, rely = 0.5, anchor = CENTER)

        #LOGIN FRAME
        login_frame.place(relheight = 1, relwidth = 1, relx = 0.5, rely = 0.5, anchor = CENTER)
        #username label
        username_label = Label(login_frame, text = "Username", bg = 'black', fg = 'White', height = 2, width = 10, font = 3)
        username_label.place(x = 300, y = 200)
        #username textbox
        username_textbox = Text(login_frame, height = 1, width = 23, font = ("Helvetica", 14))
        username_textbox.place(x = 300, y = 240)
        #password label
        password_label = Label(login_frame, text = "Password" , bg = 'black', fg = 'White', height = 2, width = 10, font = 3)
        password_label.place(x = 300, y = 300)
        #password textbox
        password_textbox = Text(login_frame, height = 1, width = 23, font = ("Helvetica", 14))
        password_textbox.place(x = 300, y = 340)
        #login button
        login_button = Button(login_frame, text = "Login", bg = 'black', fg = 'white', command = login, width = 10, height = 2, font = ("Corbel", 11))
        login_button.place(x = 300, y = 400)
        #signup button
        signup_button = Button(login_frame, text = "Signup", bg = 'black', fg = 'white', command = signup, width = 10, height = 2, font = ("Corbel", 11))
        signup_button.place(x = 450, y = 400)
        #background image label
        background_label = Label(signup_frame, image = background_image)
        background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #username signup label
        usernamesignup_label = Label(signup_frame, text = "Username", bg = 'black', fg = 'White', height = 2, width = 10, font = 3)
        usernamesignup_label.place(x = 300, y = 200)
        #username signup textbox
        usernamesignup_textbox = Text(signup_frame, height = 1, width = 23, font = ("Helvetica", 14))
        usernamesignup_textbox.place(x = 300, y = 240)
        #password signup label
        passwordsignup_label = Label(signup_frame, text = "Password" , bg = 'black', fg = 'White', height = 2, width = 10 , font = 3)
        passwordsignup_label.place(x = 300, y = 300)
        #password signup textbox
        passwordsignup_textbox = Text(signup_frame, height = 1, width = 23, font = ("Helvetica", 14))
        passwordsignup_textbox.place(x = 300, y = 340)
        #account type signup label
        acctypesignup_label = Label(signup_frame, text = "Account type \n A: Admin | C: Customer" , bg = 'black', fg = 'White' , height = 2, width = 20 , font = 3)
        acctypesignup_label.place(x = 300 , y = 400)
        #account type signup textbox
        acctypesignup_textbox = Text(signup_frame, height = 1, width = 20, font = ("Helvetica", 14))
        acctypesignup_textbox.place(x = 300, y = 440)
        #confirm signup button
        confirm_button = Button(signup_frame, text = "Confirm", bg = 'black', fg = 'white', width = 12, height = 2, font = ("Corbel", 11), command = signup_confirm)
        confirm_button.place(x = 300, y = 500)
        #back button
        back_button = Button(signup_frame, text = "back", bg = 'black', fg = 'orange', width = 12, height = 2, font = ("Corbel", 11), command = back)
        back_button.place(x = 450, y = 500)
        #result label
        result_label = Label(login_frame, bg = "black", fg = "White", height = 2, width = 30, font = ("Corbel", 12))

    #Sign up method
    def signUp(self, username, password, acctype):
        self.username = username
        self.password = password
        self.acctype = acctype

        #Get existing accounts data from file
        with open("data/Accounts.txt", "r") as accounts_file:
            accounts_file_data = accounts_file.readlines()

        #Add new account data to existing accounts data
        accounts_file_data.append(self.username)
        accounts_file_data.append(self.password)
        accounts_file_data.append(self.acctype)

        #Write new accounts data to file
        with open("data/Accounts.txt", "w+") as accounts_file:
            accounts_file.write(''.join(accounts_file_data))

        #Result label
        result_label = Label(signup_frame, bg = "black", fg = "White", height = 2, width = 30, font = ("Corbel", 12))
        result_label.place(x = 300, y = 600)
        result_label.configure(text = "Account added")

    #Login check method
    def loginCheck(self, username, password):
        self.username = username
        self.password = password

        #Get existing accounts data from file
        with open("data/Accounts.txt", "r") as accounts_file:
            accounts_file_data = accounts_file.readlines()

        accounts_file_data = [i.replace('\n', '') for i in accounts_file_data]
        #Check if username is in accounts data
        if self.username in accounts_file_data:
            #Get index of username in accounts data
            username_index = accounts_file_data.index(self.username)
            #Check is password matches password in accounts data
            if self.password == accounts_file_data[username_index + 1]:
                #Check is account type is customer
                if accounts_file_data[username_index + 2] == "C":
                    #Initialize new cart
                    with open(f"data/carts/{receipt_code}.txt", "w+") as newcart_file:
                        newcart_file.write(self.username + "\n")
                    customer_obj = Customer()
                    customer_obj.customer()
                else:
                    admin_obj = Admin()
                    admin_obj.admin()

            else:
                #Result label
                result_label = Label(login_frame, bg = "black", fg = "White", height = 2, width = 30, font = ("Corbel", 12))
                result_label.place(x = 300, y = 500)
                result_label.configure(text = "Incorrect password!")
        else:
            #Result label
            result_label = Label(login_frame, bg = "black", fg = "White", height = 2, width = 30, font = ("Corbel", 12))
            result_label.place(x = 300, y = 500)
            result_label.configure(text = "Incorrect username!")

#Cart class
class Cart(Main):
    def __init__(self, receipt_code):
        self.receipt_code = receipt_code

    #Item add method
    def add(self, item_id, qty):
        self.item_id = item_id
        self.qty = qty

        #Separate item id into two parts
        item_category = self.item_id[0] #item category eg: F - Food
        item_type = self.item_id[1] + self.item_id[2] #item type eg: VG - Vegetables

        #Set file path according to item category and type
        if item_category == 'F' and item_type == 'VG':
            stock_file_path = 'data/stock/Food/Vegetables.txt'
        elif item_category == 'F' and item_type == 'ME':
            stock_file_path = 'data/stock/Food/Meat.txt'
        elif item_category == 'F' and item_type == 'SP':
            stock_file_path = 'data/stock/Food/Spices.txt'
        elif item_category == 'F' and item_type == 'BV':
            stock_file_path = 'data/stock/Food/Beverages.txt'
        elif item_category == 'C' and item_type == 'MC':
            stock_file_path = 'data/stock/Clothing/Male.txt'
        elif item_category == 'C' and item_type == 'FC':
            stock_file_path = 'data/stock/Clothing/Female.txt'
        elif item_category == 'C' and item_type == 'CC':
            stock_file_path = 'data/stock/Clothing/Child.txt'
        elif item_category == 'C' and item_type == 'US':
            stock_file_path = 'data/stock/Clothing/Unisex.txt'
        elif item_category == 'E' and item_type == 'DK':
            stock_file_path = 'data/stock/Electronics/Desktops.txt'
        elif item_category == 'E' and item_type == 'LP':
            stock_file_path = 'data/stock/Electronics/Laptops.txt'
        elif item_category == 'E' and item_type == 'SP':
            stock_file_path = 'data/stock/Electronics/Smartphones.txt'
        elif item_category == 'E' and item_type == 'SW':
            stock_file_path = 'data/stock/Electronics/Smartwatches.txt'
        elif item_category == 'H' and item_type == 'CW':
            stock_file_path = 'data/stock/Home&Kitchen/Cookware.txt'
        elif item_category == 'H' and item_type == 'CR':
            stock_file_path = 'data/stock/Home&Kitchen/Crockery.txt'
        elif item_category == 'H' and item_type == 'SW':
            stock_file_path = 'data/stock/Home&Kitchen/Silverware.txt'
        elif item_category == 'H' and item_type == 'UT':
            stock_file_path = 'data/stock/Home&Kitchen/Utensils.txt'

        #Get existing item stock data from file
        with open(stock_file_path, "r") as item_file:
            item_file_data = item_file.readlines()

        #Get item unit price from data
        for i in range(0, len(item_file_data), 4):
            if self.item_id == item_file_data[i]:
                self.price = item_file_data[i + 2]
            else:
                pass

        #Add item data to cart file
        with open(f'data/carts/{self.receipt_code}.txt', 'a') as cart_file:
            cart_file.write(self.item_id + self.qty + self.price)

    #Item remove method
    def remove(self, item_id):
        self.item_id = item_id.replace('\n', '')
        
        #Get cart data from file
        with open(f"data/carts/{self.receipt_code}.txt", "r") as cart_file:
            cart_file_data = cart_file.readlines()

        cart_file_data = [i.replace('\n', '') for i in cart_file_data]
        #Remove item data from cart data
        if self.item_id in cart_file_data:
            id_index = cart_file_data.index(self.item_id)
            cart_file_data.remove(cart_file_data[id_index])
            cart_file_data.remove(cart_file_data[id_index])
            cart_file_data.remove(cart_file_data[id_index])
        else:
            pass

        #Write new cart data to file
        with open(f"data/carts/{self.receipt_code}.txt", "w+") as cart_file_write:
            cart_file_write.write("\n".join(cart_file_data))

    #Display cart method
    def display(self):
        #Remove item
        def remove():
            item_id = item_id_textbox.get("1.0", "end")
            self.remove(item_id)
            result_label.grid(row = 3, column = 0)
            result_label.configure(text = "Item removed")

        #Go back to customer home page
        def back():
            cart_data_frame.place_forget()
            customer_obj = Customer()
            customer_obj.customer()

        #Check if view cart button pressed or shopping history button pressed
        if self.receipt_code == "SH":
            carts = os.listdir('data/carts/receipts')
            cart_file_data = []
            for cart in carts:
                #Get cart data from file
                with open(f"data/carts/receipts/{cart}", "r") as cart_file:
                    cart_file_lines = cart_file.readlines()

                if cart_file_lines[0].replace('\n', '') == main.username:
                    cart_file_data.append("".join(cart_file_lines))
                else:
                    pass

            #CART DATA FRAME
            cart_data_frame = Frame(window, bg = "Black", height = "500", width = "500")
            cart_data_frame.place(relheight = 1, relwidth = 1, rely = 0.5, relx = 0.5, anchor = CENTER)
            #cart data label
            cart_data_label = Label(cart_data_frame, width = 15, font = 2, bg = "Black", fg = "White")
            cart_data_label.configure(text = ("\n".join(str(data) for data in cart_file_data)))
            cart_data_label.place(x = 250, y = 50)
            #cart data key label
            cart_data_key_label = Label(cart_data_frame, height = 2, width = 100, font = 3, bg = "Black", fg = "White")
            cart_data_key_label.configure(text = "COD : Cash on delivery | Number after COD is the grand total | Number before COD is discount \n Everything before that are the item ids, item quantities and item unit prices")
            cart_data_key_label.place(x = 500, y = 400)
            #back button
            back_button = Button(cart_data_frame, height = 2, width = 15, bg = "black", fg = "Orange", text = "back", command = back)
            back_button.place(x = 720, y = 300)

        else:
            with open(f'data/carts/{self.receipt_code}.txt', "r") as cart_file:
                cart_file_data = cart_file.readlines()

            #CART DATA FRAME
            cart_data_frame = Frame(window, bg = "Black", height = "500", width = "500")
            cart_data_frame.place(relheight = 1, relwidth = 1, rely = 0.5, relx = 0.5, anchor = CENTER)
            #cart data label
            cart_data_label = Label(cart_data_frame, width = 15, font = 2, bg = "Black", fg = "White")
            cart_data_label.configure(text = ("\n".join(str(data) for data in cart_file_data)))
            cart_data_label.place(x = 250, y = 50)
            #item id label
            item_id_label = Label(cart_data_frame, height = 1, width = 20, bg = "Black", fg = "White", text = "Item id: ", font = 3)
            item_id_label.place(x = 500, y = 200)
            #item id textbox
            item_id_textbox = Text(cart_data_frame, height = 1, width = 20, font = ("Helvetica", 14))
            item_id_textbox.place(x = 650, y = 200)
            #remove button
            remove_button = Button(cart_data_frame, width = 15, height = 2, bg = "Black", fg = "White", text = "Remove", command = remove)
            remove_button.place(x = 590, y = 300)
            #back button
            back_button = Button(cart_data_frame, height = 2, width = 15, bg = "black", fg = "Orange", text = "back", command = back)
            back_button.place(x = 720, y = 300)
            #result label
            result_label = Label(cart_data_frame, bg = "Black", fg = "White", font = 3)

#Order class
class Order(Cart):
    #Place order method
    def placeOrder(self):
        #PLACE ORDER FRAME
        placeorder_frame = Frame(window, bg = "Black", height = "500", width = "500" )
        placeorder_frame.place(relheight = 1, relwidth = 1, relx = 0.5, rely = 0.5, anchor = CENTER)
        #receipt code label
        receiptcode_label = Label(placeorder_frame, height = 1, width = 25, bg = "Black", fg = "White", text = f"Cart number is: {receipt_code}", font = 3)
        receiptcode_label.place(x = 50, y = 50)
        #payment method label
        paymentmethod_label = Label(placeorder_frame, height = 2, width = 30, bg = "Black", fg = "White", font = 3, text = "Payment method: \n COD : Cash on delivery | C : Card")
        paymentmethod_label.place(x = 650, y = 50)
        #payment method textbox
        paymentmethod_textbox = Text(placeorder_frame, height = 1, width = 30, font = ("Helvetica", 14))
        paymentmethod_textbox.place(x = 650, y = 100)

        #Get existing cart data from file
        with open(f'data/carts/{self.receipt_code}.txt', 'r') as cart_file:
            cart_file_data = cart_file.readlines()

        #username label
        username_label = Label(placeorder_frame, width = 15, font = 3, bg = "Black", fg = "White", text = ("\n".join(cart_file_data)))
        username_label.place(x = 400, y = 50)

        #Confirm order
        def confirm():
            #Get existing cart data from file
            with open(f'data/carts/{self.receipt_code}.txt', 'r') as cart_file:
                cart_file_data = cart_file.readlines()

            cart_file_data = cart_file_data[1:]
            cart_file_data = [i.replace('\n', '') for i in cart_file_data]

            #Calculate grand total
            self.grand_total = 0
            self.discount = 0
            for i in range(1, len(cart_file_data), 3):
                quantity_bought = int(cart_file_data[i])
                unit_price = float(cart_file_data[i + 1])
                self.grand_total += (quantity_bought * unit_price)

            #Grand total label
            grandtotal_label = Label(placeorder_frame, font = 3, bg = "Black", fg = "White", text = f"YOUR TOTAL COMES OUT TO: {self.grand_total}")
            grandtotal_label.place(x = 650, y = 250)

            #Reduce stock
            for c in range(0, len(cart_file_data), 3):
                self.item_id = cart_file_data[c]
                self.item_qty = cart_file_data[c + 1]

                #Separate item id into two parts
                item_category = self.item_id[0] #item category eg: F - Food
                item_type = self.item_id[1] + self.item_id[2] #item type eg: VG - Vegetables

                #Set file path according to item category and type
                if item_category == 'F' and item_type == 'VG':
                    stock_file_path = 'data/stock/Food/Vegetables.txt'
                elif item_category == 'F' and item_type == 'ME':
                    stock_file_path = 'data/stock/Food/Meat.txt'
                elif item_category == 'F' and item_type == 'SP':
                    stock_file_path = 'data/stock/Food/Spices.txt'
                elif item_category == 'F' and item_type == 'BV':
                    stock_file_path = 'data/stock/Food/Beverages.txt'
                elif item_category == 'C' and item_type == 'MC':
                    stock_file_path = 'data/stock/Clothing/Male.txt'
                elif item_category == 'C' and item_type == 'FC':
                    stock_file_path = 'data/stock/Clothing/Female.txt'
                elif item_category == 'C' and item_type == 'CC':
                    stock_file_path = 'data/stock/Clothing/Child.txt'
                elif item_category == 'C' and item_type == 'US':
                    stock_file_path = 'data/stock/Clothing/Unisex.txt'
                elif item_category == 'E' and item_type == 'DK':
                    stock_file_path = 'data/stock/Electronics/Desktops.txt'
                elif item_category == 'E' and item_type == 'LP':
                    stock_file_path = 'data/stock/Electronics/Laptops.txt'
                elif item_category == 'E' and item_type == 'SP':
                    stock_file_path = 'data/stock/Electronics/Smartphones.txt'
                elif item_category == 'E' and item_type == 'SW':
                    stock_file_path = 'data/stock/Electronics/Smartwatches.txt'
                elif item_category == 'H' and item_type == 'CW':
                    stock_file_path = 'data/stock/Home&Kitchen/Cookware.txt'
                elif item_category == 'H' and item_type == 'CR':
                    stock_file_path = 'data/stock/Home&Kitchen/Crockery.txt'
                elif item_category == 'H' and item_type == 'SW':
                    stock_file_path = 'data/stock/Home&Kitchen/Silverware.txt'
                elif item_category == 'H' and item_type == 'UT':
                    stock_file_path = 'data/stock/Home&Kitchen/Utensils.txt'

                #Get existing stock data from file
                with open(stock_file_path, "r") as stock_file_read:
                    stock_file_data = stock_file_read.readlines()

                #Decrement item stock accordingly
                stock_file_data = [i.replace('\n', '') for i in stock_file_data]
                for i in range(0, len(stock_file_data), 4):
                    if stock_file_data[i] == self.item_id:
                        stock_file_data[i + 3] = str(int(stock_file_data[i + 3]) - int(self.item_qty))
                    else:
                        pass

                #Write new stock to item stock file
                with open(stock_file_path, "w+") as stock_file_write:
                    stock_file_write.write("\n".join(stock_file_data))

            #Write order info to cart file
            self.payment_method = paymentmethod_textbox.get("1.0", "end")
            with open(f'data/carts/{self.receipt_code}.txt', 'a') as cart_file:
                cart_file.write(str(self.discount) + '\n' + self.payment_method + str(self.grand_total))

            #Move cart file to receipt
            os.replace(f"data/carts/{self.receipt_code}.txt", f"data/carts/receipts/{self.receipt_code}.txt")

            #order placed label
            orderplaced_label = Label(placeorder_frame, font = 3, bg = "Black", fg = "White", text = f"YOUR ORDER HAS BEEN PLACED UNDER NUMBER: {self.receipt_code}")
            orderplaced_label.place(x = 650, y = 300)

            #cntinue shopping label
            continueshopping_label = Label(placeorder_frame, font = 3, bg = "Black", fg = "White", text = f"PLEASE CONTINUE SHOPPING...")
            continueshopping_label.place(x = 650, y = 400)

            #Generating receipt code for new cart
            receipt_code = str(uuid.uuid4().hex[:6])

            #Initialize new cart
            with open(f"data/carts/{receipt_code}.txt", "w+") as newcart_file:
                newcart_file.write("Customer\n")

        #Go back to customer home page
        def back():
            placeorder_frame.place_forget()
            customer_obj = Customer()
            customer_obj.customer()

        #Exit
        def exit():
            quit()

        #Confirm button
        confirm_button = Button(placeorder_frame, height = 2, width = 15, bg = "black", fg = "White", text = "Confirm", command = confirm)
        confirm_button.place(x = 650, y = 150)
        #Back button
        back_button = Button(placeorder_frame, bg = "Black", fg = "Orange", height = 2, width = 15, text = "back", command = back)
        back_button.place(x = 800, y = 150)
        #Exit button
        exit_button = Button(placeorder_frame, bg = "Black", fg = "Orange", height = 2, width = 15, text = "exit", command = exit)
        exit_button.place(x = 950, y = 150)

#Category class
class Category:
    #Display shelf method
    def shelfDisplay(self, chosen_category, acc_type):
        self.acc_type = acc_type
        self.chosen_category = chosen_category

        #Check item category and display item types accordingly
        if self.chosen_category == "C":
            item = Item(self.chosen_category, self.acc_type)

        elif self.chosen_category == "F":
            item = Item(self.chosen_category, self.acc_type)

        elif self.chosen_category == "E":
            item = Item(self.chosen_category, self.acc_type)

        elif self.chosen_category == "HK":
            item = Item(self.chosen_category, self.acc_type)

#Item class
class Item:
    def __init__(self, chosen_category, acc_type):
        self.chosen_category = chosen_category
        self.acc_type = acc_type
        self.shelfDisplay()

    #Display shelf method
    def shelfDisplay(self):
        #Male clothing items
        def male():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Clothing/Male.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]
            
            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def female():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Clothing/Female.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]

            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def child():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Clothing/Child.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]

            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def unisex():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Clothing/Unisex.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]
            
            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def vegetables():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Food/Vegetables.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]
            
            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def meats():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Food/Meat.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]

            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def beverages():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Food/Beverages.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]

            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def spices():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Food/Spices.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]
            
            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def laptops():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Electronics/Laptops.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]
            
            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def desktops():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Electronics/Desktops.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]

            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def smartphones():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Electronics/Smartphones.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]

            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def smartwatches():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Electronics/Smartwatches.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]
            
            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def cookware():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Home&Kitchen/Cookware.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]
            
            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def silverware():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Home&Kitchen/Silverware.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]
            
            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def crockery():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Home&Kitchen/Crockery.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]
            
            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        def utensils():
            #Remove item frame
            item_frame.place_forget()
            #Place available items frame
            availableitems_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            #Get item data from file
            with open("data/stock/Home&Kitchen/Utensils.txt", "r") as items_file:
                items_file_data = items_file.readlines()

            items_ids = [items_file_data[i].replace('\n', '') for i in range(0, len(items_file_data), 4)]
            items_names = [items_file_data[n].replace('\n', '') for n in range(1, len(items_file_data), 4)]
            items_prices = [items_file_data[p].replace('\n', '') for p in range(2, len(items_file_data), 4)]
            items_stocks = [items_file_data[s].replace('\n', '') for s in range(3, len(items_file_data), 4)]
            
            #available items labels
            availableitemidsheading_label.place(x = 500, y = 150)
            availableitemnamesheading_label.place(x = 640, y = 150)
            availableitempricesheading_label.place(x = 760, y = 150)
            availableitemqtysheading_label.place(x = 880, y = 150)
            availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemids_label.place(x = 500, y = 200)
            availableitemids_label.configure(text = ("\n".join(items_ids)))
            availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemnames_label.place(x = 620, y = 200)
            availableitemnames_label.configure(text = ("\n".join(items_names)))
            availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemprices_label.place(x = 760, y = 200)
            availableitemprices_label.configure(text = ("\n".join(items_prices)))
            availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
            availableitemqtys_label.place(x = 880, y = 200)
            availableitemqtys_label.configure(text = ("\n".join(items_stocks)))
            availableitemids_label.configure(font = 3)
            availableitemnames_label.configure(font = 3)
            availableitemprices_label.configure(font = 3)
            availableitemqtys_label.configure(font = 3)

        #Add item to cart
        def addToCart():
            #Get entered item id and qty
            item_id = item_id_textbox.get("1.0", "end")
            qty = item_qty_textbox.get("1.0", "end")
            try:
                cart.add(item_id, qty)
                result_label.place(x = 800, y = 600)
                result_label.configure(text = "Item added to cart")
            except UnboundLocalError:
                result_label.place(x = 800, y = 600)
                result_label.configure(text = "Invalid item id")

        #Go back to item shelf
        def back_shelf():
            #Remove item frame
            item_frame.place_forget()
            shelves_frame.place(relheight = 1, relwidth = 1, relx = 0.5, rely = 0.5, anchor = CENTER)

        #Go back to item category
        def back_category():
            #Place item frame
            item_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
            availableitems_frame.place_forget()

        #AVAILABLE ITEMS FRAME
        availableitems_frame = Frame(window, bg = "Black", height = "700", width = "400")
        #display background image label
        background_label = Label(availableitems_frame, image = background_image)
        background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #available items headings labels
        availableitemidsheading_label = Label(availableitems_frame, bg = "Black", fg = "White", text = "ID", font = 3)
        availableitemnamesheading_label = Label(availableitems_frame, bg = "Black", fg = "White", text = "NAME", font = 3)
        availableitempricesheading_label = Label(availableitems_frame, bg = "Black", fg = "White", text = "PRICE", font = 3)
        availableitemqtysheading_label = Label(availableitems_frame, bg = "Black", fg = "White", text = "STOCK", font = 3)
        availableitemids_label = Label(availableitems_frame, bg = "Black", fg = "White")
        availableitemnames_label = Label(availableitems_frame, bg = "Black", fg = "White")
        availableitemprices_label = Label(availableitems_frame, bg = "Black", fg = "White")
        availableitemqtys_label = Label(availableitems_frame, bg = "Black", fg = "White")
        #ITEM FRAME
        item_frame = Frame(window, height = "700", width = "400", bg = "Black")
        #display background image label
        background_label = Label(item_frame, image = background_image)
        background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        item_frame.place(relheight = 1 , relwidth = 1 , relx = 0.5, rely = 0.5, anchor = CENTER)
        #available items labels
        availableitems_label = Label(item_frame, bg = "White", fg = "Black", text = "AVAILABLE ITEMS", font = 3, width = 50, height = 3)
        availableitems_label.place(x = 500, y = 200)
        #available items buttons
        male_button = Button(item_frame, bg = "Black", fg = "White", text = "Male", height = 2, width = 15, command = male)
        female_button = Button(item_frame, bg = "Black", fg = "White", text = "Female", height = 2, width = 15, command = female)
        child_button = Button(item_frame, bg = "Black", fg = "White", text = "Children", height = 2, width = 15, command = child)
        unisex_button = Button(item_frame, bg = "Black", fg = "White", text = "Unisex", height = 2, width = 15, command = unisex)
        vegetables_button = Button(item_frame, bg = "Black", fg = "White", text = "Vegetables", height = 2, width = 15, command = vegetables)
        meats_button = Button(item_frame, bg = "Black", fg = "White", text = "Meats", height = 2, width = 15, command = meats)
        beverages_button = Button(item_frame, bg = "Black", fg = "White", text = "Beverages", height = 2, width = 15, command = beverages)
        spices_button = Button(item_frame, bg = "Black", fg = "White", text = "Spices", height = 2, width = 15, command = spices)
        laptops_button = Button(item_frame, bg = "Black", fg = "White", text = "Laptops", height = 2, width = 15, command = laptops)
        desktops_button = Button(item_frame, bg = "Black", fg = "White", text = "Desktops", height = 2, width = 15, command = desktops)
        smartphones_button = Button(item_frame, bg = "Black", fg = "White", text = "Smartphones", height = 2, width = 15, command = smartphones)
        smartwatches_button = Button(item_frame, bg = "Black", fg = "White", text = "Smartwatches", height = 2, width = 15, command = smartwatches)
        cookware_button = Button(item_frame, bg = "Black", fg = "White", text = "Cookware", height = 2, width = 15, command = cookware)
        silverware_button = Button(item_frame, bg = "Black", fg = "White", text = "Silverware", height = 2, width = 15, command = silverware)
        crockery_button = Button(item_frame, bg = "Black", fg = "White", text = "Crockery", height = 2, width = 15, command = crockery)
        utensils_button = Button(item_frame, bg = "Black", fg = "White", text = "Utensils", height = 2, width = 15, command = utensils)
        back_button = Button(item_frame, text = "Back", bg = "Black", fg = "Orange", height = 2, width = 15, command = back_shelf)
        back_button.place(x = 670, y = 350)

        #Check if account type is customer
        if self.acc_type == "C":
            #Display item add to cart option for customer
            item_id_label = Label(availableitems_frame, bg = "Black", fg = "White", text = "Item id: ", font = 3)
            item_id_label.place(x = 500, y = 400)
            item_id_textbox = Text(availableitems_frame, height = 1, width = 20, font = ("Helvetica", 14))
            item_id_textbox.place(x = 600, y = 400)
            item_qty_label = Label(availableitems_frame, bg = "Black", fg = "White", text = "Item qty: ", font = 3)
            item_qty_label.place(x = 500, y = 500)
            item_qty_textbox = Text(availableitems_frame, height = 1, width = 10, font = ("Helvetica", 14))
            item_qty_textbox.place(x = 600, y = 500)
            addtocart_button = Button(availableitems_frame, text = "add to cart", bg = "Black", fg = "Orange", height = 2, width = 15, command = addToCart)
            addtocart_button.place(x = 500, y = 600)
            back_button = Button(availableitems_frame, text = "Back", bg = "Black", fg = "Orange", height = 2, width = 15, command = back_category)
            back_button.place(x = 650, y = 600)
            result_label = Label(availableitems_frame, bg = "Black", fg = "White", font = 3)
        else:
            #Only dislplay back button for admin
            back_button = Button(availableitems_frame, text = "Back", bg = "Black", fg = "Orange", height = 2, width = 15, command = back_category)
            back_button.place(x = 650, y = 600)

        #Check chosen category and place buttons accordingly
        if self.chosen_category == "C":
            male_button.place(x = 470, y = 300)
            female_button.place(x = 600, y = 300)
            child_button.place(x = 730, y = 300)
            unisex_button.place(x = 860, y = 300)
        elif self.chosen_category == "F":
            vegetables_button.place(x = 470, y = 300)
            meats_button.place(x = 600, y = 300)
            beverages_button.place(x = 730, y = 300)
            spices_button.place(x = 860, y = 300)
        elif self.chosen_category == "E":
            laptops_button.place(x = 470, y = 300)
            desktops_button.place(x = 600, y = 300)
            smartphones_button.place(x = 730, y = 300)
            smartwatches_button.place(x = 860, y = 300)
        elif self.chosen_category == "HK":
            cookware_button.place(x = 470, y = 300)
            silverware_button.place(x = 600, y = 300)
            crockery_button.place(x = 730, y = 300)
            utensils_button.place(x = 860, y = 300)

#Creating main object
main = Main()
#Creating cart object
cart = Cart(receipt_code)

window.mainloop()