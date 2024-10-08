from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import tkinter

app = CTk()
app.geometry("1400x700")
app.resizable(1, 1)  # Permitir redimensionamento da janela

set_appearance_mode("light")

# Função para trocar o frame visível
def show_frame(frame):
    frame.tkraise()

# Função para carregar imagens
def load_image(path, size):
    img_data = Image.open(path)
    return CTkImage(dark_image=img_data, light_image=img_data, size=size)

# Função para criar botões na barra lateral
def create_sidebar_button(parent, img_path, text, command, pady=(16, 0)):
    img = load_image(img_path, (30, 30))  # Tamanho ajustado para os ícones
    return CTkButton(master=parent, image=img, text=text, fg_color="transparent", font=("Arial Bold", 14),
                     hover_color="#207244", anchor="w", command=command).pack(anchor="center", ipady=5, pady=pady)

# Função para criar a barra lateral
def create_sidebar():
    sidebar = CTkFrame(master=app, fg_color="#2A8C55", corner_radius=0)
    sidebar.pack_propagate(0)
    sidebar.pack(fill="y", side="left", anchor="w", expand=False)

    logo_img = load_image("logo.png", (77.68, 85.42))
    CTkLabel(master=sidebar, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

    create_sidebar_button(sidebar, "analytics_icon.png", "Dashboard", lambda: show_frame(dashboard_frame), pady=(60, 0))
    create_sidebar_button(sidebar, "package_icon.png", "Orders", lambda: show_frame(orders_frame))
    create_sidebar_button(sidebar, "returns_icon.png", "Returns", lambda: show_frame(returns_frame))
    create_sidebar_button(sidebar, "settings_icon.png", "Settings", lambda: show_frame(settings_frame))
    create_sidebar_button(sidebar, "person_icon.png", "Customer", lambda: show_frame(customer_frame))

# Função para criar as frames principais
def create_main_frames():
    global dashboard_frame, orders_frame, returns_frame, settings_frame, customer_frame, new_order_frame
    dashboard_frame = CTkFrame(master=main_view, fg_color="white")
    orders_frame = CTkFrame(master=main_view, fg_color="white")
    returns_frame = CTkFrame(master=main_view, fg_color="white")
    settings_frame = CTkFrame(master=main_view, fg_color="white")
    customer_frame = CTkFrame(master=main_view, fg_color="white")
    new_order_frame = CTkFrame(master=main_view, fg_color="white")  # Frame para criação de pedidos

    for frame in (dashboard_frame, orders_frame, returns_frame, settings_frame, customer_frame, new_order_frame):
        frame.place(x=0, y=0, relwidth=1, relheight=1)

    # Adicionar título para indicar qual tela está sendo exibida
    CTkLabel(master=dashboard_frame, text="Dashboard", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=orders_frame, text="Orders", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=returns_frame, text="Returns", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=settings_frame, text="Settings", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=customer_frame, text="Customer", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=new_order_frame, text="Create New Order", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)

# Função para criar a tabela de "Orders"
def create_orders_table():
    title_frame = CTkFrame(master=orders_frame, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))
    CTkLabel(master=title_frame, text="Orders", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", side="left")
    CTkButton(master=title_frame, text="+ New Order", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(new_order_frame)).pack(anchor="ne", side="right")  # Trocar para o frame "new_order_frame"

    table_data = [
        ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"],
        ['3833', 'Smartphone', 'Alice', '123 Main St', 'Confirmed', 10],
    ]

    table_frame = CTkScrollableFrame(master=orders_frame, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    table.pack(expand=True)

# Função para criar a página de novo pedido
def create_new_order_page():
    CTkLabel(master=new_order_frame, text="Create Order", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29,0), padx=27)

    CTkLabel(master=new_order_frame, text="Item Name", font=("Arial Bold", 17), text_color="#52A476").pack(anchor="nw", pady=(25,0), padx=27)
    CTkEntry(master=new_order_frame, fg_color="#F0F0F0", border_width=0).pack(fill="x", pady=(12,0), padx=27, ipady=10)

    grid = CTkFrame(master=new_order_frame, fg_color="transparent")
    grid.pack(fill="both", padx=27, pady=(31,0))

    CTkLabel(master=grid, text="Customer", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=0, column=0, sticky="w")
    CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=0, ipady=10)

    CTkLabel(master=grid, text="Address", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=0, column=1, sticky="w", padx=(25,0))
    CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=1, ipady=10, padx=(24,0))

    CTkLabel(master=grid, text="Status", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=2, column=0, sticky="w", pady=(38, 0))

    status_var = tkinter.IntVar(value=0)
    CTkRadioButton(master=grid, variable=status_var, value=0, text="Confirmed", font=("Arial Bold", 14), text_color="#52A476", fg_color="#52A476", border_color="#52A476", hover_color="#207244").grid(row=3, column=0, sticky="w", pady=(16,0))
    CTkRadioButton(master=grid, variable=status_var, value=1,text="Pending", font=("Arial Bold", 14), text_color="#52A476", fg_color="#52A476", border_color="#52A476", hover_color="#207244").grid(row=4, column=0, sticky="w", pady=(16,0))
    CTkRadioButton(master=grid, variable=status_var, value=2,text="Cancelled", font=("Arial Bold", 14), text_color="#52A476", fg_color="#52A476", border_color="#52A476", hover_color="#207244").grid(row=5, column=0, sticky="w", pady=(16,0))

    CTkLabel(master=grid, text="Quantity", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=6, column=0, sticky="w", pady=(42, 0))

    quantity_frame = CTkFrame(master=grid, fg_color="transparent")
    quantity_frame.grid(row=7, column=0, pady=(21,0), sticky="w")
    CTkButton(master=quantity_frame, text="-", width=25, fg_color="#2A8C55", hover_color="#207244", font=("Arial Black", 16)).pack(side="left", anchor="w")
    CTkLabel(master=quantity_frame, text="01", text_color="#2A8C55", font=("Arial Black", 16)).pack(side="left", anchor="w", padx=10)
    CTkButton(master=quantity_frame, text="+", width=25,  fg_color="#2A8C55",hover_color="#207244", font=("Arial Black", 16)).pack(side="left", anchor="w")

    CTkLabel(master=grid, text="Description", font=("Arial Bold", 17), text_color="#52A476", justify="left").grid(row=2, column=1, sticky="w", pady=(42, 0), padx=(25,0))
    CTkTextbox(master=grid, fg_color="#F0F0F0", width=300, corner_radius=8).grid(row=3, column=1, rowspan=5, sticky="w", pady=(16,0), padx=(25,0), ipady=10)

    actions = CTkFrame(master=new_order_frame, fg_color="transparent")
    actions.pack(fill="both")

    CTkButton(master=actions, text="Back", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#2A8C55", hover_color="#eee", border_width=2, text_color="#2A8C55", command=lambda: show_frame(orders_frame)).pack(side="left", anchor="sw", pady=(30,0), padx=(27,24))
    CTkButton(master=actions, text="Creaate", width=300, font=("Arial Bold", 17), hover_color="#207244", fg_color="#2A8C55", text_color="#fff", command=lambda: show_frame(orders_frame)).pack(side="left", anchor="se", pady=(30,0), padx=(0,27))

# Inicialização principal
main_view = CTkFrame(master=app, fg_color="#fff", corner_radius=0)
main_view.pack(fill="both", side="right", expand=True, padx=(27, 0), pady=(22, 22))

create_sidebar()
create_main_frames()
create_orders_table()
create_new_order_page()

# Exibir a tela inicial (Orders)
show_frame(orders_frame)

app.mainloop()