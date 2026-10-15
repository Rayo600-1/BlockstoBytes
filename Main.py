import tkinter as tk
from tkinter import ttk
import webbrowser
import urllib.request
from io import BytesIO
from PIL import Image, ImageTk

TEXTS = {
    "Español": {
        "title": "Convertidor de Bloques de Nintendo",
        "blocks_title": "Bloques de Nintendo",
        "results_title": "Conversión desde Bloques:",
        "console_title": "Consola Activa:",
        "reverse_title": "Convertir a Bloques:",
        "unit_label": "Unidad:",
        "value_label": "Valor:",
        "result_blocks": "Bloques equivalentes:",
        "large_unit": "Unidad Grande:",
        "lang_label": "Idioma:",
        "error": "Error: Ingrese un número válido",
        "menu_help": "Ayuda / Créditos",
        "about_title": "Acerca de / Créditos",
        "about_text": "Convertidor de Bloques de Nintendo\n\nCreador: Rayo600-1\n\n¡Cuidado con las estafas! Descarga las actualizaciones oficiales únicamente desde GitHub.",
        "github_btn": "Ir al GitHub Oficial"
    },
    "English": {
        "title": "Nintendo Block Converter",
        "blocks_title": "Nintendo Blocks",
        "results_title": "Conversion from Blocks:",
        "console_title": "Active Console:",
        "reverse_title": "Convert to Blocks:",
        "unit_label": "Unit:",
        "value_label": "Value:",
        "result_blocks": "Equivalent blocks:",
        "large_unit": "Large Unit:",
        "lang_label": "Language:",
        "error": "Error: Enter a valid number",
        "menu_help": "Help / Credits",
        "about_title": "About / Credits",
        "about_text": "Nintendo Block Converter\n\nCreator: Rayo600-1\n\nBeware of fakes! Download official updates only from GitHub.",
        "github_btn": "Open Official GitHub"
    },
    "Français": {
        "title": "Convertisseur de Blocs Nintendo",
        "blocks_title": "Blocs Nintendo",
        "results_title": "Conversion depuis les blocs :",
        "console_title": "Console Active :",
        "reverse_title": "Convertir en blocs :",
        "unit_label": "Unité :",
        "value_label": "Valeur :",
        "result_blocks": "Blocs équivalents :",
        "large_unit": "Grande Unité :",
        "lang_label": "Langue :",
        "error": "Erreur : Entrez un nombre valide",
        "menu_help": "Aide / Crédits",
        "about_title": "À propos / Crédits",
        "about_text": "Convertisseur de Blocs Nintendo\n\nCréateur : Rayo600-1\n\nAttention aux faux ! Téléchargez les mises à jour officielles uniquement depuis GitHub.",
        "github_btn": "Ouvrir le GitHub Officiel"
    },
    "Italiano": {
        "title": "Convertitore di Blocchi Nintendo",
        "blocks_title": "Blocchi Nintendo",
        "results_title": "Conversione dai blocchi:",
        "console_title": "Console Attiva:",
        "reverse_title": "Converti in blocchi:",
        "unit_label": "Unità:",
        "value_label": "Valore:",
        "result_blocks": "Blocchi equivalenti:",
        "large_unit": "Unità Grande:",
        "lang_label": "Lingua:",
        "error": "Errore: Inserisci un numero valido",
        "menu_help": "Aiuto / Crediti",
        "about_title": "Informazioni / Crediti",
        "about_text": "Convertitore di Blocchi Nintendo\n\nCreatore: Rayo600-1\n\nAttenzione ai falsi! Scarica gli aggiornamenti ufficiali solo da GitHub.",
        "github_btn": "Apri GitHub Ufficiale"
    },
    "Deutsch": {
        "title": "Nintendo Block Konverter",
        "blocks_title": "Nintendo Blöcke",
        "results_title": "Umrechnung von Blöcken:",
        "console_title": "Aktive Konsole:",
        "reverse_title": "In Blöcke umrechnen:",
        "unit_label": "Einheit:",
        "value_label": "Wert:",
        "result_blocks": "Äquivalente Blöcke:",
        "large_unit": "Große Einheit:",
        "lang_label": "Sprache:",
        "error": "Fehler: Bitte geben Sie eine gültige Zahl ein",
        "menu_help": "Hilfe / Über",
        "about_title": "Über / Credits",
        "about_text": "Nintendo Block Konverter\n\nErsteller: Rayo600-1\n\nVorsicht vor Betrug! Lade offizielle Updates nur von GitHub herunter.",
        "github_btn": "Offizielles GitHub öffnen"
    },
    "Português": {
        "title": "Conversor de Blocos da Nintendo",
        "blocks_title": "Blocos da Nintendo",
        "results_title": "Conversão a partir de Blocos:",
        "console_title": "Console Ativo:",
        "reverse_title": "Converter para Blocos:",
        "unit_label": "Unidade:",
        "value_label": "Valor:",
        "result_blocks": "Blocos equivalentes:",
        "large_unit": "Unidade Grande:",
        "lang_label": "Idioma:",
        "error": "Erro: Insira um número válido",
        "menu_help": "Ajuda / Créditos",
        "about_title": "Sobre / Créditos",
        "about_text": "Conversor de Blocos da Nintendo\n\nCriador: Rayo600-1\n\nCuidado com versões falsas! Baixe atualizações apenas pelo GitHub.",
        "github_btn": "Abrir GitHub Oficial"
    },
    "日本語": {
        "title": "ニンテンドーブロックコンバーター",
        "blocks_title": "ニンテンドーブロック",
        "results_title": "ブロックからの変換:",
        "console_title": "アクティブコンソール:",
        "reverse_title": "ブロックに変換:",
        "unit_label": "単位:",
        "value_label": "値:",
        "result_blocks": "相当ブロック数:",
        "large_unit": "大容量単位:",
        "lang_label": "言語:",
        "error": "エラー: 有効な数字を入力してください",
        "menu_help": "ヘルプ / クレジット",
        "about_title": "情報 / クレジット",
        "about_text": "ニンテンドーブロックコンバーター\n\n作成者: Rayo600-1\n\n偽物に注意してください！公式アップデートはGitHubからのみダウンロードしてください。",
        "github_btn": "公式GitHubを開く"
    }
}

class NintendoConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nintendo Block Converter")
        self.root.geometry("960x540")
        
        self.root.resizable(True, True)
        self.root.minsize(650, 420)
        self.root.maxsize(960, 540)
        
        self.root.configure(bg="#FFFFFF")
        
        self.lang_var = tk.StringVar(value="English")
        self.console_var = tk.StringVar(value="Wii/DSi/3DS")
        self.large_unit_var = tk.StringVar(value="TB")
        self.reverse_unit_var = tk.StringVar(value="MB")
        
        self.blocks_input_var = tk.StringVar()
        self.reverse_input_var = tk.StringVar()
        
        self.kb_var = tk.StringVar(value="KB: 0.00")
        self.mb_var = tk.StringVar(value="MB: 0.00")
        self.gb_var = tk.StringVar(value="GB: 0.00")
        self.large_var = tk.StringVar(value="TB: 0.00")
        self.reverse_result_var = tk.StringVar(value="Bloques equivalentes: 0")
        
        self.profile_img = None
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", background="#FFFFFF", foreground="#000000")
        style.configure("TLabel", background="#FFFFFF", foreground="#000000")
        style.configure("TRadiobutton", background="#FFFFFF", foreground="#000000")
        style.configure("TLabelframe", background="#FFFFFF", foreground="#000000")
        style.configure("TLabelframe.Label", background="#FFFFFF", foreground="#000000")

        self.create_menu()
        self.create_widgets()
        self.bind_events()
        self.update_texts()

    def create_menu(self):
        self.menubar = tk.Menu(self.root)
        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label="Ayuda / Créditos", command=self.show_about)
        self.menubar.add_cascade(menu=self.help_menu, label="Ayuda")
        self.root.config(menu=self.menubar)

    def show_about(self):
        lang = self.lang_var.get()
        t = TEXTS.get(lang, TEXTS["Español"])
        
        about_window = tk.Toplevel(self.root)
        about_window.title(t["about_title"])
        about_window.geometry("400x350")
        about_window.resizable(False, False)
        about_window.configure(bg="#FFFFFF")
        about_window.transient(self.root)
        about_window.grab_set()
        
        try:
            url = "https://github.com/Rayo600-1.png"
            with urllib.request.urlopen(url, timeout=3) as response:
                image_data = response.read()
            
            img = Image.open(BytesIO(image_data))
            img = img.resize((70, 70), Image.Resampling.LANCZOS)
            self.profile_img = ImageTk.PhotoImage(img)
            
            lbl_img = ttk.Label(about_window, image=self.profile_img)
            lbl_img.pack(pady=(15, 5))
        except Exception:
            lbl_oops = ttk.Label(about_window, text="OOPS!", font=("Arial", 16, "bold"), foreground="red")
            lbl_oops.pack(pady=(15, 5))
        
        lbl = ttk.Label(about_window, text=t["about_text"], font=("Arial", 10), justify="center")
        lbl.pack(pady=10, padx=20)
        
        btn_github = ttk.Button(about_window, text=t["github_btn"], command=lambda: webbrowser.open("https://github.com/Rayo600-1/BlockstoBytes"))
        btn_github.pack(pady=5)

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        main_frame.columnconfigure(0, weight=1, uniform="col")
        main_frame.columnconfigure(1, weight=1, uniform="col")
        main_frame.rowconfigure(0, weight=4)
        main_frame.rowconfigure(1, weight=1)

        left_frame = ttk.Frame(main_frame)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        left_frame.rowconfigure(0, weight=1)
        left_frame.rowconfigure(1, weight=3)

        self.lf_blocks = ttk.LabelFrame(left_frame, text="Bloques de Nintendo")
        self.lf_blocks.grid(row=0, column=0, sticky="nsew", pady=(0, 10))
        
        self.ent_blocks = ttk.Entry(self.lf_blocks, textvariable=self.blocks_input_var, justify="center", font=("Arial", 14))
        self.ent_blocks.pack(expand=True, padx=20, pady=10, fill=tk.X)

        self.lf_results = ttk.LabelFrame(left_frame, text="Conversión desde Bloques:")
        self.lf_results.grid(row=1, column=0, sticky="nsew")

        self.ent_kb = ttk.Entry(self.lf_results, textvariable=self.kb_var, state="readonly", font=("Arial", 11))
        self.ent_kb.pack(anchor="w", padx=15, pady=4, fill=tk.X)
        
        self.ent_mb = ttk.Entry(self.lf_results, textvariable=self.mb_var, state="readonly", font=("Arial", 11))
        self.ent_mb.pack(anchor="w", padx=15, pady=4, fill=tk.X)
        
        self.ent_gb = ttk.Entry(self.lf_results, textvariable=self.gb_var, state="readonly", font=("Arial", 11))
        self.ent_gb.pack(anchor="w", padx=15, pady=4, fill=tk.X)
        
        self.ent_large = ttk.Entry(self.lf_results, textvariable=self.large_var, state="readonly", font=("Arial", 11))
        self.ent_large.pack(anchor="w", padx=15, pady=4, fill=tk.X)

        right_frame = ttk.Frame(main_frame)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        right_frame.rowconfigure(0, weight=1)
        right_frame.rowconfigure(1, weight=3)

        self.lf_console = ttk.LabelFrame(right_frame, text="Consola Activa:")
        self.lf_console.grid(row=0, column=0, sticky="nsew", pady=(0, 10))

        self.rb_wii = ttk.Radiobutton(self.lf_console, text="Wii / DSi / 3DS (128 KB)", variable=self.console_var, value="Wii/DSi/3DS")
        self.rb_wii.pack(anchor="w", padx=15, pady=5)
        self.rb_gc = ttk.Radiobutton(self.lf_console, text="GameCube (32 KB)", variable=self.console_var, value="GameCube")
        self.rb_gc.pack(anchor="w", padx=15, pady=5)

        self.lf_reverse = ttk.LabelFrame(right_frame, text="Convertir a Bloques:")
        self.lf_reverse.grid(row=1, column=0, sticky="nsew")

        rev_subframe = ttk.Frame(self.lf_reverse)
        rev_subframe.pack(fill=tk.X, padx=15, pady=10)

        self.lbl_unit = ttk.Label(rev_subframe, text="Unidad:")
        self.lbl_unit.grid(row=0, column=0, sticky="w", padx=(0, 5))
        
        self.cb_unit = ttk.Combobox(rev_subframe, textvariable=self.reverse_unit_var, state="readonly", width=8)
        self.cb_unit['values'] = ("Bytes", "KB", "MB", "GB", "TB", "PB", "EB")
        self.cb_unit.grid(row=0, column=1, sticky="w", padx=(0, 15))

        self.lbl_val = ttk.Label(rev_subframe, text="Valor:")
        self.lbl_val.grid(row=0, column=2, sticky="w", padx=(0, 5))

        self.ent_reverse = ttk.Entry(rev_subframe, textvariable=self.reverse_input_var, width=12)
        self.ent_reverse.grid(row=0, column=3, sticky="w")

        self.ent_reverse_result = ttk.Entry(self.lf_reverse, textvariable=self.reverse_result_var, state="readonly", font=("Arial", 11, "bold"))
        self.ent_reverse_result.pack(anchor="w", padx=15, pady=10, fill=tk.X)

        footer_frame = ttk.Frame(main_frame)
        footer_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        footer_inner = ttk.Frame(footer_frame)
        footer_inner.pack(anchor="center")

        self.lbl_large_unit = ttk.Label(footer_inner, text="Unidad Grande:")
        self.lbl_large_unit.pack(side=tk.LEFT, padx=(0, 5))

        self.cb_large_unit = ttk.Combobox(footer_inner, textvariable=self.large_unit_var, state="readonly", width=6)
        self.cb_large_unit['values'] = ("TB", "PB", "EB")
        self.cb_large_unit.pack(side=tk.LEFT, padx=(0, 20))

        self.lbl_lang = ttk.Label(footer_inner, text="Idioma:")
        self.lbl_lang.pack(side=tk.LEFT, padx=(0, 5))

        self.cb_lang = ttk.Combobox(footer_inner, textvariable=self.lang_var, state="readonly", width=12)
        self.cb_lang['values'] = ("Español", "English", "Français", "Italiano", "Deutsch", "Português", "日本語")
        self.cb_lang.pack(side=tk.LEFT)

    def bind_events(self):
        self.ent_blocks.bind("<KeyRelease>", self.calculate_from_blocks)
        self.ent_reverse.bind("<KeyRelease>", self.calculate_to_blocks)
        
        self.cb_unit.bind("<<ComboboxSelected>>", self.calculate_to_blocks)
        self.cb_large_unit.bind("<<ComboboxSelected>>", self.calculate_from_blocks)
        self.cb_lang.bind("<<ComboboxSelected>>", self.update_texts)
        
        self.console_var.trace_add("write", lambda *args: self.calculate_from_blocks())
        self.console_var.trace_add("write", lambda *args: self.calculate_to_blocks())

    def update_texts(self, *args):
        lang = self.lang_var.get()
        t = TEXTS.get(lang, TEXTS["Español"])
        
        self.root.title(t["title"])
        self.lf_blocks.configure(text=t["blocks_title"])
        self.lf_results.configure(text=t["results_title"])
        self.lf_console.configure(text=t["console_title"])
        self.lf_reverse.configure(text=t["reverse_title"])
        self.lbl_unit.configure(text=t["unit_label"])
        self.lbl_val.configure(text=t["value_label"])
        self.lbl_large_unit.configure(text=t["large_unit"])
        self.lbl_lang.configure(text=t["lang_label"])
        
        self.menubar.entryconfig(1, label=t["menu_help"])
        self.help_menu.entryconfig(0, label=t["menu_help"])
        
        self.calculate_from_blocks()
        self.calculate_to_blocks()

    def get_block_size_bytes(self):
        if self.console_var.get() == "GameCube":
            return 32 * 1024
        else:
            return 128 * 1024

    def calculate_from_blocks(self, event=None):
        val_str = self.blocks_input_var.get().strip()
        lang = self.lang_var.get()
        err_msg = TEXTS[lang]["error"]
        large_unit = self.large_unit_var.get()

        if not val_str:
            self.kb_var.set("KB: 0.00")
            self.mb_var.set("MB: 0.00")
            self.gb_var.set("GB: 0.00")
            self.large_var.set(f"{large_unit}: 0.00")
            return

        try:
            blocks = float(val_str)
            if blocks < 0:
                raise ValueError()
            
            block_size_bytes = self.get_block_size_bytes()
            total_bytes = blocks * block_size_bytes
            
            kb = total_bytes / 1024
            mb = kb / 1024
            gb = mb / 1024
            
            if large_unit == "TB":
                large_val = gb / 1024
            elif large_unit == "PB":
                large_val = (gb / 1024) / 1024
            else:
                large_val = ((gb / 1024) / 1024) / 1024

            self.kb_var.set(f"KB: {kb:,.2f}")
            self.mb_var.set(f"MB: {mb:,.2f}")
            self.gb_var.set(f"GB: {gb:,.2f}")
            self.large_var.set(f"{large_unit}: {large_val:,.2f}")
            
        except ValueError:
            self.kb_var.set(err_msg)
            self.mb_var.set("")
            self.gb_var.set("")
            self.large_var.set("")

    def calculate_to_blocks(self, event=None):
        val_str = self.reverse_input_var.get().strip()
        unit = self.reverse_unit_var.get()
        lang = self.lang_var.get()
        t = TEXTS[lang]

        if not val_str:
            self.reverse_result_var.set(f"{t['result_blocks']} 0")
            return

        try:
            val = float(val_str)
            if val < 0:
                raise ValueError()

            multipliers = {
                "Bytes": 1,
                "KB": 1024,
                "MB": 1024**2,
                "GB": 1024**3,
                "TB": 1024**4,
                "PB": 1024**5,
                "EB": 1024**6
            }

            total_bytes = val * multipliers.get(unit, 1)
            block_size_bytes = self.get_block_size_bytes()
            blocks = total_bytes / block_size_bytes

            self.reverse_result_var.set(f"{t['result_blocks']} {blocks:,.2f}")

        except ValueError:
            self.reverse_result_var.set(t["error"])

if __name__ == "__main__":
    root = tk.Tk()
    app = NintendoConverterApp(root)
    root.mainloop()
