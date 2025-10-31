import tkinter as tk
from tkinter import messagebox
import symmetrical as sym
import asymmetrical as asym
import hash as h
import os
from tkinter import PhotoImage

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Cryptography Project")
        self.master.geometry("600x500+500+150")
        self.path_bg_image=os.path.abspath('encreption.png')
        self.create_welcome_page()

    def create_welcome_page(self):
        self.clear_window()
        self.bg_image = PhotoImage(file=self.path_bg_image)
        self.bg_label = tk.Label(self.master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)  
        label = tk.Label(self.master, text="Welcome to Cryptography Project",bg="gray", font=("Arial", 16))
        label.pack(pady=20)

        symmetric_button = tk.Button(self.master, text="Symmetric Encryption",bg="gray", width=60, command=self.symmetric_encryption)
        symmetric_button.pack(pady=5)

        asymmetric_button = tk.Button(self.master, text="Asymmetric Encryption",bg="gray", width=60, command=self.asymmetric_encryption)
        asymmetric_button.pack(pady=5)

        hashing_button = tk.Button(self.master, text="Hashing",bg="gray", width=60, command=self.hashing)
        hashing_button.pack(pady=5)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def symmetric_encryption(self):
        self.clear_window()
        self.bg_image = PhotoImage(file=self.path_bg_image)
        self.bg_label = tk.Label(self.master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)  
        
        label = tk.Label(self.master, text="Symmetric Encryption",bg="gray", font=("Arial", 16))
        label.pack(pady=20)
        
        aes_button = tk.Button(self.master, text="AES",bg="gray", width=60, command=lambda: self.show_form("AES", "Symmetric"))
        aes_button.pack(pady=5)

        des_button = tk.Button(self.master, text="DES",bg="gray", width=60, command=lambda: self.show_form("DES", "Symmetric"))
        des_button.pack(pady=5)

        triple_des_button = tk.Button(self.master, text="3DES",bg="gray", width=60, command=lambda: self.show_form("3DES", "Symmetric"))
        triple_des_button.pack(pady=5)
        
        back_button = tk.Button(self.master, text="Back", command=self.create_welcome_page)
        back_button.pack(pady=10)

    def asymmetric_encryption(self):
        self.clear_window()
        self.bg_image = PhotoImage(file=self.path_bg_image)
        self.bg_label = tk.Label(self.master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)      
        
        label = tk.Label(self.master, text="Asymmetric Encryption",bg="gray", font=("Arial", 16))
        label.pack(pady=20)
        
        rsa_button = tk.Button(self.master, text="RSA",bg="gray", width=60, command=lambda: self.show_form("RSA", "Asymmetric"))
        rsa_button.pack(pady=5)

        ecc_button = tk.Button(self.master, text="ECC",bg="gray", width=60, command=lambda: self.show_form("ECC", "Asymmetric"))
        ecc_button.pack(pady=5)

        back_button = tk.Button(self.master, text="Back",bg="gray", command=self.create_welcome_page)
        back_button.pack(pady=10)
        
    def hashing(self):
        self.clear_window()
        self.bg_image = PhotoImage(file=self.path_bg_image)
        self.bg_label = tk.Label(self.master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)  
                
        label = tk.Label(self.master, text="Hashing",bg="gray", font=("Arial", 16))
        label.pack(pady=20)
        
        sha256_button = tk.Button(self.master, text="SHA-256",bg="gray", width=60, command=lambda: self.show_form("SHA-256", "Hash"))
        sha256_button.pack(pady=5)

        sha3_256_button = tk.Button(self.master, text="SHA3-256",bg="gray", width=60, command=lambda: self.show_form("SHA3-256", "Hash"))
        sha3_256_button.pack(pady=5)

        md5_button = tk.Button(self.master, text="MD5",bg="gray", width=60, command=lambda: self.show_form("MD5", "Hash"))
        md5_button.pack(pady=5)

        back_button = tk.Button(self.master, text="Back", command=self.create_welcome_page)
        back_button.pack(pady=10)
        
    def show_form(self, algorithm, category):
        self.clear_window()
        self.bg_image = PhotoImage(file=self.path_bg_image)
        self.bg_label = tk.Label(self.master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)  
                
        label = tk.Label(self.master, text=f"Enter your text ({algorithm})", font=("Arial", 16), bg="gray")
        label.pack(pady=20)
        
        text_entry = tk.Entry(self.master, width=60)
        text_entry.pack(pady=10)
        
        submit_button = tk.Button(self.master, text="Submit", command=lambda: self.process_encryption_or_hash(text_entry.get(), algorithm, category))
        submit_button.pack(pady=10)
        
        back_button = tk.Button(self.master, text="Back", command=self.create_welcome_page)
        back_button.pack(pady=10)

    def process_encryption_or_hash(self, text, algorithm, category):
        if not text:
            messagebox.showerror("Input Error", "Please enter some text!")
            return

        result = None
        
        try:
            if category == "Symmetric":
                sym_algo = sym.SymmetricAlgorithms()
                result = sym_algo.encrypt(text, algorithm)  
                result = f"Key: {sym_algo.key.hex()}\nIV: {sym_algo.iv.hex()}\nCiphertext: {result.hex()}"
            elif category == "Asymmetric":
                asym_algo = asym.AsymmetricAlgorithms()
                if algorithm == "RSA":
                    asym_algo.generate_rsa_keys()
                    result = asym_algo.rsa_encrypt(text)
                    result = f"Public key:\n{asym_algo.public_key.hex()}\n\nCiphertext: {result.hex()}"
                elif algorithm == "ECC":
                    asym_algo.generate_ecc_keys()
                    result = asym_algo.ecc_encrypt(text)
                    result = f"Public key:\n{asym_algo.public_key_pem.hex()}\n\nCiphertext: {result.hex()}"
            elif category == "Hash":
                hash_algo = h.Hashing()
                if algorithm == "SHA-256":
                    result = hash_algo.sha256(text)
                elif algorithm == "SHA3-256":
                    result = hash_algo.sha3_256(text)
                elif algorithm == "MD5":
                    result = hash_algo.md5(text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return
        self.show_result(result=result, algorithm=algorithm)

    def show_result(self, result, algorithm):
        new_window = tk.Toplevel(self.master)
        new_window.title("Cryptography Project - Result")
        new_window.geometry("800x700+400+50")   
        label = tk.Label(new_window, text=f"Result ({algorithm}):", font=("Arial", 16))
        label.pack(pady=20)
        
        result_text = tk.Text(new_window, wrap="word", height=30, width=100,
                              font=("Arial", 12), state="normal")
        result_text.insert("1.0", result)
        result_text.config(state="disabled")
        result_text.pack(pady=10) 
        
        back_button = tk.Button(new_window, text="Back", command=new_window.destroy)
        back_button.pack(pady=10)

root = tk.Tk()
gui = GUI(root)
root.mainloop()