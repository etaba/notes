import csv
from pprint import pprint as pp


def read_sheets(filename):
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        out = {}
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            out[row[0]] = { h : c for h, c in zip(headers[1:],row[1:])}
        return out

def get_client(time_entry):
    return clients.get(time_entry['clientId'])

def get_matter(time_entry):
    return matters.get(time_entry['matterId'])

#time_entry is key value tuple
def sync(time_entry):
    persisted = time_entries.get(time_entry[0])
    if time_entry[1] != persisted:
        time_entries[time_entry[0]] = time_entry[1]

# with open('out.csv', 'w', newline='') as csvfile:
#     fieldnames = ['client', 'total_time']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'client': 'Baked', 'total_time': 'Beans'})
#     writer.writerow({'client': 'Lovely', 'total_time': 'Spam'})
#     writer.writerow({'client': 'Wonderful', 'total_time': 'Spam'})

if __name__ == '__main__':
    time_entries = read_sheets('TimeEntries.csv')
    clients = read_sheets('Clients.csv')
    matters = read_sheets('Matters.csv')
    te_new = ('633276e8-730d-11e8-adc0-fa7ae01bbebc',{'matterId':'new'})
    te_new2 = ('633276e8-730d-11e8-adcsdfsfs0',{'matterId':'new 2'})
    sync(te_new)
    sync(te_new2)
    pp(time_entries)
