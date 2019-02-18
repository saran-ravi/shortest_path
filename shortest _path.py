from collections import deque

class CircularQueue:

    #Constructor
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = 54
        
    def reset(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = 54
        return


    #Adding elements to the queue
    def enqueue(self,data):
        if self.size() == self.maxSize-1:
            return ("Queue Full!")
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return True

    #Removing elements from the queue
    def dequeue(self):
        if self.size()==0:
            return ("Queue Empty!") 
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data

    #Calculating the size of the queue
    def size(self):
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.maxSize - (self.head-self.tail))

n = 54
adj = [[2,4,-1], [1,5,-1], [4,8,-1], [1,3,9], [2,6,10], [5,11,-1], [8,13,-1], [3,7,14], [4,10,15], [5,9,16], [6,12,17], [11,18,-1], [7,19,-1], [8,15,20], [9,14,21], [10,17,22], [11,16,23], [12,24,-1], [13,20,25], [14,19,26], [15,22,27], [16,21,28], [17,24,29], [18,23,30], [19,31,-1], [20,27,32], [21,26,33], [22,29,34], [23,28,35], [24,36,-1], [25,32,37], [26,31,38], [27,34,39], [28,33,40], [29,36,41], [30,35,42], [31,43,-1], [32,39,44], [33,38,45], [34,41,46], [35,40,47], [36,48,-1], [37,44,-1], [38,43,49], [39,46,50], [40,45,51], [41,48,52], [42,47,-1], [44,50,-1], [45,49,53], [46,52,54], [47,51,-1], [50,54,-1], [51,53,-1]];
arena = [[2,9,4,5,1,10], [4,14,8,9,3,15], [10,21,15,16,9,22], [6,16,10,11,5,17], [8,19,13,14,7,20], [15,26,20,21,14,27], [22,33,27,28,21,34], [17,28,22,23,16,29], [12,23,17,18,11,24], [20,31,25,26,19,32], [27,38,32,33,26,39], [34,45,39,40,33,46], [29,40,34,35,28,41], [24,35,29,30,23,36], [32,43,37,38,31,44], [39,49,44,45,38,50], [46,53,50,51,45,54], [41,51,46,47,40,52], [36,47,41,42,35,48]]
swap = [43, 49, 53, 54, 52, 48, 42 , 30, 18]
traverse = [];
g = 0
visited = [0] * n
dist = [-1] * n
pred = [-1] * n
axis_new = 0
#path = [-1] * 2*n
queue = CircularQueue()
node = 0
psnode = 0
pvnode = 0
pvnodex = 0

path = [[-1 for i in range(n)] for j in range(2)]



def bfs(source, dest):
    queue.reset()
    front = rear = -1
    for i in range(n):
        visited[i] = 0
        dist[i] = -1
        pred[i] = -1
    
    visited[source-1] = 1
    dist[source-1] = 0
    queue.enqueue(source)
        
    while queue.size() != 0:
        a = queue.dequeue()
        for i in range(3):
            b = adj[a-1][i]
            if b != -1:
                if visited[b-1] == 0:
                    visited[b-1] = 1
                    dist[b-1] = dist[a-1] + 1
                    pred[b-1] = a
                    queue.enqueue(b)
                    if b == dest:
                        return 1
    return 0
            
def shortestPath(source, dest,index):
    z = bfs(source, dest)
    if z == 0:
        print ("Given source and destination not connected.")
        return
    
    #print("source,dest ",source,dest)
    crawl = dest
    c = 0
    path[index][c]=dest
    c=c+1
    while pred[crawl-1] != -1:
        crawl = pred[crawl-1]
        #print('    c      : ',c)
        path[index][c] = crawl
        c = c + 1    

    #print ("Shortest path length is : ",dist[dest-1])
    #print ("Path is: ")
    #for i in range (c-1, -1, -1):
        #print (path[i], ' ')
    return int(dist[dest-1])

###############################################################################

def configuration(node):
        
        config = None
        conf = -1
        if node in swap:
            conf = conf * -1
        for j in range(3):
            
            if adj[node-1][j] < node:
               conf = conf * -1
               
        if (conf == 1):
            config = 'x'
        else:
            config = 'y'
        return config



###############################################################################
    
