# Slicing

odds = [3, 5, 7, 9, 11]
list(range(1, 3))
[odds[i] for i in range(1, 3)]
odds[1:3]
odds[1:]
odds[:3]
odds[:]

# Aggregation

sum(odds)
sum({3: 9, 5: 25})
max(range(10))
max(range(10), key=lambda x: 7 - (x - 2) * (x - 4))
all([x < 5 for x in range(5)])
perfect_square = lambda x: x == round(x**0.5) ** 2
any([perfect_square(x) for x in range(50, 60)])  # Try ,65)

# Trees


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


### +++ === ABSTRACTION BARRIER === +++ ###


def fib_tree(n):
    """Construct a Fibonacci tree.

    >>> fib_tree(1)
    [1]
    >>> fib_tree(3)
    [2, [1], [1, [0], [1]]]
    >>> fib_tree(5)
    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
    """
    if n == 0 or n == 1:
        return tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


def count_leaves(t):
    """The number of leaves in tree.

    >>> count_leaves(fib_tree(5))
    8
    """
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])


def leaves(tree):
    """Return a list containing the leaf labels of tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])


def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    print("  " * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented.


    >>> print_tree(increment_leaves(fib_tree(4)))
    3
      1
        1
        2
      2
        2
        1
          1
          2
    """
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)


def increment(t):
    """Return a tree like t but with all labels incremented.

    >>> print_tree(increment(fib_tree(4)))
    4
      2
        1
        2
      3
        2
        2
          1
          2
    """
    return tree(label(t) + 1, [increment(b) for b in branches(t)])


# Order


def fact(n):
    """Return n * n-1 * ... * 1.

    >>> fact(4)
    24
    """
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def fact_tail(n):
    """Return n * n-1 * ... * 1.

    >>> fact_tail(4)
    24
    """
    return fact_times(n, 1)


def fact_times(n, k):
    """Return k * n * n-1 * ... * 1.

    >>> fact_times(4, 3)
    72
    """
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)


haste = tree("h", [tree("a", [tree("s"), tree("t")]), tree("e")])


def print_sums(t, path_sum):
    """Print the sum of labels along the path from the root to each leaf.

    >>> print_sums(tree(3, [tree(4), tree(5, [tree(6)])]), 0)
    7
    14
    >>> print_sums(haste, '')
    has
    hat
    he
    """
    path_sum = path_sum + label(t)
    if is_leaf(t):
        print(path_sum)
    else:
        for branch in branches(t):
            print_sums(branch, path_sum)


def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """

    if is_leaf(t):
        return 0
    else:
        for bs in branches(t):
            return 1+height(tree(label(bs),branches(bs)))

def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return label(t)+max([max_path_sum(b) for b in branches(t)])
        
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ... [tree(2,
    ... [tree(3),
    ... tree(4)]),
    ... tree(5,
    ... [tree(6,
    ... [tree(7)]),
    ... tree(8)])])
    >>> print_tree(square_tree(numbers))
        1
      4
        9
        16
      25
        36
          49
        64
    """
    return tree(label(t)**2,[square_tree(b) for b in branches(t)])
    
    
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree)==x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b,x)
        if path:
            return [label(tree)]+ path
            
            
def prune_binary(t, nums):
    """
    >>> t = tree("1", [tree("0", [tree("0"), tree("1")]), tree("1", [tree("0")])])
    >>> print_tree(prune_binary(t, ["01", "110", "100"]))
    1
      0
        0
      1
        0
    """
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [x[1:] for x in nums if x[0] == label(t)]
        new_branches = []
        for b in branches(t):
            pruned_branch = prune_binary(b, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return tree(label(t),new_branches)


 

    

    