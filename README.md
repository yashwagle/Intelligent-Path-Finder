# Intelligent-Path-Finder
Implementation of the A-star algorithm to find the most efficient
path between two points in the Mendon Ponds Park considering the 
elevation, terrain type and season. The map of the park
is as follows:

![alt text](/testcases/normal/terrain.png)

Each color represents a specific type of terrain.
All the points are not at the same elevation. The elevation and 
the pixel size are determined by the [National Elevation Dataset](http://www.sciencebase.gov/catalog/item/4f70a58ce4b058caae3f8ddb).
Including the elevation the park looks some like this:

![alt text](/terrain.gif)

The elevation data can be found [here](../testcases/mpp.txt).
The map presented is for summer and changes based on the seasons.
The changes are explained below

# Design
In my implementation I try to minimize the time required to move
from one point to another. To do so each color has been assigned
a maximum speed. 

![alt text](/SpeedTable.png)

## Heuristic Function
For the heuristic function, I have used the euclidean distance 
between the two points along with the height and dividing that 
distance by the best speed i.e. 10. This function does not 
overestimate since it considers there exists a straight line 
path from any point to the destination having the best speed. 
So in the best case, the speed will be 10 and the time for the 
actual path will be equal to the heuristic distance. 
This is true for all other seasons as well since for each 
season we are decreasing speed and not increasing it.

## A-star Algorithm
For A-star algorithm, all eight neighboring points have been 
considered. I have used a priority queue(heap) to find the 
point with the lowest heuristic value and then that point is 
removed from the queue. The point is a class that contains 
the parent from which it was generated, hence when tracing 
the path we can look at the parent until the parent is None 
at which point it is the first point.


## Path Coloring:
I have created a class node that contains the X, Y, Z coordinates 
the color and a node to the parent. The parent is the point that 
generated this point in the queue. So for drawing the path I 
go from the last point to the first point.


## Seasons

### Winter
In winter, the waters can freeze. 
Any water within seven pixels of non-water is safe to walk on.
To deal with this first, the water pixels which are next to land are found, 
next BFS is applied to find the water pixels that are within 
seven pixels of the border pixels.

### Spring
In spring Any pixels within fifteen pixels of water that can be 
reached from a water pixel without gaining more 
than one meter of elevation (total) are now underwater
To deal with this first, the land pixels next to water are found. 
Then BFS is applied, but the entry in the queue also 
contains the height of the water. Hence if a pixel is 
at a height greater than 1 meter then that pixel is 
ignored and not colored.


### Fall
In the fall, leaves fall. In the park, what happens is that 
paths through the woods can become covered and hard to follow.
So, for fall, the time  for any paths through (that is, adjacent to)
easy movement forest (but only those paths) should increase,
Hence, pixels which are next to easy moving forests are found 
and are colored pink. 



# Running the Program

Pre-requisite Pillow must be installed

Lab1.py \<image name> \<elevation file> \<season> \<file with set of points>


Lab1.py "testcases/normal/terrain.png" "testcases/normal/mpp.txt" "summer"
"testcases/normal/brown.txt"