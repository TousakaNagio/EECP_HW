import sys
import os
import math

n = int(sys.argv[1])

def print_level_two_tree():
    """(10 pts) Print Out Level Two Tree

    You have to print out a level two tree in this part.
    If you don't have what a level two tree look like, you can use 'hw1_example.py' to generate a level two tree.
    It will look like this:
    
            /*\
           /***\
          /*****\
       /***********\
      /*************\
     /***************\
    /********|********\

    """
    print(" "*8+'/'+'*'+'\\')
    print(" "*7+'/'+'***'+'\\')
    print(" "*6+'/'+'*****'+'\\')
    print(" "*3+'/'+'***********'+'\\')
    print(" "*2+'/'+'*************'+'\\')
    print(" "*1+'/'+'***************'+'\\')
    print(" "*0+'/'+'*'*8+'|'+'*'*8+'\\')
    pass

def find_middle(n):
    """(10 pts) Find the Middle Line of the Tree
    
    In this part, you have to find the middle line of the tree and return the distance from the middle line to 
    left end.
    For example, if the input number is 2, you have to find the middle line of a level two tree and return the
    distance to left end that is 10.

            /*\
           /***\
          /*****\
       /***********\
      /*************\
     /***************\
    /********|********\
    1234567891
             0
    
    Similarly, if the input number is 3, you have to return 17.

                   /*\
                  /***\
                 /*****\
              /***********\
             /*************\
            /***************\
           /*****************\
        /***********************\
       /*************************\
      /************|||************\
     /*************|||*************\
    /**************|||**************\
    12345678911111111
             01234567
    """
    if (n==1):
        return 4
    elif (n==2):
        return 10
    else:
        count = int(17)
        for i in range(3,n+1):
            count += 2*(i//2+1)
            for j in range(1,i+3):
                count += 2
    return int((count-1)/2+2)

    pass

def print_level_n_tree(n):
    """(50 pts) Print Out Level N Tree
    
    In this part, you have to print the level n tree which n is a integer.
    You can use 'hw1_example.py' to take a look what a level n tree looks like.
    For example, if the input number is 2, you have to print out a level two tree, and it will looks like:
 
            /*\
           /***\
          /*****\
       /***********\
      /*************\
     /***************\
    /********|********\
    
    If the input number is 5, your tree will looks like:

                                      /*\
                                     /***\
                                    /*****\
                                 /***********\
                                /*************\
                               /***************\
                              /*****************\
                           /***********************\
                          /*************************\
                         /***************************\
                        /*****************************\
                       /*******************************\
                   /***************************************\
                  /*****************************************\
                 /*******************************************\
                /*********************************************\
               /***********************************************\
              /*************************************************\
          /*********************************************************\
         /***********************************************************\
        /****************************|||||****************************\
       /*****************************|||||*****************************\
      /******************************|||@|******************************\
     /*******************************|||||*******************************\
    /********************************|||||********************************\

    Image that n is a big number. You tree must be huge.
    !!! Notice that your result must the same as what 'hw1_example.py' print out. !!!


    """
    if n==1:
        print(' '*2+'/'+'*'+'\\')
        print(' '*1+'/'+'***'+'\\')
        print(' '*0+'/'+'*****'+'\\')
        return None

    if n==2:
        print_level_two_tree()
        return None

    print(' '*int(find_middle(n)-2)+'/'+'*'+'\\')
    print(' '*int(find_middle(n)-3)+'/'+'***'+'\\')
    print(' '*int(find_middle(n)-4)+'/'+'*****'+'\\')
    print(' '*int(find_middle(n)-7)+'/'+'***********'+'\\')
    print(' '*int(find_middle(n)-8)+'/'+'*************'+'\\')
    print(' '*int(find_middle(n)-9)+'/'+'***************'+'\\')
    print(' '*int(find_middle(n)-10)+'/'+'*'*17+'\\')

    count = int(17)

    if(n==3):
        count += 2*(n//2+1)
        count += 2
        print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
        count += 2
        print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
        for i in range(1,n+1):
                count += 2
                print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*int((count-n)/2)+'|'*n+'*'*int((count-n)/2)+'\\')
    elif(n==4):
        for i in range(3,n):
            count += 2*(i//2+1)
            for j in range(1,i+3):
                count += 2
                print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
        i += 1
        count += 2*(n//2+1)
        count += 2
        print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
        count += 2
        print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
        count += 2
        print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
        for i in range(1,n):
                count += 2
                print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*int((count-n+1)/2)+'|'*(n-1)+'*'*int((count-n+1)/2)+'\\')

    elif(n>=5):
        
        for i in range(3,n):
            count += 2*(i//2+1)
            for j in range(1,i+3):
                count += 2
                print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
        i += 1
        count += 2*(i//2+1)
        if(n%2==1 and n>=5):
            count += 2
            print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
            count += 2
            print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
            for i in range(1,n+1):
                if(i==(n//2+1)):
                    count += 2
                    print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*int((count-n)/2)+'|'*(n//2+1)+'@'+'|'*(n//2-1)+'*'*int((count-n)/2)+'\\')
                else:
                    count += 2
                    print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*int((count-n)/2)+'|'*n+'*'*int((count-n)/2)+'\\')
        else:
            count += 2
            print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
            count += 2
            print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
            count += 2
            print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*count+'\\')
            for i in range(1,n):
                if(i==((n-1)//2+1)):
                    count += 2
                    print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*int((count-n+1)/2)+'|'*((n-1)//2+1)+'@'+'|'*((n-1)//2-1)+'*'*int((count-n+1)/2)+'\\')
                else:
                    count += 2
                    print(' '*int(find_middle(n)-((count-1)/2+2))+'/'+'*'*int((count-n+1)/2)+'|'*(n-1)+'*'*int((count-n+1)/2)+'\\')
    pass

def Diffie_Hellman_cracker(p, g, A, B):
    
    """(30 pts) Diffie Hellman cracker
    In this part, you need to implement a function which can enter four numbers as 
    parameters and find out the private key a ,b and common number K then return those numbers.
    
    """
    k = []
    j = False
    for a in range(1,p):
        for b in range(1,p):
            if(g**a%p==A and g**b%p==B):
                if(B**a%p==A**b%p):
                    #print(a,b,B**a%p)
                    if(j == False):
                        k.append(a)
                        k.append(b)
                        k.append(B**a%p)
                        j = True 
                    #return
    """
    print('(',end='')
    print(",".join(str(i) for i in k),end='')
    print(')',end='\n')
    """
    return tuple(k)
    pass


print_level_n_tree(n)
print('\n')

print_level_n_tree(2)
print(find_middle(2))
print(find_middle(3))
print(Diffie_Hellman_cracker(11,3,4,9))