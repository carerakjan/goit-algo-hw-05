def input_error(old_func):
    def new_func(*args, **wargs):
        try:
            return old_func(*args, **wargs)
        except (KeyError, IndexError):
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"

    return new_func



def parse_error(old_func):
    def new_func(*args, **wargs):
        try:
            return old_func(*args, **wargs)
        except ValueError:
            return "Need enter a command"

    return new_func