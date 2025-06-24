import pyautogui
import time
import tkinter as tk
from tkinter import messagebox, scrolledtext

def start_sending():
    try:
        msg = message_entry.get()
        delay = float(delay_entry.get())
        count = int(count_entry.get())
        
        if not msg.strip():
            messagebox.showerror("Input Error", "Message cannot be empty.")
            return
        
        confirm = messagebox.askyesno("Confirm", 
            f"📩 Message: {msg}\n⏱️ Delay: {delay} sec\n🔁 Count: {count}\n\nProceed with sending?")
        
        if not confirm:
            return
        
        log_output.insert(tk.END, "\n🟡 You have 5 seconds to focus WhatsApp...\n")
        log_output.update()
        time.sleep(5)

        for i in range(1, count + 1):
            pyautogui.write(msg)
            pyautogui.press("enter")
            log_output.insert(tk.END, f"✅ Sent message {i}/{count}\n")
            log_output.see(tk.END)
            log_output.update()
            time.sleep(delay)

        log_output.insert(tk.END, f"\n🎉 Done! Total {count} messages sent.\n")
        log_output.see(tk.END)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for delay and count.")

root = tk.Tk()
root.title("📲 WhatsApp Message Spammer by Umair")
root.geometry("500x400")
root.resizable(False, False)

tk.Label(root, text="Enter Message:").pack(pady=(10, 0))
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

tk.Label(root, text="Delay Between Messages (sec):").pack()
delay_entry = tk.Entry(root, width=20)
delay_entry.pack(pady=5)

tk.Label(root, text="Total Number of Messages:").pack()
count_entry = tk.Entry(root, width=20)
count_entry.pack(pady=5)

tk.Button(root, text="🚀 Start Sending", bg="green", fg="white", command=start_sending).pack(pady=10)

tk.Label(root, text="📋 Log Output:").pack()
log_output = scrolledtext.ScrolledText(root, width=60, height=10)
log_output.pack(pady=5)

root.mainloop()
