try:
    fh=open("myfile","w")
    try:
        fh.write("this is myfile for exception handling !!")
    finally:
        print("closing the file")
        fh.close()
except IOError:
    print ("Error: can not find file")
    
