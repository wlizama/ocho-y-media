from ..dao.SQLServerConnection import SQLServerConnection

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
