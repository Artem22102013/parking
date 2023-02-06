import time
t = time

locked = "n"


print("<welcome> Welcome to parking! </welcome>")
print("<start> For start type : /park </start>")
print()
print("<hint> At the and type '[SPACE]</cm>' </hint>")
print()
print("<commands> Type /park for start </commands>")
print("<commands> Type /lock for lock your car </commands>")
print("<commands> Type /unlock for unlock your car </commands>")
print("<commands> Type /end to end your parking </commands>")
awnser = ""

while True:
    while awnser != "/end </cm>":
        end = 'no'
        awnser = input("<cm> ")
        if awnser == "/park </cm>":
            print("<bot>You have been parked!</bot>")
        if awnser == "/lock </cm>":
            key = input("Input your keyword: ")
            print("<bot> You have been locked your car! </bot>")
            locked = 'yes'
        if awnser == "/unlock </cm>":
            unlock_key = input("Your keyword: ")
            if unlock_key == key:
                print("<bot>You have been unlocked your car </bot>")
                locked = 'no'
            else:
                print("<bot> Keyword isn't correct! </bot>")
                print("<bot> Vechile is locked! </bot>")
        if awnser == "/end </cm>" and locked == 'no':
            print("<bot> Goodbye! </bot>")
            end = 'yes'
    for x in range(50):
        print()
    t.sleep(2)
    print("<debuger> Hiding HTML ... </debuger>")
    t.sleep(2)
    print(" HTML Hided! ")
    t.sleep(2)
    print(" Hiding spaces ... ")
    t.sleep(2)
    print("Spaces hided!")
    t.sleep(2)
    for x in range(50):
        print()