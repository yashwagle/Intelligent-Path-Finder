# Intelligent-Path-Finder
Implementation of the A-star algorithm to find the most efficient
path between two points in the Mendon Ponds Park. The map of the park
is as follows:

![alt text](/testcases/normal/terrain.png)

All the points are not at the same elevation. The elevation and 
the pixel size are determined by the ![National Elevation Dataset](http://www.sciencebase.gov/catalog/item/4f70a58ce4b058caae3f8ddb).
Including the elevation the park looks some like this:

![alt text](/terrain.gif)




# Running the Program

Pre-requisite Pillow must be installed

Lab1.py \<image name> \<elevation file> \<season> \<file with set of points>


Lab1.py "testcases/normal/terrain.png" "testcases/normal/mpp.txt" "summer"
"testcases/normal/brown.txt"