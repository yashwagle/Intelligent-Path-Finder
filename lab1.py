from PIL import Image, ImageDraw
import heapq
import math
import timeit
import queue
import sys


'''
@author: Yash Wagle (yw5262)

'''
X_PIXEL_DISTANCE = 10.29
Y_PIXEL_DISTANCE = 7.55
SPEED_DICTIONARY ={
    (248, 148, 18): 9,
    (255, 192, 0):6,
    (255, 255, 255): 3,
    (2,208,60): 4,
    (2,136,40): 2,
    (5,73,24): 0.5,
    (0,0,255): 0.1,
    (71,51,3): 10,
    (0,0,0): 8,
    (205, 0, 101):0.000001,
    (255,0,0):1,
    (255, 102, 204):6,
    (165, 242, 243):7}
BEST_SPEED = 10

class Node:
    def __init__(self, X, Y, Z, color, parent):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.color = color
        if parent!=None:
            self.parent = parent
            self.cost = parent.cost + get_distance(self, parent)/SPEED_DICTIONARY[parent.color]
        else:
            self.parent = None
            self.cost = 0


    def setParent(self, parentNode):
        self.parent = parentNode

    def getHueristic(self, destination):
        return get_distance(self, destination)/BEST_SPEED




    def getCoordinates(self):
        return (self.X, self.Y)

    def __eq__(self, other):
        if other == None:
            return False
        return self.X == other.X and self.Y == other.Y

    def __str__(self):
        return str(self.X) + ", " + str(self.Y) + ", " + str(self.Z)

    def __lt__(self, other):
        if self.X < other.X:
            return self
        return other

def add_to_queue(queue, point, visited, destination):
    if point.getCoordinates() not in visited:
        heapq.heappush(queue, (point.getHueristic(destination) + point.cost,point))





def A_Star(StartX, StartY, EndX, EndY, elevation, image, parent, season):
    queue = []
    visited = set()
    startNode = Node(StartX, StartY, float(elevation[StartY][StartX]), image.getpixel((StartX, StartY)), parent)
    destination = Node(EndX, EndY, float(elevation[EndY][EndX]), image.getpixel((EndX,EndY)), None)
    heapq.heappush(queue, (0,startNode))
    added_Dict = {}
    while queue:
        point = heapq.heappop(queue)
        #print(point[0], point[1])
        point = point[1]
        visited.add(point.getCoordinates())
        #print(point)
        if point == destination:
            return point
        if point.X>0:
            newnode = Node(point.X-1, point.Y, float(elevation[point.Y][point.X-1]), image.getpixel((point.X-1,point.Y)), point)
            if newnode.getCoordinates() in added_Dict and added_Dict[newnode.getCoordinates()]>newnode.cost:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
            elif newnode.getCoordinates() not in added_Dict:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
        if point.X>0 and point.Y>0:
            newnode = Node(point.X-1, point.Y-1, float(elevation[point.Y-1][point.X-1]), image.getpixel((point.X-1,point.Y-1)), point)
            if newnode.getCoordinates() in added_Dict and added_Dict[newnode.getCoordinates()]>newnode.cost:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
            elif newnode.getCoordinates() not in added_Dict:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
        if point.X>0 and point.Y+1<len(elevation)-5:
            newnode = Node(point.X-1, point.Y+1, float(elevation[point.Y+1][point.X-1]), image.getpixel((point.X-1,point.Y+1)), point)
            if newnode.getCoordinates() in added_Dict and added_Dict[newnode.getCoordinates()]>newnode.cost:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
            elif newnode.getCoordinates() not in added_Dict:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
        if point.X+1<len(elevation[0])-5:
            newnode = Node(point.X + 1, point.Y, float(elevation[point.Y][point.X + 1]),image.getpixel((point.X + 1, point.Y)), point)
            if newnode.getCoordinates() in added_Dict and added_Dict[newnode.getCoordinates()]>newnode.cost:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
            elif newnode.getCoordinates() not in added_Dict:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
        if point.X+1<len(elevation[0])-5 and point.Y+1<len(elevation)-5:
            newnode = Node(point.X + 1, point.Y+1, float(elevation[point.Y+1][point.X + 1]),image.getpixel((point.X + 1, point.Y+1)), point)
            if newnode.getCoordinates() in added_Dict and added_Dict[newnode.getCoordinates()]>newnode.cost:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
            elif newnode.getCoordinates() not in added_Dict:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
        if point.X+1<len(elevation[0])-5 and point.Y>0:
            newnode = Node(point.X + 1, point.Y-1, float(elevation[point.Y-1][point.X + 1]),image.getpixel((point.X + 1, point.Y-1)), point)
            if newnode.getCoordinates() in added_Dict and added_Dict[newnode.getCoordinates()]>newnode.cost:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
            elif newnode.getCoordinates() not in added_Dict:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
        if point.Y>0:
            newnode = Node(point.X, point.Y - 1, float(elevation[point.Y][point.X]),image.getpixel((point.X, point.Y-1)), point)
            if newnode.getCoordinates() in added_Dict and added_Dict[newnode.getCoordinates()]>newnode.cost:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
            elif newnode.getCoordinates() not in added_Dict:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
        if point.Y+1<len(elevation)-5:
            newnode = Node(point.X, point.Y + 1, float(elevation[point.Y][point.X]),image.getpixel((point.X, point.Y + 1)), point)
            if newnode.getCoordinates() in added_Dict and added_Dict[newnode.getCoordinates()]>newnode.cost:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)
            elif newnode.getCoordinates() not in added_Dict:
                added_Dict[newnode.getCoordinates()] = newnode.cost
                add_to_queue(queue, newnode, visited, destination)







