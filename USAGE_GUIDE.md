# Complex GUI Application - Usage Guide

This guide provides detailed information on how to use and understand the Complex GUI Application.

## Getting Started

### Running the Application

```bash
python3 complex_gui_app.py
```

The application will open in a 1200x700 window with a sidebar on the left and the Home page displayed.

## User Interface Overview

### Sidebar

The sidebar is located on the left side of the application and provides navigation to different pages.

**Components:**
- **Toggle Button (☰)**: Click to collapse/expand the sidebar
- **Menu Items**: Four navigation options with icons
  - 🏠 Home
  - 📊 Dashboard
  - ⚙️ Settings
  - ℹ️ About

**States:**
- **Expanded**: 220px width, shows icons and text labels
- **Collapsed**: 60px width, shows only icons

### Main Content Area

The main content area displays the currently selected page and adapts to the available space.

## Pages

### 1. Home Page

The Home page provides a welcome message and overview of the application features.

**Features:**
- Welcome message
- Feature list
- "Explore Dashboard" button for quick navigation

### 2. Dashboard Page

The Dashboard displays statistics and visual data representation.

**Features:**
- Three statistic cards showing:
  - Total Users
  - Active Sessions
  - Revenue
- Interactive bar chart with sample data
- Clean, modern layout

### 3. Settings Page

The Settings page allows you to configure application preferences.

**Features:**
- Toggle switches for:
  - Enable Notifications
  - Dark Mode
  - Auto-Save
  - Sound Effects
- Profile settings:
  - Username field
  - Email field
- Action buttons:
  - Save Changes
  - Reset

### 4. About Page

The About page provides information about the application.

**Features:**
- Application name and version
- Feature description
- Technology stack information
- Copyright notice

## Interactions

### Navigation

1. **Click on Menu Items**: Click any menu item in the sidebar to navigate to that page
2. **Active State**: The currently active page is highlighted in blue
3. **Hover Effects**: Menu items change color when you hover over them

### Sidebar Toggle

1. Click the hamburger menu icon (☰) in the sidebar header
2. The sidebar will smoothly animate to its collapsed or expanded state
3. In collapsed state, only icons are visible
4. In expanded state, both icons and text labels are shown

### Page Transitions

1. When navigating between pages, the current page fades out
2. The new page then fades in
3. All transitions are smooth and animated

## Animations

The application features several types of animations:

### Sidebar Animation
- **Duration**: 300ms
- **Easing**: Cubic ease-in-out
- **Property**: Width (220px ↔ 60px)

### View Transitions
- **Fade Out Duration**: 200ms
- **Fade In Duration**: 300ms
- **Easing**: Cubic ease-in-out

### Hover Effects
- **Duration**: 200ms
- **Easing**: Cubic ease-in-out
- **Property**: Background color

## Keyboard Shortcuts

Currently, the application primarily uses mouse interactions. Keyboard navigation could be added in future versions.

## Window Management

### Resizing

The application supports window resizing:
- **Minimum Size**: 800x500 pixels
- **Default Size**: 1200x700 pixels
- The layout adapts automatically to window size changes

### Responsive Behavior

- Content areas expand/contract with window size
- Cards and components maintain proper spacing
- Text remains readable at different sizes

## Technical Notes

### Animation Engine

The application uses a custom animation engine that:
- Runs at approximately 60 FPS (16ms frame updates)
- Uses cubic ease-in-out easing for smooth, natural motion
- Supports callbacks for animation completion
- Can handle multiple concurrent animations

### Performance

The application is designed for smooth performance:
- Efficient widget updates
- Optimized animation loops
- Minimal resource usage
- Clean memory management

## Troubleshooting

### Application Won't Start

**Problem**: `ModuleNotFoundError: No module named 'tkinter'`

**Solution**:
```bash
# On Ubuntu/Debian
sudo apt-get install python3-tk

# On Fedora
sudo dnf install python3-tkinter

# On macOS
# tkinter comes with Python, no action needed

# On Windows
# tkinter comes with Python, no action needed
```

### Display Issues on Linux

**Problem**: Application doesn't show or crashes on headless systems

**Solution**: Use a virtual display
```bash
export DISPLAY=:99
Xvfb :99 -screen 0 1024x768x24 &
python3 complex_gui_app.py
```

### Animations Are Choppy

**Possible Causes**:
- System under heavy load
- Outdated graphics drivers
- Running on a virtual machine

**Solutions**:
- Close unnecessary applications
- Update graphics drivers
- Run on native hardware if possible

## Customization

### Changing Colors

Colors are defined inline in the code. Key colors:

```python
# Sidebar
sidebar_bg = "#2c3e50"
sidebar_header = "#1a252f"

# Menu Items
menu_normal = "#2c3e50"
menu_hover = "#34495e"
menu_active = "#3498db"

# Page Headers
home_color = "#3498db"
dashboard_color = "#2ecc71"
settings_color = "#9b59b6"
about_color = "#e74c3c"
```

### Adding New Pages

To add a new page:

1. Create a new view class inheriting from `BaseView`
2. Implement the `setup_ui` method
3. Add the view to the `views` dictionary in `ComplexGUIApp`
4. Add a new menu item in the `Sidebar.create_menu_items` method

### Modifying Animations

Animation parameters can be adjusted:

```python
# Sidebar toggle duration
self.animation_engine.animate(0.3, ...)  # Change 0.3 to desired seconds

# View fade duration
self.animation_engine.animate(0.3, ...)  # Fade in
self.animation_engine.animate(0.2, ...)  # Fade out
```

## Best Practices

1. **Navigation**: Use the sidebar for all navigation
2. **Testing**: Run the demo script to verify functionality
3. **Customization**: Modify colors and styles to match your preferences
4. **Performance**: Avoid running heavy operations during animations

## Support

For issues, questions, or contributions:
- Check the README.md for general information
- Run `python3 demo_complex_gui.py` to verify installation
- Review the code comments for technical details

## Future Enhancements

Potential features for future versions:
- Keyboard navigation support
- Additional page types
- More animation options
- Theme switching (dark/light mode)
- User preferences persistence
- More interactive components
- Touch screen support
