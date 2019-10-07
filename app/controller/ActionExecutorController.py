class ActionExecutorController:

    @staticmethod
    def getActionTypeList():
        print("retornar lista tipos de acciones")
        return [
            {
                'value': 'uid01',
                'name': 'Description 01',
                'action_script': 'python action_script.py'
            },
            {
                'value': 'uid02',
                'name': 'Description 02',
                'action_script': 'sh action_script.sh'
            },
            {
                'value': 'uid03',
                'name': 'Description 03',
                'action_script': 'java -jar action_script.java'
            },
        ]