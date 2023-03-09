This code is creating a twoSum code using Python.

twoSum goal is finding the two value in given list that can sum it to the target number

in this code I use dict_Done to keep the value that we already check it


1.We create an empty dictionary.
2.We loop through the nums list. The first number is 2.
3.We compute the difference between target and 2, which is 7.
4.We check if 7 is in the dictionary. It is not, so we add 2 to the dictionary with key 2 and value 0.
5.We move on to the next number in the list, which is 7.
6.We compute the difference between target and 7, which is 2.
7.We check if 2 is in the seen dictionary. It is, with value 0.
8.We return the value 0 and 1 in a list [0, 1], indicating that the numbers at those value (2 and 7) add up to target.