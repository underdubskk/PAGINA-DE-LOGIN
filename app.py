# importando o flet
import flet as ft

# controlando às informações do flet
def main(page:ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True
    page.window_resizable = False

    # controlando os botões
    def logar(e):
        page.remove(register)
        page.add(login)
        page.update()

    def regist(e):
        page.remove(login)
        page.add(register)
        page.update()

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
                                text_vertical_align = 1,
                                keyboard_type = ft.KeyboardType.EMAIL
                            ),

                            ft.TextField(
                                hint_text = 'Digite a sua senha',
                                width = 300,
                                height = 40,
                                border_radius = 40,
                                prefix_icon = ft.icons.LOCK,
                                text_vertical_align = 1,
                                password = True,
                                can_reveal_password = True,
                                keyboard_type = ft.KeyboardType.VISIBLE_PASSWORD
                            ),

                            ft.ElevatedButton(
                                text = 'Sing-In',
                                bgcolor = ft.colors.GREEN_200,
                                on_hover = ft.colors.GREEN_100,
                                width = 300,
                                height = 40
                            ),

                            ft.Row([
                                ft.TextButton('Recuperar conta'),
                                ft.TextButton(
                                    text = 'Criar nova conta',
                                    on_click = regist
                                    )
                            ],width = 300, alignment = ft.MainAxisAlignment.SPACE_BETWEEN)

                        ],spacing = 10),

                        ft.Row([
                            ft.IconButton(icon = ft.icons.EMAIL),
                            ft.IconButton(icon = ft.icons.FACEBOOK),
                            ft.IconButton(icon = ft.icons.TELEGRAM),
                        ],alignment = 'center')
              
                    ],horizontal_alignment = 'center')

                )
            ],horizontal_alignment = 'center', alignment = 'center')
        )
    ])

    register = ft.Column([
        ft.Container(
            bgcolor = ft.colors.GREEN_200,
            width = page.window_width - 10,
            height = page.window_height - 60,
            border_radius = 10,

            content = ft.Column([
                ft.Container(
                    bgcolor = ft.colors.WHITE70,
                    width = 400,
                    height = 450,
                    border_radius = 10,

                    content = ft.Column([
                        ft.Container(
                            padding = ft.padding.only(
                                top = 10,
                                bottom = 12,
                            ),
                            content = ft.Column([
                                ft.Text(
                                    value = 'Register',
                                    weight = 'bold',
                                    size = 20
                                )
                            ])    
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text = 'Primeiro nome',
                                width = 300,
                                height = 40,
                                border_radius = 40,
                                prefix_icon = ft.icons.PERSON,
                                text_vertical_align = 1,
                                keyboard_type = ft.KeyboardType.NAME
                            ),

                            ft.TextField(
                                hint_text = 'Segundo nome',
                                width = 300,
                                height = 40,
                                border_radius = 40,
                                prefix_icon = ft.icons.PERSON,
                                text_vertical_align = 1,
                                keyboard_type = ft.KeyboardType.NAME
                            ),

                            ft.TextField(
                                hint_text = 'Digite o seu email',
                                width = 300,
                                height = 40,
                                border_radius = 40,
                                prefix_icon = ft.icons.EMAIL,
                                text_vertical_align = 1,
                                keyboard_type = ft.KeyboardType.EMAIL
                            ),

                            ft.TextField(
                                hint_text = 'Digite o seu telefone',
                                width = 300,
                                height = 40,
                                border_radius = 40,
                                prefix_icon = ft.icons.PHONE,
                                text_vertical_align = 1,
                                keyboard_type = ft.KeyboardType.PHONE
                            ),

                            ft.TextField(
                                hint_text = 'Digite a sua senha',
                                width = 300,
                                height = 40,
                                border_radius = 40,
                                prefix_icon = ft.icons.LOCK,
                                text_vertical_align = 1,
                                password = True,
                                can_reveal_password = True,
                                keyboard_type = ft.KeyboardType.VISIBLE_PASSWORD
                            ),

                            ft.TextField(
                                hint_text = 'Digite a senha novamente',
                                width = 300,
                                height = 40,
                                border_radius = 40,
                                prefix_icon = ft.icons.LOCK,
                                text_vertical_align = 1,
                                password = True,
                                can_reveal_password = True,
                                keyboard_type = ft.KeyboardType.VISIBLE_PASSWORD
                            ),


                            ft.ElevatedButton(
                                text = 'Register',
                                bgcolor = ft.colors.GREEN_200,
                                on_hover = ft.colors.GREEN_100,
                                width = 300,
                                height = 40
                            ),

                            ft.Row([
                                ft.TextButton('Recuperar conta'),
                                ft.TextButton(
                                    text = 'Já tenho uma conta',
                                    on_click = logar
                                    )
                            ],width = 300, alignment = ft.MainAxisAlignment.SPACE_BETWEEN)

                        ],spacing = 10),
              
                    ],horizontal_alignment = 'center')

                )
            ],horizontal_alignment = 'center', alignment = 'center')
        )
    ])

    # resolvendo problemas da resolução
    def resize_controls(e):
        login.controls[0].width = page.window_width - 10
        login.controls[0].height = page.window.height - 60
    
        register.controls[0].width = page.window_width - 10
        register.controls[0].height = page.window.height - 60
    
        page.update()
        
    page.on_resize.subscribe(resize_controls)
    page.add(login)

# criando a aplicação do flet
if __name__ == '__main__':
    ft.app(target = main)