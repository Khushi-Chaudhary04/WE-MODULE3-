# -*- coding: utf-8 -*-
"""Practice(Idli).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13L8DyxVjBRF4wCfCoasdAaoqjC4AIcP4

You are the benevolent ruler of Dosapuri, and today you're distributing idlis. Your subjects are in a line, and some of them already have some idlis in their hand. You must distribute as few idlis as possible according to the following rules: Every time you give an idli to some person, you must also give an idli to the person immediately behind them; that is you distribute two idlis at a time. Given the number of idlis already held by each citizen, find the minimum number of idlis you must distribute to satisfy the two rules above. If this is not possible, return -1.
A person may receive any number of idlis in toto.
After all the idlis are distributed, each person must have an even number of idlis.
"""

def distribute_idlis_optimized(idlis):
  """
  This function calculates the minimum number of idlis needed to distribute
  using lists such that everyone ends up with an even number of idlis.

  Args:
      idlis: A list containing the number of idlis each person already has.

  Returns:
      The minimum number of idlis to distribute, or -1 if it's impossible.
  """
  if len(idlis) == 0:
    return 0  # No distribution needed for empty list

  # Single person case (handled earlier)
  # ... (your previous code for handling single person)

  total_odd_idlis = sum(idli % 2 for idli in idlis)  # Count total odd idlis

  # Check if even distribution is possible
  if total_odd_idlis % 2 != 0:
    return -1  # Can't distribute evenly if total odd idlis is odd

  # Track cumulative oddness (0 for even, 1 for odd)
  cumulative_oddness = [idlis[0] % 2] * len(idlis)  # Initialize based on first element (avoid empty list case)

  for i in range(1, len(idlis)):
    cumulative_oddness[i] = (cumulative_oddness[i - 1] + idlis[i]) % 2

  # Minimum idlis needed to distribute (considering cumulative oddness)
  min_needed = max(cumulative_oddness)

  return min_needed

# Test cases
test_cases = [
  ([1, 2, 3, 0], 2),  # Two idlis needed (distribute to first two people)
  ([2, 3, 0, 1], 2),  # Two idlis needed (distribute to last two people)
  ([1], -1),           # Impossible (one person with odd idli)
  ([], 0),             # No distribution needed (empty list)
  ([2, 4, 6], 0),      # All even idlis (no distribution needed)
]

for idlis, expected_result in test_cases:
  result = distribute_idlis_optimized(idlis.copy())
  if result == expected_result:
    print(f"Test case: idlis = {idlis}, Expected result: {expected_result}, Got: {result} - Passed")
  else:
    print(f"Test case: idlis = {idlis}, Expected result: {expected_result}, Got: {result} - Failed")

def distribute_idlis_optimized(idlis):
  """
  This function calculates the minimum number of idlis needed to distribute
  using lists such that everyone ends up with an even number of idlis.

  Args:
      idlis: A list containing the number of idlis each person already has.

  Returns:
      The minimum number of idlis to distribute, or -1 if it's impossible.
  """
  if len(idlis) == 0:
    return 0  # No distribution needed for empty list

  # Single person case
  if len(idlis) == 1:
    return -1 if idlis[0] % 2 != 0 else 0  # Single person with odd idli or even idli

  total_odd_idlis = sum(idli % 2 for idli in idlis)  # Count total odd idlis

  # Check if even distribution is possible
  if total_odd_idlis % 2 != 0:
    return -1  # Can't distribute evenly if total odd idlis is odd

  # Track cumulative oddness (0 for even, 1 for odd)
  cumulative_oddness = [idlis[0] % 2] * len(idlis)  # Initialize based on first element

  for i in range(1, len(idlis)):
    cumulative_oddness[i] = (cumulative_oddness[i - 1] + idlis[i]) % 2

  # Minimum idlis needed to distribute (considering cumulative oddness)
  min_needed = max(cumulative_oddness)

  return min_needed

# Test cases
test_cases = [
  ([1, 2, 3, 0], 2),  # Two idlis needed (distribute to first two people)
  ([2, 3, 0, 1], 2),  # Two idlis needed (distribute to last two people)
  ([1], -1),           # Impossible (one person with odd idli)
  ([], 0),             # No distribution needed (empty list)
  ([2, 4, 6], 0),      # All even idlis (no distribution needed)
]

for idlis, expected_result in test_cases:
  result = distribute_idlis_optimized(idlis.copy())
  if result == expected_result:
    print(f"Test case: idlis = {idlis}, Expected result: {expected_result}, Got: {result} - Passed")
  else:
    print(f"Test case: idlis = {idlis}, Expected result: {expected_result}, Got: {result} - Failed")
