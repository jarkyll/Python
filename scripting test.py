#! /usr/bin/env python

def hello_command(name, print_counter=False, repeat=10):
    """Print nice greetings."""
    for i in range(repeat):
        if print_counter:
            x = i
            print '1'
        print 'Hello, %s!' % name

if __name__ == '__main__':
    import scriptine
    scriptine.run()
