import os
import shutil



def copy_dir(src, dist, first_call=True):
    if first_call:
        if os.path.exists(dist):
            print(f"removing: {dist}")
            shutil.rmtree(dist)
        os.makedirs(dist, exist_ok=True)

    if not os.path.exists(src):
        raise FileNotFoundError(f"Trying to copy from a non existing directory: {src}")

    files = os.listdir(src)
    for file in files:
        src_path = os.path.join(src, file)
        dist_path = os.path.join(dist, file)

        if os.path.isfile(src_path):
            print(f"copying file: {src_path} -> {dist_path}")
            shutil.copy(src_path, dist_path)
        else:
            # directory
            print(f"copying directory: {src_path} -> {dist_path}")
            os.makedirs(dist_path, exist_ok=True)
            copy_dir(src_path, dist_path, first_call=False)



