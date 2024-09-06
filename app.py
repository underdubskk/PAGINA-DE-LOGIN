# importando o flet
import flet as ft

# controlando às informações do flet
def main(page:ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True
    page.window_resizable = False

    login = ft.Column([
        ft.Container(
            bgcolor = ft.colors.GREEN_200,
            width = page.window_width - 10,
            height = page.window_height - 60,
            border_radius = 10,

            content = ft.Column([
                ft.Container(
                    bgcolor = ft.colors.WHITE70,
                    width = 400,
                    height = 320,
                    border_radius = 10,

                    content = ft.Column([
                        ft.Container(
                            padding = ft.padding.only(
                                top = 10,
                                bottom = 12,
                            ),
                            content = ft.Column([
                                ft.Text(
                                    value = 'Sign-In',
                                    weight = 'bold',
                                    size = 20
                                )
                            ])    
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text = 'Digite o seu email',
                                width = 300,
                                height = 40,
                                border_radius = 40,
                                prefix_icon = ft.icons.PERSON,
                                keyboard_type = ft.KeyboardType.EMAIL
                            )
                        ])
              
                    ],horizontal_alignment = 'center')

                )
            ],horizontal_alignment = 'center', alignment = 'center')
        )
    ])

    register = ft.Column([

    ])

    page.add(login)

# criando a aplicação do flet
if __name__ == '__main__':
    ft.app(target = main)