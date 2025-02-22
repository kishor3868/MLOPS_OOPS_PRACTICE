class chatbook:
    __user_id =1 # static value
    def __init__(self):
        self.__name="Default user"# using encapsulation in python
        self.id = chatbook.__user_id # class access the static attribute 
        chatbook.__user_id +=1
        self.username=""
        self.password=""
        self.loggedin=False
        # self.menu()

    def getter(self):# these are the method to get the hidden attribute and set the hidden attreibute
        return self.__name
    def set_name(self,value):#setter
        self.__name=value
    @staticmethod
    def get_id():
        return chatbook.__user_id
    @staticmethod
    def set_id(value):
        chatbook.__user_id=value


    def menu(self):
        user_input =input ("""**Welcome to the chatbook | How would you like to proceeds
                      1. Press 1 to singup
                      2. Press 2 to singin
                      3. Press 3 to write a post
                      4. Press 4 to msg a friend
                      5. Press any key to exit()
                           ==> """)

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.post()
        elif user_input== "4":
            self.msg()
        else:
            print("Welcome back")
            exit()
    def signup(self):
        email=input("Enter user name ==> ")
        password=input("Set you password ==> ")
        self.username=email
        self.password=password 
        print("Signup succesful ")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username=="" and self.password=="":
            print("Please first do signup in main menu")
        else:
            uname=input("Enter your username here ==> ")
            upass=input("Enter your password ==> ")
            if self.username==uname and self.password==upass:
                print("SingedIn Succesfully")
                self.loggedin=True 
            else:
                print("Incorrect username and password")
        print("\n")
        self.menu()    
    def post(self):
        if self.loggedin==True:
            post=input("Write a post==> ")
            print(f"Your post is published==> {post}")
        else:
            print("you need to do signin first by pressing 2 in menu")
        print("\n")
        self.menu()
    def msg(self):
        if self.loggedin==True:
            friend_name=input("Whom you want to send a msg=>")
            msg=input("Write a message here ==> ")
            print(f"Your msg has been sent to {friend_name}")
        else:
            print("You need to sign in first to send msg to your friend")
        print("\n")
        self.menu()


        
        


    
# user1=chatbook()       