#convertir csv a pdf


import csv
import os







def main():
    #abrir el archivo csv
    with open('archivo.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        #abrir el archivo pdf
        with open('archivo.pdf', 'w') as pdf_file:
            for line in csv_reader:
                pdf_file.write(line)
                pdf_file.write('\n')
                
    #cerrar el archivo csv
    csv_file.close()
    #cerrar el archivo pdf
    pdf_file.close()

if __name__ == '__main__':
    main()