def get_distance(Node1, Node2):
    return math.sqrt(((Node1.X-Node2.X)*X_PIXEL_DISTANCE)**2 + ((Node1.Y - Node2.Y)*Y_PIXEL_DISTANCE)**2 + (Node1.Z - Node2.Z)**2)

def get_image(imageName):
    matrix = []
    image = Image.open(imageName).convert("RGB",matrix)
    return image


def parse_fall(image):
    xmax, ymax = image.size
    #fall color = 255, 102, 204
    for i in range(xmax):
        for j in range(ymax):
            if image.getpixel((i,j)) != (255,255,255):
                if i>0 and image.getpixel((i-1,j))==(255,255,255):
                    image.putpixel((i,j),(255,102,204))
                elif i + 1 < xmax and image.getpixel((i + 1, j)) == (255, 255, 255):
                    image.putpixel((i, j), (255, 102, 204))
                elif j> 0 and image.getpixel((i, j-1))== (255, 255, 255):
                    image.putpixel((i, j), (255, 102, 204))
                elif j+1 < ymax and image.getpixel((i, j+ 1)) == (255, 255, 255):
                    image.putpixel((i, j), (255, 102, 204))


def parse_winter(image):
    xmax, ymax = image.size
    #ice color = 165, 242, 243
    border = set()
    q = queue.Queue()
    for i in range(xmax):
        for j in range(ymax):
            if (i,j) not in border and image.getpixel((i,j)) == (0,0,255):
                if i>0 and (i-1,j) not in border and image.getpixel((i-1,j))!=(0,0,255):
                    q.put([(i-1,j),1])
                    border.add((i-1,j))
                if i<xmax-1 and (i+1,j) not in border and image.getpixel((i + 1, j)) != (0, 0, 255):
                    q.put([(i+1,j),1])
                    border.add((i + 1, j))
                if j>0 and (i, j - 1 ) not in border and  image.getpixel((i, j - 1)) != (0, 0, 255):
                    q.put([(i,j-1),1])
                    border.add((i, j-1))
                if j < ymax-1 and (i, j + 1) not in border and image.getpixel((i, j + 1)) != (0, 0, 255):
                    q.put([(i,j+1),1])
                    border.add((i,j+1))
    print(border)
    while not q.empty():
        p = q.get()
        print(p)
        image.putpixel(p[0],(165, 242, 243))
        i = p[0][0]
        j = p[0][1]
        if i > 0 and (i - 1, j) not in border and image.getpixel((i - 1, j)) == (0, 0, 255) and p[1]<6:
            q.put([(i - 1, j), p[1]+1])
            border.add((i - 1, j))
        if i < xmax - 1 and (i + 1, j) not in border and image.getpixel((i + 1, j))  == (0, 0, 255) and p[1]<6:
            q.put([(i + 1, j), p[1]+1])
            border.add((i + 1, j))
        if j > 0 and (i, j - 1) not in border and image.getpixel((i, j - 1))  == (0, 0, 255) and p[1]<6:
            q.put([(i, j - 1), p[1] + 1])
            border.add((i, j - 1))
        if j < ymax - 1 and (i, j + 1) not in border and image.getpixel((i, j + 1))  == (0, 0, 255) and p[1]<6:
            q.put([(i, j + 1), p[1] +  1])
            border.add((i, j + 1))



