def swap_every_two_pairs(arr):
    """
    Swaps every two adjacent pairs in the given list.

    Args:
        arr (list): List of integers.

    Returns:
        list: A new list with swapped elements.
    """
    for i in range(0, len(arr) - 3, 4):
        arr[i], arr[i + 1], arr[i + 2], arr[i + 3] = (
            arr[i + 2], arr[i + 3], arr[i], arr[i + 1]
        )
    return arr


def main():
    """
    Main function to take user input, call swap_every_two_pairs, and handle exceptions.
    """
    try:
        length = int(input("Enter the length of the list: "))

        if length <= 0:
            print("List length must be a positive integer.")
            return

        arr = [int(input(f"Enter number {i+1}: ")) for i in range(length)]
        result = swap_every_two_pairs(arr)
        print("Swapped List:", result)

    except ValueError:
        print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()
