import os
import zipfile

def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            # Exclude some unnecessary folders if they exist
            if '.git' in dirs:
                dirs.remove('.git')
            
            for file in files:
                # Do not zip the zip file itself and python scripts to keep it clean
                if file == 'voz-direita.zip' or file.endswith('.py'):
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

if __name__ == '__main__':
    zip_directory('.', 'voz-direita.zip')
    print("voz-direita.zip has been successfully created.")
