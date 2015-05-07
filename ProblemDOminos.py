import copy
num_units = 0
target_num_units = 0
total_units = 0
found_fit = False
shapes = []

def generate_valid_shapes(size):
    global shapes
    for x in range(size):
        for y in range(size):
            print("generating shapes: x: " + str(x) + " y: " + str(y))
            shapegrid = [[0 for x in range(size)] for x in range(size)]
            fill_shape(x,y,shapegrid,1)
    #print("Generated shapes... ")
    #for x in shapes:
    #    print(x)
    return shapes
    
def fill_shape(x,y,grid,size):
    global shapes
    #print("filling shape")
    grid[x][y] = 1
    if size == units_per_omino:
        print("generated a shape: ", grid, " size: ", size)
        return shapes.append(grid)
    grid2 = copy.deepcopy(grid)
    if (x > 0):
        if grid[x-1][y] == 0:
            fill_shape(x-1,y,grid2,size+1)
    grid2 = copy.deepcopy(grid)
    if (y > 0):
        if grid[x][y-1] == 0:
            fill_shape(x,y-1,grid2,size+1)
    grid2 = copy.deepcopy(grid)
    if (x < units_per_omino-1):
        if grid[x+1][y] == 0:
            fill_shape(x+1,y,grid2,size+1)
    grid2 = copy.deepcopy(grid)
    if (y < units_per_omino-1):
        if grid[x][y+1] == 0:
            fill_shape(x,y+1,grid2,size+1)
    return -1
    
def shape_gen_algorithm(x_start,y_start,grid):
    global num_units
    global total_units
    global target_num_units
    print("x_start: " + str(x_start) + " y_start: " + str(y_start))
    print("num_units: " + str(num_units) + " total_units: " + str(total_units) + " target_num_units: " + str(target_num_units))
    print("grid : ", grid)
    grid[x_start][y_start] = 1
    num_units = num_units + 1
    if num_units == units_per_omino:
        total_units = total_units + num_units
        num_units = 0
        if total_units < target_num_units:
            for x, y in zip(range(R), range(C)):
                if grid[x][y] == 0:
                    return shape_gen_algorithm(x,y,grid)
        if total_units == target_num_units:
            return 1
    if (x_start > 0):
        if grid[x_start-1][y_start] == 0:
            return shape_gen_algorithm(x_start-1,y_start,grid)
    if (y_start > 0):
        if grid[x_start][y_start-1] == 0:
            return shape_gen_algorithm(x_start,y_start-1,grid)
    if (x_start < C-1):
        if grid[x_start+1][y_start] == 0:
            return shape_gen_algorithm(x_start+1,y_start,grid)
    if (y_start < R-1):
        if grid[x_start][y_start+1] == 0:
            return shape_gen_algorithm(x_start,y_start+1,grid)
    num_units = 0
    return 0


with open('problemDinput1', 'r') as openfileobject:
    i = 0
    for line in openfileobject:
        found_fit = False
        num_units = 0
        total_units = 0
        values = line.split()
        if i == 0:
            T = values[0]
        if i > 0:
            X = int(values[0])#number of blocks/units in our shape
            R = int(values[1])#number of rows
            C = int(values[2])#number of columns
            print("X: " + str(X) + " R: " + str(R) + " C: " + str(C))
            target_num_units = R*C
            units_per_omino = X
            generate_valid_shapes(units_per_omino)
            for x, y in zip(range(R), range(C)):
                testgrid = [[0 for x in range(R)] for x in range(C)]
            #for x in range(R):
                #for y in range(C):
                print("testgrid: ", testgrid)
                print("i: " + str(i) + " x: " + str(x) + " y: " + str(y)) 
                if shape_gen_algorithm(y,x,testgrid) == 1:
                    print("FOUND A FIT THAT WORKS! GABRIEL WINS!")
                    found_fit = True
                    break
            print(line)
            if found_fit == True:
                print("Case #"+str(i)+": GABRIEL")
            if found_fit == False:
                print("Case #"+str(i)+": RICHARD")
        i = i + 1



    
    
