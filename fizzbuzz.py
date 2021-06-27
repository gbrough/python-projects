# Fizzbuzz - print numbers from 1 to 100. 
# For numbers divisible by 3 print fizz
# For numbers divisible by 5 print buzz
# For numbers divisible by 15 print fizzbuzz

#%%
def fizzbuzz():
  for i in range(1,101):
    if (i % 15 == 0):
      print("fizzbuzz")
    elif (i % 5 == 0):
      print("buzz")
    elif (i % 3 == 0):
      print("fizz")
    else:
      print(i)


fizzbuzz()
# %%
