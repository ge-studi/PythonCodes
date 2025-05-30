# Read a text and convert it into upper case and write in second file

# Open the first file in read mode
with open("abc.txt","r") as fo:
    content = fo.read()
    
upper_content = content.upper() # convert first file into upper case

# write in second file
with open("xyz.txt","w") as fw:
    fw.write(upper_content)
  


