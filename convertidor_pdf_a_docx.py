from pdf2docx import Converter

pdf_file = 'esto.pdf' #introducir el nombre del pdf, tiene que estar en la misma carpeta que este archivo.
docx_file ='esto.docx' #nombre del archivo convertido y puesto en la misma carpeta.
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
