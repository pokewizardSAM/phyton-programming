import gemini
import tkinter as tk
import threading

# Create a Gemini API client
gemini_client = gemini.PrivateClient()

# Create the main application window
root = tk.Tk()
root.title("Gemini Pro Chat")

# Create the chat window
chat_window = tk.Text(root, height=20, width=80)
chat_window.pack()

# Create the input field
input_field = tk.Entry(root)
input_field.pack()

# Create the send button
send_button = tk.Button(root, text="Send", command=lambda: send_message())
send_button.pack()

# Define the send message function
def send_message():
    message = input_field.get()
    input_field.delete(0, tk.END)

    # Create a new thread to handle sending the message
    thread = threading.Thread(target=send_message_thread, args=(message,))
    thread.start()

# Define the send message thread function
def send_message_thread(message):
    try:
        # Send the message to Gemini
        response = gemini_client.send_message(message)

        # Update the chat window with the response
        chat_window.insert(tk.END, f"{response}\n")
    except Exception as e:
        # Handle any errors
        chat_window.insert(tk.END, f"Error: {e}\n")

# Create the receive message thread function
def receive_message_thread():
    while True:
        try:
            # Receive a message from Gemini
            message = gemini_client.receive_message()

            # Update the chat window with the message
            chat_window.insert(tk.END, f"{message}\n")
        except Exception as e:
            # Handle any errors
            chat_window.insert(tk.END, f"Error: {e}\n")

# Create a new thread to handle receiving messages
thread = threading.Thread(target=receive_message_thread)
thread.start()

# Define the main loop function
def main_loop():
    root.mainloop()

# Create a new thread to handle the main loop
thread = threading.Thread(target=main_loop)
thread.start()


# Start the application
if __name__ == "__main__":
    main_loop()