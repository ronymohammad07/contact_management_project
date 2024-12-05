import csv
from save_data import load_books
from add_new_contact import add_book_informations
from view_all_data import view_all_book_data
from remove_contact import remove_data
from update_contact import book_update
from search_contact import search_contact

book_list = load_books()

while True:
    print('Welcome to Contact Book Management System.')
    print('0. Exit Program.')
    print('1. Add Contact.')
    print('2. View All Contacts.')
    print('3. Update Contact Information.')
    print('4. Remove Contact.')
    print('5. Search Contact by Name or Phone Number.')

    enter_choice = input('Enter Your Choice: ')

    if enter_choice == '0':
        print('Thanks for using the Contact Book Management system.')
        break
    
    elif enter_choice == '1':
        add_book_informations(book_list)
        
    elif enter_choice == '2':
        view_all_book_data(book_list)
        
    elif enter_choice == '3':
        book_update(book_list)
        
    elif enter_choice == '4':
        remove_data(book_list)
        
    elif enter_choice == '5':
        search_contact(book_list)
        
    else:
        print('Invalid Choice.')
