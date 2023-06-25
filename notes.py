def approx_ln(x, n):
    if x <= 0 or n <= 0:
        print("Error: x and n must be greater than 0")
        return

    # Initialize a & g
    a = (1 + x) / 2
    g = x ** 0.5

    def update_a(a, g):
        a = (a + g) / 2
        return a

    def update_g(a, g):  # a i+1 is used as input
        g = (a + g) ** 0.5
        return g

    def iterate(a, g, n):
        if n == 0:
            print(f"Approximate for ln(x) = {(x - 1) / a}")
            return

        a = update_a(a, g)
        g = update_g(a, g)
        n -= 1
        iterate(a, g, n)

    iterate(a, g, n)
    # approximate ln(x)
    #print(f"Approximate for ln(x) = {(x - 1) / a}")


approx_ln(100, 5)