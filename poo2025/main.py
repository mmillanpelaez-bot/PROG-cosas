from person import Person
from point import Point
from sphere import Sphere
from cylinder import Cylinder

#point
p1 = Point(2, 3,0)
p2 = Point(9, 1,0)
p2.x = 2
p2.x = 3

print (p1 == p2)

p1 = p2
p3 = p2

p1.x = 999999999
p3.x = 100
print (p1.toString())
print (p2)

print (p1.x)

# Person
manolo = Person ('Manolo', 69, '123456789Y', 'Calle Sinsalida', 'Musulman')
manuela = Person ("Manuela", 96, "123456789Y", "Calle Consalida", "Manmusul")
#manolo = Person (nome ='Manolo', age = 69, dni ='123456789Y', adress ='Calle Sinsalida', nacionality ='Musulman')

def main(): #Point, Shape3D, Cylinder, Sphere
    center = Point(1, 2, 3)

    sphere = Sphere(center, 4)
    cylinder = Cylinder(center, 3, 7)

    print(sphere)
    print()
    print(cylinder)

    # Export results to file
    with open("shapes_results.txt", "w") as f:
        f.write(str(sphere) + "\n\n" + str(cylinder))

if __name__ == "__main__":
    main()