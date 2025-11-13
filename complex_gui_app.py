import tkinter as tk
from tkinter import ttk
import time
import math


class AnimationEngine:
    def __init__(self, root):
        self.root = root
        self.animations = []
    
    def ease_in_out_cubic(self, t):
        if t < 0.5:
            return 4 * t * t * t
        else:
            return 1 - pow(-2 * t + 2, 3) / 2
    
    def animate(self, duration, callback, on_complete=None):
        start_time = time.time()
        
        def step():
            elapsed = time.time() - start_time
            progress = min(elapsed / duration, 1.0)
            eased_progress = self.ease_in_out_cubic(progress)
            
            callback(eased_progress)
            
            if progress < 1.0:
                self.root.after(16, step)
            else:
                if on_complete:
                    on_complete()
        
        step()


class SidebarMenuItem:
    def __init__(self, parent, text, icon, command, animation_engine):
        self.parent = parent
        self.text = text
        self.icon = icon
        self.command = command
        self.animation_engine = animation_engine
        self.is_active = False
        self.is_hovered = False
        self.current_color = "#2c3e50"
        self.hover_color = "#34495e"
        self.active_color = "#3498db"
        
        self.frame = tk.Frame(parent, bg=self.current_color, cursor="hand2")
        self.frame.pack(fill=tk.X, pady=2)
        
        self.icon_label = tk.Label(
            self.frame,
            text=self.icon,
            font=("Arial", 16),
            bg=self.current_color,
            fg="white",
            width=3
        )
        self.icon_label.pack(side=tk.LEFT, padx=(10, 5), pady=10)
        
        self.text_label = tk.Label(
            self.frame,
            text=self.text,
            font=("Arial", 11),
            bg=self.current_color,
            fg="white",
            anchor="w"
        )
        self.text_label.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=10)
        
        self.frame.bind("<Button-1>", self.on_click)
        self.icon_label.bind("<Button-1>", self.on_click)
        self.text_label.bind("<Button-1>", self.on_click)
        
        self.frame.bind("<Enter>", self.on_enter)
        self.frame.bind("<Leave>", self.on_leave)
        self.icon_label.bind("<Enter>", self.on_enter)
        self.icon_label.bind("<Leave>", self.on_leave)
        self.text_label.bind("<Enter>", self.on_enter)
        self.text_label.bind("<Leave>", self.on_leave)
    
    def on_click(self, event):
        if self.command:
            self.command()
    
    def on_enter(self, event):
        if not self.is_active:
            self.is_hovered = True
            self.animate_color(self.hover_color)
    
    def on_leave(self, event):
        if not self.is_active:
            self.is_hovered = False
            self.animate_color(self.current_color if not self.is_active else self.active_color)
    
    def set_active(self, active):
        self.is_active = active
        target_color = self.active_color if active else self.current_color
        self.animate_color(target_color)
    
    def animate_color(self, target_color):
        start_color = self.get_current_bg()
        
        def interpolate_color(progress):
            r1, g1, b1 = self.hex_to_rgb(start_color)
            r2, g2, b2 = self.hex_to_rgb(target_color)
            
            r = int(r1 + (r2 - r1) * progress)
            g = int(g1 + (g2 - g1) * progress)
            b = int(b1 + (b2 - b1) * progress)
            
            color = self.rgb_to_hex(r, g, b)
            self.frame.config(bg=color)
            self.icon_label.config(bg=color)
            self.text_label.config(bg=color)
        
        self.animation_engine.animate(0.2, interpolate_color)
    
    def get_current_bg(self):
        return self.frame.cget("bg")
    
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def rgb_to_hex(self, r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def hide_text(self):
        self.text_label.pack_forget()
    
    def show_text(self):
        self.text_label.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=10)


