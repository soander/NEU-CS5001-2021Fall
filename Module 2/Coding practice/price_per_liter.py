def main():
    # Input prices of two products
    pack_price = float(input("Price per six-pack:"))
    liter_price = float(input("Price per two-liter:"))

    # Compute two products' per price
    pack_price_per_liter = pack_price / (6 * 0.355)
    liter_price_per_liter = liter_price / 2

    # Output result
    print("Six-pack price per liter:", pack_price_per_liter)
    print("Two-liter price per liter:", liter_price_per_liter)


if __name__ == '__main__':
    main()
