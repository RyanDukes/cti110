# Keeps a running total of bugs collected over 5 days.
# 10/10/2019
# CTI-110 P4T2 - Bug Collector
# Ryan Dukes
#

# User inputs the number of bugs collected each day for 5 days.
# Add bugs collected to total.
# Display total number of bugs collected.

# The Accumulator
total = 0

# Bugs collected each day.
for day in range(1, 6):
    print("Enter the bugs collected on day", day)

    #User input
    bugs = int(input())
    total += bugs

# Display the total bugs.
print("You collected a total of", total, "bugs.")
