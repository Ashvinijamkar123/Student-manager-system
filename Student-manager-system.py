db={101:{"name":"Ashvini","city":"nashik","per":85,"Course":"python"}}
print("-"*115)
print("Student management system".center(130))
print("-"*115)
while True:
    print("""
            Dashboard
          1.Add student details
          2.display student details
          3.update student details
          4.delete student details
          5.filter student details
          6.Break
""")
    ch=int(input("Enter your choice: "))
    if ch==1:
        Reg_no=eval(input("Enter Reg_no:"))
        name=input("Enter name:")
        city=input("Enter city:")
        per=eval(input("Enter per:"))
        course=input("Enter course:")
        db[Reg_no]={"name":name,"city":city,"per":per,"Course":course}
        print("Added successfully...")
    elif ch==2:
        print("-"*105)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Reg_no","name","city","percentag","course"))
        print("-"*105)
        for i in db:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["city"],db[i]["per"],db[i]["Course"]))
            print("-"*105)
    elif ch==3:
        Reg_no=eval(input("Enter Reg_no:"))
        print("""
        1.name
        2.city
        3.per
        4.course      
    """)
        ch=int(input("Enter your choice: "))
        if ch==1:
            uname=input("Enter name:")
            db[Reg_no]["name"]=uname
            print("updated successfully..")

        elif ch==2:
            ucity=input("Enter city:")
            db[Reg_no]["city"]=ucity
            print("updated successfully..") 
        elif ch==3:
            uper=input("Enter per:")
            db[Reg_no]["per"]=uper
            print("updated successfully..") 
        elif ch==4:
            ucourse=input("Enter course:")
            db[Reg_no]["course"]=ucourse
            print("updated successfully..")
        else:
            print("invalid input")
    elif ch==4:
        Reg=eval(input("Enter Reg_no:"))
        del db[Reg]
        print("delete successfully..")

    elif ch==5:
        print("""
        1.name
        2.city
        3.per
        4.course      
    """)
        print("-"*105)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("Reg_no","name","city","percentag","course"))
        print("-"*105)
        for i in db:
            if db[i]["city"]==city:
                print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["city"],db[i]["per"],db[i]["course"]))
                print("-"*105)
            elif ch==1:
                    if db[i]["course"]==course:
                        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["city"],db[i]["per"],db[i]["course"]))
                        print("-"*105)

            elif ch==3:
                    if db[i]["per"]==per:
                        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["city"],db[i]["per"],db[i]["course"]))
                        print("-"*105)
            else:
                    print("invalid input")
    else:
            print("invalid choice:")                