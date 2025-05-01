from random import randint
import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import requests
from io import BytesIO

def get_pokemon_image(pokemon_id):
    url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png"
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

def create_silhouette(image):
    # Converte para escala de cinza e depois para preto/branco (modo "1")
    grayscale = image.convert("L")
    inverted = ImageOps.invert(grayscale)
    silhouette = inverted.point(lambda x: 0 if x < 255 else 255, '1')  # tudo vira preto
    return silhouette.convert("RGBA")

def show_image(img):
    tk_img = ImageTk.PhotoImage(img)
    label.config(image=tk_img)
    label.image = tk_img  # mantém referência

def on_button_click():
    try:
        original = get_pokemon_image(randint(1, 1000))
        original = original.resize((300, 300))
        silhouette = create_silhouette(original)
        show_image(silhouette)
    except Exception as e:
        print(f"Erro: {e}")

# GUI
root = tk.Tk()
root.title("Quem é esse Pokémon?")

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Mostrar Silhueta", command=on_button_click)
btn.pack()

label = tk.Label(root)
label.pack()

root.mainloop()
