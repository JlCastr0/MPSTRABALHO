from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import tkinter


table_data = [
    ["Código", "Nome", "Categoria", "Custo de Compra", "Preço sugerido", "Quantidade", "Estoque Mínimo", "Estoque Máximo"]
]

#teste
app = CTk()
app.geometry("1400x700")
app.resizable(1, 1)  # Permitir redimensionamento da janela

set_appearance_mode("light")
app.title("Sistema de Estoque")

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

    create_sidebar_button(sidebar, "analytics_icon.png", "Relatórios", lambda: show_frame(dashboard_frame), pady=(60, 0))
    create_sidebar_button(sidebar, "package_icon2.png", "Produtos", lambda: show_frame(orders_frame))
    create_sidebar_button(sidebar, "exit_icon.png", "Saída", lambda: show_frame(exit_frame))
    create_sidebar_button(sidebar, "enter_icon.png", "Entrada", lambda: show_frame(enter_frame))
    create_sidebar_button(sidebar, "person_icon.png", "Clientes", lambda: show_frame(customer_frame))
    create_sidebar_button(sidebar, "seller_icon.png", "Vendedores", lambda: show_frame(seller_frame))
    create_sidebar_button(sidebar, "factory_icon.png", "Fornecedores", lambda: show_frame(factory_frame))
    create_sidebar_button(sidebar, "categories_icon.png", "Categorias", lambda: show_frame(category_frame))



# Função para criar as frames principais
def create_main_frames():
    global dashboard_frame, orders_frame, exit_frame, settings_frame, customer_frame, new_order_frame,seller_frame, factory_frame, enter_frame
    global create_product_frame, search_product_frame, delete_product_frame, edit_product_frame, category_frame,forgot_password_frame, error_frame


    dashboard_frame = CTkFrame(master=main_view, fg_color="white")
    orders_frame = CTkFrame(master=main_view, fg_color="white")
    exit_frame = CTkFrame(master=main_view, fg_color="white")
    enter_frame = CTkFrame(master=main_view, fg_color="white")
    settings_frame = CTkFrame(master=main_view, fg_color="white")
    seller_frame = CTkFrame(master=main_view, fg_color="white")
    factory_frame = CTkFrame(master=main_view, fg_color="white")
    customer_frame = CTkFrame(master=main_view, fg_color="white")
    new_order_frame = CTkFrame(master=main_view, fg_color="white") 
    category_frame = CTkFrame(master=main_view, fg_color="white") 
    forgot_password_frame = CTkFrame(master=main_view, fg_color="white") 
    error_frame = CTkFrame(master=main_view, fg_color="white") 

    
    #Botoes dos Produtos 
    create_product_frame = CTkFrame(master=main_view, fg_color="white")
    search_product_frame = CTkFrame(master=main_view, fg_color="white")
    delete_product_frame = CTkFrame(master=main_view, fg_color="white")
    edit_product_frame = CTkFrame(master=main_view, fg_color="white")


    for frame in (dashboard_frame, orders_frame, exit_frame, settings_frame, customer_frame, 
                  new_order_frame, seller_frame, factory_frame, enter_frame, create_product_frame, search_product_frame, 
                  delete_product_frame, edit_product_frame,category_frame, forgot_password_frame, error_frame):
        frame.place(x=0, y=0, relwidth=1, relheight=1)

    # Adicionar título para indicar qual tela está sendo exibida
    CTkLabel(master=dashboard_frame, text="Relatórios", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=orders_frame, text="Produtos", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=exit_frame, text="Saída", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=settings_frame, text="Categorias", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=seller_frame, text="Vendedores", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=factory_frame, text="Fornecedores", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=customer_frame, text="Clientes", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=enter_frame, text="Entrada", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=new_order_frame, text="Create New Order", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)
    CTkLabel(master=category_frame, text="Categorias", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="center", pady=50)

