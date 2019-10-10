import os
from ..controller.ActionController import ActionController

class OchoYMediaController:

    @staticmethod
    def exec_actions():
        objActionContr = ActionController()
        actions = objActionContr.get_actions_list_model()

        for action in actions:
            print(f"Ejecutando acción: {action.name}")
            os.system(action.action_path)
            print(f"Fin acción: {action.name}")