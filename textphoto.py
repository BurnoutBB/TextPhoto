from tkinter import Tk, Label, Button, filedialog
from PIL import Image

def create_text_file(image_path):
    try:
        image = Image.open(image_path)
        width, height = image.size
        with open('image.txt', 'w') as f:
            f.write(f"Width: {width}px, Height: {height}px\n")
            for y in range(height):
                for x in range(width):
                    r, g, b = image.getpixel((x, y))
                    hex_value = f"{r//16:01X}{g//16:01X}{b//16:01X}"
                    f.write(f"{hex_value}\n")
        print("Saved image.txt")
    except FileNotFoundError:
        print("The specified image path is invalid.")
    except Exception as e:
        print("An error occurred:", e)

def recreate_image(text_file_path):
    try:
        with open(text_file_path, 'r') as f:
            lines = f.readlines()
        width = int(lines[0].split(':')[1].split('px')[0].strip())
        height = int(lines[0].split(':')[2].split('px')[0].strip())
        image = Image.new("RGB", (width, height))
        for i, line in enumerate(lines[1:]):
            hex_value = line.strip()
            r = int(hex_value[0], 16) * 16
            g = int(hex_value[1], 16) * 16
            b = int(hex_value[2], 16) * 16
            x = i % width
            y = i // width
            if x < width and y < height:
                image.putpixel((x, y), (r, g, b))
        image.save('recreated_image.jpg')
        print("Image recreated.")
    except FileNotFoundError:
        print("The specified text file path is invalid.")
    except Exception as e:
        print("An error occurred:", e)

def choose_image():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("all files", "*.*")))
    return filename

def choose_text_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Text File", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    return filename

def main():
    root = Tk()
    root.title("Image Text Converter")

    # Configure dark theme
    root.configure(bg='#333333')
    root.geometry('300x200')  # Larger window size

    def create_text():
        image_path = choose_image()
        if image_path:
            create_text_file(image_path)

    def recreate_image_gui():
        text_file_path = choose_text_file()
        if text_file_path:
            recreate_image(text_file_path)

    button_create = Button(root, text="Create Text File from Image", command=create_text, bg='#555555', fg='white')
    button_create.pack()

    button_recreate = Button(root, text="Recreate Image from Text File", command=recreate_image_gui, bg='#555555', fg='white')
    button_recreate.pack()

    button_exit = Button(root, text="Exit", command=root.quit, bg='#555555', fg='white')
    button_exit.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
