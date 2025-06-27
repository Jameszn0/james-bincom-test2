import random
import statistics
import psycopg2
import re

# Sample data (replace this with the actual data extraction from your web page)
colors = ["red", "blue", "green", "red", "blue", "yellow", "red", "green", "blue", "blue"]

# 1. Mean color (most frequent)
def mean_color(colors):
    return statistics.mode(colors)

# 2. Most worn color
def most_worn_color(colors):
    return statistics.mode(colors)

# 3. Median color
def median_color(colors):
    return statistics.median(colors)

# 4. Variance of colors
def color_variance(colors):
    color_freq = {color: colors.count(color) for color in set(colors)}
    return statistics.variance(color_freq.values())

# 5. Probability of choosing red
def probability_red(colors):
    return colors.count("red") / len(colors)

# 6. Save colors and their frequencies in PostgreSQL database
def save_to_db(colors):
    connection = psycopg2.connect(
        dbname="your_dbname",
        user="your_username",
        password="your_password",
        host="localhost"
    )
    cursor = connection.cursor()
    
    color_freq = {color: colors.count(color) for color in set(colors)}
    for color, freq in color_freq.items():
        cursor.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, freq))
    
    connection.commit()
    cursor.close()
    connection.close()

# 7. Recursive searching algorithm
def recursive_search(arr, target, index=0):
    if index >= len(arr):
        return False
    if arr[index] == target:
        return True
    return recursive_search(arr, target, index + 1)

# 8. Generate random 4-digit binary number and convert to base 10
def binary_to_decimal():
    binary_number = ''.join(random.choice('01') for _ in range(4))
    return binary_number, int(binary_number, 2)

# 9. Sum the first 50 Fibonacci numbers
def fibonacci_sum(n=50):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return sum(fib_sequence)

# Main execution
if __name__ == "__main__":
    print("Mean Color:", mean_color(colors))
    print("Most Worn Color:", most_worn_color(colors))
    print("Median Color:", median_color(colors))
    print("Color Variance:", color_variance(colors))
    print("Probability of Red:", probability_red(colors))
    
    save_to_db(colors)
    
    # Example usage of recursive search
    numbers_list = [1, 2, 3, 4, 5]
    search_target = 3
    print("Number found:", recursive_search(numbers_list, search_target))
    
    # Generate and convert binary number
    binary_num, decimal_num = binary_to_decimal()
    print(f"Random binary number: {binary_num}, Decimal: {decimal_num}")
    
    # Sum of Fibonacci sequence
    print("Sum of first 50 Fibonacci numbers:", fibonacci_sum())