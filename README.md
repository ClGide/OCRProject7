# The 0/1 Knapsack Problem. 

This repository is the project 7 of my Open ClassRooms path. The story is that I am working for AlgoIvest, a fintech trying to optimize its investment strategies using algorithms in order to gain more client profits. The algorithm I chose needs to parse an Excel file containing thousands of items. Each item represents a company's share. Each share has a price and an expected return on investment after two years. The first constraint is that we cannot simply buy all the shares. We can only spend 500 euros per client. There is a second constraint: our algorithm must yield a result in under a second.     

## 🔧 SET UP 

The only library that needs to be installed is openpyxl in order to load the stylesheets in Python.   

## 📄 Description 

bruteforce.py contains the brute force approach to the 0/1 KP problem. It evaluates all the combinations of items then eliminates the ones that do not respect the weight constraint. Between the remaining combinations it chooses the most valuable. Although it is straight-forward, it is very inefficient. For only 20 items it takes more than one second. 

optimized.py contains the dynamic programming approach. Instead of computing all the possible combinations, it divides the bigger problem into subproblems of the same structure. The solution to the bigger problem is found by mixing up the subproblems' solutions. 

Presentation_of_p7.pptx explains in more detail the though process behind the optimized solution.
It also contains the time and space complexity analysis of the two algorithms and their limitations. Finally, it contains a dataset exploration comparing the optimized solution output with the one of an alternative algorithm. 

# 👷‍♂️ Contributors

Gide Rutazihana, student, giderutazihana81@gmail.com 
Ashutosh Purushottam, mentor

# License

 There's no license 
