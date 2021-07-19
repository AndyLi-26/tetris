tetriminos=[[1, 1, 1, 1], [[2, 0, 0], [2, 2, 2]], [[0, 0, 3], [3, 3, 3]], [[4, 4], [4, 4]], [[0, 5, 5], [5, 5, 0]], [[0, 6, 0], [6, 6, 6]], [[7, 7, 0], [0, 7, 7]]]
def prt_list(alist):
    for i in alist:
        if type(i)==type([]) and type(i[0])==type([]):
            prt_list(i)
        else:
            print(i)
            
                
if __name__=="__main__":
    for i in tetriminos:
        prt_list(i)
        print()
