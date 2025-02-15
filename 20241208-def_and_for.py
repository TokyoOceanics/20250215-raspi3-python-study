def repeat_msg(msg, repeat=3):
    for i in range(repeat):
        print(msg)

repeat_msg("test")
repeat_msg("testtest", repeat=5)