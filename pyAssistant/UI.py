import tkinter as tk
from PIL import Image, ImageTk
import pyAssistant, os


window = tk.Tk()
window.geometry('500x500')
window.configure(bg='white')
window.title('pyAssistant')

def read_setupLogs(file):
    log = []
    with open(file, 'r') as f:
        for i in f.readlines():
            log.append(i.replace('\n', ''))

    locations = {i.split('|')[0]: i.split('|')[1] for i in log}
    return locations


def setting_pane():

    top = tk.Toplevel(window)
    top.geometry('500x500')
    top.configure(bg='white')
    top.title('pyAssistant-Settings')
    tk.Label(top, bg='white', text='Applications', font=('arial', 12, 'bold')).grid(row=0, column=0, padx=10, pady=20)
    tk.Label(top, bg='white', text='Name of the app (application.exe)', font=('arial', 12, 'bold')).grid(row=0, column=1, padx=10, pady=20)
    
    tk.Label(top, bg='white', text='Chrome location', font=('arial', 10)).grid(row=1, column=0, padx=10, pady=20)
    googleL = tk.Entry(top, borderwidth=0, bg='#cccfcd', width=40, textvariable=tk.StringVar())
    
    
    tk.Label(top, bg='white', text='Edge location', font=('arial', 10)).grid(row=2, column=0, padx=10, pady=20)
    edgeL = tk.Entry(top, borderwidth=0, bg='#cccfcd', width=40, textvariable=tk.StringVar())
    
    
    tk.Label(top, bg='white', text='Excel location', font=('arial', 10)).grid(row=3, column=0, padx=10, pady=20)
    xlsxL = tk.Entry(top, borderwidth=0, bg='#cccfcd', width=40, textvariable=tk.StringVar())

    locations = read_setupLogs(path('setup_logs.txt')[0])

    def containt_save():
        file = open(path('setup_logs.txt')[0], 'r+')
        file.truncate()
        file.write('google chrome|%s\n'%googleL.get())
        file.write('microsoft edge|%s\n'%edgeL.get())
        file.write('excel|%s\n'%xlsxL.get())
        top.destroy()

    
    googleL.insert(0, locations['google chrome'])    
    edgeL.insert(0, locations['microsoft edge'])
    xlsxL.insert(0, locations['excel'])
    
    def default_save():
        file = open(path('setup_logs.txt')[0], 'r+')
        file.truncate()
        file.write('google chrome|C:/Program Files/Google/Chrome/Application/chrome.exe\n')
        file.write('microsoft edge|C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe\n')
        file.write('excel|C:/Program Files/Microsoft Office/root/Office16/EXCEL.exe\n')
        top.destroy()
        

    tk.Button(top, text='Default', font=('arial', 10, 'bold'), width=7, height=1, command=lambda: default_save(), borderwidth=0, bg='#f55f5f', fg='white').grid(row=0, column=2, pady=20)

    tk.Button(top, text='Save Settings', font=('arial', 10, 'bold'), width=11, height=2, command=lambda: containt_save(), borderwidth=0, bg='#f55f5f', fg='white').grid(row=4, column=0, pady=20)
    tk.Button(top, text='Cancel', font=('arial', 10, 'bold'), width=7, height=2, command=lambda: top.destroy(), borderwidth=0, bg='#f55f5f', fg='white').grid(row=4, column=1, pady=20)
    tk.Button(top, text='Quit', font=('arial', 10, 'bold'), width=6, height=2, command=lambda: window.destroy(), borderwidth=0, bg='#f55f5f', fg='white').grid(row=4, column=2, pady=20)

    googleL.grid(row=1, column=1, padx=20, pady=20)

    edgeL.grid(row=2, column=1, padx=20, pady=20)

    xlsxL.grid(row=3, column=1, padx=20, pady=20)


def path(file_name, dir_name='pyAssistant'):
    PATH = ''
    PATH_DIR = ''
    for root, dir, files in os.walk(f'{os.getcwd()[0]}:/'):
        for f in files:
            if f == file_name:
                PATH = os.path.join(root, f)
        for d in dir:
            if d == dir_name:
                PATH_DIR = os.path.join(root, d)
    return PATH.replace('\\', '/'), PATH_DIR.replace('\\', '/')


mic_image = Image.open(path(file_name='microphone.png')[0])
resizee = mic_image.resize((60, 60))

setting_image = Image.open(path(file_name='gear.png')[0])
resize_gear = setting_image.resize((40, 40))

mic_icon = ImageTk.PhotoImage(resizee)
setting_icon = ImageTk.PhotoImage(resize_gear)

tk.Button(window, image=setting_icon, borderwidth=0, bg='white', command=lambda: setting_pane()).place(x=10, y=10)
tk.Label(window, text='Say somthing to Aniket...',  font=('arial', 20, 'bold'), bg='white', fg='gray').pack(pady=20)
tk.Label(window, text='Click "microphone" and talk with Aniket!',  font=('arial', 10, 'bold'), bg='white').pack(pady=10)
tk.Button(window, image=mic_icon, fg='gray', command=lambda: pyAssistant.take_command(), bg='white', font=('ink free', 20, 'bold'), borderwidth=0).pack(pady=20)
tk.Label(window, text='Try this', font=('arial', 12, 'bold'), bg='white').pack(pady=10)
tk.Label(window, text='"Aniket, who is APJ abdul kalam.."', font=('ink free', 15, 'bold'), bg='white', fg='#f55f5f').pack(pady=10)
tk.Label(window, text='"Aniket, what is the time now.."', font=('ink free', 15, 'bold'), bg='white', fg='#f55f5f').pack(pady=10)
tk.Label(window, text='"Aniket, launch you tube.."', font=('ink free', 15, 'bold'), bg='white', fg='#f55f5f').pack(pady=10)


window.mainloop()