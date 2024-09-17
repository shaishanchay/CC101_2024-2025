def count_characters(string):

  lower_count = 0
  upper_count = 0
  digit_count = 0
  symbol_count = 0

  for char in string:
    if char.islower():
      lower_count += 1
    elif char.isupper():
      upper_count += 1
    elif char.isdigit():
      digit_count += 1
    else:
      symbol_count += 1


  return {
      "lower_case": lower_count,
      "upper_case": upper_count,
      "digits": digit_count,
      "symbols": symbol_count
  }

input_string = "Hello, My name is Claire! I am 18 years of age and I love my Sunny."
result = count_characters(input_string)
print(result)
