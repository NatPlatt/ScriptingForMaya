import maya.cmds as cmds
import RandomGeneratorUI as randGen
import RenamerWithWindow as renamer
import FreezeDelete as freezeDelete
import GroupAndMatch as groupMatch
import ParentScaleConstrain as psConstrain
import ToggleLocalRotation as toggleRot

class ToolsUI():
    def __init__(self):
        self.myWindow = "MyWindowTool"

    def makeTheWindow(self):
        self.delete()
        self.myWindow = cmds.window(title="MyToolsToolbox",
                                        widthHeight=(300, 200))
        self.colmLayout = cmds.columnLayout(parent=self.myWindow,
                                                adjustableColumn=True)
        cmds.text(label='Select the tool you want to use', align='center')
        cmds.button(label='Random Generate', command=self.RandomGenOpen)
        cmds.button(label='Rename', command=self.RenamerOpen)
        cmds.button(label='Freeze and Delete', command=self.FreezeDeleteOpen)
        cmds.button(label='Group and Match Transforms', command=self.GroupMatchOpen)
        cmds.button(label='Parent and Scale Constrain', command=self.ParentScaleOpen)
        cmds.button(label='Toggle Local Axis', command=self.ToggleOpen)
        cmds.button(label='Close', command=('cmds.deleteUI(\"' + self.myWindow + '\", window=True)'))

        cmds.showWindow(self.myWindow)

    def delete(self):
        if cmds.window(self.myWindow, exists=True):
            cmds.deleteUI(self.myWindow)

    def RandomGenOpen(self, myWindow):
        randGen.RandomGeneratorUI().makeAWindow()

    def RenamerOpen(self, myWindow):
        renamer.RenamerUI().makeAWindow()

    def FreezeDeleteOpen(self, myWindow):
        freezeDelete.FreezeAndDelete().makeAWindow()

    def GroupMatchOpen(self, myWindow):
        groupMatch.GroupAndMatch().makeAWindow()

    def ParentScaleOpen(self, myWindow):
        psConstrain.ParentAndScaleConstrain().makeAWindow()

    def ToggleOpen(self, myWindow):
        toggleRot.ToggleRotation().makeAWindow()



#toolWindow = ToolsUI()
#toolWindow.makeTheWindow()