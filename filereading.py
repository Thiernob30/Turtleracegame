file_object = open('test.txt','r' )

for lines in file_object:
    each_line = lines.split('.')
    Try:
        print(each_line[9]
        except:
            print("specified index is invalid")
