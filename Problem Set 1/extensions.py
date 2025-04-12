#input file name, use lower() and use replace to replace . with space
name=input("File name:").lower().replace("."," ").split()
#now compare the last name of your file
x=len(name)-1
match name[x]:
    case 'gif': print("image/gif")
    case 'jpg': print("image/jpg")
    case 'jpeg': print("image/jpg")
    case 'png': print("image/png")
    case 'pdf': print("application/pdf")
    case 'txt': print("application/txt")
    case 'zip':print("application/zip")
    case _: print("application/octet-stream")