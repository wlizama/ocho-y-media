class ActionModel:

    def __init__(self, uid, name, description, action_path):
        self.__uid = uid
        self.__name = name
        self.__description = description
        self.__action_path = action_path

    def __str__(self):
        return f"""\
        uid={self.__uid},
        name={self.__name},
        description={self.__description},
        action_path={self.__action_path}\
        """
