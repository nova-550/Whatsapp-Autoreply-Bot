import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key=""
)

def is_last_message_from_sender(chat_log, sender_name = "Shivraj Patil"):
    # Split the chat log intoindividual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True
    return False

# Step 1 : Click on the icon at coordinates(1639, 1412)
pyautogui.click(1639, 1412)
time.sleep(2) # Wait for 1 second to ensure the click is registered

while True:
    # Step 2 : Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(1388, 153)
    pyautogui.dragTo(1893, 856, duration=1.0, button='left') # Drag for 1 second

    # Step 3 : Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2) # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1994, 281)

    # Step 4 : Retrieve the text from the clipboard and stored it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create
        (
            model = "gpt-3.5-turbo",
            messages =
            [
                ("role": "system", "content": "You are a person named shiv who is an engineering student. He is from India. You analyze chat history and respond like Shiv"),
                ("role": "user", "content": text)
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5 : Click at coordinates(1808, 1328)
        pyautogui.click(1808,1328)
        time.sleep(2) # Wait for 1 second to ensure the click is registered

        # Step 6 : Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2) # Wait for 1 second to ensure the paste command is completed

        # Step 7 : Press Enter
        pyautogui.press('enter')
