def ins_stk(el):
    stk.append(el)
def del_stk():
    try:
        print("element deleted is", stk.pop())
    except:
        print("underflow")
        print()
def dis_stk():
    for i in stk:
        print("%.4f" % i)
stk=[]
while True:
    print("1. insert into stack")
    print("2. delete from stack")
    print("3. display stack")
    print("0. exit")
    a=int(input("enter your choice: "))
    if a==1:
        e = eval(input("enter element to be added: "))
        ins_stk(e)
    elif a==2:
        del_stk()
    elif a==3:
        dis_stk()
    elif a==0:
        break
    else:
        print("wrong choice")