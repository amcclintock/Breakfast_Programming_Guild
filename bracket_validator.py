# You're working with an intern that keeps coming to you with JavaScript code that won't run because the braces,
# rackets, and parentheses are off. To save you both some time, you decide to write a
# braces/brackets/parentheses validator.
# Let's say:
#    '(', '{', '[' are called "openers."
#    ')', '}', ']' are called "closers."
# Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.
# Examples:
#   "{ [ ] ( ) }" should return True
#   "{ [ ( ] ) }" should return False
#   "{ [ }" should return False
# The trick was to use a stack.
#   Two common uses for stacks are:
#       parsing (like in this problem)
#       tree or graph traversal (like depth-first traversal)

openers_to_closers = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
openers = set(openers_to_closers.keys())
closers = set(openers_to_closers.values())


def is_valid(code):
    openers_stack = []
    for char in code:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                return False
            else:
                last_unclosed_opener = openers_stack.pop()
                if not openers_to_closers[last_unclosed_opener] == char:
                    return False
        # print(char)
    return True


if __name__ == '__main__':
    print(is_valid("This is the { Put anything in[ (( best.  You can type anything ))]\n ( ) way} to progress"))
    print(is_valid("{ [ ( ] ) }"))
    print(is_valid("{ [ }"))

