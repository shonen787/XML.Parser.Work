import xml.etree.ElementTree as ET
import os.path
global files
files = 0
context = ET.iterparse('file.xml', events=('end', ))
tree = ET.parse('file.xml')
root = tree.getroot()
leftover = 0
save_path = './files/'

def Amount_of_files():
    children = 0
    for child in root:
        children += 1
    print children, " Children"
    files = children / 10
    print files, " Files"
    leftover = children % 10
    if leftover != 0:
        files +=1
    print "We will make", files ,"files"
    print "One file will contain", leftover ,"tags"
    return files

def Copy_contents():
    index = 0
    for event, elem in context:
            if elem.tag == 'HEADER':
                completeName = os.path.join(save_path,"header.xml")
                filename = completeName
                with open(filename, 'wb') as f:
                    f.write(ET.tostring(elem))
            if elem.tag == 'IP':
                completeName = os.path.join(save_path, str(index)+".1xml"   )
                filename = completeName
                index += 1
                with open(filename, 'wb') as f:
                    f.write(ET.tostring(elem))

def Merger():
    current_new_file = 0
    current_old_file = 0
    iptags = 0
    header = 0
    print "entering while loop"
    print current_new_file
    files = Amount_of_files()
    print files
    while (current_new_file < files):
        print "entered while loop"
        newfilename = os.path.join(save_path,str(current_new_file)+".xml")
        iptags = 0
        print "writing to ", newfilename
        while iptags < 10:
            if header == 0:
                header = open(os.path.join(save_path,'header.xml'))
                header_contents = header.read()
                header.close()
                f3 = open(newfilename, "a+")
                f3.write(header_contents)
                f3.close()
                header = 1
            completeName = os.path.join(save_path,str(current_old_file)+".1xml")
            if os.path.isfile(completeName) == False:
                print "entered"
                return
            f1 = open(completeName)
            f1_contents = f1.read()
            f1.close()
            f3 = open(newfilename, "a+") # open in `w` mode to write
            f3.write(f1_contents) # concatenate the contents
            f3.close()
            print "Removing, ", completeName
            current_old_file +=1
            completeName = os.path.join(save_path,str(current_old_file)+".1xml")
            if os.path.isfile(completeName) == False:
                print "entered"
                return
            f2 = open(completeName)
            f2_contents = f2.read()
            f2.close()
            print "Removing, ", completeName
            current_old_file += 1
            f3 = open(newfilename, "a+") # open in `w` mode to write
            f3.write(f2_contents) # concatenate the contents
            f3.close()
            iptags = iptags + 1
        current_new_file = current_new_file + 1
        header = 0

def Clean_up():
    files = Amount_of_files
    current = 0
    while current < files:
        completeName = os.path.join(save_path,str(current)+".1xml")
        if os.path.isfile(completeName) == False:
            print "entered"
            return
        os.remove(completeName)
        current = current + 1

def main():
    Amount_of_files()
    Copy_contents()
    print "Starting the mergert"
    Merger()
    print "Finished the merger"
    print "Clean up time"
    Clean_up()

main()
#f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
