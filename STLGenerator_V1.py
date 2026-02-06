import math
import random


filename = ""
angleMax = input("What is the maximum angle for your wing? Type a single integer\n")
widthBMax = input("What is your maximum width of the wing? Type a single integer\n")
widthCMax = input("What is your maximum width for the column of your wing? Type a single integer\n")
lengthMax = input("What is your maximmum length for the your wing? Type a single integer\n")
lengthCMax = input("What is your maximum length for the column of your wing? Type a single integer\n")
heightCMax = input("What is your maximum height for the column of your wing? Type a single integer\n")

def generate_wing(filename,angle, widthB, widthC,length,lengthC,heightC):
    v = [
        (0,0,0), #0
        (widthB,0,0), #1
        (0,length,0), #2
        (widthB,length,0), #3
        (0,length,math.tan(angle)*length), #4
        (widthB,length, math.tan(angle)*length), #5

        ((widthB/2)-widthC*0.5,(length/2)-lengthC*0.5,0), #6
        ((widthB/2)+widthC*0.5,(length/2)-lengthC*0.5,0), #7
        ((widthB/2)-widthC*0.5,(length/2)+lengthC*0.5,0), #8
        ((widthB/2)+widthC*0.5,(length/2)+lengthC*0.5,0), #9

        ((widthB/2)-widthC*0.5,(length/2)-lengthC*0.5,heightC), #10
        ((widthB/2)+widthC*0.5,(length/2)-lengthC*0.5,heightC), #11
        ((widthB/2)-widthC*0.5,(length/2)+lengthC*0.5,heightC), #12
        ((widthB/2)+widthC*0.5,(length/2)+lengthC*0.5,heightC), #13
    ]

    faces = [
        (0,1,2),
        (2,3,1),
        (0,2,4),
        (1,3,5),
        (4,2,5),
        (5,3,2),

        (4,1,0),
        (5,1,4),

        (6,10,7),
        (7,11,10),

        (8,12,10),
        (6,10,8),

        (8,9,13),
        (13,12,8),

        (9,13,11),
        (11,7,9),

        (10,11,12), #floor of column
        (11,12,13)  #floor of column
    ]

    with open(filename, "w") as f:
        f.write("solid cube\n")
        for face in faces:
            f.write("  facet normal 0 0 0\n")
            f.write("    outer loop\n")
            for idx in face:
                x, y, z = v[idx]
                f.write(f"      vertex {x} {y} {z}\n")
            f.write("    endloop\n")
            f.write("  endfacet\n")
        f.write("endsolid cube\n")


#generate_wing("generateWingTest.stl",3, 200, 10,20,15,30)


i = 0
angleGenerated = 0
widthBGenerated = 0
widthCMaxGenerated = 0
lengthGenerated = 0
lengthCGenerated = 0
heightCGenerated = 0
for i in range(2):
    angleGenerated = random.randint(0,int(angleMax))
    widthBGenerated = random.randint(0,int(widthBMax))
    widthCGenerated = random.randint(0,int(widthCMax))
    lengthGenerated = random.randint(0,int(lengthMax))
    lengthCGenerated = random.randint(0,int(lengthCMax))
    heightCGenerated = random.randint(0,int(heightCMax))
    generate_wing(f"generateWing{i}.stl",angleGenerated,widthBGenerated,widthCGenerated,lengthGenerated,lengthCGenerated,heightCGenerated)
    
    print(f"\nangle generated {i}")
    print(angleGenerated)

    print(f"\nwidthB generated {i}")
    print(widthBGenerated)
    
    print(f"\nwidthCGenerated {i}")
    print(widthCGenerated)

    print(f"\nlengthGenerated {i}")
    print(lengthGenerated)

    print(f"\nlengthCGenerated {i}")
    print(lengthCGenerated)

    print(f"\nheightCGenerated {i}")
    print(heightCGenerated)
