import csv
def save_book_all_data(book_list):
    with open('contacts.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Phone_number', 'Gmail', 'Address'])
        for contact in book_list:
            writer.writerow([contact['name'], contact['phone_number'], contact['gmail'], contact['address']])

def load_books():
    book_list = []
    try:
        with open('contacts.csv', 'r', newline='') as read_file:
            reader = csv.reader(read_file)
            next(reader)
            for contact in reader:
                book_list.append({
                    'name': contact[0],
                    'phone_number': contact[1],
                    'gmail': contact[2],
                    'address': contact[3],
                })
    except FileNotFoundError:
        print("No contacts file found. Starting with an empty contact book.")
    # except Exception as e:
    #     print(f"Error loading data: {e}")
    return book_list
