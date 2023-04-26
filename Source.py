# Task - D 
def main():
    var=0
    while True:
        print('-------------------------------------------------------------------------')
        print('1.  Create Dictionary of Books.')
        print('2.  Remove an item from Dictionary.')
        print('3.  Delete Dictionary.')
        print('4.  Search specific item from dictionary.')
        print('5.  Insert an item to dictionary.')
        print('6.  Update a specific value from dictionary.')
        print('7.  Count number of items in dictionary.')
        print('8.  To Exit the program.')
        print('-------------------------------------------------------------------------')
        x=int(input('\nEnter here = '))
        if x==1:
            dictionary={}
            var+=1
            print('New Empty Dictionary is created :)')
        elif x==2:
            if var==0:
                print('No Dictionary Found X(\n create the dictionary first')
            elif len(dictionary)==0:
                print('Dictioanry is already empty :(')                
            else:
                while True:
                    print(dictionary)
                    key=str(input('Enter the key to remove that item = '))
                    if key in dictionary:
                        dictionary.pop(key)
                        print('Item removed :)')
                        print(dictionary)
                        break
                    else:
                        print('Wrong input X(\n try again')
        elif x==3:
            if var==0:
                 print('No Dictionary Found X(\n create the dictionary first')
            else :
                del dictionary
                var=0
                print('Dictionary is deleted successfully')
        elif x==4:
            if var==0:
                print('No Dictionary Found X(\n create the dictionary first')
            elif len(dictionary)==0:
                print('Dictioanry is already empty :(')                
            else:
                print(dictionary)
                key=str(input('Enter the key name to find = '))
                if key in dictionary:
                    print(dictionary[key])
                else:
                    print('No item found :(')
        elif x==5:
            if var==0:
                print('No Dictionary Found X(\n create the dictionary first')
            else:
                key=input('Enter the name of key = ')
                while True:
                    print('Enter 1 for entering integer type item.')
                    print('Enter 2 for entering string type item.')
                    print('Enter 3 for entering float type item.')
                    print('Enter 4 for entering bool type item.')
                    check=int(input('Enter here = '))
                    if check==1:
                        item=int(input('Enter integer item data = ')) 
                        break
                    elif check==2:
                        item=str(input('Enter string item data = ')) 
                        break
                    elif check==3:
                        item=float(input('Enter float item data = '))
                        break
                    elif check==4:
                        item=bool(input('Enter bool item data = '))
                        break
                    else:
                        print('Wrong Input :(\n Try again')
                dictionary[key]=item
                print('New item is Added :)')
                print(dictionary)
                var+=1
        elif x==6:
            if var==0:
                print('No Dictionary Found X(\n create the dictionary first')
            elif len(dictionary)==0:
                print('Dictionary is already empty :(') 
            else :
                while True:
                    print(dictionary)
                    key=str(input('Enter the name of key = '))
                    if key in dictionary.keys():
                        while True:
                            print('Enter 1 for entering integer type item.')
                            print('Enter 2 for entering string type item.')
                            print('Enter 3 for entering float type item.')
                            print('Enter 4 for entering bool type item.')
                            check=int(input('Enter here = '))
                            if check==1:
                                item=int(input('Enter integer item data = ')) 
                                break
                            elif check==2:
                                item=str(input('Enter string item data = ')) 
                                break
                            elif check==3:
                                item=float(input('Enter float item data = '))
                                break
                            elif check==4:
                                item=bool(input('Enter bool item data = '))
                                break
                            else:
                                print('Wrong Input :(\n Try again')
                            break
                        dictionary.update({key:item}) 
                        print('Item is updated successfully :)')  
                        print(dictionary)                     
                        break
                    else:
                        print('Key error!!\nNo key found to update\nTry again...')
        elif x==7:
            if var==0:
                print('No Dictionary Found X(\n create the dictionary first')
            else:
                print(dictionary)
                print('Total item length is = ',len(dictionary))
        elif x==8:
            print('Thank you for your time :)')
            break
        elif x>=9 or x<=0:
            print('Wrong Input\nTry Again by Enterying correct Value')
        x=int(input('\nEnter \'1\' to continue and \'0\' to exit = '))   
        if x==1:
            continue
        else:
            print('Thank you for your time :)')
            break    
main()