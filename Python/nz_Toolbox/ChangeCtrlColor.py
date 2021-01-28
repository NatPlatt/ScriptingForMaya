import maya.cmds as cmds


class ChangeCtrlColor():
    def __init__(self):
        self.myWindow = "MyCtrlColorWindow"

    def getTheControl(self, *_):
        ctrlsList = cmds.ls(sl=True)
        myColor = cmds.colorIndexSliderGrp(self.colorIndexSliderObj, query=True, value=True)
        myColor = myColor - 1
        print("My color value is " + str(myColor))

        for ctrl in ctrlsList:
            shapeNodes = []
            shape = cmds.listRelatives(ctrl, shapes=True)
            shapeNodes.append(shape)
            cmds.setAttr(shape[0] + '.overrideEnabled', 1)
            for shape in shapeNodes:
                cmds.setAttr(shape[0] + '.overrideColor', myColor)

    def makeAWindow(self):
        self.delete()
        self.myWindow = cmds.window(title="MyCtrlColorWindow",
                                    widthHeight=(300, 100))
        self.colmLayout = cmds.columnLayout(parent=self.myWindow,
                                            adjustableColumn=True)
        cmds.text(label='Select the ctrl shapes and then the color', align='center')
        self.colorIndexSliderObj = cmds.colorIndexSliderGrp(label='ChangeColor', min=0, max=31)
        cmds.button(parent=self.colmLayout,
                    label='Color It!',
                    command=self.getTheControl)
        cmds.button(parent=self.colmLayout,
                    label='Close',
                    command=('cmds.deleteUI(\"' + self.myWindow + '\", window=True)'))
        cmds.setParent('..')

        cmds.showWindow(self.myWindow)

    def delete(self):
        if cmds.window(self.myWindow, exists=True):
            cmds.deleteUI(self.myWindow)


#ctrlColor = ChangeCtrlColor()
#ctrlColor.makeAWindow()