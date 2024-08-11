#Run this scipt first in the maya script editor, it will build the shelf with needed buttons

import maya.cmds as cmds

def create_rigging_toolbox_shelf():
    shelf_name = "Rigging_Toolbox"
    
    # Delete existing shelf with the same name if it exists
    if cmds.shelfLayout(shelf_name, exists=True):
        cmds.deleteUI(shelf_name, layout=True)

    # Create the new shelf
    shelf = cmds.shelfLayout(shelf_name, parent="ShelfLayout")

    # Add a buttons to the shelf
    cmds.shelfButton(
        label="Tools",
        command='''print("Tools button pressed")''',
        image="commandButton.png",  # This uses the default Maya icon, change if you have a custom one
        parent=shelf
    )

# Call the function to create the shelf
create_rigging_toolbox_shelf()
