# using a genetic algorithm to solve N-queens
#### Adam Dhalla [adamdhalla.com](https://adamdhalla.com/)

This program attempts to solve a popular computer-science problem - the N-queens problem. 

By denoting the locations of queens on an N-dimensional chessboard with an N-dimensional list of positions, we can use genetic algorithms to combine and recombine parts of the string in a random fashion, reminiscent of the way that genes are passed, mutated, and crossed over (during meiosis). After a certain amount of "generations", the function `geneticAlgorithm()` will return the string of Queen positions where all N queens cannot attack eachother. 

### **Input Syntax**
The function (that calls all the other necessary functions located in  `genetic8queens.py`) is called  `geneticAlgorithm()`. It returns the string of queen locations. This functino requres a few things to be passed in. 

General input syntax: `geneticAlgorithm(N, hfunc, popsize, parentcutoff, p, stoppoint)`

Where:
* `N` is the dimension of the chessboard (and in extension the amount of queens) 
* `hfunc` is the heuristic function you want to MAXIMIZE. This heuristic should be indicative of the status of your chessboard - more queens fighting should be return a low heuristic output, only a few queens fighting should show large. I include a heuristic function, `heuristic()` in the .py file. The one I made counts the total pairs of fighting queens. 
* `popsize` is the population size at all times - e.g, how many different strings of locations are being cycled through at each generation. This stays static in size. 
* `parentcutoff` is the amount of pairs per generation that should be allowed to make offspring - these `parentcutoff ` parents with the highest heuristic will be chosen to combine and make the next generation
* `p` is the amount of parents per combination. The common choice is two, but if you have a very large chessboard you might want more. 
* `stoppoint` is the amount of generations you want the algorithm to stop at if it has not found a viable solution yet.  

### **Under the Hood**
I won't elaborate too much on the process since I wrote a pretty comprehensive article [here](https://adamdhalla.medium.com/how-ai-can-learn-from-genetics-b24f31adf494) 

Basically, the process to find the best string is as follows: 

1. `popsize` amount of strings (actually lists, but for ease of language, strings) are randomly chosen. Each of these strings are N-dimensional, representing the placement of queens on each _column_ of the chessboard (0 is the bottom row, N is the top row). 
2. all the `popsize` strings are listed in order of highest to lowest score on the heuristic. Since the heuristic needs to be maximized, the best candidates are at the top of this "queue". 
3. the top `parentcutoff` x `p` strings are chosen, and the rest are discarded. These top are allowed to pair off into size `p` parent groups. 
4. In each of these parent groups, the members of the parent group randomly "donate" parts of their string to their offspring. An offspring might have the first 5 string entries of Parent 1, and the last 3 from Parent 2. This is meant to hopefully find good combinations, and mix them together. 
5. Each of these parent groups make some amount of "children" so that all the children of all the parent groups = `popsize`. 
6. Each of these children, the new generation now, is randomly mutated. Just a little bit - maybe one of it's values change, maybe none. This is meant to keep the population diverse - to avoid 'inbreeding'. 
7. These are then re-listed once again according to their heuristic. 
8. If the heuristic finds *no* fighting queens in some population it will return that string. If not, it will keep going until it reaches `stoppoint` generations. 