class Sidebar:
    def __init__(self, parent, animation_engine, on_navigate):
        self.parent = parent
        self.animation_engine = animation_engine
        self.on_navigate = on_navigate
        self.is_expanded = True
        self.expanded_width = 220
        self.collapsed_width = 60
        self.current_width = self.expanded_width
        
        self.frame = tk.Frame(parent, bg="#2c3e50", width=self.expanded_width)
        self.frame.pack(side=tk.LEFT, fill=tk.Y)
        self.frame.pack_propagate(False)
        
        self.header = tk.Frame(self.frame, bg="#1a252f", height=60)
        self.header.pack(fill=tk.X)
        self.header.pack_propagate(False)
        
        self.toggle_btn = tk.Button(
            self.header,
            text="☰",
            font=("Arial", 20),
            bg="#1a252f",
            fg="white",
            bd=0,
            cursor="hand2",
            command=self.toggle
        )
        self.toggle_btn.pack(side=tk.LEFT, padx=15, pady=15)
        
        self.title_label = tk.Label(
            self.header,
            text="Menu",
            font=("Arial", 14, "bold"),
            bg="#1a252f",
            fg="white"
        )
        self.title_label.pack(side=tk.LEFT, padx=10)
        
        self.menu_frame = tk.Frame(self.frame, bg="#2c3e50")
        self.menu_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        self.menu_items = []
        self.create_menu_items()
    
    def create_menu_items(self):
        menu_data = [
            ("Home", "🏠", "home"),
            ("Dashboard", "📊", "dashboard"),
            ("Settings", "⚙️", "settings"),
            ("About", "ℹ️", "about")
        ]
        
        for text, icon, page in menu_data:
            item = SidebarMenuItem(
                self.menu_frame,
                text,
                icon,
                lambda p=page: self.navigate_to(p),
                self.animation_engine
            )
            self.menu_items.append(item)
        
        self.menu_items[0].set_active(True)
    
    def navigate_to(self, page):
        for item in self.menu_items:
            item.set_active(False)
        
        for item in self.menu_items:
            if item.text.lower() == page:
                item.set_active(True)
                break
        
        if self.on_navigate:
            self.on_navigate(page)
    
    def toggle(self):
        self.is_expanded = not self.is_expanded
        target_width = self.expanded_width if self.is_expanded else self.collapsed_width
        start_width = self.current_width
        
        def update_width(progress):
            self.current_width = int(start_width + (target_width - start_width) * progress)
            self.frame.config(width=self.current_width)
        
        def on_complete():
            if not self.is_expanded:
                for item in self.menu_items:
                    item.hide_text()
                self.title_label.pack_forget()
            else:
                self.title_label.pack(side=tk.LEFT, padx=10)
                for item in self.menu_items:
                    item.show_text()
        
        if self.is_expanded:
            on_complete()
        
        self.animation_engine.animate(0.3, update_width, on_complete if not self.is_expanded else None)


class BaseView:
    def __init__(self, parent, animation_engine):
        self.parent = parent
        self.animation_engine = animation_engine
        self.frame = tk.Frame(parent, bg="#ecf0f1")
        self.opacity = 0.0
        self.setup_ui()
    
    def setup_ui(self):
        pass
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.fade_in()
    
    def hide(self, callback=None):
        self.fade_out(lambda: self.complete_hide(callback))
    
    def complete_hide(self, callback):
        self.frame.pack_forget()
        if callback:
            callback()
    
    def fade_in(self):
        def update_opacity(progress):
            self.opacity = progress
            alpha = int(255 * progress)
            color = f'#{alpha:02x}{alpha:02x}{alpha:02x}'
        
        self.animation_engine.animate(0.3, update_opacity)
    
    def fade_out(self, callback=None):
        def update_opacity(progress):
            self.opacity = 1.0 - progress
        
        self.animation_engine.animate(0.2, update_opacity, callback)


