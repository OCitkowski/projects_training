def make_pizza(size, *args):
    if args:
        print(f'components for size {size} - {args}' )
    else:
        print(f'sorry? but not components')


def build_profile(first, last, **kwargs):
    kwargs['first name'] = first
    kwargs['last name'] = last
    print(f"{kwargs.get('location')} - location")
    print(f"{kwargs.get('sex')} - sex")
    return kwargs