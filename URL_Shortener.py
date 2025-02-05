import tkinter as tk
import hashlib
import webbrowser
url_mapping={}
def custom_shorten(long_url):
    if not long_url:
        return ""
    hash_object=hashlib.md5(long_url.encode())
    short_code=hash_object.hexdigest()[:6]
    short_url=f"http://short.ly/{short_code}"
    url_mapping[short_url] = long_url
    return short_url
def update_short_url(event=None):
    long_url= url_entry.get().strip()
    short_url=custom_shorten(long_url)
    result_var.set(short_url)
def open_short_url():
    short_url=result_var.get()
    if short_url in url_mapping:
        webbrowser.open(url_mapping[short_url])
root=tk.Tk()
root.title("URL Shortener")
root.geometry("400x200")
root.resizable(False, False)
tk.Label(root, text="Enter Long URL:").pack(pady=5)
url_entry=tk.Entry(root, width=50)
url_entry.pack(pady=5)
url_entry.bind("<KeyRelease>", update_short_url)
result_var=tk.StringVar()
result_label=tk.Label(root,textvariable=result_var,fg="blue",font=("Arial",12,"bold"),cursor="hand2")
result_label.pack(pady=5)
result_label.bind("<Button-1>",lambda e:open_short_url())
root.mainloop()