def parse_spring(image, elevation):
    xmax, ymax = image.size
    # mud color = 255, 0, 0
    mud_color = (255, 0, 0)
    border = set()
    q = queue.Queue()
    for i in range(xmax):
        for j in range(ymax):
            if (i, j) not in border and image.getpixel((i, j)) == (0, 0, 255):
                if i > 0 and (i - 1, j) not in border and image.getpixel((i - 1, j)) != (0, 0, 255) and float(elevation[j][i])+1>float(elevation[j][i-1]):
                    q.put([(i - 1, j), 1,  float(elevation[j][i])])
                    border.add((i - 1, j))
                if i < xmax - 1 and (i + 1, j) not in border and image.getpixel((i + 1, j)) != (0, 0, 255) and float(elevation[j][i])+1>float(elevation[j][i+1]):
                    q.put([(i + 1, j), 1,  float(elevation[j][i])])
                    border.add((i + 1, j))
                if j > 0 and (i, j - 1) not in border and image.getpixel((i, j - 1)) != (0, 0, 255) and float(elevation[j][i])+1>float(elevation[j-1][i]):
                    q.put([(i, j - 1), 1,  float(elevation[j][i])])
                    border.add((i, j - 1))
                if j < ymax - 1 and (i, j + 1) not in border and image.getpixel((i, j + 1)) != (0, 0, 255) and float(elevation[j][i])+1>float(elevation[j+1][i]):
                    q.put([(i, j + 1), 1,  float(elevation[j][i])])
                    border.add((i, j + 1))
    print(border)

    while not q.empty():
        p = q.get()
        print(p)
        image.putpixel(p[0], mud_color)
        i = p[0][0]
        j = p[0][1]
        waterHeight = p[2]
        if i > 0 and (i - 1, j) not in border and image.getpixel((i - 1, j)) != (0, 0, 255) and p[1] < 14 and float(elevation[j][i-1])-waterHeight<=1:
            print(elevation[j][i-1], image.getpixel((i-1,j)))
            q.put([(i - 1, j), p[1] + 1, waterHeight])
            border.add((i - 1, j))
        if i < xmax - 1 and (i + 1, j) not in border and image.getpixel((i + 1, j)) != (0, 0, 255) and p[1] < 14 and  float(elevation[j][i+1]) - waterHeight<=1:
            print(elevation[j][i+1], image.getpixel((i+1,j)))
            q.put([(i + 1, j), p[1] + 1, waterHeight])
            border.add((i + 1, j))
        if j > 0 and (i, j - 1) not in border and image.getpixel((i, j - 1)) != (0, 0, 255) and p[1] < 14 and   float(elevation[j-1][i])-waterHeight<=1:
            print(elevation[j-1][i], image.getpixel((i,j-1)))
            q.put([(i, j - 1), p[1] + 1,waterHeight])
            border.add((i, j - 1))
        if j < ymax - 1 and (i, j + 1) not in border and image.getpixel((i, j + 1)) != (0, 0, 255) and p[1] < 14 and float(elevation[j+1][i])- waterHeight<=1:
            print(elevation[j+1][i], image.getpixel((i-1,j+1)))
            q.put([(i, j + 1), p[1] + 1, waterHeight])
            border.add((i, j + 1))



def get_elevation(filename):
    elevation = []
    with open(filename) as f:
        for line in f:
            row = line.split()
            elevation.append(row)
    return elevation


def draw_path(node, image, inputPoints, draw):
    total_distance = 0
    for p in inputPoints:
        draw.ellipse((p[0]-1, p[1]-1, p[0]+1, p[1]+1), fill=(148, 0, 211), outline=(148, 0, 211))
    while(node.parent!=None):
        total_distance = total_distance + get_distance(node, node.parent)
        image.putpixel(node.getCoordinates(), (148,0,211))
        node = node.parent
    return total_distance,image

def main(imagefile, elevationfile, season, textfile, outputfile):
    elevation = get_elevation(elevationfile)
    image = get_image(imagefile)
    draw = ImageDraw.Draw(image)
    start = timeit.default_timer()
    filename =textfile
    inputPoints = set()
    if season == "fall":
        parse_fall(image)
        SPEED_DICTIONARY[(255, 255, 255)] = 0.85 * SPEED_DICTIONARY[(255, 255, 255)]
    elif season == "winter":
        parse_winter(image)
        SPEED_DICTIONARY[(165, 242, 243)] = 4
    elif season == "spring":
        parse_spring(image, elevation)
    with open(filename) as f:
        line = f.readline()
        coordinates = line.split()
        x = int(coordinates[0])
        y = int(coordinates[1])
        inputPoints.add((x, y))
        line = f.readline()
        parent = None
        while line:
            coordinates = line.split(" ")
            x1 = int(coordinates[0])
            y1 = int(coordinates[1])
            inputPoints.add((x1, y1))
            print(x, y)
            path = A_Star(x, y, x1, y1, elevation, image, parent, season)
            parent = path
            x = x1
            y = y1
            line = f.readline()

    path, new_image = draw_path(path, image, inputPoints,draw)
    end = timeit.default_timer()
    print("time =", end - start)
    print("distance = ", path)
    image.show()
    image.save(outputfile)


if __name__ == '__main__':
    image_file = sys.argv[1]
    elevation = sys.argv[2]
    season = sys.argv[3]
    textfile = sys.argv[4]
    outputfile = sys.argv[5]
    main(image_file,elevation,season,textfile, outputfile)