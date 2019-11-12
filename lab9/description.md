# GRS Activity
The function `substring()` is a recursive function that goes through `string`, and finds all occurences of `s`. Note: `substring` is case-sensitive.

## Sample output and test cases

`substring('Agatha', 'a', 0)`  
Found a at index 2  
Found a at index 5  

`substring('', '', 0)`   
[no output]  

`substring('a', 'Agatha', 0)`  
[no output]   

`substring('dogs dogs dogs dogs dogs', 'dogs', 0)`   
Found dogs at index 0   
Found dogs at index 5  
Found dogs at index 10  
Found dogs at index 15  
Found dogs at index 20  
