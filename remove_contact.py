from save_data import save_book_all_data

def remove_data(book_list):
    contact_info = input("Enter the Phone Number or Gmail to remove the contact: ")

    contact_found = None
    if contact_info.isdigit():
        for contact in book_list:
            if contact['phone_number'] == contact_info:
                contact_found = contact
                break
    else:
        for contact in book_list:
            if contact['gmail'] == contact_info:
                contact_found = contact
                break
    
    if contact_found:
        book_list.remove(contact_found)
        save_book_all_data(book_list)
        print(f"{' ':<15}Contact with {contact_found['phone_number']} has been removed successfully.")
    else:
        print(f"{' ':<15}Error: Contact with {contact_info} not found.")
