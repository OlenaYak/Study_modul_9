
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
    return f'You have added a contact {name}'

@input_error
def changes(name, phone):  # зміна номеру мобільного для вказаного імені
    if name not in phone_number_dict:
        raise KeyError(f'No contact {name} in the notebook')
    phone_number_dict[name] = phone
    return f'You have changed the {name} contact phone number'

@input_error
def show_phone(name): # вивід номеру телефону по запиту
    if name not in phone_number_dict:
        raise KeyError(f'No contact {name} in the notebook')
    result = f"Phone number is {phone_number_dict[name]} for {name}" 
    return result

@input_error
def show_all():  # вивід всього змісту записника
    if not phone_number_dict:
        print('The notebook is empty')
        return 'The notebook is empty'
    return phone_number_dict

# Вся логіка взаємодії з користувачем реалізована у функції main, всі print та input відбуваються тільки там
def main():
    bot_helper = True
    while bot_helper:
        command = input("Enter a command and info for the notebook: ").lower()
        block = command.split()
        if block[0] == 'hello':
            print('How can I help you?')
        elif block[0] == 'add':
            if len(block) < 3:
                print('Name and phone number are missing') 
            else:
                name = block[1]
                phone = block[2]
                result = notation(name, phone)
                print(result)
        elif block[0] =='change':
            if len(block) < 3:
                print('Name and phone number are missing')
            else:
                name = block[1]
                phone = block[2]
                result = changes(name, phone)
                print(result)
        elif block[0] == 'phone':
            if len(block) < 2:
                print('Name is missing')
            else:
                name = block[1]
                result = show_phone(name)
                print(result)
        elif block[0] == 'show' and block[1] == 'all':
            result = show_all()
            print(result)
        elif block[0] in ['good', 'bye', 'close', 'exit']:
            print('Good bye!')
            bot_helper = False
        else:
            print("Don't understand the command. Please, try again!")

if __name__ == "__main__":
    main()
