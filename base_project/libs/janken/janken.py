import logging
import random

logger = logging.getLogger(__name__)
j_logger = logging.getLogger("janken")


OPTIONS = ["グー", "チョキ", "パー"]


class JankenSimulator:
    def __init__(self):
        self.computer_choice = None
        self.human_choice = None

    @staticmethod
    def print_option():
        OPTIONS_WITH_INDEX = (
            f"({index}) {option}" for index, option in enumerate(OPTIONS, 1)
        )
        print("\n".join(OPTIONS_WITH_INDEX))

    def get_human_choice(self):
        human_choice_num = int(input("「グー」か「チョキ」か「パー」を番号で選んでください : "))
        self.human_choice = OPTIONS[human_choice_num - 1]

    def get_computer_choice(self):
        self.computer_choice = random.choice(OPTIONS)

    def print_choices(self):
        print(f"あなたが選んだのは「{self.human_choice}」です。")
        print(f"コンピュータが選んだのは「{self.computer_choice}」です。")

    def judge_result(self):
        if self.human_choice == self.computer_choice:
            return "draw"
        elif (
            (self.human_choice, self.computer_choice) == ("グー", "チョキ")
            or (self.human_choice, self.computer_choice) == ("チョキ", "パー")
            or (self.human_choice, self.computer_choice) == ("パー", "グー")
        ):
            return "win"
        else:
            return "loose"

    def print_result(self, result):
        if result == "win":
            print("おめでとうございます。あなたの勝ちです。")
        elif result == "loose":
            print("残念でした。コンピュータの勝ちです。")
        else:
            print("引き分けです")

    def simulate(self):
        logger.debug("Jankenを開始しました。")
        self.print_option()
        self.get_human_choice()
        self.get_computer_choice()
        self.print_choices()
        result = self.judge_result()
        self.print_result(result)
        j_logger.info(
            f"human_choice:{self.human_choice},"
            f"computer_choice:{self.computer_choice},"
            f"result:{result}"
        )
        logger.debug("Jankenを終了しました。")
