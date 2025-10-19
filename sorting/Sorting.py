def sort_numbers():
    print("=== Number Sorting Program ===")

    # Get numbers from the user
    numbers = input("Enter numbers separated by spaces: ")

    # Convert input into a list of numbers
    num_list = [float(n) for n in numbers.split()]

    # Ask user for sorting preference
    order = input("Sort in ascending or descending order? (a/d): ").lower()

    if order == 'a':
        num_list.sort()
        print("\nNumbers sorted in ascending order:")
    elif order == 'd':
        num_list.sort(reverse=True)
        print("\nNumbers sorted in descending order:")
    else:
        print("\nInvalid choice! Sorting in ascending order by default.")
        num_list.sort()

    print(num_list)
    print(f"the sum of the numbers is: {sum(num_list)}")


# Run the program
sort_numbers()
input("press any key to end...")
