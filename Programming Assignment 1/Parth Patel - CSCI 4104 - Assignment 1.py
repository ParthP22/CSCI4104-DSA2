# Student name: Parth Patel.
#
# Assignment Instructions: (DO NOT DELETE... you will lose points).
#
# Implement the insertion sort and heap sort algorithms in the
# functions that follow. Also implement the is_sorted function
# to check if a list is sorted, and the random_list function to
# generate a list of random integers. When you are working on
# implementing heap sort, in addition to the heap_sort function,
# you will likely want to begin by implementing all of its helper
# functions, which include: _build_max_heap, _max_heapify, _left,
# and _right. Carefully read the comments I have throughout, as I
# made a few minor adjustments relative to the textbook pseudocode.
# After implementing all of the functions, write some code in the
# if block at the very bottom of this file to test that your two
# sorts, your is_sorted, and your random_list works.
#
# Make sure that you carefully read the docstrings that I've provided
# for the functions, which specifies what you are to implement.
# DO NOT delete the docstrings (the multiline strings immediately after
# the signature lines of the functions). You will lose points if you
# delete the docstrings. You may delete comments that I inserted to give
# you hints.
#
# Don't change the names of any of the functions or the names of the
# parameters. 
#
# IMPORTANT: Remember that the textbook pseudocode uses 1-based indexing,
# while Python uses 0-based indexing, so you may need to make minor
# adjustments from the pseudocode (pay specific attention to the _left
# and _right helper functions for heap_sort, but those are not the only
# places where such adjustments are needed).  
#
# Note: You don't need the pass statements that I inserted, so you
# can delete them after you implement the functions.  I put them
# in temporarily so that you have valid syntax to start with.  A function
# requires at least one statement in the body.  The pass statement does
# nothing, but is a statement none-the-less.
#
# IMPORTANT: DO NOT have any print statements in the functions in this
# Python file (e.g., in the is_sorted, random_list, insertion_sort,
# heap_sort, and heap_sort's various helper functions).
# In general, you want to separate output from the computation.  You'll
# be outputting results (e.g., using print) in the if block at the very
# bottom of this module.

import random

def is_sorted(A) :
    """Returns True if A is sorted in non-decreasing order,
    and returns False if A is not sorted.
    
    Keyword arguments:
    A - a Python list.
    """

    # pass # Here temporarily (Delete this pass and put your code here)

    for i in range(0, len(A) - 1, 1):
        if A[i] > A[i + 1]:
            return False
    return True
    

    ## Hints for implementing issorted:
    ##
    ## You may deletes these hint comments if you want.
    ##
    ## Hint 1: DO NOT use the built-in function sorted in this function.
    ##       E.g., if you are tempted to call sorted and then compare
    ##       result to A, this would be wrong (or at least it would be a
    ##       terribly inefficient way to do this).  Python's sorted function
    ##       actually does a sort generating a new list that is a sorted copy
    ##       of the original.  This would be a silly, and costly, way to check
    ##       if your list is sorted.  You will get 0 points for the issorted
    ##       function if you call Python's sorted function.
    ## Hint 2: If A is sorted then A[0] <= A[1] <= A[2] <= ....
    ##       So, you can write a loop whose body does one
    ##       comparison of adjacent elements, returning False if there is a violation
    ##       within the loop. If you manage to get through the loop without returning,
    ##       then the list must be sorted, so return True.





