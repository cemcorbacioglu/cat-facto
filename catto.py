import requests
import tkinter as tk
from PIL import Image, ImageTk
import io

root = tk.Tk()
root.title("MeowFacts & CATAAS")

fact_label = tk.Label(root, text="Click the button to get a cat fact and image!")
fact_label.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

def get_cat_fact():
    url = "https://meowfacts.herokuapp.com/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            fact = response.json()['data'][0]
            return fact
        else:
            return f"Request failed with status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed with an error: {e}"

def get_cat_image():
    url = "https://cataas.com/cat"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            img_data = response.content
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((300, 300))
            img = ImageTk.PhotoImage(img)
            return img
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

def update_fact_and_image():
    fact = get_cat_fact()
    if fact:
        fact_label.config(text=fact)
    else:
        fact_label.config(text="Failed to fetch cat fact")

    img = get_cat_image()
    if img:
        image_label.config(image=img)
        image_label.image = img
    else:
        image_label.config(text="Failed to fetch cat image")

button = tk.Button(root, text="Get Cat Fact and Image", command=update_fact_and_image)
button.pack(pady=10)

root.mainloop()
