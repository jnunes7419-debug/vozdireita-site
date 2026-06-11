import os
import glob
from PIL import Image

def main():
    assets_dir = r"D:\direita_intelectual\assets"
    project_dir = r"D:\direita_intelectual"
    
    # 1. Converter imagens para WebP
    converted_files = {} # old_name -> new_name
    
    # Encontrar imagens
    for ext in ['*.png', '*.jpg', '*.jpeg']:
        for img_path in glob.glob(os.path.join(assets_dir, ext)):
            filename = os.path.basename(img_path)
            name, old_ext = os.path.splitext(filename)
            webp_filename = name + ".webp"
            webp_path = os.path.join(assets_dir, webp_filename)
            
            # Converter
            try:
                with Image.open(img_path) as img:
                    # Redimensionar se for gigantesca (largura > 1600px)
                    if img.width > 1600:
                        ratio = 1600 / img.width
                        new_h = int(img.height * ratio)
                        img = img.resize((1600, new_h), Image.Resampling.LANCZOS)
                        
                    # Converter para RGB se for necessário (Pillow não salva RGBA em JPG, mas salva em WEBP. Porém, WEBP suporta alpha)
                    img.save(webp_path, 'webp', optimize=True, quality=80)
                
                converted_files[filename] = webp_filename
                
                # Excluir a original para economizar espaço
                os.remove(img_path)
                print(f"Converted {filename} to {webp_filename}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

    # 2. Atualizar todos os HTMLs
    for html_path in glob.glob(os.path.join(project_dir, '*.html')):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        for old_name, new_name in converted_files.items():
            if old_name in content:
                content = content.replace(old_name, new_name)
                modified = True
                
        if modified:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated HTML: {os.path.basename(html_path)}")

if __name__ == "__main__":
    main()
