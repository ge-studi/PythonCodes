data = input("Enter sample data: ")
print("Sample data :",data)
mylist=data.split(",") #convert data into list. List is mutable.
print("List :",mylist)
mylist=tuple(mylist) #convert list into tuple.Tuple is immutable.
print("Tuple :",mylist)