#I use this file as a module to store
#functions I consistently use across
#AoC challenge


"""
param:      filename    -> The path to the relevant file
return:     lines       ->
Description:            -> Reads a specified file and returns
                        the lines in the file
"""
def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines