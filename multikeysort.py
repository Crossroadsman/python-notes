def multikeysort(dictlist, columns):
    """Sorts on arbitrary multiple columns of a dictionary.

    `columns` is a list of column names. Any names prefixed with '-' are
    sorted in descending order

    Inspired by: https://stackoverflow.com/questions/1143671/python-sorting-list-of-dictionaries-by-multiple-keys
    """
    import operator
    
    # produce a list of tuples where the first is the cleaned-up column name
    # and the second is a bool for whether to reverse the sort order 
    comparers = []
    for column in columns:
        if column.startswith("-"):
            comparers.append(
                (operator.itemgetter(column[1:].strip()),
                 True)
            )
        else:
            comparers.append(
                (operator.itemgetter(column.strip()),
                 False)
            )
    
    """Because Python uses a stable algorithm, we can sort by multiple keys
    by sorting the comparers list in reverse order
    
    Note that because the specific algorithm is Timsort, multiple sorts are
    efficient because we take advantage of anything already in order in the
    dataset
    https://docs.python.org/3/howto/sorting.html
    """
    for fn, reverse in comparers[::-1]:
        dictlist.sort(key=fn, reverse=reverse)
    
    return dictlist
