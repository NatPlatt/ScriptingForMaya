import maya.cmds as cmds


class FreezeAndDelete():
    def __init__(self):
        self.myWindow = 'myFreezeAndDeleteWindow'

    def deleteHistory(self,*_):
        sels = cmds.ls(sl=True)
        cmds.constructionHistory(query=True, toggle=True)
        cmds.delete(ch=True)

    def freezeTransforms(self,*_):
        sels = cmds.ls(sl=True)
        if sels >= 1:
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=2)
        else:
            cmds.error('You need to select the object or objects you want to freeze')

    def makeAWindow(self):
        self.delete()
        self.myWindow = cmds.window(title="myFreezeAndDeleteWindow",
                                    widthHeight=(300, 100))
        self.colmLayout = cmds.columnLayout(parent=self.myWindow,
                                            adjustableColumn=True)
        cmds.text(label='Select objects you want to freeze and delete history', align='center')
        cmds.button(parent=self.colmLayout,
                    label='Delete History',
                    command=self.deleteHistory)
        cmds.button(parent=self.colmLayout,
                    label='Freeze Transformations',
                    command=self.freezeTransforms)
        cmds.button(parent=self.colmLayout,
                    label='Close',
                    command=('cmds.deleteUI(\"' + self.myWindow + '\", window=True)'))
        cmds.setParent('..')

        cmds.showWindow(self.myWindow)

    def delete(self):
        if cmds.window(self.myWindow, exists=True):
            cmds.deleteUI(self.myWindow)
