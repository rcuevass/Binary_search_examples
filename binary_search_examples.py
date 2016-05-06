# We need random Python library to generate our numbers to be searched
import random
# In a separate file (sorting) we have implemented a merge sort function
from sorting import merge_sort
#
from math import log


def generate_numbers(T):
    """
    This function generates a range of integers between 0 (inclusive) and
     T-1 (inclusive)
    :param T: Integer to set the maximum number in the range (T-1)
    :return: list of UNSORTED numbers
    """
    return random.sample(range(0, T), T)


def lin_search(x, key):
    """
    Function that does a brute-force search on the list; element by element
    :param x: list to be searched
    :param key: element to be found in list
    :return: number of comparisons made before finding the element in the list
    """
    # Set counter to zero
    count_ = 0
    # For each element in the list...
    for x_ in x:
        # ... compare it with the key.
        if key != x_:
            # If not found, increase counter
            count_ += 1
            # otherwise break for cycle
        else:
            break
    # provide number of comparisons
    return count_


def bin_search(x, key, count_):
    """
    Function that does binary search to find element in a list
    :param x: List to be searched
    :param key: Element to be found in list
    :param count_: integer that keeps track of number of comparisons
    :return: Number of comparisons made before the element is found
    """
    # Get length of list
    len_ = len(x)
    # If 0 or 1, then the key is the element in the list
    if len_ <= 1: return count_ + 1
    # Otherwise, find the "middle point" in the list...
    middle = len_ // 2
    # If the middle element is the key, we are finished and
    # increase counter by one.
    if x[middle] == key:
        count_ += 1
        return count_
    # If the middle element is less than the key...
    elif x[middle] < key:
        # find the sub-list to the right of the element while increasing
        # counter ...
        right = x[middle:]; count_ += 1
        # ... and repeat the process in the right sub-list
        return bin_search(right, key, count_)
    # Do something similar if the middle element is greater than the key
    elif key < x[middle]:
        left = x[:middle]; count_ += 1
        return bin_search(left, key, count_)


def isPerfectPower(n):
    """
    Function that determines whether a given integer if perfect.
    An integer n is perfect if there exists alpha and beta such that
    alpha^beta = n.
    This function determines this based on binary search
    :param n: Given integer to be checked
    :return: If the integer is perfect the function returns the pair (alpha,beta);
            None otherwise
    """
    # Get upper bound to do the binary search
    upper_bound = int(log(n,2))
    # Candidates for beta will be searched in the
    # interval [1,upper_bound+1]
    for beta in range(1,upper_bound+1):
        # Get ends of interval
        ci,di = 1,n
        # While the length of interval is greater than one ...
        while abs(ci-di)>1:
            # Find the middle point (binary search spirit!)
            alpha = (ci+di) // 2
            # If alpha^beta = n then we are finished...
            if alpha**beta == n: return [alpha,beta]
            # If alpha**beta is greater than alpha
            # then focus on the left sub-interval...
            if alpha**beta > n: di = alpha
            # ...otherwise focus on the right sub-interval
            if alpha**beta < n: ci = alpha
    # If binary search failed to find alpha and beta then return None
    return None


def main():
    """
    Function that executes program
    :return: Prints to screen results of algorithms
    """

    # Generate a list
    xTest = generate_numbers(100000)

    # Sort it using merge sort and let the user know when the
    # sorting is finished.
    xTest = merge_sort(xTest)
    print "Sorting is finished!"
    print " "

    # Execute linear and binary search and print number of comparisons to screen
    print "Number of comparisons with linear search ... ", lin_search(xTest, 90000)
    print "Number of comparisons with binary search ... ", bin_search(xTest, 90000, 0)

    # We now show an example of binary search for perfect power
    print " "
    print "The perfect power decomposition of 961 is ", isPerfectPower(961)

if __name__ == '__main__':
    main()


