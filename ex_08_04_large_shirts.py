def make_shirt(size='large', text='I love Python'):
    """Displays a message with the shirt size and text printed on it."""
    print("\nThis t-shirt is size " + size + " and has the word(s): " + text + ".")

#default message
make_shirt()

#keyword argument
make_shirt(size='small', text='Puma')