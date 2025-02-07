def greet():
    print("Hello")
    """
    Simple function printing hello
    :return: None
    """
def greet_improved(name):
    """
    Simple function printing hello with a name
    :param name: str
    :return: None
    """
    print(f"Hello {name}")

greet_improved("John")
greet_improved("Jane")

def custom_op(x = 0, y = 0):
    """_summary_

    Args:
        x (_type_): first number
        y (_type_): second number
        result (_type_): number, 10x+y
    """
    result = 10 * x + y
    return result
x = custom_op(5, 8)
print(f"The result of custom_op is {x}")
x = custom_op(8, 5)
print(f"The result of custom_op is {x}")

def bond_intro(name):
    print(f"The name is:", name)

def bond_name(first, last):
    return f"{last}, {first} {last}"

print(bond_name("James", "Bond"))
bond_intro(bond_name("James", "Bond"))