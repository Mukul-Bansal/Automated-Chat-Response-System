import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
   api_key="________________"
 )
def is_last_message_from(chat_log,sender_name="________________"):
  messages=chat_log.strip().split("________________")[-1]
  if sender_name in messages:
    return True
  return False
    




pyautogui.click(1078,1048)


time.sleep(1)  # Wait for 1 second to make sure the click is registered
while True :
  # Drag to select text
  pyautogui.moveTo(516, 198)
  pyautogui.dragTo(746, 927, duration=1,button='left')  # Drag with a duration of 1 second

  # Copy the selected text to the clipboard
  pyautogui.hotkey('ctrl', 'c')
  time.sleep(1)
    # Wait for the clipboard to update
  pyautogui.click(616,356)

  # Get the text from the clipboard
  chathistory = pyperclip.paste()

  # Print the selected text (or use it as needed)
  print(f"Selected text: {chathistory}")
  print(is_last_message_from(chathistory))
  if is_last_message_from(chathistory):



    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a person named  Mukul, who knows hindi and english.you are from India .You analyse chat history and respond like Mukul.Output should be the next chat response(text message only)"},
        {"role": "user", "content": chathistory}
    ]
    )

    response=completion.choices[0].message.content
    pyperclip.copy(response)



  # Click on the specified coordinates
    pyautogui.click(671,970)
    time.sleep(0.5)  # Short wait to ensure the click is registered

  # Paste the text from the clipboard
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)  # Short wait to ensure the paste action is completed

  # Press Enter
    pyautogui.press('enter')