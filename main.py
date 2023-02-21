from vec2 import *
import sys

# Gets an input, and if the input is a float, it will it return it, otherwise it will quit
def get_float_input(msg) -> float:
    inp = input(msg)
    try:
        return float(inp)
    except:
        sys.exit("Not valid number")



if __name__ == "__main__":
    # Use cases
    firstVec = Vec2(get_float_input("\nfirst vectors x-component\n"), get_float_input("\nfirst vectors y-component\n"))
    secondVec = Vec2(get_float_input("\nSecond vectors x-component\n"), get_float_input("\nSecond vectors y-component\n"))

    print(f"\nDegrees between firstVec and secondVed: {firstVec.degrees_between(secondVec)}\n")

    thirdVec = firstVec + secondVec

    print(f"Third vectors length: {thirdVec.length}\n")

    scalarProduct = firstVec * secondVec
    print(f"The scalar product is: {scalarProduct}\n")

    print(f"The first vectors cross vector is: {firstVec.get_cross_vector()}\n")

    print(f"The first vector normalized is: {firstVec.normalize()}\n")

