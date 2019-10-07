class ActionModel:

    def __init__(self, uid, name, description, action_executor):
        self.__uid = uid
        self.__name = name
        self.__description = description
        self.__action_executor = action_executor

    def __str__(self):
        return f"""\
        uuid={self.__uid},
        name={self.__name},
        description={self.__description},
        action_executor={self.__action_executor}\
        """
