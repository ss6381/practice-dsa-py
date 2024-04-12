# META PHONE SCREEN
# April 2024
# Given a list of city names and their corresponding populations, write a program to output a city name subject to the following constraint: the probability of the program to output a city's name is based on its population divided by the sum of all cities' population. Assume the program will be repeatedly called many times.
# For example:
# NY: 7MM
# SF: 5MM
# LA: 8MM
# The probability to generate NY is 7/20, SF is 1/4.
# Looking for an optimal solution.

"""
Assumptions:
- The population is a non-negative number (including 0)
- Unsorted


Solution:
1. Take in a dictionary of city to population
2. Get a sum of the total population
3. Math.rand ?
"""