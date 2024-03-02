def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

if __name__ == '__main__':
    standard_arg(2)
    standard_arg(arg=2)

    pos_only_arg(1)
    # pos_only_arg(arg=1)

    # kwd_only_arg(3)
    kwd_only_arg(arg=3)

    # combined_example(1, 2, 3)
    combined_example(1, 2, kwd_only=3)
    combined_example(1, standard=2, kwd_only=3)
    # combined_example(pos_only=1, standard=2, kwd_only=3)
    