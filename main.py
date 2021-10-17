import ai


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conversation_object = ai.Conversation("davinci", 0.9)

    currentInput = ""
    while currentInput != "end":
        currentInput = input()
        print(conversation_object.continue_conversation(currentInput))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
