# 1. TASK: print "Hello World"
print( "hello world" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( "hello, world" )	# with a comma
print(f"hello, {name}" )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( "hello, world" )	# with a comma
print(f"hello {name} world" )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

print(fave_food1) # with .format()
print(f"{fave_food1} {fave_food2}") # with an f string

print(f"I love to eat {fave_food1}, and {fave_food2}")

