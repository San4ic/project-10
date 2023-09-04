class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)
        self.phones = []

    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        self.phones.append(phone)

    def remove_phone(self, phone_value):
        for phone in self.phones:
            if phone.value == phone_value:
                self.phones.remove(phone)

    def edit_phone(self, old_phone_value, new_phone_value):
        for phone in self.phones:
            if phone.value == old_phone_value:
                phone.value = new_phone_value

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def remove_record(self, name_value):
        if name_value in self.data:
            del self.data[name_value]

    def find_records(self, **kwargs):
        results = []
        for record in self.data.values():
            match = True
            for field_name, field_value in kwargs.items():
                if hasattr(record, field_name) and getattr(record, field_name).value.lower() != field_value.lower():
                    match = False
                    break
            if match:
                results.append(record)
        return results

    def find_record_by_name(self, name_value):
        name_value = name_value.lower()
        for name, record in self.data.items():
            if name.lower() == name_value:
                return record
        return None

def create_record():
    name_value = input("Enter the name: ")
    record = Record(name_value)
    while True:
        phone_value = input("Enter a phone number (or 'done' to finish adding phones): ")
        if phone_value.lower() == "done":
            break
        record.add_phone(phone_value)
    return record

def main():
    address_book = AddressBook()

    while True:
        user_input = input("Enter a command: ").lower()

        if user_input == "good bye" or user_input == "close" or user_input == "exit":
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add"):
            record = create_record()
            address_book.add_record(record)
            print(f"Added {record.name.value} with phone number(s).")
        elif user_input.startswith("remove"):
            _, name = user_input.split()
            address_book.remove_record(name)
            print(f"Removed {name} from the address book.")
        elif user_input.startswith("find"):
            _, field_name, field_value = user_input.split()
            if field_name == "name":
                record = address_book.find_record_by_name(field_value)
                if record:
                    print(f"Found record: {record.name.value}: {', '.join(phone.value for phone in record.phones)}")
                else:
                    print(f"No records found with name = {field_value}")
            else:
                results = address_book.find_records(**{field_name: field_value})
                if results:
                    print("Found records:")
                    for result in results:
                        print(f"{result.name.value}: {', '.join(phone.value for phone in result.phones)}")
                else:
                    print(f"No records found with {field_name} = {field_value}")
        elif user_input == "show all":
            if address_book.data:
                print("All contacts:")
                for record in address_book.data.values():
                    print(f"{record.name.value}: {', '.join(phone.value for phone in record.phones)}")
            else:
                print("No contacts found.")
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()