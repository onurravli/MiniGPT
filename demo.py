from main import MiniGPT

__all__ = ["MiniGPT"]


def main():
    mgpt = MiniGPT(
        key="sk-################################################"
    )
    resp = mgpt.chat(
        "gpt-3.5-turbo",
        "assistant",
        "Hello, how can you help me?",
        temp=1
    )
    print(resp)


if __name__ == "__main__":
    main()
