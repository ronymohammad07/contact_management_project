def view_all_book_data(book_list):
    if not book_list:
        print("No contacts available.")
    else:
        print(f"{'Name':<25} {'Phone Number':<18} {'Gmail':<23} {'Address':<28}")
        print("=" * 80)
        for index, contact in enumerate(book_list, start=1):
            print(f"{index}.{contact['name']:<20} {contact['phone_number']:<15} {contact['gmail']:<25} {contact['address']:<25}")
            print('_'*80)
            
        # print("=" * 80)
