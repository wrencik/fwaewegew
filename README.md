# Python GUI Applications

This repository contains multiple Python GUI applications built with tkinter, demonstrating various levels of complexity from basic form handling to advanced animations and responsive design.

## Applications

### 1. Simple Form Application (`gui_app.py`)

A simple and clean Python GUI application that demonstrates basic form handling and user interaction.

**Features:**
- User Information Form: Collect user details (name, email, age)
- Calculator: Perform basic arithmetic operations on two numbers
- Input Validation: Validates user input with helpful error messages
- Clean Interface: Modern, user-friendly interface with organized layout
- Result Display: Shows results in a dedicated text area

### 2. Complex GUI Application (`complex_gui_app.py`)

An advanced GUI application showcasing modern UI patterns, smooth animations, and responsive design.

**Features:**
- **Collapsible Sidebar**: Expandable/collapsible navigation menu with smooth animations
- **Multiple Views**: Navigate between Home, Dashboard, Settings, and About pages
- **Smooth Animations**: Custom animation engine with easing functions
  - Sidebar collapse/expand animations
  - Fade-in/fade-out view transitions
  - Hover effects with color transitions
- **Interactive Dashboard**: Visual data representation with charts and statistics
- **Responsive Layout**: Adapts to window resizing
- **Modern Design**: Clean, professional interface with card-based layouts

## Requirements

- Python 3.x
- tkinter (included with standard Python installation)

## Installation

No installation required! tkinter comes bundled with Python.

On Linux systems, if tkinter is not installed:
```bash
sudo apt-get install python3-tk
```

## Usage

### Run the Simple Form Application:

```bash
python gui_app.py
```

Or on some systems:

```bash
python3 gui_app.py
```

### Run the Complex GUI Application:

```bash
python complex_gui_app.py
```

Or on some systems:

```bash
python3 complex_gui_app.py
```

## Simple Form Application Features

### Form Submission
1. Enter your full name
2. Enter your email address
3. Enter your age
4. Click "Submit Form" to see a summary with age category classification

### Calculator
1. Enter two numbers in the "Number 1" and "Number 2" fields
2. Click "Calculate Sum" to see arithmetic operations (sum, difference, product, division)

### Clear All
Click "Clear All" to reset all input fields and results

### Validation
- All form fields are required
- Age must be a valid number between 0-150
- Calculator requires valid numeric inputs
- Division by zero is handled gracefully

## Complex GUI Application Features

### Navigation
- Use the sidebar menu to navigate between different pages
- Click the hamburger menu icon (☰) to collapse/expand the sidebar
- Enjoy smooth animations during navigation

### Pages
- **Home**: Welcome screen with application overview
- **Dashboard**: Interactive statistics and charts
- **Settings**: Configuration options and profile settings
- **About**: Application information and credits

### Animations
- Sidebar smoothly animates between expanded (220px) and collapsed (60px) states
- View transitions feature fade-in/fade-out effects
- Menu items have hover effects with smooth color transitions
- All animations use cubic easing for natural motion

## Technical Details

### Complex GUI Architecture

The complex GUI application is built with a clean, modular architecture:

- **AnimationEngine**: Manages time-based animations with easing functions
- **Sidebar**: Collapsible navigation menu with animated menu items
- **SidebarMenuItem**: Individual menu items with hover effects
- **BaseView**: Abstract base class for all page views
- **View Classes**: HomeView, DashboardView, SettingsView, AboutView
- **ComplexGUIApp**: Main application orchestrator

### Animation System

The custom animation engine supports:
- Cubic ease-in-out easing function for smooth, natural animations
- Time-based progress tracking (16ms frame rate targeting ~60 FPS)
- Callback support for animation completion
- Multiple concurrent animations

### Responsive Design

The application handles window resizing gracefully:
- Flexible layouts using pack and grid geometry managers
- Minimum window size constraints
- Content adapts to available space
- Maintains visual hierarchy at different sizes

## Testing

Run the test suite for the complex GUI:

```bash
python3 test_complex_gui.py
```

This will verify:
- Application initialization
- View creation and navigation
- Sidebar functionality
- Animation system

## License

This is a demonstration project for educational purposes.
