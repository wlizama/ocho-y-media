class ActionExecutorModel:

    def __init__(self, uid, description, action_script):
        self.__uid = uid
        self.__description = description
        self.__action_script = action_script

    def __str__(self):
        return f"""\
        uuid={self.__uid},
        description={self.__description},
        action_script={self.__action_script}\
        """
