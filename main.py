from vec2 import *

if __name__ == "__main__":
    # Use cases
    firstVec = Vec2(float(input("\nfirst vectors x-component\n")), float(input("\nfirst vectors y-component\n")))
    secondVec = Vec2(float(input("\nSecond vectors x-component\n")), float(input("\nSecond vectors y-component\n")))

    print(f"\nDegrees between firstVec and secondVed: {firstVec.degrees_between(secondVec)}\n")

    thirdVec = firstVec + secondVec

    print(f"Third vectors length: {thirdVec.length}\n")

    scalarProduct = firstVec * secondVec
    print(f"The scalar product is: {scalarProduct}\n")

    print(f"The first vectors cross vector is: {firstVec.get_cross_vector()}\n")

    print(f"The first vector normalized is: {firstVec.normalize()}\n")

