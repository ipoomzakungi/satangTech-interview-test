The goal of the rotation problem is to shift the elements of an array A to the right by K positions. To do this, we first check if the length of A is zero. If it is, we return A as is. or we calculate the actual number of rotations needed by taking the remainder of K divided by the length of A.

If the number of rotations needed is zero, we return A as is.
or we create a new empty list B and the working of the program if we rotate K time the the last K elements in A is going to be the first so we gonna append the last K elements in A to B and append the rest of A to B

to use the program , the user can run it through python or in VSCode
if it return `OK` it mean the code Pass the test case that I created