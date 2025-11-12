import sys

try:
    import tkinter as tk
    from tkinter import messagebox, ttk
    print("✓ tkinter imports successful")
    
    import gui_app
    print("✓ gui_app module imports successful")
    
    print("✓ SimpleFormApp class available:", hasattr(gui_app, 'SimpleFormApp'))
    print("✓ main function available:", hasattr(gui_app, 'main'))
    
    print("\nAll imports and basic checks passed!")
    print("The GUI application is ready to run.")
    print("\nTo launch the GUI, run: python3 gui_app.py")
    
    sys.exit(0)
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Unexpected error: {e}")
    sys.exit(1)
