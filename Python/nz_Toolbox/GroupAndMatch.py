import maya.cmds as cmds

class GroupAndMatch():
    def __init__(self):
        self.myWindow = 'groupAndMatchWindow'

    def GroupMatchParent(self, group_name):
        polySel = cmds.ls(sl=True)
        cmds.group(absolute=True, empty=True, name=group_name, world=True)
        groupSel = cmds.ls(sl=True)
        cmds.select(polySel, add=True)
        cmds.MatchTransform(groupSel, polySel)
        cmds.select(groupSel, d=True)
        cmds.select(groupSel, add=True)
        cmds.Parent(polySel, groupSel)

    def makeAWindow(self):
        self.delete()
        self.myWindow = cmds.window(title="groupAndMatchWindow",
                                    widthHeight=(300, 100))
        self.colmLayout = cmds.columnLayout(parent=self.myWindow,
                                            adjustableColumn=True)
        self.name_field = cmds.textField(parent=self.colmLayout,
                                         placeholderText="Enter the group name")
        cmds.text(label='Select the object you want to group and match transforms', align='center')
        cmds.button(parent=self.colmLayout,
                    label='Make Group and Match Transforms',
                    command=self.getTheName)
        cmds.button(parent=self.colmLayout,
                    label='Close',
                    command=('cmds.deleteUI(\"' + self.myWindow + '\", window=True)'))
        cmds.setParent('..')

        cmds.showWindow(self.myWindow)

    def getTheName(self, group_name):
        name_field = self.makeAWindow
        group_name = cmds.textField(self.name_field, query=True, text=True)
        self.GroupMatchParent(group_name)

    def delete(self):
        if cmds.window(self.myWindow, exists=True):
            cmds.deleteUI(self.myWindow)
