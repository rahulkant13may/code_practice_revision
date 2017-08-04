from sys import stdin, stdout


def main():

    # array input similar method
    arr = [int(x) for x in stdin.readline().split()]

    # initialize variable
    summation = 0

    # calculate sum
    for x in arr:
        summation += x

    # could use inbuilt summation = sum(arr)

    # print answer via write
    # write method writes only
    # string operations
    # so we need to convert any
    # data into string for input
    stdout.write(str(summation))


# call the main method
if __name__ == "__main__":
    main()
