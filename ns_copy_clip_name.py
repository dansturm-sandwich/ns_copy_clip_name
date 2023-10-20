import os
import hiero


def copy_clip_name():
    sequence = hiero.ui.activeSequence()
    selection = hiero.ui.getTimelineEditor(sequence).selection()
    name_to_copy = selection[0].name()

    # Determine the platform
    platform = os.name

    # Copy to clipboard based on the platform
    if platform == 'posix':  # Linux or macOS
        os.system(f"echo '{name_to_copy}' | pbcopy")
    elif platform == 'nt':  # Windows
        os.system(f"echo {name_to_copy} | clip")
    else:
        print("Unsupported platform")
