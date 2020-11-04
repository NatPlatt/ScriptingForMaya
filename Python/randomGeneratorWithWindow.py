import maya.cmds as cmds
import random as rand

def duplicateIt(duplicateNum):

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

def defaultButtonPush():
    print "Button was pushed"
def getTheNums(num):
    nums = cmds.intField(intFieldGrp, query = True, value = True)
    if nums > 0:
        duplicateIt(nums)
    
window = cmds.window( title="Duplicate Amount", iconName='Short Name', widthHeight=(300, 100) )
cmds.columnLayout( adjustableColumn=True )
intFieldGrp = cmds.intField("Enter the number of duplicates you want.", minValue=0, maxValue=100)
cmds.button( label='Duplicate!', command = getTheNums)
cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.setParent( '..' )
cmds.showWindow( window )



