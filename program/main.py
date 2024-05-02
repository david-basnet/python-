import sys
import datetime
from land_manager import LandManager
from rent_land import rent_land
from return_land import return_land

def main():
    file_path = "land_data.txt"
    land_manager = LandManager(file_path)

    while True:
        print("\nOptions:")
        print("1. Read Land Data")
        print("2. Rent Land")
        print("3. Return Land")
        print("4. Exit Program")

        choice = input("Select your pick: ")

        if choice == '1':
            land_manager.display_land_availability()
        elif choice == '2':
            customer_name = input("Enter the customer name: ")
            kitta_number = int(input("Enter the kitta number of the land: "))
            duration = int(input("Enter the duration of the rent (in months): "))
            rent_land(land_manager, customer_name, kitta_number, duration)
        elif choice == '3':
            customer_name = input("Enter the customer name: ")
            kitta_number = int(input("Enter the kitta number of the land: "))
            return_date = datetime.datetime.strptime(input("Enter the return date (YYYY-MM-DD): "), '%Y-%m-%d')
            return_land(land_manager, customer_name, kitta_number, return_date)
        elif choice == '4':
            print("Exiting program...")
            sys.exit()
        else:
            print("Invalid pick. Please pick a valid option.")

if __name__ == "__main__":
    main()
