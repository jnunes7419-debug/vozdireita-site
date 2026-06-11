import os

total_size = 0
img_count = 0
for root, dirs, files in os.walk(r'D:\direita_intelectual\assets'):
    for file in files:
        if file.lower().endswith(('.webp')):
            size = os.path.getsize(os.path.join(root, file)) / 1024
            total_size += size
            img_count += 1
            if size > 100:
                print(f'{file}: {size:.2f} KB')
print(f'Total: {img_count} images, {total_size:.2f} KB')
