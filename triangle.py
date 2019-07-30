while True:
    print("welcome")
    A=int(input("enter the the value of side A"))
    B=int(input("enter the value of side B"))
    C=int(input("enter the value of side C"))
    if A==0 or B==0 or C==0:
        print("0 wacha ufala ushai ona 0 kwa triangle")
    elif A == B == C:
     print("the triangle is an equilateral triangle")
    elif A == B and A !=C:
     print("The triangle is an isocles triangle")
    elif B == C and B !=A:
        print("The triangle is an isocles triangle")
    elif C == A and C !=B:
     print("The triangle is an isocles triangle")
    elif A!=B and A!=C and B!=C:
      print("the triangle is an scalene triangle")
    else:
      print("that is not a triangle")
    try:
      pass
    except expression as identifier:
     pass
    finally:
      pass
