import csv
import pandas as pd

# Apri il file CSV originale e crea il file CSV di output
with open('data\portfolioFromGSheets.csv', newline='') as csvfile, open('data\portfolio.csv', 'w') as output_file:
    reader = csv.reader(csvfile)

    # Salta la riga dell'intestazione
    next(reader)
    output_file.write('date,daily_invested,contribution_value,counter_value\n')
    
    # Itera su ogni riga
    for row in reader:
        try:
            # Rimuovi il carattere € e converte in float, arrotondando a due decimali
            column0 = row[0]
            column1 = round(float(row[1].replace('â‚¬ ', '').replace('.', '').replace(',', '.')), 2)
            print(column1)
            column2 = round(float(row[2].replace('â‚¬ ', '').replace('.', '').replace(',', '.')), 2)
            
            # Calcola column3 in base ai valori precedenti e successivi
            if row[3] != '':
                column3 = round(float(row[3].replace(' â‚¬ ', '').replace('.', '').replace(',', '.')), 2)
            else:
                column3 = ''
            
            # Scrivi i valori convertiti nel file di output
            output_file.write(f'{column0},{column1},{column2},{column3}\n')
        except ValueError as e:
            print('Error: ', e)

# Leggi il file CSV di output
df = pd.read_csv('data\portfolio.csv', parse_dates=['date'], dayfirst=True)

# Interpola i valori mancanti in 'counter_value'
df['counter_value'] = pd.to_numeric(df['counter_value'], errors='coerce')  # Converte alla numerica, ignorando errori
df['counter_value'] = df['counter_value'].interpolate()

# Arrotonda i valori float nel DataFrame a due decimali
df = df.round(2)

# Mostra il DataFrame aggiornato
df.to_csv('data\portfolio.csv', index=False)

# Somma dei valori nella colonna 1
sum_column1 = df['daily_invested'].sum()
print('Sum of column[1]:', sum_column1)
