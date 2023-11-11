# race of A,B,C,D four tie -> none else winner name
Speeds = {
    'A' : int(input("Enter speed of A: ")),
    'B' : int(input("Enter speed of B: ")),
    'C' : int(input("Enter speed of C: ")),
    'D' : int(input("Enter speed of D: "))
}
if(Speeds['A']==Speeds['B'] or Speeds['B']==Speeds['C'] or Speeds['C']==Speeds['D'] or Speeds['D']==Speeds['A'] or Speeds['D']==Speeds['B'] or Speeds['A']==Speeds['C'] ):
    print("NONE")
else:
    winner = max(Speeds['A'],Speeds['B'],Speeds['C'],Speeds['D'])
    for keys in Speeds:
        if(Speeds[keys]==winner):
            print(keys)