def direct (mapx , pvnode, axis):
    #print(axis, " axis in direct")
    node =0
    prnode=0
    nxnode=0
    bnode=0
    count = 0
    pvnode = 0
    global axis_new
    conf = -1
    drive = []
    global g,pvnodex
    turn =None
    config = None
    for i in range (g-1):
        prnode= mapx[i]
        
        nxnode = mapx[i+1]
        node = mapx[i]
        config = configuration(node)                             ##### finding conf using configuration function
        
        
        if pvnode == 0 and i == 0:
            #print(prnode,'  prnode', config," config")
            if config == 'x':
                if axis == 1:
                    if (nxnode>prnode):
                    
                        turn = 'r'
                    elif (nxnode<prnode):
                        turn = 'l'
                    elif nxnode == pvnodex :
                        turn = 'u'
                elif axis == 2:
                    if (nxnode<prnode):
                    
                        turn = 'r'
                    elif nxnode == prnode+1:
                        turn = 'u'
                    elif nxnode>prnode:
                        turn = 'l'
                elif axis == 3:
                    if (nxnode==prnode+1):
                    
                        turn = 'l'
                    elif nxnode > prnode:
                        turn = 'r'
                    elif nxnode == pvnodex:
                        turn = 'u'
            if config == 'y':
                if axis == 1:
                    if (nxnode+1==prnode):
                        turn = 'r'
                    elif nxnode > prnode:
                        turn = 'm'
                    elif nxnode ==pvnodex:
                        turn = 'u'
                elif axis == 2:
                    #print('into 2')
                    if (nxnode>prnode):
                        #print('prefect')
                        turn = 'r'
                    elif nxnode == pvnodex:
                        turn = 'u'
                    elif nxnode < prnode:
                        turn = 'l'
                elif axis == 3:
                    if (nxnode+1==prnode):
                    
                        turn = 'l'
                    elif nxnode<prnode:
                        turn = 'r'
                    elif nxnode == pvnodex:
                        turn = 'u'
               # print(turn, "  turn"," nxnode",nxnode, "  prnode ", prnode,)


        
        else:
                
            if i>0 :
                pvnode = mapx[i-1]
            bnode = 0
            if node in swap:
                
                bnode = bnode + 1
            #config = configuration(node)
            #print(prnode," test result conf   ",config)
            """
                conf = conf * -1
            for j in range(3):
                
                if adj[node-1][j] < prnode:
                   
                    conf = conf * -1
            if (conf == 1):
                print('conf x')
                config = 'x'
            else:
                print('conf y')
                config = 'y'               """         ### tesing configuration
            if ((config == 'x') and (pvnode>0)):
                if pvnode>prnode or ((bnode!=0)and(pvnode>prnode)) :
                    if pvnode!= (prnode+1):
                        if nxnode == (prnode+1):
                            turn = 'r'
                            
                        else:
                            turn = 'l'
                    else :
                        if nxnode > prnode and (bnode==0):
                            turn = 'l'
                        else:
                            turn = 'r'
                            
                else :
                    if nxnode == (prnode+1):
                        turn = 'l'
                    else:
                        turn = 'r'
                        
            elif config == 'y'and pvnode>0:
                
                if pvnode < prnode:
                    if prnode == (pvnode+1):
                        #print ("prev node"+ pvnode +"present node"+ prnode)
                        if prnode>nxnode:
                            turn = 'l'
                        else :
                            turn = 'r'
                            
                    else:
                        if prnode<nxnode:
                            turn = 'l'
                        else:
                            turn = 'r'
                else:
                    if nxnode == (prnode-1):
                        turn  = 'l'
                    else:
                        turn = 'r'

    



                       
        drive.append (turn)
        traverse.append (turn)
    print(nxnode,"  ",prnode,"  end of 1 traversal")
    drive.append (node_action(nxnode,prnode,axis_new))
    traverse.append (node_action(nxnode,prnode,axis_new))

    
    #for i in range(g-1):
        #print(drive[i])
    print(str(drive))
    return prnode
        
