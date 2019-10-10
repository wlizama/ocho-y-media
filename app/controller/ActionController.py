from ..dao.SQLServerConnection import SQLServerConnection
from ..model.ActionModel import ActionModel

class ActionController:

    def __init__(self):
        self.__sql_con = SQLServerConnection()


    def add_action(self, action_vals):
        uid = self.__sql_con.execute_insert(
            "action",
            ("name", "description", "action_path"),
            (action_vals["name"], action_vals["description"], action_vals["action_path"])
        )
        return uid


    def get_actions_list(self):
        list = self.__sql_con.execute_list("action")
        return list


    def get_actions_list_model(self):
        action_list = self.get_actions_list()

        action_list_model = []
        for action in action_list:
            objActionM = ActionModel(action[0], action[1], action[2], action[3])
            action_list_model.append(objActionM)

        return action_list_model