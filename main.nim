echo "Hello World"

proc add(a, b: int): int {.noSideEffect.} =
    # Echo has side effects.
    # echo("Value of a is:", a)
    #
    return a + b

for i in 0..20:
    echo add(i, i)

