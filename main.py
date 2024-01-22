phone_number_dict = {}

def input_error(func):
    def exception_handling(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Please, enter a name"
        except ValueError:
            return "Please, enter name and phone number"
        except IndexError:
            return "Incorrect command"
    return exception_handling

@input_error
def notation(name, phone):   # запис телефону в словник
    if name in phone_number_dict:
        raise ValueError('The contact is already in the notebook')
    phone_number_dict[name] = phone
    #print(f'You have added a contact {name}')
    return f'You have added a contact {name}'

@input_error
def changes(name, phone):  # зміна номеру мобільного для вказаного імені
    if name not in phone_number_dict:
        raise KeyError(f'No contact {name} in the notebook')
    phone_number_dict[name] = phone
    #print(f'You have changed the {name} contact phone number')
    return f'You have changed the {name} contact phone number'

@input_error
def show_phone(name): # вивід номеру телефону по запиту
    if name not in phone_number_dict:
        raise KeyError(f'No contact {name} in the notebook')
    result = f"Phone number is {phone_number_dict[name]} for {name}" 
    #print(result)
    return result

@input_error
def show_all():  # вивід всього змісту записника
    if not phone_number_dict:
        #print('The notebook is empty')
        return 'The notebook is empty'
    #print(phone_number_dict)
    return phone_number_dict

# Вся логіка взаємодії з користувачем реалізована у функції main, всі print та input відбуваються тільки там
def main():
    bot_helper = True
    while bot_helper:
        command = input("Enter a command and info for the notebook: ").lower()
        if command == 'hello':
            print('How can I help you?')
        elif command.startswith('add'):
            try:
                name, phone = command.split()[1:]
                result = notation(name, phone)
            except ValueError as e:
                result = str(e)
            print(result)
        elif command.startswith('change'):
            try:
                name, phone = command.split()[1:]
                result = changes(name, phone)
            except ValueError as e:
                result = str(e)
            print(result)
        elif command.startswith('phone'):
            try:
                name = command.split()[1]
                result = show_phone(name)
            except ValueError as e:
                result = str(e)
            print(result)
        elif command == 'show all':
            print(show_all())
        elif command in ['good bye', 'close', 'exit']:
            print('Good bye!')
            bot_helper = False
        else:
            print("Don't understand the command. Please, try again!")

if __name__ == "__main__":
    main()