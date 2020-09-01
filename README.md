# Secret-Message-Maker
Turns a message into an array of numbers, the numbers are based on the position of the first letter in the letter, and then the positions of the other letteres relative to each other letter. The code moves from right to left.

For example, the string "because" would be [2, 3, 2, 25, 7, 25, 14], 2 denotes the b's numerical position in the alphabet, 3 donotes the distance from b to e on the alphabet moving to the right, and 2 denotes the distance from e to c moving left, 25 denotes c's and a's distance moving to the right

The code as it is, cannot deal with numbers, capitals letters, or special characters. It does have a space making the alphabet 27 characters long, however. 
