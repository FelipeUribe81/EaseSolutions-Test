# EaseSolutions-Test

Let’s say you hopped on a flight to the Kitzbühel ski resort in Austria. Being a software engineer you 
can’t help but value efficiency, so naturally you want to ski as long as possible and as fast as possible 
without having to ride back up on the ski lift. So you take a look at the map of the mountain and try 
to find the longest ski run down.
In digital form the map looks like the number grid below.

|  |  |  |  |
| ------------ | ------------ | ------------ | ------------ |
| 4  | 4  |   |   |
|  4 | 8  | 7  | 3  |
| 2  | 5  | 9  | 3  |
| 6  | 3  | 2  | 5  |
| 4  | 4  |  1 | 6  |


The first line (4 4) indicates that this is a 4x4 map. Each number represents the elevation of that area 
of the mountain. From each area (i.e. box) in the grid you can go north, south, east, west - but only if 
the elevation of the area you are going into is less than the one you are in. I.e. you can only ski 
downhill. You can start anywhere on the map and you are looking for a starting point with the 
longest possible path down as measured by the number of boxes you visit. And if there are several 
paths down of the same length, you want to take the one with the steepest vertical drop, i.e. the 
largest difference between your starting elevation and your ending elevation.
On this particular map, the longest path down is of length=5 and it’s highlighted in bold below: 9-5-
3-2-1.

|  |  |  |  |
| ------------ | ------------ | ------------ | ------------ |
| 4  | 4  |   |   |
|  4 | 8  | 7  | 3  |
| 2  | **5**  | **9**  | 3  |
| 6  | **3**  | **2**  | 5  |
| 4  | 4  |  **1** | 6  |


There is another path that is also length five: 8-5-3-2-1. However, the tie is broken by the first path 
being steeper, dropping from 9 to 1, a drop of 8, rather than just 8 to 1, a drop of 7.
Your challenge is to write a program to find the longest (and then steepest) path on the specified 
map in the format above. It’s 1000x1000 in size, and all the numbers on it are between 0 and 1500.

## Instructions for using the program

To run the code you do the following:

You, in the terminal (bash, cmd, etc) must be located in the 'code' folder once cloned the repository. In the 'input' folder, you will find the maps available for testing, you can include yours with '.txt' extension inside the folder.

Located in the 'code' folder you execute the file 'app.py' as follows:

`python app.py "name_of_input.txt"`

![image](https://user-images.githubusercontent.com/66666430/145697558-2c841bce-d81f-49d6-b0e6-96f5ba9b2b1e.png)

