import flet as ft


def main(page: ft.Page):
    page.title = "Calculatorr"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = 400
    page.window_width = 400

    txt_field = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=300, read_only=True,)




    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        txt_field,
                    ], alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.TextButton("7", data=7),
                        ft.TextButton("8", data=8),
                        ft.TextButton("9", data=9),
                        ft.TextButton("+", data="+"),
                    ], alignment=ft.MainAxisAlignment.CENTER,

                ),
                ft.Row(
                    [
                        ft.TextButton("4", data=4),
                        ft.TextButton("5", data=5),
                        ft.TextButton("6", data=6),
                        ft.TextButton("-", data="-"),
                    ], alignment=ft.MainAxisAlignment.CENTER,

                ),
                ft.Row(
                    [
                        ft.TextButton("1", data=1),
                        ft.TextButton("2", data=2),
                        ft.TextButton("3", data=3),
                        ft.TextButton("x", data="x"),
                    ], alignment=ft.MainAxisAlignment.CENTER,

                ),
                ft.Row(
                    [
                        ft.TextButton("C",),
                        ft.TextButton("0", data=0),
                        ft.TextButton("=",),
                        ft.TextButton("/", data="/"),
                    ], alignment=ft.MainAxisAlignment.CENTER,

                ),
            ]
        )
    )


ft.app(target=main)
