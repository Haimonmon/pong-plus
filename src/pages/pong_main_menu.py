class MainMenuUI:
    """
    Main Menu of the game or so called Home
    """
    def __init__(self, app):
        self.app = app
        self.app_window = self.app.window
        self.app_widget = self.app.widget
        self.app_widget_list = self.app.widget_list


    def render(self) -> None:
        """ Display Main menu UI """
        self.app_window.set_title('Pong Classic ( Alpha )')
        self.app_window.clear_page(self.app_widget_list)

        main_canvas = self.app_widget.create_canvas(width=1000, height=580, background="#1D313C", highlightthickness=0, pack={"fill": 'both', "expand": True})
        self.app_widget_list.append(main_canvas)

        inner_canvas = self.app_widget.create_canvas(parent_widget=main_canvas, width=955, height=534, background="#1D313C", highlightthickness=2, bd=0, relief='solid', highlightcolor='#FADAC1', place={"relx": 0.5, "rely": 0.5, "anchor": "center"})
        self.app_widget_list.append(inner_canvas)

        menu_option_canvas = self.app_widget.create_canvas(parent_widget=inner_canvas, width=325, height=264, background="#1D313C", highlightthickness=2, bd=0, relief='solid', highlightcolor='#FADAC1', place={"x": 325, "y": 243})
        self.app_widget_list.append(menu_option_canvas)
      
        self.display_game_logo(inner_canvas)

        self.display_options(menu_option_canvas)

      
    def display_game_logo(self, canvas) -> None:
        """ Game logo """
        self.app_widget.create_canvas_image(canvas, 325, 60, orig_image=r"src\assets\Paddle_Wshadow.png", img_width=33, img_height=140)
        self.app_widget.create_canvas_image(canvas, 380, 70, orig_image=r"src\assets\PongTxt_Wshadow.png", img_width=243, img_height=63)
        self.app_widget.create_canvas_image(canvas, 380, 138, orig_image=r"src\assets\ClassicTxt_Wshadow.png", img_width=245, img_height=45)
        self.app_widget.create_canvas_image(canvas, 633, 60, orig_image=r"src\assets\Paddle_Wshadow.png", img_width=33, img_height=140)


    def display_options(self, canvas) -> None:
        """ Main menu options """
        start_button = self.app_widget.create_canvas_button_text(canvas, 162.5 ,60,orig_text="Start",sub_text=">>    Start    <<",font=("Pixelify Sans",14), fill='#F37844')
        settings_button = self.app_widget.create_canvas_button_text(canvas, 162.5 ,108,orig_text="Settings",sub_text=">>    Settings    <<",font=("Pixelify Sans",14), fill='#FADAC1')
        about_button = self.app_widget.create_canvas_button_text(canvas, 162.5 ,157,orig_text="About",sub_text=">>    About    <<",font=("Pixelify Sans",14), fill='#FADAC1')
        quit_button = self.app_widget.create_canvas_button_text(canvas, 162.5 ,206,orig_text="Quit",sub_text=">>    Quit    <<",font=("Pixelify Sans",14), fill='#F37844')

        self.handle_inputs(canvas, start_button, settings_button, about_button, quit_button)

        
    def handle_inputs(self, menu_option_canvas: int, start_btn: int, settings_btn: int, about_btn: int, quit_btn: int) -> None:
        """ Handles user inputs """
        menu_option_canvas.tag_bind(start_btn, "<Button-1>", lambda event: self.app.gamemodes.render())
        menu_option_canvas.tag_bind(settings_btn, "<Button-1>", lambda event: self.app.settings.render())
        menu_option_canvas.tag_bind(quit_btn, "<Button-1>",lambda event: self.app.quit())

        # self.app_widget.apply_canvas_cursor_auto_move(canvas=menu_option_canvas, point_coordinates=[(162.5, 60), (162.5, 108), (162.5, 157), (162.5, 206)], navigations="WASD", avail_work_navs = [0,2])