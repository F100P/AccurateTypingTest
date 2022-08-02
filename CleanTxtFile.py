from xml.etree.ElementInclude import include

## klar med denna fil kör inte igen haha

# with open('VanligaOrd.txt') as f:
#     lines = f.readlines()
#     # for line in lines : 
#     #     if 
#     #         print(line)
# with open("VanligaOrd.txt", "w") as f:
#     for line in lines:
#         if not " " in line :

# with open('OrdArray.txt', 'a+') as file_object:
#     file_object.write("[")
#     with open('VanligaOrd.txt') as f:
#         lines = f.readlines()
#     for line in lines:
#         file_object.write('"')
#         file_object.write(line)
#         file_object.write('"')
#         file_object.write(",")

# file_object.write("]")
# file_object.close



with open('OrdArray.txt') as f:
    lines = f.readlines()
    # for line in lines : 
    #     if 
    #         print(line)
with open("OrdArray.txt", "w") as f:
    for line in lines:
        newstr = line.strip()
        f.write(newstr)
