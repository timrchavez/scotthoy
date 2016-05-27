ABOUT
=====

I don't know if it's video games or hwat but it's so unfair to blame your code
for its exceptions.  Will you please stop?

EXAMPLE
=======

    from scotthoy import scotthoy


    try:
        with scotthoy():
            raise TypeError
    except scotthoy.VideoGameException, scotthoy.HwatException:
        scotthoy.will_you_please_stop()
