# Python program to display the examination schedule. 
# exam_st_date=(11, 12, 2014)
# print("The examination will start from :  %i / %i / %i" % exam_st_date)

data =input("Enter data")
exam_st_date = tuple(map(int, data.split(",")))
print("The examination will start from :  %i / %i / %i" % exam_st_date)