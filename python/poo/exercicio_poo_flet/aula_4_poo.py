import flet as ft

# ------------------ MODELOS ------------------ #
class Cliente:
    def __init__(self, nome, tel, email, id):
        self.__nome, self.tel, self.email, self.id = nome, tel, email, id

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return f"Cliente {self.id} - Nome: {self.nome} - Email: {self.email} - Telefone: {self.tel}"


class Quarto:
    def __init__(self, num, tipo, preco_diaria):
        self.num, self.tipo, self.preco_diaria = num, tipo, preco_diaria
        self.status = True

    def verificar_disponibilidade(self):
        return self.status

    def alterar_status(self):
        self.status = not self.status

    def __str__(self):
        return f"Quarto {self.num} - Tipo: {self.tipo} - Preço diária: R${self.preco_diaria} - Disponibilidade: {'Disponível' if self.status else 'Indisponível'}"


class Reserva:
    def __init__(self, cliente, quarto, qtd_dias):
        self.cliente, self.quarto, self.qtd_dias = cliente, quarto, qtd_dias
        self.status = True
        self.total = self.qtd_dias * self.quarto.preco_diaria

    def __str__(self):
        return f"Reserva\nCliente: {self.cliente.nome}\nQuarto: {self.quarto.num}\nQuantidade de dias: {self.qtd_dias}\nTotal da reserva: R${self.total}"


class GerenciadorDeReservas:
    def __init__(self):
        self.reservas = []
        self.quartos = [
            Quarto(num=101, tipo="single", preco_diaria=100),
            Quarto(num=102, tipo="double", preco_diaria=200),
            Quarto(num=103, tipo="suite", preco_diaria=300),
        ]
        self.clientes = []

    def cadastrar_quarto(self, num, tipo, preco_diaria):
        quarto = Quarto(num, tipo, preco_diaria)
        self.quartos.append(quarto)
        return f"Quarto {num} cadastrado com sucesso"

    def listar_quartos(self):
        return [str(quarto) for quarto in self.quartos]

    def listar_clientes(self):
        return [str(cliente) for cliente in self.clientes]

    def cadastrar_cliente(self, nome, email, tel):
        id_cliente = len(self.clientes)
        cliente = Cliente(nome, tel, email, id_cliente)
        self.clientes.append(cliente)
        return f"Cliente {cliente.id} criado com sucesso"

    def criar_reserva(self, id_cliente, num_quarto, qtd_dias):
        quarto = self.get_quarto(num_quarto)
        cliente = self.get_cliente(id_cliente)
        if quarto and quarto.verificar_disponibilidade():
            reserva = Reserva(cliente, quarto, qtd_dias)
            quarto.alterar_status()
            self.reservas.append(reserva)
            return f"Reserva criada com sucesso para {cliente.nome}"
        return "Erro ao criar reserva"

    def get_quarto(self, num_quarto):
        for quarto in self.quartos:
            if quarto.num == num_quarto:
                return quarto
        return False

    def get_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id == id_cliente:
                return cliente
        return False

    def listar_reservas(self):
        return [str(reserva) for reserva in self.reservas]

    def cancelar_reserva(self, id_cliente):
        for reserva in self.reservas:
            if reserva.cliente.id == id_cliente and reserva.status:
                reserva.status = False
                reserva.quarto.alterar_status()
                return f"Reserva cancelada com sucesso"
        return f"Não foi encontrada uma reserva ativa para este cliente"


# ------------------ INTERFACE FLET ------------------ #
def main(page: ft.Page):
    page.title = "Sistema de Reservas - Flet"
    gerenciador = GerenciadorDeReservas()

    # Inputs
    nome = ft.TextField(label="Nome do Cliente")
    email = ft.TextField(label="Email")
    tel = ft.TextField(label="Telefone")

    num_quarto = ft.TextField(label="Número do quarto")
    tipo_quarto = ft.TextField(label="Tipo do quarto")
    preco_quarto = ft.TextField(label="Preço diária")

    id_cliente_reserva = ft.TextField(label="ID Cliente")
    num_quarto_reserva = ft.TextField(label="Número do quarto")
    qtd_dias_reserva = ft.TextField(label="Quantidade de dias")

    id_cliente_cancelar = ft.TextField(label="ID Cliente para cancelar reserva")

    # Listas
    lista_quartos = ft.Column()
    lista_clientes = ft.Column()
    lista_reservas = ft.Column()

    def refresh_quartos():
        lista_quartos.controls.clear()
        for q in gerenciador.listar_quartos():
            lista_quartos.controls.append(ft.Text(q))
        page.update()

    def refresh_clientes():
        lista_clientes.controls.clear()
        for c in gerenciador.listar_clientes():
            lista_clientes.controls.append(ft.Text(c))
        page.update()

    def refresh_reservas():
        lista_reservas.controls.clear()
        for r in gerenciador.listar_reservas():
            lista_reservas.controls.append(ft.Text(r))
        page.update()

    # Botões
    def on_cadastrar_cliente(e):
        msg = gerenciador.cadastrar_cliente(nome.value, email.value, tel.value)
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        nome.value, email.value, tel.value = "", "", ""
        refresh_clientes()
        page.update()

    def on_cadastrar_quarto(e):
        msg = gerenciador.cadastrar_quarto(int(num_quarto.value), tipo_quarto.value, float(preco_quarto.value))
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        num_quarto.value, tipo_quarto.value, preco_quarto.value = "", "", ""
        refresh_quartos()
        page.update()

    def on_criar_reserva(e):
        msg = gerenciador.criar_reserva(int(id_cliente_reserva.value), int(num_quarto_reserva.value), int(qtd_dias_reserva.value))
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        id_cliente_reserva.value, num_quarto_reserva.value, qtd_dias_reserva.value = "", "", ""
        refresh_reservas()
        refresh_quartos()
        page.update()

    def on_cancelar_reserva(e):
        msg = gerenciador.cancelar_reserva(int(id_cliente_cancelar.value))
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        id_cliente_cancelar.value = ""
        refresh_reservas()
        refresh_quartos()
        page.update()

    # Layout
    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("Cadastro de Cliente"),
                        nome,
                        email,
                        tel,
                        ft.ElevatedButton("Cadastrar Cliente", on_click=on_cadastrar_cliente),
                        ft.Divider(),
                        ft.Text("Cadastro de Quarto"),
                        num_quarto,
                        tipo_quarto,
                        preco_quarto,
                        ft.ElevatedButton("Cadastrar Quarto", on_click=on_cadastrar_quarto),
                        ft.Divider(),
                        ft.Text("Criar Reserva"),
                        id_cliente_reserva,
                        num_quarto_reserva,
                        qtd_dias_reserva,
                        ft.ElevatedButton("Criar Reserva", on_click=on_criar_reserva),
                        ft.Divider(),
                        ft.Text("Cancelar Reserva"),
                        id_cliente_cancelar,
                        ft.ElevatedButton("Cancelar Reserva", on_click=on_cancelar_reserva),
                    ],
                    expand=True,
                ),
                ft.Column(
                    [
                        ft.Text("Quartos"),
                        lista_quartos,
                        ft.Divider(),
                        ft.Text("Clientes"),
                        lista_clientes,
                        ft.Divider(),
                        ft.Text("Reservas"),
                        lista_reservas,
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
    )

    # Inicializa listas
    refresh_quartos()
    refresh_clientes()
    refresh_reservas()


if __name__ == "__main__":
    ft.app(target=main)
