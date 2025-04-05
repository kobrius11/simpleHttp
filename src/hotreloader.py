import os
import sys
import threading


class HotReloader():
    def __init__(self):
        pass

    def get_make_time(self):
        """Get the make time of the file."""
        mtimes = []
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    mtime = os.path.getmtime(filepath)
                    mtimes.append(mtime)
        return max(mtimes) if mtimes else 0
    
    def check_for_changes(self, last_mtime):
        """Check if any .py file has been modified since last_mtime."""
        current_mtime = self.get_make_time()
        if current_mtime > last_mtime:
            return True
        return False
    
    def start(self, run_server):
        last_mtime = self.get_make_time()
        def reload():
            """Reload the application."""
            print("Reloading application...")
            while True:
                
                if self.check_for_changes(last_mtime):
                    print("Changes detected, reloading...")
                    os.execv(sys.executable, [sys.executable] + sys.argv)

        threading.Thread(target=reload, daemon=True).start()
        
        try:
            run_server()
        except KeyboardInterrupt:
            print("\n Server interrupted. Shutting down.")
            sys.exit(0)