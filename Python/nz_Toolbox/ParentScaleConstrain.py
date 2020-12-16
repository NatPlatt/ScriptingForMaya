import maya.cmds as cmds

class ParentAndScaleConstrain():
    def __init__(self):
        self.myWindow = 'myParentAndConstrainWindow'
    def parentAndScale(self, *_):
        sels = cmds.ls(sl=True)

        if len(sels) % 2 == 1:
            print "You need to select an even number of objects"
            cmds.error("You need to select an even number of objects")

        selNum = len(sels)

        for i in range(0, selNum, 2):
            cmds.parentConstraint(sels[i+1], sels[i], maintainOffset=True)
            cmds.scaleConstraint(sels[i+1], sels[i], maintainOffset=True)

    def makeAWindow(self):
        self.delete()
        self.myWindow = cmds.window(title="myParentAndConstrainWindow",
                                    widthHeight=(400, 100))
        self.colmLayout = cmds.columnLayout(parent=self.myWindow,
                                            adjustableColumn=True)
        cmds.text(label='Select each object to parent and scale constrain (joint then ctrl)', align='center')
        cmds.button(parent=self.colmLayout,
                    label='Parent and Scale Constrain Selection',
                    command=self.parentAndScale)
        cmds.button(parent=self.colmLayout,
                    label='Close',
                    command=('cmds.deleteUI(\"' + self.myWindow + '\", window=True)'))
        cmds.setParent('..')

        cmds.showWindow(self.myWindow)

    def delete(self):
        if cmds.window(self.myWindow, exists=True):
            cmds.deleteUI(self.myWindow)