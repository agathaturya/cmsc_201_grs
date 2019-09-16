# If-statements Practice Problems

1. Ask the user for how much money they spent this week. If they spent less than $0, print `"smells like broke in here!!"`. If they spent $0, print `"don't you have bills to pay?"`. If they spent greater than $0 and up to and including (inclusive) $100, print `"you are wise with your money"`. Otherwise, print `"you're a big spender!"`.     
**Sample output**  
```
[agatha3@linux6 lab3] python3 prob1.py
How much money did you spend this week?
34
you are great at budgeting!!

[agatha3@linux6 lab3] python3 prob1.py
How much money did you spend this week?
-27
it smells like broke in here!!

[agatha3@linux6 lab3] python3 prob1.py
How much money did you spend this week?
1
you are great at budgeting!!
```

2. Ask the user for their favorite number. If the number is divisible by 2, print `"you really like even numbers."` If the number is 13, print `"cursed number!"`. If the number is odd, print `"you are very odd!"`. If the number is 666, print 
`"that's the devils number!!"`.  
**Sample output**  
```
[agatha3@linux6 lab3] python3 prob2.py
what's your favorite number?
666
you really like even numbers.
that's the devils number!!
[agatha3@linux6 lab3] python3 prob2.py
what's your favorite number?
13
cursed number!
you are very odd!
[agatha3@linux6 lab3] python3 prob2.py
what's your favorite number?
72
you really like even numbers.
[agatha3@linux6 lab3] python3 prob2.py
what's your favorite number?
86
you really like even numbers.
[agatha3@linux6 lab3] python3 prob2.py
what's your favorite number?
33
you are very odd!
[agatha3@linux6 lab3]
```

**Challenge Problem**  
3. Write a program that takes in a user's birth month and birthday, and prints out their zodiac sign. Make sure the months and dates are valid!. If the user's birthday is invalid, print `your birthday is invalid, can't get zodiac sign`.  These are the corresponding dates and signs.    

```
Virgo: August 24 – September 22
Libra: September 23 – October 23
Scorpio: October 24 – November 22
Sagittarius: November 23 – December 21
Capricorn: December 22 – January 20
Aquarius: January 21 – February 18
Pisces: February 19 - March 20
Aries: March 21 - April 20
Taurus: April 21 – May 21
Gemini: May 22 – June 21
Cancer:  June 22 – July 22
Leo: July 23 – August 23
```
**Sample output**  
```
[agatha3@linux6 lab3] python3 prob3.py
enter your birth month
5
enter your birth date
24
you're a gemini!
[agatha3@linux6 lab3] python3 prob3.py
enter your birth month
10
enter your birth date
14
you're a libra!
[agatha3@linux6 lab3] python3 prob3.py
enter your birth month
2
enter your birth date
31
birth date is invalid!
[agatha3@linux6 lab3] python3 prob3.py
enter your birth month
18
enter your birth date
46
Birth month is invalid!
[agatha3@linux6 lab3] python3 prob3.py
enter your birth month
87
enter your birth date
45
Birth month is invalid!
[agatha3@linux6 lab3] python3 prob3.py
enter your birth month
1
enter your birth date
1
you're a capricorn!
[agatha3@linux6 lab3]
```
