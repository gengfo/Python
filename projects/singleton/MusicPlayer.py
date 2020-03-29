# coding=utf-8
class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        else:
            print("init ...")
            MusicPlayer.init_flag = True


if __name__ == "__main__":
    player1 = MusicPlayer()
    print(player1)
    player2 = MusicPlayer()
    print(player2)
