def main():
    # Input integer width and height of rectangle
    width = float(input("Enter width:"))
    height = float(input("Enter height:"))

    # Compute the area, perimeter and diagonal of rectangle
    area = width * height
    perimeter = (width + height) * 2
    diagonal = (width ** 2 + height ** 2) ** 0.5

    # Output the results
    print("The area of the rectangle is ", float(area))
    print("The perimeter of the rectangle is", float(perimeter))
    print("The diagonal of the rectangle is", float(diagonal))


if __name__ == '__main__':
    main()
