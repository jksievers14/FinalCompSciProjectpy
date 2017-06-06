''' purpose of the function: make code more readable, reuse multiple times, write shorter code '''

print('Welcome to my cooking recipe!')
print('Your cooking skills will be put to the test')
print('You must figure out which various foods apply to recipes given')
print('If you mangae to do so, you pass with flying colors')
print('However if you dont, you better pray')
print('Keep in mind the same mealcannot be made more than once')


# Question 1
def mix_and_cook():
    print('Place layers in cooking tool')
    print('Place tomato sauce on dough')
    print('Apply cheese')
    print('Apply other light toppings of choice')
    print('Place food in the oven')
    print('Enjoy!!')
    
print('You have made it through the first stage of this game')
print('Now that your delicious meal is complete, what is it that you made?')
print('A. Tacos')
print('B. Cheeseburger')
print('C. Hamburger')
print('D. Pizza')
print('E. Ziti')
choice=input('Your choice: ')
if Q1response == 'D' or Q1response == 'd':
    print('You are correct!')

else:
    print('Too Bad')
    print('Your current score is ' + str(score) + 'out of 4')


print('Thats not all')
print('You now have extra ingredients to place on your pizza')


def fancy_pizza(*ingredients):
    print('mix_and_cook fancy_pizza' == 'fancy_pizza with {} ingredients'.format(len(ingredients)))
    print(fancy_pizza('parmesan','pepperoni','onion','red peppers','mushrooms'))
    return fancy_pizza


# Question 2
def mix_and_cook():
    print('Place layers in cooking tool')
    print('Place tomato sauce on the base layer')
    print('Apply several layers of cheese')
    print('Apply other light toppings of choice')
    print('Place food in the oven')
    print('Enjoy!!')
    
print('The second meal you just made is now complete, what is it?')
print('A. Oyster')
print('B. Lasagna')
print('C. Hamburgers')
print('D. Pizza')
print('E. Macaroni and Cheese')
choice=input('Your choice: ')
if Q2response == 'B' or 'b':
    print('You are correct!')

else:
    print ('Not even close')
    print('Your current score is ' + str(score) + 'out of 4')

print('Thats not all')
print('You now have extra ingredients to place on your Lasagna')

def fancy_lasagna(*ingredients):
    print('mix_and_cook fancy_lasagna' == 'fancy_lasagna with {} ingredients'.format(len(ingredients))) 
    print(fancy_lasagna('parmesan', 'scallions','basil', 'onions'))
    return fancy_lasagna


# Question 3
def mix_and_cook():
    print('Place layers in cooking tool')
    print('Place tomato sauce on the base layer')
    print('Apply several layers of cheese')
    print('Apply other light toppings of choice')
    print('Place food in the oven')
    print('Enjoy!!')

print('Your third delicious meal is finally complete, do you know what you made now?')
print('A. Lobster')
print('B. Enchiladas')
print('C. Empanadas')
print('D. Ducks')
print('E. Sausages')
choice=input('Your choice: ')
if Q3response == 'B' or 'b':
    print('You are correct!')

else:
    print ('SMH')
    print('Your current score is ' + str(score) + 'out of 4')

print('You woulda thought you were done')
print('You now have extra ingredients to place on your freshly made enchiladas')

def fancy_enchiladas(*ingredients):
    print('mix_and_cook fancy_enchiladas' == 'fancy_enchiladas with {} ingredients'.format(len(ingredients))) 
    print(fancy_enchiladas('parmesan', 'scallions','basil', 'onions'))
    return fancy_enchiladas

# Question 4
def mix_and_cook():
    print('Place layers in cooking tool')
    print('Place sauce on base layer')
    print('Apply cheese')
    print('Apply other light toppings of choice')
    print('Place food in the oven')
    print('Enjoy!!')

print('Your fourth fantastic meal is finally complete, what is it that you made now?')
print('A. Hot dogs')
print('B. Enchiladas')
print('C. Quesadilla')
print('D. Tacos')
print('E. Sausages')
choice=input('Your choice: ')
if Q3response == 'D' or 'd':
    print('You are correct!')

else:
    print ('Not even close')
    print('Your current score is ' + str(score) + 'out of 4')

print('Dont stop there')
print('You now have extra ingredients to place on your freshly made tacos')

def fancy_tacos(*ingredients):
    print('mix_and_cook fancy_tacos' == 'fancy_tacos with {} ingredients'.format(len(ingredients))) 
    print(fancy_tacos('parmesan', 'scallions','basil', 'onions', 'cheddar'))
    return fancy_tacos












                                                                                 

    
                                                                                 
