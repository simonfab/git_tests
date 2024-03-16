''' test file for git issues and branch merging'''

def farenheit_to_celsius(farenheit):
    '''convert users farenheit temperature to celsius'''
    return (farenheit - 32) * 5 / 9

user_input = input('Please enter your message for printing..')
print(f'Your message is "{user_input}"')

user_farenheit = float(input('Enter your temp in farenheit: '))
celsius = farenheit_to_celsius(user_farenheit)
print (f'{user_farenheit}F is {celsius:.2f}C')
