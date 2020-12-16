import maya.cmds as cmds

class ToggleRotation():
    def __init__(self):
        self.myWindow = "myToggleWindow"

    def ToggleItOn(self, *_):
        sels = cmds.ls(sl=True)
        selsNum = len(sels)

        for i in range(selsNum):
            cmds.toggle(sels[i], localAxis=True)
            cmds.setAttr(sels[i]+".displayLocalAxis", k=True)
            cmds.setAttr(sels[i] + ".jointOrientX", k=True)
            cmds.setAttr(sels[i] + ".jointOrientY", k=True)
            cmds.setAttr(sels[i] + ".jointOrientZ", k=True)

    def makeAWindow(self):
        self.delete()
        self.myWindow = cmds.window(title="myToggleWindow",
                                    widthHeight=(400, 100))
        self.colmLayout = cmds.columnLayout(parent=self.myWindow,
                                            adjustableColumn=True)
        cmds.text(label='Toggle on to view local rotation axis', align='center')
        cmds.button(parent=self.colmLayout,
                    label='Toggle On',
                    command=self.ToggleItOn)
        cmds.button(parent=self.colmLayout,
                    label='Close',
                    command=('cmds.deleteUI(\"' + self.myWindow + '\", window=True)'))
        cmds.setParent('..')

        cmds.showWindow(self.myWindow)

    def delete(self):
        if cmds.window(self.myWindow, exists=True):
            cmds.deleteUI(self.myWindow)

#toggleWindow = ToggleRotation()
#toggleWindow.makeAWindow()