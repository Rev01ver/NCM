import difflib
def htmldifflib(text1 ,text2  ):
   
    d = difflib.HtmlDiff()# делает сравнение текста в формате HTML
   
    return  d.make_table (text1.split('\n'), text2.split('\n'))+ '\n'
