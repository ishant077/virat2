def insert():
    global rear
    if(rear==size-1):
        print("queue is full:")
        return
    item=int(input("Enter the element to be inserted:"))
    rear+=1
    x.insert(rear,item)
def delete():
    global front
    if(front>rear):
        print("queue is empty:")
        return
    print("elementerd deleted is",x[front])
    front+=1
def display():
    if(front>rear):
        print("queue is empty:")
        return
    for i in range(front,rear+1):
        print(x[i])
        x=[]
        size=5
        rear=-1
        front=0
        while True:
            print("1:insert 2:delete 3:display")
            ch=int(input("enter your choice:"))
            if(ch==1):
                insert()
            elif(ch==2):
                delete()
            elif(ch==3):
                display()
            else:
                print("wrong choice")
