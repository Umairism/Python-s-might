import pyautogui
import time

def get_user_input():
    message = input("📝 Enter the message to send: ")
    
    while True:
        try:
            delay = float(input("⏱️ Enter delay between messages (in seconds): "))
            break
        except ValueError:
            print("❌ Please enter a valid number for delay.")

    while True:
        try:
            count = int(input("🔁 Enter number of messages to send: "))
            break
        except ValueError:
            print("❌ Please enter a valid integer for count.")
    
    return message, delay, count

def confirm_and_send(message, delay, count):
    print("\n🔒 Summary:")
    print(f"📩 Message: {message}")
    print(f"⏱️ Delay: {delay} seconds")
    print(f"🔁 Count: {count}")
    
    confirm = input("\n🚀 Proceed with sending? (yes/no): ").strip().lower()

    if confirm == 'yes':
        print("\nYou have 5 seconds to focus the WhatsApp chat...")
        time.sleep(5)

        for i in range(1, count + 1):
            pyautogui.write(message)
            pyautogui.press("enter")
            print(f"✅ Sent message {i}/{count}")
            time.sleep(delay)

        print(f"\n🎉 Done! Total {count} messages sent.")
    else:
        print("\n❌ Cancelled. No messages were sent.")

# MAIN
message, delay, count = get_user_input()
confirm_and_send(message, delay, count)
