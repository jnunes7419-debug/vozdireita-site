import re

def main():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The issue is the double quotes inside the x-data attribute
    # desc: 'Como a mídia legitima o terrorismo sob disfarce de "apelo à paz".'
    # We will replace those double quotes with &quot;
    
    # Or just replace the specific string
    old_string = 'desc: \'Como a mídia legitima o terrorismo sob disfarce de "apelo à paz".\''
    new_string = 'desc: \'Como a mídia legitima o terrorismo sob disfarce de &quot;apelo à paz&quot;.\''
    
    if old_string in content:
        content = content.replace(old_string, new_string)
        print("Fixed specific double quotes in desc.")
    else:
        # Let's just do a regex replace if it's slightly different
        content = re.sub(r'sob disfarce de "apelo à paz"', r'sob disfarce de &quot;apelo à paz&quot;', content)
        print("Fixed double quotes using regex.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
