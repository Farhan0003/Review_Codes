def find_target_indices(lst, target):
    """
    Finds all pairs of indices where the sum of elements at those indices equals the target.

    Args:
        lst (list): List of integers.
        target (int): Target sum.

    Returns:
        list: A list containing index pairs that sum up to the target.
    """
    shw = []
    length = len(lst)

    for i in range(length):
        for j in range(i + 1, length):
            if lst[i] + lst[j] == target:
                shw.extend([i, j])

    return shw


def main():
    """
    Main function to take user input and call find_target_indices.
    Handles input validation and exceptions.
    """
    try:
        target = int(input("Enter the target: "))
        length = int(input("Enter the length of the list: "))

        if length <= 0:
            print("List length must be a positive integer.")
            return

        lst = [int(input(f"Enter number {i+1}: ")) for i in range(length)]
        result = find_target_indices(lst, target)
        print("Indices:", result)

    except ValueError:
        print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()
