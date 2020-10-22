import maya.cmds as cmds
import random as rand

def duplicateIt(duplicateNum):

    #duplicateNum = 0
    for i in range(duplicateNum):
        cmds.polySphere(axis=[0, 0, 0],
                        createUVs=2,
                        name="bubble",
                        object=True,
                        radius=1,
                        subdivisionsAxis=10,
                        subdivisionsHeight=10,
                        sy=10,
                        sx=10)
        transXValue = rand.randrange(-10, 10)
        transYValue = rand.randrange(0, 20)
        transZValue = rand.randrange(-10, 10)
        scaleValue = rand.randrange(1, 3)
        cmds.xform( translation=[transXValue, transYValue, transZValue],
                    scale=[scaleValue, scaleValue, scaleValue],
                    worldSpace=True)

    count = 0

    while count < duplicateNum:
        cube = cmds.polyCube(name = "cube")
        cubeShape = cube[0]

        randXValue = rand.randrange(-10, 10)
        randZValue = rand.randrange(-10, 10)
        cmds.setAttr(cubeShape+".translateX", randXValue)
        cmds.setAttr(cubeShape + ".translateY", 1)
        cmds.setAttr(cubeShape + ".translateZ", randZValue)
        count += 1

#enter the amount of duplicates of both spheres and cubes you want
duplicateIt(40)