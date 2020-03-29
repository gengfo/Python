class Tool_2(object):

    count = 0

    @classmethod
    def show_tool_count(cls):
        print("tool count is %d" % cls.count)


    def __init__(self, name):
        self.name = name
        Tool_2.count +=1



tool1 = Tool_2("tool1")
tool2 = Tool_2("tool2")

Tool_2.show_tool_count()






