Weight = int(input("Weight: "))
Convert = input("(L)bs or (K)g: ")
if Convert == "L":
    New_Weight = Weight / 2.2
    print(f"You are {New_Weight} kilos")
else:
    New_Weight = Weight * 2.2
    print(f"You are {New_Weight} pounds")
