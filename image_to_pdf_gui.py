import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def convert_image_to_pdf():
    # בחר קובץ תמונה
    img_path = filedialog.askopenfilename(
        title="בחר תמונה",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )

    if not img_path:
        return

    try:
        # פתח תמונה
        image = Image.open(img_path).convert("RGB")

        # בחר מיקום לשמירה
        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="בחר מיקום לשמירת PDF"
        )

        if not save_path:
            return

        # שמור כ־PDF
        image.save(save_path)
        messagebox.showinfo("המרה הצליחה", f"הקובץ נשמר:\n{save_path}")

    except Exception as e:
        messagebox.showerror("שגיאה", f"לא הצלחנו להמיר את הקובץ:\n{e}")

# יצירת GUI בסיסי
root = tk.Tk()
root.title("ממיר תמונה ל־PDF")
root.geometry("300x150")

label = tk.Label(root, text="ברוך הבא!\nלחץ על הכפתור כדי להמיר תמונה ל־PDF", justify="center")
label.pack(pady=20)

convert_button = tk.Button(root, text="בחר תמונה והמר", command=convert_image_to_pdf)
convert_button.pack()

root.mainloop()