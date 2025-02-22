from chatbook_proj import chatbook
#create user from here and then use the chatbook
# user1=chatbook()
# print(user1.__name)# this is not accessable beacause when we create attrubute using
# __ then it save like obj_classname__name   (this called encapsulation concept)
# print(user1._chatbook__name)
# you cant fully protect your data in python python developers explain that matured persons are working on 
# python not all are fool 

# Getter and setter
# print(user1.getter())
# user1.set_name("soniya")
# print(user1.getter())
#
#Statics variable
# user1=chatbook()
# print(user1.id)

# user2=chatbook()
# print(user2.id)

# user3=chatbook()
# print(user3.id)

# Static method call
user1=chatbook()
print(user1.id)

chatbook.set_id(10)
user2=chatbook()
print(user2.id)
