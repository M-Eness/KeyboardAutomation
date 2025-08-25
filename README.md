# Keyboard Automation Script

A simple Python automation script that automatically types a specified text into the active window and sends it by pressing `Enter`. It is designed to save time in repetitive tasks, especially in messaging applications like WhatsApp Web/Desktop or for filling out forms.

## 🎯 Key Features

  - **Cross-Platform:** Works seamlessly on both macOS and Windows.
  - **Full Unicode Support:** Thanks to the `pyperclip` library, it correctly handles special characters and emojis.
  - **Platform-Aware Shortcuts:** Automatically uses `Command+V` for pasting on macOS and `Ctrl+V` on Windows.
  - **Auto-Send:** Automatically presses `Enter` after pasting the message.
  - **Loopable:** Can be easily placed inside a `while` loop for continuous, repeated messaging.

## ⚙️ How It Works

The script follows a simple logic:

1.  It copies the specified text to the system clipboard.
2.  Using the `pyautogui` library, it simulates the paste command (`Cmd+V` or `Ctrl+V`) in the currently active window.
3.  Finally, it simulates an `Enter` key press to complete the action.

## 📋 Prerequisites

  - Python 3.7 or higher
  - Required Python libraries:
      - `pyperclip`
      - `pynput`

## 🚀 Installation & Usage

1.  **Clone the Repository (Optional):**

    ```bash
    git clone https://github.com/your-username/keyboard-automation.git
    cd keyboard-automation
    ```

2.  **Install the Required Libraries:**

    ```bash
    pip install pyperclip pynput
    ```

3.  **Prepare to Run the Script:**

      - Set your desired message in the script file.
      - Open the target application window and, most importantly, **click on the text input field to ensure the cursor is active.**

4.  **Run the Script:**
    It's good practice to include a countdown timer to give yourself a moment to focus on the correct window before the script starts typing.

    ```bash
    python keyboard_automation.py
    ```

    Once executed, your message will be typed into the focused window.

### 🔁 Continuous Messaging (Loop)

You can run the script in a loop to send messages continuously. Adding a short delay (`time.sleep`) between iterations is crucial to prevent system freezes or application rate-limiting.

-----

## ⚠️ Important Warnings

>   - **USE WITH CAUTION:** When running the script in an infinite loop, you **must** stop it by pressing `Ctrl+C` in the terminal. Otherwise, it will continue sending messages indefinitely.
>   - **ACTIVE WINDOW FOCUS:** The script sends keystrokes only to the **currently active and focused window**. If you accidentally click on another window (like your code editor or a browser tab), the message will be sent there.
>   - **TEST IN A SAFE ENVIRONMENT:** Before using this script in live chats or important applications, always test it in a safe place like a text editor (e.g., Notepad, TextEdit).
>   - **MACOS PERMISSIONS:** macOS users may need to grant accessibility permissions to their terminal or code editor. For example, if you execute the script from the command line, you must grant permissions to Terminal. If you run it from within an IDE, you'll need to grant permissions to that specific application (e.g., Visual Studio Code, PyCharm). This can be configured in System Settings > Privacy & Security > Accessibility.

