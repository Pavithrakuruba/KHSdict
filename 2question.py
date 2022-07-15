# k program likhiye jisse ki agar di hui key pehle se dictionary me
#  exist karti ho toh “exists “ print kare aur agar nahi karti ho toh
#  “not exists” print kare. Example :


dict={"name":"Raju", "marks":56}
name=input("enter the name")
if name in dict:
    print("exists")
else:
    print("not exists")

