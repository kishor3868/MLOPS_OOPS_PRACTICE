class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.menu()

    def menu(self):
        user_input =input ("""**Welcome to the chatbook | How would you like to proceeds
                      1. Press 1 to singup
                      2. Press 2 to singin
                      3. Press 3 to write a post
                      4. Press 4 to msg a friend
                      5. Press any key to exit()
                           ==> """)

        if user_input == "1":
            self.singup()
        elif user_input == "2":
            self.singin()
        elif user_input == "3":
            self.post()
        elif user_input== "4":
            self.msg()
        else:
            print("Welcome back")
            exit()
user1=chatbook()       