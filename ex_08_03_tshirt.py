def make_shirt(size, text):
    """Displays a message with the shirt size and text printed on it."""
    print("\nThis t-shirt is size " + size + " and has the word(s): " + text + ".")

# positional argument
make_shirt('medium', 'Nike')

#keyword argument
make_shirt(size='large', text='Adidas')