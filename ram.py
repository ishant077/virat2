m=[1,3,5,7,8,6,9]
key=int(input("enter key element to be searchead"))
for i in range(len(m)):
    if key==m[i]:
        print("element find at posative")
        break
    else:
        print("element not present in the list")