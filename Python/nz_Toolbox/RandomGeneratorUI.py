import maya.cmds as cmds
import random as rand

class RandomGeneratorUI():
    def __init__(self):
        self.myWindow = "MyWindowTool"

    def duplicateIt(self, duplicateNum):
        Xmin = cmds.intField(self.int_fieldXmin, query=True, value=True)
        Xmax = cmds.intField(self.int_fieldXmax, query=True, value=True)
        Ymin = cmds.intField(self.int_fieldYmin, query=True, value=True)
        Ymax = cmds.intField(self.int_fieldYmax, query=True, value=True)
        Zmin = cmds.intField(self.int_fieldZmin, query=True, value=True)
        Zmax = cmds.intField(self.int_fieldZmax, query=True, value=True)
        scaleMin = cmds.intField(self.int_fieldScaleMin, query=True, value=True)
        scaleMax = cmds.intField(self.int_fieldScaleMax, query=True, value=True)
        sels = cmds.ls(sl=True)
        for i in range(duplicateNum):
            cmds.duplicate(sels)
            transXValue = rand.randrange(Xmin, Xmax)
            transYValue = rand.randrange(Ymin, Ymax)
            transZValue = rand.randrange(Zmin, Zmax)
            scaleValue = rand.randrange(scaleMin,scaleMax)
            cmds.xform(translation=[transXValue, transYValue, transZValue],
                       scale=[scaleValue, scaleValue, scaleValue],
                       worldSpace=True)
            sels = cmds.ls(sl=True)
    def defaultButtonPush(self):
        print "Button was pushed"

    def getTheNums(self, nums):
        nums = cmds.intField(self.intFieldGrp, query=True, value=True)

        if nums > 0:
            self.duplicateIt(nums)

    def makeAWindow(self):
        self.window = cmds.window(title="Duplicate Amount", iconName='Short Name', widthHeight=(400, 500))
        self.colmLayout = cmds.columnLayout(adjustableColumn=True)
        cmds.text(label='Select the object you want to duplicate and fill in all the values', align='center')
        cmds.text(label='Duplicate Amount', align='left')
        self.intFieldGrp = cmds.intField("Enter the number of duplicates you want.", minValue=0, maxValue=100)
        cmds.text(label='X minimum', align='left')
        self.int_fieldXmin = cmds.intField("Enter the X minimum you want",
                                           minValue=-100,
                                           maxValue=100,
                                           parent=self.colmLayout)
        cmds.text(label='X maximum', align='left')
        self.int_fieldXmax = cmds.intField("Enter the X maximum you want",
                                           minValue=-100,
                                           maxValue=100,
                                           parent=self.colmLayout)
        cmds.text(label='Y minimum', align='left')
        self.int_fieldYmin = cmds.intField("Enter the Y minimum you want",
                                           minValue=-100,
                                           maxValue=100,
                                           parent=self.colmLayout)
        cmds.text(label='Y maximum', align='left')
        self.int_fieldYmax = cmds.intField("Enter the Y maximum you want",
                                           minValue=-100,
                                           maxValue=100,
                                           parent=self.colmLayout)
        cmds.text(label='Z minimum', align='left')
        self.int_fieldZmin = cmds.intField("Enter the Z minimum you want",
                                           minValue=-100,
                                           maxValue=100,
                                           parent=self.colmLayout)
        cmds.text(label='Z maximum', align='left')
        self.int_fieldZmax = cmds.intField("Enter the Z maximum you want",
                                           minValue=-100,
                                           maxValue=100,
                                           parent=self.colmLayout)
        cmds.text(label='Scale Minimum', align='left')
        self.int_fieldScaleMin = cmds.intField("Enter the scale minimum you want",
                                               minValue=-100,
                                               maxValue=100,
                                               parent=self.colmLayout)
        cmds.text(label='Scale Maximum', align='left')
        self.int_fieldScaleMax = cmds.intField("Enter the scale maximum you want",
                                               minValue=-100,
                                               maxValue=100,
                                               parent=self.colmLayout)
        cmds.button(label='Duplicate!', command=self.getTheNums)
        cmds.button(label='Close', command=('cmds.deleteUI(\"' + self.window + '\", window=True)'))
        cmds.setParent('..')
        cmds.showWindow(self.window)



#randGenWindow = RandomGeneratorUI()
#randGenWindow.makeAWindow()
