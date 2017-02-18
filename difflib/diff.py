import difflib
def diff():
    file1 = open('text.txt', 'r')
    file2 = open('text1.txt', 'r')
    d = difflib.HtmlDiff()# делает сравнение текста в формате HTML
   
    return  d.make_table (file1.readlines(), file2.readlines())+ '\n'