def node_action(prnode,pvnode,axis):              #####   s =staright,  e = 120 degree left turn , i = 120 degree right turn

    go = []
    config = configuration(prnode)
    
    if axis == 3:                       ###### all the axis is reference to our aerena design and not to the flex
        if config == 'x':
            if pvnode<prnode:
                go = 's'
            elif pvnode == prnode+1:
                go = 'e'
            elif pvnode > prnode:
                go = 'i'
        elif config == 'y':
            
            if pvnode > prnode:
                go = 's'
            elif prnode == pvnode+1:
                go = 'e'
            elif pvnode < prnode:
                go = 'i'
    if axis == 2:
        if config == 'y':
            if prnode == pvnode+1:
                go = 's'
            elif pvnode > prnode:
                go = 'i'
            elif pvnode < prnode:
                go = 'e'
        elif config == 'x':
            if pvnode == prnode+1:
                go = 's'
            elif pvnode > prnode:
                go = 'e'
            elif pvnode < prnode:
                go = 'i'
    if axis == 1:
        if config == 'x':
            if pvnode < prnode:
                go = 'e'
            elif pvnode == prnode+1:
                go = 'i'
            elif pvnode > prnode:
                go = 's'
        elif config == 'y':
            if pvnode+1==prnode:
                go = 'i'
            elif pvnode > prnode:
                go = 'e'
            elif pvnode < prnode:
                go = 's'
    
    return go


def main():

    map_ = []
    m = 2
    global pvnode,g,n,pvnodex
    axis = 2
    global axis_new
    
    start = int(input("Enter start 1 or 2 "))
    #source = int(input("Enter source (node#): "))
    cell = int(input("Enter destination 1 (cell): "))
    orient = int(input("Enter destination 1 (axis): "))
    cell_2 = int(input("Enter destination 2 (cell): "))
    orient_2 = int(input("Enter destination 2 (axis): "))
    #source = int(input("Enter source (node#): "))
    #dest = int(input("Enter destination node: "))
    if start is 1:
        s = 25
    elif start is 2:
        s = 30
    
    while(m!=0):
        d1 = 0
        d2 = 0
        if m is 2:
            if orient is 2:
                orient = 3
            elif orient is 3:
                orient = 2
           
            axis_new = orient
            for i in range(len(arena)+1):
                
                for j in range(4):
                    
                    if i == cell:
                        
                        if j == orient:
                            
                            if j==1:
                                
                                d1=int(arena[i-1][0])
                                d2=int(arena[i-1][1])
                            if j==2:
                                
                                d1=int(arena[i-1][2])
                                d2=int(arena[i-1][3])
                            if j==3:
                                
                                d1=int(arena[i-1][4])
                                d2=int(arena[i-1][5])
                                            
                       
            l1 = shortestPath(s, d1,0)
           
           
            l2 = shortestPath(s, d2,1)
                   
            
            
        elif m==1:
            
            d1=0
            d2=0
            if orient_2 == 2:
                orient_2 = 3
            elif orient_2 == 3:
                orient_2 = 2

            axis_new = orient_2
            
            for i in range(len(arena)+1):
                for j in range(4):
                    if i == cell_2:
                        if j == orient_2:
                            if j==1:
                                d1=int(arena[i-1][0])
                                d2=int(arena[i-1][1])
                            if j==2:
                                d1=int(arena[i-1][2])
                                d2=int(arena[i-1][3])
                            if j==3:
                                
                                d1=int(arena[i-1][4])
                                d2=int(arena[i-1][5])




            
           
            l1 = shortestPath(s, d1,0)
           
            l2 = shortestPath(s, d2,1)
 
        g=0
        
        
        #print("path  ",path)
        if l1<l2:
            index = 0
            c = l1
            st = l2
        else :
            index = 1
            c = l2
            st = l1
        #print('range ',range(c-1, -1, -1))
        #print("index  ",path)
        #print("size ",c)
        #print("c+1",path[index][c])
        #map_.append(path[index][c])
        #g = g+1
        #print(path[index])
        for i in range(c, -1, -1):
                g = g+1
                map_.append(int(path[index][i]))
                
        print(map_)
        #print(axis, " axis in main")
        x = direct(map_,pvnode,axis)
        pvnodex = x
        axis = axis_new
        pvnode = 0 
        s = int(map_[g-1])

        
        #path.clear()
        #map_.clear()
        
        for i in range(2):
            for j in range(n):
                path[i][j] = -1
                
        #path = [[-1 for i in range(n)] for j in range(2)]
        map_.clear()
        #print("path",path)
        
        #print(map_)



        
        m = m-1
    print ("\n\t\t directions of bot \n")
    for i in range (len(traverse)):
        print ((traverse[i]))
   
    #shortestPath(source, dest)
    

if __name__ == '__main__':
    s='y'
    while(s=='y'):
        main()
        s = input('Enter y to cont')
