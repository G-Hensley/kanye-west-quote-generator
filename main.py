from tkinter import *
import requests

# API call to get a random Kanye quote
def get_quote():

    global quote_text

    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    # Delete the existing quote text
    canvas.delete(quote_text)
    # Create a new quote text
    quote_text = canvas.create_text(150, 207, text=response.json()["quote"], width=250, font=("Arial", 18, "bold"), fill="black")

# Create the window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create the canvas
canvas = Canvas(width=300, height=414)
# Add the background image to the canvas
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
# Create the quote text
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="black")
canvas.grid(row=0, column=0)
    
# Create the Kanye button
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, relief="flat")
kanye_button.grid(row=1, column=0)

# Start the main loop
window.mainloop()