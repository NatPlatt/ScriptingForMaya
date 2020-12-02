import maya.cmds as cmds

class RenamerUI():
    def __init__(self):
        self.myWindow = "MyWindowTool"

    def renameIt(self, name_string):
        '''
        -function that sequentially renames a set of selected objects with given parameter
        -meant to follow the naming convention of Name_###_Name with as many # characters as needed
         -will rename the objects in the order they were selected
        '''
        char_list = list(name_string)

        sels = cmds.ls(sl=True)

        # returns the number of '#'
        hash_num = name_string.count('#')

        # returns ('Cube_', '###', '_Obj')
        parts = name_string.partition('#' * hash_num)

        # returns the first instances index 5
        piece = name_string.find("#")
        print 'piece starts as ', piece

        # returns last index location of # 7
        index_num = (piece + hash_num)

        # make list to hold extra # characters
        hash_list = []
        end_hash = index_num - 1

        # remove excess # characters and put in a list
        for i in range(piece, end_hash, 1):
            hash = char_list.pop(i)
            hash_list.extend(hash)

        # make new name with only one # character
        new_name_string = ''.join(char_list)

        replace_num_string = '1'

        replace_num_int = 1

        final_name_string = ''

        # check if # characters are sequential, if they are, then sequentially rename them
        if parts[1]:
            print 'Characters are sequential'
            for s in sels:
                new_num = replace_num_string.zfill(hash_num)
                final_name_string = new_name_string.replace('#', new_num)
                replace_num_int += 1
                cmds.rename(final_name_string)
                replace_num_string = str(replace_num_int)
        else:
            cmds.error('Characters are not sequential. Input another string.')


    def defaultButtonPush(self):
        print "Button was pushed"

    def makeAWindow(self):
        self.delete()
        self.myWindow = cmds.window(title="MyWindowTool",
                                    widthHeight=(300, 100))
        self.colmLayout = cmds.columnLayout(parent=self.myWindow, 
                                            adjustableColumn=True)
        self.name_field = cmds.textField(parent=self.colmLayout,
                                         placeholderText="Enter name format 'name###name' ")
        cmds.button(parent=self.colmLayout, 
                    label='Rename It!', 
                    command=self.getTheName)
        cmds.button(parent=self.colmLayout, 
                    label='Close', 
                    command=('cmds.deleteUI(\"' + self.myWindow + '\", window=True)') )
        cmds.setParent('..')
        
        cmds.showWindow(self.myWindow)
        
    def getTheName(self,name_string):
        name_field = self.makeAWindow
        name_string = cmds.textField(self.name_field, query=True, text=True)
        self.renameIt(name_string)

    def delete(self):
        if cmds.window(self.myWindow, exists=True ):
            cmds.deleteUI(self.myWindow)


myWindow = RenamerUI()
myWindow.makeAWindow()