# Função para criar a tabela de "Orders"
def create_orders_table():
    
    global table
    table_frame = CTkScrollableFrame(master=orders_frame, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)

    # Criar tabela com os dados iniciais
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    table.pack(expand=True)

    # Salvar o frame e a tabela para reconstrução
    table_frame.table = table
    table_frame.pack_frame = table_frame

    # Frame para os botões (agora embaixo da tabela)
    button_frame = CTkFrame(master=orders_frame, fg_color="transparent")
    button_frame.pack(anchor="center", side="bottom", pady=(5, 21))

    # Criando os quatro botões
    CTkButton(master=button_frame, text="Cadastrar Produto", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(create_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Editar Produto", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(edit_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Deletar Produto", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(delete_product_frame)).pack(side="left", padx=5)
    
    CTkButton(master=button_frame, text="Buscar Produto", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(search_product_frame)).pack(side="left", padx=5)

def create_enter_table():
    
    table_data = [
    ["Nome do Produto", "Quantidade", "Data de Entrada", "Vendedor"],
    ['Monitor', 10, '23/12/2023', "Carlos Eduardo"],
    ['Teclado', 20, '25/12/2023', "Ana Beatriz"],
    ['Mouse', 15, '26/12/2023', "Ricardo Santos"],
    ['Impressora', 5, '27/12/2023', "Fernanda Costa"],
    ['Cafeteira', 30, '28/12/2023', "João Silva"],
    ['Smartphone', 8, '29/12/2023', "Larissa Manoela"],
    ['Notebook', 12, '30/12/2023', "Roberto Lima"],
    ['Smart TV', 7, '31/12/2023', "Mariana Almeida"],
    ['Ar Condicionado', 3, '01/01/2024', "Paulo Henrique"],
    ['Ventilador', 25, '02/01/2024', "Juliana Martins"]
]


    table_frame = CTkScrollableFrame(master=enter_frame, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    table.pack(expand=True)

    # Frame para os botões (agora embaixo da tabela)
    button_frame = CTkFrame(master=enter_frame, fg_color="transparent")
    button_frame.pack(anchor="center", side="bottom", pady=(5, 21))

    # Criando os quatro botões
    CTkButton(master=button_frame, text="Cadastrar Entrada", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(create_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Editar Entrada", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(edit_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Deletar Entrada", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(delete_product_frame)).pack(side="left", padx=5)
    
    CTkButton(master=button_frame, text="Buscar Entrada", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(search_product_frame)).pack(side="left", padx=5)

def create_category_table():
    # Frame para a tabela de checkboxes
    table_frame = CTkScrollableFrame(master=category_frame, fg_color="transparent", width=300, height=300)
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)

    # Lista de categorias para os checkboxes
    categories = ["Eletrônicos", "Vestuário", "Alimentos", "Serviços", "Móveis"]
    for i in range(20):  # Adiciona categorias para simular muitos elementos
        categories.append(f"Categoria {i+6}")

    # Dicionário para armazenar as variáveis dos checkboxes
    checkbox_vars = {}

    # Loop para criar um checkbox para cada categoria na lista
    for category in categories:
        var = IntVar()
        checkbox = CTkCheckBox(table_frame, text=category, variable=var, fg_color='#2A8C55')
        checkbox.pack(pady=5, anchor="w")
        checkbox_vars[category] = var

    button_frame = CTkFrame(master=category_frame, fg_color="transparent")
    button_frame.pack(anchor="center", side="bottom", pady=(5, 21))

    # Criando os quatro botões
    CTkButton(master=button_frame, text="Cadastrar Categoria", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(create_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Editar Categoria", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(edit_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Deletar Categoria", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(delete_product_frame)).pack(side="left", padx=5)
    
    CTkButton(master=button_frame, text="Buscar Categoria", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(search_product_frame)).pack(side="left", padx=5)



def create_exit_table():
    
    table_data = [
    ["Produto", "Quantidade", "Tipo de saída", "Data de saída", "Destinatário", "Vendedor"],
    ['Smartphone', 2, 'Venda para consumidor', "23/01/2024", "Larissa Manoela", "Carlos Alberto"],
    ['Notebook', 1, 'Venda para consumidor', "24/01/2024", "Mariana Silva", "Fernanda Costa"],
    ['Cafeteira', 5, 'Venda para atacadista', "25/01/2024", "José Oliveira", "Ricardo Lima"],
    ['Smart TV', 3, 'Venda para consumidor', "26/01/2024", "Ana Paula", "Paulo Santos"],
    ['Geladeira', 1, 'Venda para loja', "27/01/2024", "Loja de Eletrodomésticos X", "Lucas Martins"],
    ['Fone de Ouvido', 10, 'Venda para consumidor', "28/01/2024", "Bruno Mendes", "Juliana Almeida"],
    ['Teclado', 7, 'Venda para consumidor', "29/01/2024", "Gustavo Rocha", "Ana Beatriz"],
    ['Máquina de Lavar', 2, 'Venda para consumidor', "30/01/2024", "Fernanda Lima", "Carlos Almeida"],
    ['Ventilador', 4, 'Venda para atacadista', "31/01/2024", "Cláudio Silva", "Roberto Costa"],
    ['Ar Condicionado', 1, 'Venda para loja', "01/02/2024", "Loja de Eletrodomésticos Y", "Marcos Pereira"]
]



    table_frame = CTkScrollableFrame(master=exit_frame, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    table.pack(expand=True)

    # Frame para os botões (agora embaixo da tabela)
    button_frame = CTkFrame(master=exit_frame, fg_color="transparent")
    button_frame.pack(anchor="center", side="bottom", pady=(5, 21))

    # Criando os quatro botões
    CTkButton(master=button_frame, text="Cadastrar Saída", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(create_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Editar Saída", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(edit_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Deletar Saída", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(delete_product_frame)).pack(side="left", padx=5)
    
    CTkButton(master=button_frame, text="Buscar Saída", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(search_product_frame)).pack(side="left", padx=5)

def create_custumers_table():
    
    table_data = [
    ["Nome", "CPF", "Endereço", "Telefone", "Código do Cliente"],
    ['João Lucas', '123.456.789-11', 'R. 12', "(92)99123-3241", 1110],
    ['Maria Silva', '987.654.321-00', 'Av. das Flores, 45', "(92)99234-5678", 1111],
    ['Pedro Santos', '123.987.654-22', 'R. Amazonas, 789', "(92)99345-6789", 1112],
    ['Ana Paula', '456.321.789-33', 'R. Igarapé, 101', "(92)99456-7890", 1113],
    ['Lucas Oliveira', '789.123.456-44', 'Av. Brasil, 202', "(92)99567-8901", 1114],
    ['Carla Souza', '321.654.987-55', 'Rua das Orquídeas, 303', "(92)99678-9012", 1115],
    ['Roberto Lima', '654.987.321-66', 'Rua Palmeiras, 404', "(92)99789-0123", 1116],
    ['Fernanda Costa', '111.222.333-77', 'Rua do Sol, 505', "(92)99890-1234", 1117],
    ['Paulo Almeida', '222.333.444-88', 'Av. Central, 606', "(92)99901-2345", 1118],
    ['Luciana Ramos', '333.444.555-99', 'R. das Laranjeiras, 707', "(92)99012-3456", 1119]
]



    table_frame = CTkScrollableFrame(master=customer_frame, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    table.pack(expand=True)

    # Frame para os botões (agora embaixo da tabela)
    button_frame = CTkFrame(master=customer_frame, fg_color="transparent")
    button_frame.pack(anchor="center", side="bottom", pady=(5, 21))

    # Criando os quatro botões
    CTkButton(master=button_frame, text="Cadastrar Cliente", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(create_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Editar Cliente", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(edit_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Deletar Cliente", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(delete_product_frame)).pack(side="left", padx=5)
    
    CTkButton(master=button_frame, text="Buscar Cliente", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(search_product_frame)).pack(side="left", padx=5)

def create_factory_table():
    
    table_data = [
    ["Nome da Empresa", "Nome do Gerente", "CNPJ", "Endereço", "Telefone", "Código do Fornecedor"],
    ['Castro Motores', 'Fernando Castro', '12.345.678/0001-90', "R. 14", "(92)99123-3241", 1110],
    ['Fornecedora X', 'Ana Paula', '23.456.789/0001-01', "Av. das Flores, 45", "(92)99234-5678", 1111],
    ['Tech Solutions', 'Carlos Almeida', '34.567.890/0001-12', "R. Amazonas, 789", "(92)99345-6789", 1112],
    ['Construções Y', 'Roberto Lima', '45.678.901/0001-23', "R. Igarapé, 101", "(92)99456-7890", 1113],
    ['Móveis e Decoração', 'Fernanda Costa', '56.789.012/0001-34', "Av. Brasil, 202", "(92)99567-8901", 1114],
    ['Distribuidora Z', 'Juliana Martins', '67.890.123/0001-45', "Rua das Orquídeas, 303", "(92)99678-9012", 1115],
    ['Eletrodomésticos A', 'Ricardo Santos', '78.901.234/0001-56', "Rua Palmeiras, 404", "(92)99789-0123", 1116],
    ['Roupas e Acessórios B', 'Lucas Oliveira', '89.012.345/0001-67', "Rua do Sol, 505", "(92)99890-1234", 1117],
    ['Alimentos e Bebidas C', 'Maria Lusia', '90.123.456/0001-78', "Av. Central, 606", "(92)99901-2345", 1118],
    ['Equipamentos D', 'Paulo Henrique', '01.234.567/0001-89', "R. das Laranjeiras, 707", "(92)99012-3456", 1119]
]


    table_frame = CTkScrollableFrame(master=factory_frame, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    table.pack(expand=True)

    # Frame para os botões (agora embaixo da tabela)
    button_frame = CTkFrame(master=factory_frame, fg_color="transparent")
    button_frame.pack(anchor="center", side="bottom", pady=(5, 21))

    # Criando os quatro botões
    CTkButton(master=button_frame, text="Cadastrar Fornecedor", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(create_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Editar Fornecedor", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(edit_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Deletar Fornecedor", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(delete_product_frame)).pack(side="left", padx=5)
    
    CTkButton(master=button_frame, text="Buscar Fornecedor", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(search_product_frame)).pack(side="left", padx=5)

def create_sellers_table():
    
    table_data = [
    ["Nome", "CPF", "Endereço", "Telefone", "CTPS", "Data de Nascimento", "Código"],
    ['Maria Lusia', '133.656.749-12', 'R. 12', "(92)99123-3241", 1234567890, "23/12/2004", 1021],
    ['Carlos Almeida', '234.567.890-23', 'Av. das Flores, 45', "(92)99234-5678", 2345678901, "15/06/1990", 1022],
    ['Ana Beatriz', '345.678.901-34', 'R. Amazonas, 789', "(92)99345-6789", 3456789012, "10/03/1995", 1023],
    ['Ricardo Santos', '456.789.012-45', 'R. Igarapé, 101', "(92)99456-7890", 4567890123, "05/01/1988", 1024],
    ['Julia Martins', '567.890.123-56', 'Av. Brasil, 202', "(92)99567-8901", 5678901234, "28/08/1992", 1025],
    ['Thiago Oliveira', '678.901.234-67', 'Rua das Orquídeas, 303', "(92)99678-9012", 6789012345, "30/04/1985", 1026],
    ['Fernanda Costa', '789.012.345-78', 'Rua Palmeiras, 404', "(92)99789-0123", 7890123456, "12/11/1998", 1027],
    ['Bruno Lima', '890.123.456-89', 'Rua do Sol, 505', "(92)99890-1234", 8901234567, "22/02/1993", 1028],
    ['Luana Pereira', '901.234.567-90', 'Av. Central, 606', "(92)99901-2345", 9012345678, "18/07/1991", 1029],
    ['Paulo Henrique', '012.345.678-01', 'R. das Laranjeiras, 707', "(92)99012-3456", 2123456789, "29/09/1989", 1030]
]

    table_frame = CTkScrollableFrame(master=seller_frame, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    table.pack(expand=True)

    # Frame para os botões (agora embaixo da tabela)
    button_frame = CTkFrame(master=seller_frame, fg_color="transparent")
    button_frame.pack(anchor="center", side="bottom", pady=(5, 21))

    # Criando os quatro botões
    CTkButton(master=button_frame, text="Cadastrar Vendedor", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(create_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Editar Vendedor", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(edit_product_frame)).pack(side="left", padx=5)

    CTkButton(master=button_frame, text="Deletar Vendedor", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(delete_product_frame)).pack(side="left", padx=5)
    
    CTkButton(master=button_frame, text="Buscar Vendedor", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=lambda: show_frame(search_product_frame)).pack(side="left", padx=5)


# Função para criar os botões na tela de Relatórios
def create_report_buttons():
    button_frame = CTkFrame(master=dashboard_frame, fg_color="transparent")
    button_frame.pack(anchor="center", pady=(100, 0))  # Posicionamento dos botões

    # Botões para os diferentes relatórios
    CTkButton(master=button_frame, text="Gerar Relatório de Entrada", font=("Arial Bold", 15), fg_color="#2A8C55",
              hover_color="#207244", command=lambda: print("Relatório de Entrada")).pack(pady=10, fill="x")
    
    CTkButton(master=button_frame, text="Gerar Relatório de Saída", font=("Arial Bold", 15), fg_color="#2A8C55",
              hover_color="#207244", command=lambda: print("Relatório de Saída")).pack(pady=10, fill="x")
    
    CTkButton(master=button_frame, text="Gerar Relatório de Principais Clientes", font=("Arial Bold", 15), fg_color="#2A8C55",
              hover_color="#207244", command=lambda: print("Relatório de Principais Clientes")).pack(pady=10, fill="x")
    
    CTkButton(master=button_frame, text="Gerar Relatório de Permanência de Produto em Estoque", font=("Arial Bold", 15), fg_color="#2A8C55",
              hover_color="#207244", command=lambda: print("Relatório de Permanência")).pack(pady=10, fill="x")
    
    CTkButton(master=button_frame, text="Gerar Relatório de Lucro/Prejuízo", font=("Arial Bold", 15), fg_color="#2A8C55",
              hover_color="#207244", command=lambda: print("Relatório de Lucro/Prejuízo")).pack(pady=10, fill="x")

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

# Função para criar a página de novo pedido
def update_orders_table():
    """Atualiza a tabela após inserir novos dados."""
    global table_data, table

    # Limpa e recria a tabela com os novos dados
    table.pack_forget()  # Remove a tabela antiga
    table = CTkTable(master=table.master, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    table.pack(expand=True)




def create_create_product_page():
    CTkLabel(master=create_product_frame, text="Preencher Dados do Produto", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29, 0), padx=27)

    # Campos de entrada
    CTkLabel(master=create_product_frame, text="Nome do Produto", font=("Arial Bold", 17), text_color="#52A476").pack(anchor="nw", pady=(25, 0), padx=27)
    product_name_entry = CTkEntry(master=create_product_frame, fg_color="#F0F0F0", border_width=0)
    product_name_entry.pack(fill="x", pady=(12, 0), padx=27, ipady=10)

    grid = CTkFrame(master=create_product_frame, fg_color="transparent")
    grid.pack(fill="both", padx=27, pady=(31, 0))

    CTkLabel(master=grid, text="Custo de Compra", font=("Arial Bold", 17), text_color="#52A476").grid(row=0, column=0, sticky="w")
    cost_entry = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
    cost_entry.grid(row=1, column=0, ipady=10)

    CTkLabel(master=grid, text="Preço Sugerido", font=("Arial Bold", 17), text_color="#52A476").grid(row=0, column=1, sticky="w", padx=(25, 0))
    price_entry = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300)
    price_entry.grid(row=1, column=1, ipady=10, padx=(24, 0))

    CTkLabel(master=grid, text="Categoria", font=("Arial Bold", 17), text_color="#52A476").grid(row=2, column=0, sticky="w", pady=(38, 0))
    category_options = ["Eletrônico", "Vestimenta", "Serviço"]
    category_var = tkinter.StringVar(value=category_options[0])
    CTkOptionMenu(master=grid, variable=category_var, values=category_options, font=("Arial Bold", 14), text_color="#52A476", fg_color="#F0F0F0").grid(row=3, column=0, sticky="w", pady=(16, 0))

    CTkLabel(master=grid, text="Estoque Máximo", font=("Arial Bold", 17), text_color="#52A476").grid(row=2, column=1, sticky="w", pady=(42, 0))
    max_stock_entry = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=100)
    max_stock_entry.grid(row=3, column=1, pady=(21, 0), sticky="w")

    CTkLabel(master=grid, text="Quantidade", font=("Arial Bold", 17), text_color="#52A476").grid(row=4, column=0, sticky="w", pady=(42, 0))
    quantity_entry = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=100)
    quantity_entry.grid(row=5, column=0, pady=(21, 0), sticky="w")

    CTkLabel(master=grid, text="Estoque Mínimo", font=("Arial Bold", 17), text_color="#52A476").grid(row=4, column=1, sticky="w", pady=(42, 0))
    minimum_stock_entry = CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=100)
    minimum_stock_entry.grid(row=5, column=1, pady=(21, 0), sticky="w")

    actions = CTkFrame(master=create_product_frame, fg_color="transparent")
    actions.pack(fill="both", pady=(20, 0))

    def add_product():
        product_name = product_name_entry.get()
        cost = cost_entry.get()
        price = price_entry.get()
        category = category_var.get()
        quantity = quantity_entry.get()
        max_stock = max_stock_entry.get()
        minimum_stock = minimum_stock_entry.get()

        # Verificações de validação
        try:
            cost = float(cost)
            price = float(price)
        except ValueError:
            print("Custo e preço devem ser números válidos.")
            chamar_erro("Custo e preço devem ser números válidos.")
            return

        if not quantity.isdigit():
            print("Quantidade deve ser um número inteiro.")
            chamar_erro("Quantidade deve ser um número inteiro.")
            return
        
        if not max_stock.isdigit():
            print("Maximo estoque deve ser um número inteiro.")
            chamar_erro("Maximo estoque deve ser um número inteiro.")
            return

        if not minimum_stock.isdigit():
            print("Estoque mninimo deve ser um número inteiro.")
            chamar_erro("Estoque mninimo deve ser um número inteiro.")
            return

        if product_name.strip() == "":
            print("O nome do produto não pode estar vazio.")
            chamar_erro("O nome do produto não pode estar vazio.")
            return

        if int(quantity) < 0:
            print("A quantidade deve ser maior ou igual a zero.")
            chamar_erro("A quantidade deve ser maior ou igual a zero.")
            return

        # Cadastro do produto se todas as validações forem atendidas
        if product_name and cost and price and category and quantity and max_stock and minimum_stock:
            try:
                # Atualiza a lista de dados
                table_data.append([len(table_data), product_name, category, f"{cost:.2f}", f"{price:.2f}", quantity, max_stock, minimum_stock])
                update_orders_table()  # Reconstrói a tabela

                # Limpa os campos de entrada após o cadastro
                product_name_entry.delete(0, 'end')
                cost_entry.delete(0, 'end')
                price_entry.delete(0, 'end')
                quantity_entry.delete(0, 'end')
                max_stock_entry.delete(0, 'end')
                minimum_stock_entry.delete(0, 'end')
                category_var.set(category_options[0])  # Reseta para a primeira categoria

                show_frame(orders_frame)  # Volta para a tela de produtos
            except Exception as e:
                print(f"Erro ao adicionar o produto: {e}")
        else:
            print("Preencha todos os campos para cadastrar o produto.")

    CTkButton(master=actions, text="Confirmar", width=300, font=("Arial Bold", 17), hover_color="#207244", fg_color="#2A8C55", text_color="#fff", command=add_product).pack(side="left", anchor="se", pady=(30, 0), padx=(20, 10))
    CTkButton(master=actions, text="Cancelar", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#FF0000", hover_color="#eee", border_width=2, text_color="#FF0000", command=lambda: show_frame(orders_frame)).pack(side="left", anchor="se", pady=(30, 0), padx=(10, 27))


def create_search_product_page():
    CTkLabel(master=search_product_frame, text="Buscar Produto", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29, 0), padx=27)

    CTkLabel(master=search_product_frame, text="Nome do Produto", font=("Arial Bold", 17), text_color="#52A476").pack(anchor="nw", pady=(25, 0), padx=27)
    CTkEntry(master=search_product_frame, fg_color="#F0F0F0", border_width=0).pack(fill="x", pady=(12, 0), padx=27, ipady=10)

    grid = CTkFrame(master=search_product_frame, fg_color="transparent")
    grid.pack(fill="both", padx=27, pady=(31, 0))


    actions = CTkFrame(master=search_product_frame, fg_color="transparent")
    actions.pack(fill="x", pady=(20, 0), padx=27)

    # Botões na seção de ações
    CTkButton(master=actions, text="Buscar", width=300, font=("Arial Bold", 17), hover_color="#207244", fg_color="#2A8C55", text_color="#fff", command=lambda: print("Produto buscado")).pack(side="left", pady=(30, 0), padx=(0, 10))

    CTkButton(master=actions, text="Cancelar", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#FF0000", hover_color="#eee", border_width=2, text_color="#FF0000", command=lambda: show_frame(orders_frame)).pack(side="left", pady=(30, 0), padx=(10, 27))


def create_delete_product_page():
    CTkLabel(master=delete_product_frame, text="Deletar Fornecedor", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29,0), padx=27)

    CTkLabel(master=delete_product_frame, text="Nome do Fornecedor", font=("Arial Bold", 17), text_color="#52A476").pack(anchor="nw", pady=(25,0), padx=27)
    CTkEntry(master=delete_product_frame, fg_color="#F0F0F0", border_width=0).pack(fill="x", pady=(12,0), padx=27, ipady=10)

    grid = CTkFrame(master=delete_product_frame, fg_color="transparent")
    grid.pack(fill="both", padx=27, pady=(31,0))

    
    actions = CTkFrame(master=delete_product_frame, fg_color="transparent")
    actions.pack(fill="x", pady=(20, 0), padx=27)  # Ajuste de espaçamento com o Entry

    # Dados da tabela
    



    # Botões organizados e alinhados no frame de ações
    CTkButton(master=actions, text="Buscar", width=300, font=("Arial Bold", 17), hover_color="#207244", fg_color="#2A8C55", text_color="#fff", command=lambda: print("Produto buscado")).pack(side="left", pady=(30,0), padx=(0, 10))

    CTkButton(master=actions, text="Cancelar", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#FF0000", hover_color="#eee", border_width=2, text_color="#FF0000", command=lambda: show_frame(orders_frame)).pack(side="left", pady=(30,0), padx=(10, 10))

def create_edit_product_page():
    CTkLabel(master=edit_product_frame, text="Editar Fornecedor", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29,0), padx=27)

    CTkLabel(master=edit_product_frame, text="Nome do Fornecedor", font=("Arial Bold", 17), text_color="#52A476").pack(anchor="nw", pady=(25,0), padx=27)
    CTkEntry(master=edit_product_frame, fg_color="#F0F0F0", border_width=0).pack(fill="x", pady=(12,0), padx=27, ipady=10)

    grid = CTkFrame(master=edit_product_frame, fg_color="transparent")
    grid.pack(fill="both", padx=27, pady=(31,0))


    actions = CTkFrame(master=edit_product_frame, fg_color="transparent")
    actions.pack(fill="x", pady=(20, 0), padx=27)  # Ajuste o espaçamento com o Entry

    # Alinha os botões com o Entry acima, mantendo-os lado a lado
    CTkButton(master=actions, text="Buscar", width=300, font=("Arial Bold", 17), hover_color="#207244", fg_color="#2A8C55", text_color="#fff", command=lambda: show_frame(create_product_frame)).pack(side="left", pady=(30,0), padx=(0, 10))

    CTkButton(master=actions, text="Cancelar", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#FF0000", hover_color="#eee", border_width=2, text_color="#FF0000", command=lambda: show_frame(orders_frame)).pack(side="left", pady=(30,0), padx=(10,0))

def create_login_screen():
    global login_frame

    login_frame = CTkFrame(master=main_view, fg_color="white")
    # Frame principal da tela de login
    login_frame.place(relwidth=1, relheight=1)

    # Título
    CTkLabel(master=login_frame, text="Login", font=("Arial Black", 25), text_color="#2A8C55").pack(pady=(50, 20))

    # Campo de entrada para o e-mail
    CTkLabel(master=login_frame, text="E-mail", font=("Arial", 14), text_color="#52A476").pack(pady=(10, 5))
    email_entry = CTkEntry(master=login_frame, fg_color="#F0F0F0", width=300)
    email_entry.pack(pady=(0, 20))

    # Campo de entrada para a senha
    CTkLabel(master=login_frame, text="Senha", font=("Arial", 14), text_color="#52A476").pack(pady=(10, 5))
    password_entry = CTkEntry(master=login_frame, fg_color="#F0F0F0", show="*", width=300)
    password_entry.pack(pady=(0, 20))

    # Função para validar o login
    def validate_login():
        email = email_entry.get()
        password = password_entry.get()
        if email == "" and password == "":
            create_sidebar()
            show_frame(orders_frame)  # Redireciona para a tela de Produtos
            print("teste")
        else:
            CTkLabel(master=login_frame, text="Credenciais inválidas!", font=("Arial", 12), text_color="red").pack()

    # Função para cadastro
    def open_registration():
        CTkLabel(master=login_frame, text="Tela de Cadastro em construção...", font=("Arial", 12), text_color="#52A476").pack(pady=(20, 0))

    # Função para recuperação de senha
    def forgot_password():
        show_frame(forgot_password_frame)

    # Botão de login
    CTkButton(master=login_frame, text="Login", font=("Arial Bold", 14), text_color="#fff", fg_color="#2A8C55",
              hover_color="#207244", command=validate_login).pack(pady=(20, 10))

    # Botões Cadastrar e Esqueci minha senha
    button_frame = CTkFrame(master=login_frame, fg_color="transparent")
    button_frame.pack(pady=(10, 0))

    CTkButton(master=button_frame, text="Cadastrar", font=("Arial", 12), text_color="#2A8C55", fg_color="transparent",
              hover_color="#eeeeee", command=open_registration).pack(side="left", padx=10)
    CTkButton(master=button_frame, text="Esqueci minha senha", font=("Arial", 12), text_color="#2A8C55", fg_color="transparent",
              hover_color="#eeeeee", command=forgot_password).pack(side="left", padx=10)

def chamar_erro(erro):
    create_error_frame(erro)
    show_frame(error_frame)

def create_forgot_password():
    CTkLabel(master=forgot_password_frame, text="Esqueci Minha Senha", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29,0), padx=27)

    CTkLabel(master=forgot_password_frame, text="Email", font=("Arial Bold", 17), text_color="#52A476").pack(anchor="nw", pady=(25,0), padx=27)
    CTkEntry(master=forgot_password_frame, fg_color="#F0F0F0", border_width=0).pack(fill="x", pady=(12,0), padx=27, ipady=10)

    

    actions = CTkFrame(master=forgot_password_frame, fg_color="transparent")
    actions.pack(fill="x", pady=(20, 0), padx=27)  # Ajuste o espaçamento com o Entry

    # Alinha os botões com o Entry acima, mantendo-os lado a lado
    CTkButton(master=actions, text="Confirmar", width=300, font=("Arial Bold", 17), hover_color="#207244", fg_color="#2A8C55", text_color="#fff", command=lambda: print("confirmado")).pack(side="left", pady=(30,0), padx=(0, 10))

    CTkButton(master=actions, text="Cancelar", width=300, fg_color="transparent", font=("Arial Bold", 17), border_color="#FF0000", hover_color="#eee", border_width=2, text_color="#FF0000", command=lambda: login_frame.tkraise()).pack(side="left", pady=(30,0), padx=(10,0))


def create_error_frame(erro):
    for widget in error_frame.winfo_children():
        widget.destroy()
    CTkLabel(master=error_frame, text=erro, font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", pady=(29,0), padx=27)
    

    actions = CTkFrame(master=error_frame, fg_color="transparent")
    actions.pack(fill="x", pady=(20, 0), padx=27)  # Ajuste o espaçamento com o Entry

    # Alinha os botões com o Entry acima, mantendo-os lado a lado
    CTkButton(master=actions, text="Confirmar", width=300, font=("Arial Bold", 17), hover_color="#207244", fg_color="#2A8C55", text_color="#fff", command=lambda: show_frame(orders_frame)).pack(side="left", pady=(30,0), padx=(0, 10))




# Inicialização principal
main_view = CTkFrame(master=app, fg_color="#fff", corner_radius=0)
main_view.pack(fill="both", side="right", expand=True, padx=(27, 0), pady=(22, 22))





create_main_frames()
create_orders_table()
#Telas do Produto
create_new_order_page()
create_create_product_page()
create_search_product_page()
create_delete_product_page()
create_edit_product_page()

create_report_buttons()
create_custumers_table()
create_sellers_table()
create_factory_table()
create_exit_table()
create_enter_table()
create_forgot_password()

create_category_table()
create_login_screen()


# Exibir a tela inicial (Orders)

app.mainloop()