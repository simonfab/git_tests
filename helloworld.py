''' test file for git issues and branch merging'''

def get_user_message():
    '''Prompt the user for a message and return it.'''
    user_input = input('Please enter your message for printing: ')
    return user_input

def get_fahrenheit_temperature():
    '''Prompt the user for a temperature in Fahrenheit and validate it's a number.'''
    while True:
        try:
            fahrenheit = float(input('Enter temperature in Fahrenheit: '))
            return fahrenheit
        except ValueError:
            print('Please enter a valid number.')

def fahrenheit_to_celsius(fahrenheit):
    'Convert Fahrenheit to Celsius.'
    return (fahrenheit - 32) * 5 / 9

def main():
    '''main'''
    # Handle users message
    message = get_user_message()
    print(f'Your message is "{message}"')

    # Handle temperature conversion
    fahrenheit = get_fahrenheit_temperature()
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f'{fahrenheit}F is {celsius:.2f}C')

if __name__ == '__main__':
    main()
