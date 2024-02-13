from PIL import Image

def create_text_file():
    try:
        image_path = input("Enter the path to the image: ")
        image = Image.open(image_path)
        width, height = image.size
        with open('image.txt', 'w') as f:
            f.write(f"Width: {width}px, Height: {height}px\n")
            for y in range(height):
                for x in range(width):
                    r, g, b = image.getpixel((x, y))
                    f.write(f"{r},{g},{b}\n")
        print("Saved image.txt")
    except FileNotFoundError:
        print("The specified image path is invalid.")
    except Exception as e:
        print("An error occurred:", e)

def recreate_image():
    try:
        text_file_path = input("Enter the path to the text file: ")
        with open(text_file_path, 'r') as f:
            lines = f.readlines()
        width = int(lines[0].split(':')[1].split('px')[0].strip())
        height = int(lines[0].split(':')[2].split('px')[0].strip())
        image = Image.new("RGB", (width, height))
        for i, line in enumerate(lines[2:]):
            r, g, b = map(int, line.strip().split(','))
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

def main():
    choice = input("Choose an option:\n1. Create a new text file from an image\n2. Recreate an existing text file\nChoice: ")
    if choice == '1':
        create_text_file()
    elif choice == '2':
        recreate_image()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
