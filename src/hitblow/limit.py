def get_max_tries():
    while True:
        try:
            max_tries = int(input("挑戦回数を入力してください（1以上）："))

            if max_tries >= 1:
                return max_tries
            else:
                print("1以上の数字を入力してください。")

        except ValueError:
            print("数字を入力してください。")