class HomeView(BaseView):
    def setup_ui(self):
        header = tk.Frame(self.frame, bg="#3498db", height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(
            header,
            text="🏠 Welcome Home",
            font=("Arial", 24, "bold"),
            bg="#3498db",
            fg="white"
        )
        title.pack(pady=20)
        
        content = tk.Frame(self.frame, bg="#ecf0f1")
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        welcome_card = tk.Frame(content, bg="white", relief=tk.RAISED, bd=2)
        welcome_card.pack(fill=tk.BOTH, expand=True)
        
        card_title = tk.Label(
            welcome_card,
            text="Welcome to the Complex GUI Application",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        card_title.pack(pady=(30, 10))
        
        description = tk.Label(
            welcome_card,
            text="This application demonstrates advanced tkinter features including:\n\n"
                 "• Collapsible sidebar with smooth animations\n"
                 "• Multiple page navigation\n"
                 "• Fade transitions between views\n"
                 "• Hover effects with color animations\n"
                 "• Responsive layout design\n\n"
                 "Use the sidebar menu to navigate between different pages.",
            font=("Arial", 12),
            bg="white",
            fg="#34495e",
            justify=tk.LEFT
        )
        description.pack(pady=20, padx=40)
        
        button_frame = tk.Frame(welcome_card, bg="white")
        button_frame.pack(pady=30)
        
        explore_btn = tk.Button(
            button_frame,
            text="Explore Dashboard",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            bd=0,
            command=lambda: self.parent.master.navigate_to_page("dashboard")
        )
        explore_btn.pack()


class DashboardView(BaseView):
    def setup_ui(self):
        header = tk.Frame(self.frame, bg="#2ecc71", height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(
            header,
            text="📊 Dashboard",
            font=("Arial", 24, "bold"),
            bg="#2ecc71",
            fg="white"
        )
        title.pack(pady=20)
        
        content = tk.Frame(self.frame, bg="#ecf0f1")
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        stats_frame = tk.Frame(content, bg="#ecf0f1")
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.create_stat_card(stats_frame, "Total Users", "1,234", "#3498db", 0)
        self.create_stat_card(stats_frame, "Active Sessions", "89", "#2ecc71", 1)
        self.create_stat_card(stats_frame, "Revenue", "$12.5K", "#f39c12", 2)
        
        chart_frame = tk.Frame(content, bg="white", relief=tk.RAISED, bd=2)
        chart_frame.pack(fill=tk.BOTH, expand=True)
        
        chart_title = tk.Label(
            chart_frame,
            text="Activity Chart",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        chart_title.pack(pady=(20, 10))
        
        canvas = tk.Canvas(chart_frame, bg="white", height=300, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True, padx=30, pady=(10, 30))
        
        self.draw_simple_chart(canvas)
    
    def create_stat_card(self, parent, title, value, color, column):
        card = tk.Frame(parent, bg="white", relief=tk.RAISED, bd=2)
        card.grid(row=0, column=column, padx=10, sticky="ew")
        parent.grid_columnconfigure(column, weight=1)
        
        icon_frame = tk.Frame(card, bg=color, width=60, height=60)
        icon_frame.pack(pady=(20, 10))
        icon_frame.pack_propagate(False)
        
        icon_label = tk.Label(icon_frame, text="📈", font=("Arial", 24), bg=color)
        icon_label.pack(expand=True)
        
        value_label = tk.Label(
            card,
            text=value,
            font=("Arial", 24, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        value_label.pack()
        
        title_label = tk.Label(
            card,
            text=title,
            font=("Arial", 11),
            bg="white",
            fg="#7f8c8d"
        )
        title_label.pack(pady=(5, 20))
    
    def draw_simple_chart(self, canvas):
        canvas.update_idletasks()
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        
        if width <= 1:
            width = 600
        if height <= 1:
            height = 300
        
        data = [30, 50, 40, 70, 60, 80, 75, 90, 85, 95]
        
        margin = 40
        chart_width = width - 2 * margin
        chart_height = height - 2 * margin
        
        canvas.create_line(margin, height - margin, width - margin, height - margin, fill="#bdc3c7", width=2)
        canvas.create_line(margin, margin, margin, height - margin, fill="#bdc3c7", width=2)
        
        max_value = max(data)
        bar_width = chart_width / len(data) * 0.7
        spacing = chart_width / len(data)
        
        for i, value in enumerate(data):
            x = margin + i * spacing + spacing / 2
            bar_height = (value / max_value) * chart_height
            y = height - margin - bar_height
            
            canvas.create_rectangle(
                x - bar_width / 2, y,
                x + bar_width / 2, height - margin,
                fill="#3498db",
                outline="#2980b9",
                width=2
            )


class SettingsView(BaseView):
    def setup_ui(self):
        header = tk.Frame(self.frame, bg="#9b59b6", height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(
            header,
            text="⚙️ Settings",
            font=("Arial", 24, "bold"),
            bg="#9b59b6",
            fg="white"
        )
        title.pack(pady=20)
        
        content = tk.Frame(self.frame, bg="#ecf0f1")
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        settings_card = tk.Frame(content, bg="white", relief=tk.RAISED, bd=2)
        settings_card.pack(fill=tk.BOTH, expand=True)
        
        settings_content = tk.Frame(settings_card, bg="white")
        settings_content.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        self.create_setting_item(settings_content, "Enable Notifications", True, 0)
        self.create_setting_item(settings_content, "Dark Mode", False, 1)
        self.create_setting_item(settings_content, "Auto-Save", True, 2)
        self.create_setting_item(settings_content, "Sound Effects", False, 3)
        
        divider = tk.Frame(settings_content, bg="#ecf0f1", height=2)
        divider.pack(fill=tk.X, pady=20)
        
        profile_label = tk.Label(
            settings_content,
            text="Profile Settings",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        profile_label.pack(anchor="w", pady=(10, 20))
        
        self.create_input_field(settings_content, "Username:", "john_doe")
        self.create_input_field(settings_content, "Email:", "john@example.com")
        
        button_frame = tk.Frame(settings_content, bg="white")
        button_frame.pack(pady=(30, 0))
        
        save_btn = tk.Button(
            button_frame,
            text="Save Changes",
            font=("Arial", 12, "bold"),
            bg="#2ecc71",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            bd=0
        )
        save_btn.pack(side=tk.LEFT, padx=5)
        
        reset_btn = tk.Button(
            button_frame,
            text="Reset",
            font=("Arial", 12),
            bg="#95a5a6",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            bd=0
        )
        reset_btn.pack(side=tk.LEFT, padx=5)
    
    def create_setting_item(self, parent, text, default_value, row):
        item_frame = tk.Frame(parent, bg="white")
        item_frame.pack(fill=tk.X, pady=10)
        
        label = tk.Label(
            item_frame,
            text=text,
            font=("Arial", 12),
            bg="white",
            fg="#2c3e50"
        )
        label.pack(side=tk.LEFT)
        
        var = tk.BooleanVar(value=default_value)
        checkbox = tk.Checkbutton(
            item_frame,
            variable=var,
            bg="white",
            cursor="hand2"
        )
        checkbox.pack(side=tk.RIGHT)
    
    def create_input_field(self, parent, label_text, default_value):
        field_frame = tk.Frame(parent, bg="white")
        field_frame.pack(fill=tk.X, pady=10)
        
        label = tk.Label(
            field_frame,
            text=label_text,
            font=("Arial", 11),
            bg="white",
            fg="#7f8c8d",
            width=15,
            anchor="w"
        )
        label.pack(side=tk.LEFT)
        
        entry = tk.Entry(
            field_frame,
            font=("Arial", 11),
            bg="#ecf0f1",
            relief=tk.FLAT,
            bd=5
        )
        entry.insert(0, default_value)
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True)


class AboutView(BaseView):
    def setup_ui(self):
        header = tk.Frame(self.frame, bg="#e74c3c", height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(
            header,
            text="ℹ️ About",
            font=("Arial", 24, "bold"),
            bg="#e74c3c",
            fg="white"
        )
        title.pack(pady=20)
        
        content = tk.Frame(self.frame, bg="#ecf0f1")
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        about_card = tk.Frame(content, bg="white", relief=tk.RAISED, bd=2)
        about_card.pack(fill=tk.BOTH, expand=True)
        
        about_content = tk.Frame(about_card, bg="white")
        about_content.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        app_title = tk.Label(
            about_content,
            text="Complex GUI Application",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        app_title.pack(pady=(0, 10))
        
        version = tk.Label(
            about_content,
            text="Version 1.0.0",
            font=("Arial", 11),
            bg="white",
            fg="#7f8c8d"
        )
        version.pack(pady=(0, 30))
        
        description = tk.Label(
            about_content,
            text="This is a demonstration of advanced tkinter GUI development\n"
                 "featuring smooth animations, responsive design, and modern UI patterns.\n\n"
                 "Built with Python and tkinter, this application showcases:\n\n"
                 "• Custom animation engine with easing functions\n"
                 "• Collapsible sidebar navigation\n"
                 "• Multiple view management\n"
                 "• Smooth transitions and hover effects\n"
                 "• Responsive layout that adapts to window resizing\n"
                 "• Clean, modern design principles\n\n"
                 "Technologies Used:\n"
                 "• Python 3.x\n"
                 "• tkinter (standard library)\n"
                 "• Custom animation framework\n\n",
            font=("Arial", 11),
            bg="white",
            fg="#34495e",
            justify=tk.LEFT
        )
        description.pack(pady=20)
        
        footer = tk.Label(
            about_content,
            text="© 2024 Complex GUI Application. All rights reserved.",
            font=("Arial", 9),
            bg="white",
            fg="#95a5a6"
        )
        footer.pack(side=tk.BOTTOM, pady=(20, 0))


class ComplexGUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Complex GUI Application")
        self.root.geometry("1200x700")
        self.root.minsize(800, 500)
        
        self.root.configure(bg="#ecf0f1")
        
        self.animation_engine = AnimationEngine(self.root)
        
        self.main_container = tk.Frame(self.root, bg="#ecf0f1")
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        self.sidebar = Sidebar(self.main_container, self.animation_engine, self.navigate_to_page)
        
        self.content_area = tk.Frame(self.main_container, bg="#ecf0f1")
        self.content_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.views = {
            "home": HomeView(self.content_area, self.animation_engine),
            "dashboard": DashboardView(self.content_area, self.animation_engine),
            "settings": SettingsView(self.content_area, self.animation_engine),
            "about": AboutView(self.content_area, self.animation_engine)
        }
        
        self.current_view = None
        self.navigate_to_page("home")
        
        self.root.bind("<Configure>", self.on_window_resize)
    
    def navigate_to_page(self, page_name):
        if page_name not in self.views:
            return
        
        new_view = self.views[page_name]
        
        if self.current_view == new_view:
            return
        
        if self.current_view:
            self.current_view.hide(lambda: new_view.show())
        else:
            new_view.show()
        
        self.current_view = new_view
    
    def on_window_resize(self, event):
        pass


def main():
    root = tk.Tk()
    app = ComplexGUIApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
