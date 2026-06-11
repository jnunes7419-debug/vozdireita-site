import re

def main():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the keywords property from all articles in the array
    # It looks like: \n            keywords: '...'\n
    content = re.sub(r",\s*keywords:\s*'[^']*'", "", content)
    content = re.sub(r",\s*keywords:\s*\"[^\"]*\"", "", content)

    # 2. Update the filter function
    # return this.articles.filter(a => (a.title + ' ' + a.desc + ' ' + a.keywords).toLowerCase().includes(q));
    # to:
    # return this.articles.filter(a => (a.title + ' ' + a.desc).toLowerCase().includes(q));
    
    content = content.replace("a.title + ' ' + a.desc + ' ' + a.keywords", "a.title + ' ' + a.desc")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Keywords removed from search component.")

if __name__ == '__main__':
    main()
