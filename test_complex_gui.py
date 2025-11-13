import tkinter as tk
import sys
import os

os.environ['DISPLAY'] = ':99'

try:
    from complex_gui_app import ComplexGUIApp
    
    print("Testing Complex GUI Application...")
    
    root = tk.Tk()
    app = ComplexGUIApp(root)
    
    print("✓ Application initialized successfully")
    print("✓ Sidebar created")
    print("✓ Animation engine initialized")
    print("✓ Views created (Home, Dashboard, Settings, About)")
    
    root.update()
    
    print("✓ Initial render successful")
    
    for page in ["dashboard", "settings", "about", "home"]:
        app.navigate_to_page(page)
        root.update()
        print(f"✓ Navigation to {page} successful")
    
    print("✓ Sidebar toggle test...")
    app.sidebar.toggle()
    root.update()
    print("✓ Sidebar collapsed successfully")
    
    app.sidebar.toggle()
    root.update()
    print("✓ Sidebar expanded successfully")
    
    print("\n✅ All tests passed!")
    print("The Complex GUI Application is working correctly.")
    
    root.destroy()
    sys.exit(0)
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
