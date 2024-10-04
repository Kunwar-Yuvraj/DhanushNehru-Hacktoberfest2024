def merge_sort(array):
    """Sorts an array using the merge sort algorithm.

    Args:
        array (list): The list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements.
    """
    if len(array) <= 1:  # Base case: an array of 0 or 1 element is already sorted.
        return array

    # Find the middle point to divide the array into two halves
    mid_index = len(array) // 2

    # Recursively sort the two halves
    left_half = merge_sort(array[:mid_index])
    right_half = merge_sort(array[mid_index:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """Merges two sorted lists into a single sorted list.

    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.

    Returns:
        list: A new list containing all elements from both input lists, sorted.
    """
    merged_array = []
    left_index, right_index = 0, 0

    # Traverse both lists and append the smaller element to the merged array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1

    # Collect any remaining elements from the left list
    merged_array.extend(left[left_index:])
    # Collect any remaining elements from the right list
    merged_array.extend(right[right_index:])

    return merged_array


def main():
    """Main function to execute the merge sort program."""
    try:
        # Get user input for the array to be sorted
        user_input = input("Enter numbers separated by spaces: ")
        array = list(map(int, user_input.split()))  # Convert input string to a list of integers

        # Sort the array using merge sort
        sorted_array = merge_sort(array)

        # Display the sorted array
        print("Sorted array:", sorted_array)

    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces.")


if __name__ == "__main__":
    main()
