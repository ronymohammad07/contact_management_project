from save_data import save_book_all_data

def add_book_informations(book_list):
    name = str(input('Enter your full Name: '))
    # if not name.isalpha():
    #     print(f'{' ':<15}Error:The contact name must be alphabatic characters only.')
    #     return

    phone_number = input('Enter Phone Number: ').strip()
    if not phone_number.isdigit():
        print(f"{' ':<10}Error: Phone number must be numeric. Please enter a valid number (e.g, 018000000000).")
        return
    if len(phone_number) != 11:
        print(f'{' ':<15}Error: Phone number must be exactly 11 digits long.')
        return
    for contact in book_list:
        if contact['phone_number'] == phone_number:
            print(f"{' ':<15}Error: The phone number {phone_number} is already assigned to another contact.")
            return
    
    gmail = str(input('Enter Gmail: '))
    if "@" not in gmail or "." not in gmail:
        print(f"{' ':<15}Error: Please enter a valid Gmail address (e.g., example@gmail.com).")
        return
    for contact in book_list:
        if contact['gmail'] == gmail:
            print(f"{' ':<15}Error: The Gmail {gmail} is already assigned to another contact.")
            return
    
    address = str(input('Enter Address: '))

    new_contact = {
        'name': name,
        'phone_number': phone_number,
        'gmail': gmail,
        'address': address,
    }

    book_list.append(new_contact)
    
    save_book_all_data(book_list)

    print(f'{' ':<15}Contact added successfully.')
