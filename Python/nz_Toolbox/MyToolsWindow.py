import maya.cmds as cmds
import RandomGeneratorUI as randGen
import RenamerWithWindow as renamer

class ToolsUI():
    def __init__(self):
        self.myWindow = "MyWindowTool"

    def makeTheWindow(self):
        self.delete()
        self.myWindow = cmds.window(title="MyToolsToolbox",
                                        widthHeight=(300, 100))
        self.colmLayout = cmds.columnLayout(parent=self.myWindow,
                                                adjustableColumn=True)

        cmds.button(label='RandomGenerate', command=self.RandomGenOpen)
        cmds.button(label='Rename', command=self.RenamerOpen)
        cmds.button(label='Close', command=('cmds.deleteUI(\"' + self.myWindow + '\", window=True)'))

        cmds.showWindow(self.myWindow)

    def delete(self):
        if cmds.window(self.myWindow, exists=True):
            cmds.deleteUI(self.myWindow)

    def RandomGenOpen(self, myWindow):
        randGen.RandomGeneratorUI().makeAWindow()
        #randomGenerator()


    def RenamerOpen(self, myWindow):
        renamer.RenamerUI().makeAWindow()
        #renamerWindow()


#toolWindow = ToolsUI()
#toolWindow.makeTheWindow()