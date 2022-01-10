from base_project.settings import LOG_DIR

"""loggingの設定
    iniファイル：
        Filterの設定できない
        書き方がちょっと独特
    yamlファイル：
        辞書型に読み取れるなら何でもいいらしいのでそれだったら
        pyファイルでいいんじゃない
    py(辞書型)：
        jsonとかでもいいけど、pyファイルにしといて方が出力さきとかを
        ほかのpyファイルから動的に読み取れるからこっちのほうが良さそう。

    ****注意事項****
    [propagate]
    loggersで propagate を False にしておかないと親ロガーも継承する。
    例えば root で設定しているhandlerを個別ロガーで除外しても、
    個別側でも継承され適用され続ける。

    [disable_existing_loggers]
    Falseにしておかないと困ったという人が多いみたい。
    loggerConfigの読み込むタイミングによってうまく動かないときがあるもよう。
    僕のに関しては__init__でログ設定してしまうので問題ないが、明示的にFalseに
    設定しておく
"""

loggging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    "loggers": {
        "errorLog": {"level": "ERROR", "handlers": ["errorFile"], "propagate": False},
        "janken": {"level": "DEBUG", "handlers": ["janken"], "propagate": False},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": f"{LOG_DIR}/log.log",
            "mode": "w",
            "encoding": "utf-8",
        },
        "errorFile": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "error",
            "filename": f"{LOG_DIR}/error.log",
            "mode": "w",
            "encoding": "utf-8",
        },
        "janken": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "janken",
            "filename": f"{LOG_DIR}/janken.log",
            "mode": "a",
            "encoding": "utf-8",
        },
    },
    "formatters": {
        "error": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %I:%M:%S %p",
        },
        "simple": {
            "format": (
                "%(asctime)s - %(levelname)-8s - %(name)-12s - %(module)-10s - "
                "%(funcName)-10s - %(lineno)-3s - %(message)s"
            ),
            "datefmt": "%Y-%m-%d %I:%M:%S %p",
        },
        "janken": {
            "format": "%(asctime)s - %(message)s",
            "datefmt": "%Y-%m-%d %I:%M:%S %p",
        },
    },
}
