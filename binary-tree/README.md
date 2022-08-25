# binary-tree_python
___


Code and theory based on: 
- [Binary Trees in Python. LucidProgramming](https://www.youtube.com/watch?v=aM-oswPn19o&list=PL5tcWHG-UPH2fmYC6kgey1RIxP2iK9EEL), 
- [Binary Tree Data Structure GeeksForGeeks](https://www.geeksforgeeks.org/binary-tree-data-structure/), 
- [Python - Binary Tree by TutorialPoint](https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm),
- [Binary Tree Algorithms for Technical Interviews by FreeCodeCamp](https://www.youtube.com/watch?v=fAAZixBzIAI).

___

### Theory:

 Tree represents the nodes connected by edges. It is a non-linear data structure. It has the following properties:

- One node is marked as Root node.
- Every node other than the root is associated with one parent node.

 - Each node can have an arbiatry number of chid node.





Common ways to traverse in depth-first order:

#### Pre-order 
<img width="150" align="right" alt="image" src="https://user-images.githubusercontent.com/52755167/186539350-b729e430-ffc2-4f96-82b0-335afaf1388d.png">

1.1 Check if curent node is empty/null
1.2 Display data
1.3 Go down througth left subtree recursievly calling the pre-order function
1.4 Repeat for right subtree 


#### In-order 
<img width="150" align="right" alt="image" src="https://user-images.githubusercontent.com/52755167/186545064-7e2d4441-3ade-4636-b9d1-884d4a77fb35.png">

1.1 Check if curent node is empty/null 
1.2 Traverse the left subtree recursievly
1.3 Display data
1.4 Traverse right subtree

#### Post-order 
<img width="150" align="right" alt="image" src="https://user-images.githubusercontent.com/52755167/186545030-8e38f04c-8871-4a28-b10b-b70a07cbc54d.png">

1.1 Check if curent node is empty/null 
1.2 Go down througth left subtree recursievly 
1.3 Go down througth right subtree recursievly 
1.4 Display data
