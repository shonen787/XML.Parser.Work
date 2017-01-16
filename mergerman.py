import os.path
save_path = './files/'

def merge(totalfiles):
    current_new_file = 0
    current_old_file = 1
    iptags = 0
    header = 0
    while current_new_file < int(totalfiles) :
        newfilename = os.path.join(save_path,str(current_new_file)+".xml")
        iptags = 0
        while iptags < 10:
            if header == 0:
                header = open('header.xml')
                header_contents = header.read()
                header.close()
                f3 = open(newfilename, "w")
                f3.write(header_contents)
                f3.close()
                header = 1
            completeName = os.path.join(save_path,str(current_old_file)+".1xml")
            f1 = open(completeName)
            f1_contents = f1.read()
            f1.close()
            print "Removing, ", current_old_file
            os.remove(current_old_file)
            current_old_file +=1
            completeName = os.path.join(save_path,str(current_old_file)+".1xml")
            f2 = open(completeName)
            f2_contents = f2.read()
            f2.close()
            print "Removing, ", current_old_file
            os.remove(current_old_file)
            current_old_file += 1
            f3 = open(newfilename, "w") # open in `w` mode to write
            f3.write(f1_contents + f2_contents) # concatenate the contents
            f3.close()
            iptags +=1
        current_new_file += 1
