import maya.cmds as cmds

class RenamerUI:
    def _init_(self, name, makeAWindow, renameIt):
        self.name = name
        self.makeAWindow()
        self.renameIt()

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

    #renameIt('Sphere_###_Obj')

    def defaultButtonPush(self):
        print "Button was pushed"

    def makeAWindow(self, myWindow):
        window = cmds.window(title="Duplicate Amount", iconName='Short Name', widthHeight=(300, 100))
        cmds.columnLayout(adjustableColumn=True)
        intFieldGrp = cmds.intField("Enter the number of duplicates you want.", minValue=0, maxValue=100)
        cmds.button(label='Duplicate!', command=self.getTheNums())
        cmds.button(label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)'))
        cmds.setParent('..')
        cmds.showWindow(window)

    def getTheNums(self, num):
        intFieldGrp = self.makeAWindow()
        nums = cmds.intField(intFieldGrp, query=True, value=True)
        if nums > 0:
            self.renameIt(nums)