def random_list(length, low=0, high=100) :
    """Generates and returns a Python list of random integer values.
    The integers in the list are generated uniformly at random from
    the interval [low, high], inclusive of both end points.
    
    Keyword arguments:
    length - the length of the list.
    low - the lower bound for the random integers.
    high - the upper bound for the random integers.
    """

    # pass # here temporarily (Delete this pass and put your code here)

    A = []
    for i in range(0,length):
        A.append(random.randint(low,high))
    return A
    

    ## Hint:
    ##
    ## You may deletes these hint comments if you want.
    ##
    ## Look at the documentation for the random module.
    ## There are useful functions there for generating random numbers.
    ## There are two functions in particular that generate random integers,
    ## One of them includes the upper bound, and the other does not.
    ## Also, DO NOT use the random.sample function.  The random.sample
    ## function doesn't allow repeat selection.
    ##
    ## You can either find the documentation online, or recall from
    ## the videos that the shell has a help function.  So you can
    ## import random, and then do help(random) to see all of the
    ## documentation.  dir(random) will just list the function names.
    ##
    ## Another hint: You can use a Python list comprehension to
    ## generate the list.
    ##
    ## Yet another hint: If you follow the above hints, it is possible
    ## to implement this function with a single line of code,
    ## a return statement with a list comprehension.
    ##
    ## One more hint: Recall that Python allows default values for
    ## parameters. For example, the low=0 means that if the programmer
    ## doesn't pass anything for the low parameter, then low will be 0;
    ## but otherwise low will be whatever is passed for it.
    ## Make sure your code uses the parameter variables.  The most common
    ## mistake I see with this is implementations that only work with the
    ## defaults.


def insertion_sort(A) :
    """Implementation of the insertion sort algorithm
    as specified on page 19 of the textbook.

    But keep in mind that the textbook pseudocode uses 1
    as the first index into an array, but Python list
    indexes begin at 0, so you will need to think how to
    adjust for that.
    
    Keyword arguments:
    A - a Python list.
    """
    
    # pass  # Here temporarily. Remove and replace with your code.

    for i in range(1, len(A), 1):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key



