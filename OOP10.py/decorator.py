# a function that extends the behaviour of another function without modifying base function
# pass base function as an argument to the decorator


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Here is your sprinkles 🎊")
        func(*args, **kwargs)

    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Here is your fudge added🍫")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream 🍦")


get_ice_cream("vanilla")
