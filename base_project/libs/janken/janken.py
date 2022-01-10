import logging
import random

logger = logging.getLogger(__name__)
j_logger = logging.getLogger("janken")


OPTIONS = ["グー", "チョキ", "パー"]


def print_option():
    OPTIONS_WITH_INDEX = [
        f"({index}) {option}" for index, option in enumerate(OPTIONS, 1)
    ]
    print("\n".join(OPTIONS_WITH_INDEX))


def get_human_choice():
    # リストのインデックスと合わせるために -1
    human_choice_num = int(input("「グー」か「チョキ」か「パー」を番号で選んでください : "))
    human_choice = OPTIONS[human_choice_num - 1]
    return human_choice


def get_computer_choice():
    computer_choice = random.choice(OPTIONS)
    return computer_choice


def print_choices(human_choice, computer_choice):
    print(f"あなたが選んだのは「{human_choice}」です。")
    print(f"コンピュータが選んだのは「{computer_choice}」です。")


def judge_result(human_choice, computer_choice):
    if human_choice == computer_choice:
        return "draw"
    elif (
        (human_choice, computer_choice) == ("グー", "チョキ")
        or (human_choice, computer_choice) == ("チョキ", "パー")
        or (human_choice, computer_choice) == ("パー", "グー")
    ):
        return "win"
    else:
        return "loose"


def print_result(result):
    if result == "win":
        print("おめでとうございます。あなたの勝ちです。")
    elif result == "loose":
        print("残念でした。コンピュータの勝ちです。")
    else:
        print("引き分けです")


def main():
    logger.debug("Jankenを開始しました。")
    print_option()
    human_choice = get_human_choice()
    computer_choice = get_computer_choice()
    print_choices(human_choice, computer_choice)
    result = judge_result(human_choice, computer_choice)
    print_result(result)
    j_logger.info(
        f"human_choice:{human_choice},"
        f"computer_choice:{computer_choice},"
        f"result:{result}"
    )
    logger.debug("Jankenを終了しました。")