def heap_sort(A) :
    """Implementation of the heapsort algorithm
    as specified on page 170 of the textbook.

    But keep in mind that the textbook pseudocode uses 1
    as the first index into an array, but Python list
    indexes begin at 0, so you will need to think how to
    adjust for that both in this function and its helpers.

    Keyword arguments:
    A - a Python list.
    """

    # I wrote the statement that corresponds to line 1
    # of the pseudocode from page 170 for you, mainly
    # because I'm altering how the heap_size is maintained
    # compared with how it is maintained in the textbook.
    # Multiple helper functions need it. The textbook assumes
    # that it is a property of A, but we cannot add fields to
    # a Python list. So _build_max_heap will initialize it
    # and return it, and then we'll pass it around as a parameter
    # wherever it is needed.
    heap_size = _build_max_heap(A)

    
    # Parth's note: loop ends at 0, since if it was 1, then it wouldn't be
    # inclusive, which would leave one of the elements
    # as unsorted
    
    for i in range(heap_size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size = heap_size - 1
        _max_heapify(A, 0, heap_size)

    # Implement the rest of the algorithm as specified on page 170
    # here. You probably want to work on the helper functions first
    # though (see below).

    # Hint: When you call _max_heapify, in addition to the parameters
    # indicated in textbook pseudocode, you will need to pass the
    # heap_size as well because of the minor adjustments I made.


def _build_max_heap(A) :
    """Helper function for heap_sort.
    This should be mostly as described on page 167.
    The one modification is that this function should
    return the heap_size. The textbook version relies
    on A having it as a property, but we cannot do that
    here because A is a Python list and we cannot add
    properties to it. But other helper functions need
    access to it, so we will return it here, and then
    pass around as a parameter as needed.

    But keep in mind that the textbook pseudocode uses 1
    as the first index into an array, but Python list
    indexes begin at 0, so you will need to think how to
    adjust for that.

    Keyword arguments:
    A - The list we are sorting.
    """

    # I wrote this statement for you. This is the
    # equivalent of line 1 of the pseudocode of page 167.
    heap_size = len(A)

    # YOUR CODE HERE: Implement the rest of _build_max_heap here.

    
    # Parth's note: the loop ends at -1, because if it was 0, then it
    # wouldn't be inclusive, which would leave one of the elements
    # as unsorted
    
    for i in range((heap_size) // 2 - 1, -1, -1):
        _max_heapify(A,i,heap_size)

    # Hint 1: When you call _max_heapify, in addition to the parameters
    # indicated in textbook pseudocode, you will need to pass the
    # heap_size as well because of the minor adjustments I made.
    #
    # Hint 2: The loop uses floor of the result of a division.
    # You actually don't really need to explicitly call floor.
    # Instead, using Python's integer division operator // will accomplish
    # that. Although make sure you first consider the effects on that
    # statement of 0-based indexes rather than the textbook's assumption
    # of 1-based indexes.

    # Return the heap_size (after implementing rest of function
    # above). See docstring for explanation of why we are
    # returning this here.
    return heap_size


def _left(i) :
    """Returns the index of the left child of index i.

    But keep in mind that the textbook pseudocode uses 1
    as the first index into an array, but Python list
    indexes begin at 0, so you will need to think how to
    adjust for that.

    Keyword arguments:
    i - An index into the heap.
    """

    # pass # Replace this pass statement with the return statement that you need.

    return 2*i + 1

def _right(i) :
    """Returns the index of the right child of index i.

    But keep in mind that the textbook pseudocode uses 1
    as the first index into an array, but Python list
    indexes begin at 0, so you will need to think how to
    adjust for that.

    Keyword arguments:
    i - An index into the heap.
    """

    # pass # Replace this pass statement with the return statement that you need.

    return 2*i + 2


def _max_heapify(A, i, heap_size) :
    """This is the helper function described with pseudocode
    on page 165 of the textbook. It is a little different than
    the textbook version. Specificially, it has a parameter for
    the heap_size.

    But keep in mind that the textbook pseudocode uses 1
    as the first index into an array, but Python list
    indexes begin at 0, so you will need to think how to
    adjust for that.

    Keyword arguments:
    A - The list to sort.
    i - The index.
    heap_size - The heap_size as used on page 165, but passed as
            a parameter.
    """

    # Remove this pass statement and replace with your code.
    # The pass is here temporarily so that this is valid syntax.
    
    # pass
    
    l = _left(i)
    r = _right(i)
    largest = -1
    if (l < heap_size and A[l] > A[i]):
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        _max_heapify(A,largest,heap_size)

    # Hint: When you recursively call _max_heapify, in addition to
    # the parameters indicated in textbook pseudocode, you will need
    # to pass the heap_size as well.
    

    
if __name__ == "__main__" :

    ## Indented within this if block, do the following:
    ## 1) Write a few lines of code to demonstrate that your
    ##    is_sorted works correctly (i.e., that it returns True
    ##    if given a list that is sorted, and False otherwise).
    ## 2) Write a few lines of code to demonstrate that insertion_sort
    ##    correctly sorts a list (your random_list function will be useful
    ##    here).  Output (i.e., with print statements) the contents
    ##    of the list before sorting, and then again after sorting).
    ## 3) Repeat 2 to demonstrate that your heap_sort sorts correctly.

    # pass # Here temporarily (replace with your code)

    print("Random List A")
    A = random_list(50,-200,200)
   
    for i in range(0,len(A),1):
        print(A[i])
    print("\nIs It Sorted Before Insertion Sort?: " + str(is_sorted(A)))
    
    print("\nInsertion Sort")
    insertion_sort(A)
    for i in range(0,len(A),1):
        print(A[i])
       
    print("\nSorted with Insertion Sort: " + str(is_sorted(A)))



    print("\n\nRandom List B")
    B = random_list(50,-200,200)
    
    for i in range(0,len(B),1):
        print(B[i])
    print("\nIs It Sorted Before Heap Sort?: " + str(is_sorted(B)))
    
    print("\nHeap Sort")
    heap_sort(B)
    for i in range(0,len(B),1):
        print(B[i])
    
    print("\nSorted with Heap Sort: " + str(is_sorted(B)))
