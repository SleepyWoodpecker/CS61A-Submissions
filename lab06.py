HW_SOURCE_FILE = __file__
# list.append() returns None

def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurrence of entry and then returns lst.

    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> test_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> double_lst = [1, 2, 1, 2, 3, 3]
    >>> double_lst = insert_items(double_lst, 3, 4)
    >>> double_lst
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    >>> # Ban creating new lists
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'insert_items',
    ...       ['List', 'ListComp', 'Slice'])
    True
    """
    "*** YOUR CODE HERE ***"
    # I mean I tried this with an try... except... loop, but I guess that does not work as elegantly as this...
    index = 0
    while index < len(lst):
        if lst[index] == entry:
            lst.insert(index + 1, elem)
            index += 2
        else:
            index += 1
    
    return lst


def count_occurrences(t, n, x):
    """Return the number of times that x appears in the first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(s, 1, 3)
    1
    >>> count_occurrences(s, 3, 2)
    3
    >>> next(s)
    1
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> count_occurrences(s2, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
    # 0th element counts as first element
    iter_count, match_count = 0, 0
    current = next(t)
    while iter_count < n:
        if current == x:
            match_count += 1
        # move the iterator to the next elements
        if iter_count < n - 1:
            current = next(t)
        iter_count += 1
        
    return match_count

    #answer uses a for loop to loop over the iterator, which I guess is definitely a much better idea...
    # for _ in range(n):



def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.
    Iterate through the items such that if the same iterator is passed into
    the function twice, it continues in the second call at the point it left
    off in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    current_streak_number, current_streak = None, 0
    while True:
        current = next(t)
        # check if the current element has been recorded in the dictionary
        if current_streak_number != current:
            current_streak_number, current_streak = current, 1
        else:
            current_streak += 1

        if current_streak == k:
            return current_streak_number

def partial_reverse(lst, start):
    """Reverse part of a list in-place, starting with start up to the end of
    the list.

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    "*** YOUR CODE HERE ***"
    # count the number of swaps you have to make
    for i in range(0, len(lst) - start - 1):
        lst.insert(start + i, lst.pop())


def index_largest(seq):
    """Return the index of the largest element in the sequence.

    >>> index_largest([8, 5, 7, 3 ,1])
    0
    >>> index_largest((4, 3, 7, 2, 1))
    2
    """
    assert len(seq) > 0
    "*** YOUR CODE HERE ***"
    max, index = seq[0], 0
    for i in range(1, len(seq)):
        if seq[i] > max:
            max, index = seq[i], i
    return index


def pizza_sort(lst):
    """Perform an in-place pizza sort on the given list, resulting in
    elements in descending order.

    >>> a = [8, 5, 7, 3, 1, 9, 2]
    >>> pizza_sort(a)
    >>> a
    [9, 8, 7, 5, 3, 2, 1]
    """
    pizza_sort_helper(lst, 0)

# sort in ascending order first, then flip everything around
# input for lst should always be lst, so that the same list is always the one being modified
# what if I used start as the number of iterations
def pizza_sort_helper(lst, start):
    # print("DEBUG:", "LOOP IS HAPPENING", start)
    if start < len(lst):
        # print("DEBUG:", index_largest(lst[start:]), lst[start:])
        partial_reverse(lst, index_largest(lst[start:]) + start)
        partial_reverse(lst, start)
        # print("DEBUG:", lst, "\n")
        pizza_sort_helper(lst, start + 1)
