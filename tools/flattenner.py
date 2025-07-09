import os
import shutil
import sys

def flatten_directory(root_dir, remove_empty_dirs=True):
    if not os.path.isdir(root_dir):
        print(f"{root_dir} is not a valid directory path.")
        return

    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        if dirpath == root_dir:
            continue
        for filename in filenames:
            src_path = os.path.join(dirpath, filename)
            dst_path = os.path.join(root_dir, filename)

            if os.path.exists(dst_path):
                base, ext = os.path.splitext(filename)
                count = 1
                while True:
                    new_name = f"{base}_{count}{ext}"
                    new_dst_path = os.path.join(root_dir, new_name)
                    if not os.path.exists(new_dst_path):
                        dst_path = new_dst_path
                        break
                    count += 1
            
            shutil.move(src_path, dst_path)
            print(f"Moved: {src_path} -> {dst_path}")

        if remove_empty_dirs:
            try:
                os.rmdir(dirpath)
                print(f"Removed empty dir: {dirpath}")
            except OSError:
                pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python flatten.py <directory path>")
        sys.exit(1)

    root_directory = sys.argv[1]
    rm_dir = sys.argv[2]
    if rm_dir == "normdir":
        flatten_directory(root_directory, False)
    else:
        flatten_directory(root_directory)
